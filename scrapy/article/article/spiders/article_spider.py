from w3lib.html import remove_tags, remove_tags_with_content
from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd
import scrapy

class ArticleSpider(scrapy.Spider):
    name = "article"
    conn_string = 'postgresql://postgres:postgres@localhost/news'    
    
    def __init__(self, name=None,year=0, *args, **kwargs):
        super(ArticleSpider, self).__init__(*args, **kwargs)        
        self.start_time = datetime.now()
        self.year = year
        
    def get_urls(self):    
        engine = create_engine(self.conn_string, echo=False)
        query = "select id, date, url from news.news_id where extract(year from date)= %(year)s order by id;"
#         query = "select id, date, url from news.news_id where extract(year from date) = %(year)s limit 7"
        data = {'year': self.year}
        url_gen = engine.execute(query, data).fetchall()
        return(url_gen)
        
    def start_requests(self):
        print("----------", self.year) 
        print("-----------", self.start_time)
        url_gen = self.get_urls()        
        for indx, date, url in iter(url_gen): 
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta['indx'] = indx
            request.meta['date'] = date
            yield request

    def parse(self, response):
        body = response.css("div._3YYSt.clearfix").get()
        if not body:
            body = response.css("div.fewcent-408590._1_Akb.clearfix").get() 
        if not body:
            body = response.css("div.Normal").get()        
            
        if body:            
            content = remove_tags(remove_tags_with_content(body))
            yield {
                'id': response.meta['indx'],
                'date': response.meta['date'],
                'url': response.url,
                'title' : response.url.split("/")[-3],
                'category': response.url.split("/")[-5:-3],
                'article': content                
                    }
        else:
            yield {
                'id': response.meta['indx'],
                'date': response.meta['date'],
                'url': response.url
                    }                
    
    def closed(self, response):
        self.ending_time = datetime.now()
        duration = self.ending_time - self.start_time
        print(duration)        
       