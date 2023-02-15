# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 00:23:17 2022

@author: Venisa Tewu
"""

import re
from word2num_test import *
import word2num_test

class entity_bed_position:
    
    def __init__(self):
        self.units             = 'nol|pertama|satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|seratus'
        self.bed               = r'\b[A]|[a]|[B]|[b]\b'
        self.num               = '1|2|3'

        self.convertWordNumber = wordNum()
        
        
    def get_bed_position(self, input_string):          
        pattern_1    = '('+self.units+')' #[nol-seratus]
        bed       = '('+self.bed+')'
        space        = '\s'
        pattern_2 = '('+self.num+')'
   
        #Pattern for recognize bed position
        pattern_word      = '('+pattern_1+space+bed+')'
        pattern_num       = '('+pattern_2+space+bed+')'

        # Combine all the patterns
        pattern_all = '('+pattern_word+')|'+'('+pattern_num+')'
        
        #List declaration
        collect      = []
        
        #Convert untuk extract entity dari full-string
        count = 0
        display = re.finditer(pattern_all, input_string)
        for match in display:
            count +=1
            
            #Change all input string to lowercase
            input_string = input_string.casefold()
            
            #Convert all textual number to numeric
            #Match group are all the entity found
            get_bedPosition = self.convertWordNumber.text2int(match.group().casefold())
       
            #Count all specific type in string
            bed_count = ('<posisiBed%d>' % count)
            
            value = get_bedPosition
            
            dict_dom = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : bed_count,
                'Value'         : ''+value
                }
            
            # to add new dict_dom at the end of the list.
            collect.append(dict_dom)
        
        return collect


def main():
    entity_system_bed_position = entity_bed_position()
           
    input_string = ' 1b , dua A. 2 b'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_bed_position.get_bed_position(input_string)
    print('\nEntity: \n{0}'.format(result_entity))

if __name__ == '__main__' :
      main()