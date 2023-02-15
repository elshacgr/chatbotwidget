#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 21:33:47 2022

@author: elshadairampengan
"""

# import calendar
import datetime
import time
from datetime import date
import calendar

class current_datetime:
    def __init__(self):
        self.dict_bulan = {
                "1" : "Januari",
                "2" : "Februari",
                "3" : "Maret",
                "4" : "April",
                "5" : "Mei",
                "6" : "Juni",
                "7" : "Juli",
                "8" : "Agustus",
                "9" : "September",
                "10" : "Oktober",
                "11" : "November",
                "12" : "Desember"
                }
        self.dict_hari = {
                "Sunday" : "Minggu",
                "Monday" : "Senin",
                "Tuesday" : "Selasa",
                "Wednesday" : "Rabu",
                "Thursday" : "Kamis",
                "Friday" : "Jumat",
                "Saturday" : "Sabtu"
                }
        
    def current_month (self):
        # using now() to get current time
        current_time = datetime.datetime.now()
        x= str(current_time.month)

        if x in self.dict_bulan:
            y = self.dict_bulan.get(x)
        
        # print("Month : ", y)
        return y
    
    def current_date (self):
        current_time = datetime.datetime.now()
        tanggal = current_time.day
        return tanggal
        
    def current_day (self):
        my_date = date.today()
        # Hari dalam bhs inggris
        hari = calendar.day_name[my_date.weekday()]

        # if condition jika hari ada di dalam dict_hari
        if hari in self.dict_hari:
            hari_string = self.dict_hari.get(hari) # taubah jadi indo
            
        # print(hari_string)
        return hari_string
    
    def current_waktu (self):
        curr_time = time.strftime("%H:%M:%S", time.localtime())

        # print("Sekarang jam", curr_time)
        return curr_time
    
    def current_year(self):
        current_time = datetime.datetime.now()
        year = current_time.year
        return year
        
        
# Bulan

        
def main():
    current = current_datetime()
    tanggal = current.current_date()
    bulan = current.current_month()
    hari = current.current_day()
    jam = current.current_waktu()
    tahun = current.current_year()
    print('Tanggal', tanggal)
    print('Bulan', bulan)
    print("Hari", hari)
    print("Sekarang jam ", jam)
    print("Tahun ", tahun)
    print(f'Ini tanggal berapa {tanggal} {bulan}, {tahun}')

if __name__ == '__main__' :
      main()



