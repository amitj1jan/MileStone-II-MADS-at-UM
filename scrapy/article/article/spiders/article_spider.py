from w3lib.html import remove_tags, remove_tags_with_content
from sqlalchemy import create_engine
from datetime import datetime
import pandas as pd
import scrapy

basepath = '/mnt/d/Amit/data-science/MADS/SIADS696/'
filepath = 'datasets/'
filename = 'url_df.csv'
filepath_name = basepath + filepath + filename


class ArticleSpider(scrapy.Spider):
    name = "articles"    
    
    def __init__(self, name=None,year=0, *args, **kwargs):
        super(ArticleSpider, self).__init__(*args, **kwargs)        
        self.start_time = datetime.now()
        self.year = year
        
    def get_urls(self):            
        print("----------", filepath_name)
        df = pd.read_csv(filepath_name, usecols=['id', 'date','url'])
        url_gen = df.loc[pd.DatetimeIndex(df.date).year == int(self.year)]
        return(url_gen.iterrows())
        
    def start_requests(self):
        print("----------", self.year) 
        print("-----------", self.start_time)
        url_gen = self.get_urls()        
        for _, row in iter(url_gen): 
            request = scrapy.Request(url=row[2], callback=self.parse)
            request.meta['indx'] = row[0]
            request.meta['date'] = row[1]
            yield request

    def parse(self, response):
        body = response.css("div._3YYSt.clearfix").get()
        if not body:
            body = response.css("div.fewcent-408590._1_Akb.clearfix").get() 
        if not body:
            body = response.css("div.Normal").getall()   
            body = " ".join(body)
            
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
       