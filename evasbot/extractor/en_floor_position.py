# -*- coding: utf-8 -*-
"""
Created on input_stringn Sep 19 02:15:09 2022

@author: Venisa Tewu
"""

import re
from word2num_test import *
import word2num_test

class entity_floor_position:
    
    def __init__(self):
        self.units             = 'nol|pertama|satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|seratus'
        self.floor             = r'\blantai|lante\b'

        self.convertWordNumber = wordNum()
        
        
    def get_floor_position(self, input_string):          
        pattern_1    = '('+self.units+')'
        lantai       = '('+self.floor+')'
        space        = '\s'
   
        #Pattern for recognize flooer position
        pattern      = '('+lantai+space+pattern_1+')'

        #Change all input string to lowercase
        input_string = input_string.casefold()
        
        #List declaration
        collect      = []
        
        #Convert untuk extract entity dari full-string
        count = 0
        display = re.finditer(pattern, input_string)
        for match in display:
            count +=1
            #Convert all textual numbeer to numeric
            get_floorPosition = self.convertWordNumber.text2int(match.group().casefold())
            
            #Count all specific type in string
            floor_count = ('<posisiLantai%d>' % count)
            
            #Remove room-dict from entity to put in Value (take only value)
            val = re.sub(lantai, '', get_floorPosition)
            value = val.replace(' ', '')
            
            dict_dom = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : floor_count,
                'Value'         : ''+value
                }
            
            collect.append(dict_dom)
        
        return collect
       
        #Convert untuk ditampilkan di full-string
        # input_string = input_string.replace(',', ' ,') #jadi koma displit dulu sebulum dipanggil untuk ditampilkan hasil convert ke dalam string
        # curstring = self.convertWordNumber.text2int(input_string) #ERROR atau #JADI tapi harus split koma:,
        # curstring = curstring.replace(' ,', ',') #setelah berhasil diconvert, sambungkan kembali komanya ke string atau convert angka (ketempat semula)
        # print('\n')
        # print('Output: ', curstring)
   

def main():
    entity_system_floor_position = entity_floor_position()
           
    input_string = 'lantai satu, lantai dua'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_floor_position.get_floor_position(input_string)
    print('\nEntity: \n{0}'.format(result_entity))

if __name__ == '__main__' :
      main()