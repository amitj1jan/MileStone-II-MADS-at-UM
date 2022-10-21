from w3lib.html import remove_tags, remove_tags_with_content
from itertools import count
from sqlalchemy import create_engine
from scrapy.linkextractors import LinkExtractor
from datetime import datetime
from datetime import timedelta, date
# import pandas as pd
import scrapy

base_url = "https://timesofindia.indiatimes.com/"
init_date = date(2004, 1, 1)
beg_date = date(2004, 1, 1)
# choose the date till which to get the news article urls
end_date = date(2022, 9, 30)
init_time = 37987

valid_url1 = 'articleshow'
valid_url2 = base_url.replace('https', 'http')


def get_first_date(year, month=1):
    '''
    Provides the first date of an year
    year: year for which first date is inquired
    '''
    first_day = date(year, month, 1)
    return(first_day)

def get_next_date(init_date, init_time):
    '''
    init_date: takes any date
    init_time: numeric code for that date
    returns:returns next date and next init_time code(times of India numeric code for a date)
    '''
    next_date = init_date + timedelta(days = 1)
    init_time += 1
    return(next_date, init_time)

def create_param(next_date, init_time):    
    """
    Return the predicates to access an news article webpage
    :param next_date: date for which to create predicates
    :param init_time: numeric code for that day news articles archive webpage(for every date archive, webpage ends with a numeric value, which is what we are trying to get here to generte the webpage url)
    :return: returns the url predicates
    """
    date_lst = [next_date.year, next_date.month, next_date.day]
    date_str = [str(item) for item in date_lst]
    date_num = [next_date.year, next_date.month, init_time]
    date_param = '/'.join(date_str) 
    PARAMS = ['year-', 'month-', 'starttime-']
    param_str = ''
    for time, param in zip(date_num, PARAMS):
        param_str += param  + str(time) + ','
    param_str = param_str[:-1]
    return(date_param + '/archivelist/' + param_str)

def create_predicates(beg_date):
    """
    generate predicates for all the dates till end date
    :param beg_date: starting date from which to generate the predicates
    """
#     first_day = get_first_date(beg_year)
    init_time = get_init_time_for_date(beg_date)
    predicates = {}
    next_date = beg_date 
    curr_date = date.today()
#     curr_date = end_date
    while next_date <= curr_date:
        yield next_date, create_param(next_date, init_time)
        next_date,init_time = get_next_date(next_date, init_time) 
        
def get_init_time_for_date(curr_date):
    date_diff = (curr_date - init_date).days
    curr_init = init_time + date_diff
    return(curr_init)        
        
pred_gen = enumerate(create_predicates(beg_date))


class NewsURLSpider(scrapy.Spider):
    name = "newsurl"
    le1 = LinkExtractor()
    
    def __init__(self, name=None, **kwrgs):
        self.start_time = datetime.now()
        self.iter_count = count(0)
        
    def start_requests(self):
        for indx, param in iter(pred_gen): 
            date, predicate = param
            url = base_url + predicate + '.cms'
            request = scrapy.Request(url=url, callback=self.parse)
            request.meta['date'] = date
            request.meta['iter_count'] = self.iter_count
            yield request
            
    def parse(self, response):
        num = 0
        for link in self.le1.extract_links(response): 
            if valid_url1 in link.url and valid_url2 in link.url:
                num += 1
                yield {
                    'id': next(response.meta['iter_count']),
                    'date': response.meta['date'],
                    'url': link.url
                        }
    
    def closed(self, response):
        self.ending_time = datetime.now()
        duration = self.ending_time - self.start_time
        print(duration)        
       