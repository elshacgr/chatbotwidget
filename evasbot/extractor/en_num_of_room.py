# -*- coding: utf-8 -*-
"""
Created on mon Sep 19 02:15:09 2022

@author: Venisa Tewu
"""

import re
# from ordinal2num_test import *
from word2num_test import *
import word2num_test

class entity_num_of_room:
    
    def __init__(self):
        self.units             = 'nol|pertama|satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|sebelas|seratus' #tambah yang sebutan 'dua nol satu' atau 'dua kosong satu'
        self.scales            = 'belas|puluh|ratus|ribu|juta|miliar|triliun' 
        self.room              = r'\bkamar|bilik|room|ruangan\b'

        self.convertWordNumber = wordNum()
        
        
    def get_num_of_room(self, input_string):     
        pattern_1    = '('+self.units+')'
        pattern_2    = '('+self.units+'|'+self.scales+')'
        kamar        = '('+self.room+')' 
        space        = '\s' 
        num          = '\d'
        
        #Pattern for recognice number of room
        pattern      = '('+pattern_1+space+pattern_2+space+pattern_1+space+pattern_2+space+pattern_1+space+kamar+')|'+'('+pattern_1+space+pattern_2+space+pattern_1+space+pattern_2+space+kamar+')|'+'('+pattern_1+space+pattern_2+space+pattern_1+space+kamar+')|'+'('+pattern_1+space+pattern_2+space+kamar+')|'+'('+pattern_1+space+kamar+')'
        
        #Change all input string to lowercase
        input_string = input_string.casefold()
        
        #List declaration
        collect      = []
        
        #Convert untuk extract entity dari full-string
        count = 0
        for match in re.finditer(pattern,input_string):
            count +=1
            #Convert all textual numbeer to numeric
            get_jumlahKamar = self.convertWordNumber.text2int(match.group().casefold())
            
            #Count all specific type in string
            jumlahKamar_count = ('<jumlahKamar%d>' % count)
            
            #Remove room-dict from entity to put in Value (take only value)
            value = re.sub(kamar, '', get_jumlahKamar)
            
            dict_dom = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : jumlahKamar_count,
                'Value'         : int(value)
                }
            
            collect.append(dict_dom)
        
        return collect
   

def main():
    entity_system_noKamar = entity_num_of_room()
           
    input_string = 'tiga kamar, dua ratus sebelas kamar, dua ratus sebelas kamar'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_noKamar.get_num_of_room(input_string)
    print('\nEntity: \n{0}'.format(result_entity))

if __name__ == '__main__' :
      main()