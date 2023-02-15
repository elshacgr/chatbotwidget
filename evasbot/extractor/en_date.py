# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 23:59:00 2022

@author: Venisa Tewu
"""

import re
from datetime import datetime

class entity_date:
    def __init__(self):
        self.januari   = "januari|january|jan"
        self.februari  = "februari|february|feb"
        self.maret     = "maret|march|mar"
        self.april     = "april|apr"
        self.mei       = "mei|may"
        self.juni      = "juni|june|jun"
        self.juli      = "juli|july|jul"
        self.agustus   = "agustus|august|aug"
        self.september = "september|sept|sep"
        self.oktober   = "oktober|october|okt|oct"
        self.november  = "november|nov"
        self.desember  = "Desember|december|des|dec"
        # self.matches = '(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})'
        # self.day = "(?P<day>[12][0-9]|3[0-1]|0?[1-9])"
        self.matches = r'\b\d{2,4}(?: +|\/)\S+(?: +|\/)\d{2,4}\b|\b[a-z]+ +\d{1,2},? +\d{4}\b'
        
    def date_is_valid(self, day: int, month: int, year: int) -> bool:
        return (month not in (2, 4, 6, 9, 11)   # 31 days in month (Jan, Mar, May, Jul, Aug, Oct, Dec).
        or day < 31 and month in (4, 6, 9, 11)  # 30 days in month (Feb, Apr, Jun, Sep, Nov).
        or month == 2 and day == 29 and year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
                                                # February, 29th in a Gregorian leap year.
        or month == 2 and day < 29)             # February, 1st-28th.
    
    def date_detector(self, text: str):
        text = text.casefold()
        space = "\s"
        coba       = "("+self.januari+")"
        test = "\d"
        
        date_pattern = re.compile('''
        (?P<day>[12][0-9]|3[0-1]|0?[1-9])   # to detect days from 1 to 31
        (?P<sep>[./-]|\s)                   # to detect different separations
        (?P<month>1[0-2]|0?[1-9])           # to detect number of months
        (?P=sep)                            # to detect different seperations
        (?P<year>2?1?[0-9][0-9][0-9])       # to detect number of years from 1000-2999 years
        '(\d{2}[\/ ](\d{2}|January|Jan|February|Feb|March|Mar|April|Apr|May|May|June|Jun|July|Jul|August|Aug|September|Sep|October|Oct|November|Nov|December|Dec)[\/ ]\d{2,4})'
          ''', re.VERBOSE)
        
        
        # testt = "("+self.matches+")"
        lagi = "("+self.matches+")"
        pattern = "("+lagi+")"
    
        
        #Convert untuk extract entity dari full-string
        hitung = 0
        kumpul = []
        display = re.finditer(pattern, text)
        for i in display:  
            hitung +=1
            
            text = re.sub(self.januari, '1', text)
            text = re.sub(self.februari, '2', text)
         
            value = i.group()   
         
            dict_dom = {
                "Entity"        : ""+i.group(0),
                "StartIndex"    : i.start(),
                "EndIndex"      : i.end(),
                "Type"          : "<DATE>",
                "Value"         : ""+value
                }
            
            kumpul.append(dict_dom)
            # entity = i.group()
            # mulai = i.start()
            # selesai = i.end()
            # print(entity)
            # print(mulai)
            # print(selesai)
            
        # return kumpul
        date_pattern = re.compile('''
        (?P<day>[12][0-9]|3[0-1]|0?[1-9])   # to detect days from 1 to 31
        (?P<sep>[./-]|\s)                   # to detect different separations
        (?P<month>1[0-2]|0?[1-9])           # to detect number of months
        (?P=sep)                            # to detect different seperations
        (?P<year>2?1?[0-9][0-9][0-9])       # to detect number of years from 1000-2999 years
          ''', re.VERBOSE)
    
        dates = []
        collect = []
        count = 0
        
        for match in date_pattern.finditer(text):
            text = re.sub(self.januari, '1', text)
            text = re.sub(self.februari, '2', text)
            date = match.groupdict()                            # convert Match object to dictionary.
            # print("ini:", match.group(0))                         
            del date['sep']                                     # we don't need the separator any more.
            date = {key: int(val) for key, val in date.items()} # apply int() to all items.
            
            if self.date_is_valid(date['day'], date['month'], date['year']):
                for fmt in ('%Y-%m-%d', '%d-%m-%Y', '%d/%m/%Y', '%d.%m.%Y','%d %m %Y', '%Y-%d-%m',
                            '%b %d %Y', '%m %d %Y', '%Y-%d-%b', '%d-%b-%Y', '%d/%b/%Y'):
                    try:
                        example_time =  datetime.strptime(match.group(), fmt)
                        final_output =  datetime.strftime(example_time, "%d-%m-%Y")
                        # print("Default format:",final_output)
                    except ValueError:
                        continue
                count +=1
                
                #Mengambil string yang sesuai dengan regex email
                # get_date = match.group()
                
                #Count all specific type in string
                date_count = ("<DATE%d>" % count)
                
                dict_dom = {
                    "Entity"        : ""+match.group(0),
                    "StartIndex"    : match.start(),
                    "EndIndex"      : match.end(),
                    "Type"          : date_count,
                    "Value"         : ""+final_output
                    }
                collect.append(dict_dom)
                
                # dates.append(date)
    
        semua = kumpul + collect
        
    
        if len(dates) > 0:
            for date in dates:
                print(date)
                
        return semua

def main():
    entity_system_person = entity_date()
           
    input_string = 'tanggal 31 January 2000, 31 feb 2022, 01-03-2021, 31/feb/2022  31/02/2002'

    print("Input: ", input_string)
    print("\n")
    print(entity_system_person.date_detector(input_string))
    print()

if __name__ == "__main__" :
      main()