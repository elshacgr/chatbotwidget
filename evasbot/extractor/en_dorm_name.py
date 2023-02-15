# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 19:11:03 2022

@author: Venisa Tewu
"""
import re
from word2num_test import *
import word2num_test

class entity_dorm_name:
    
    def __init__(self):
        self.units            = '\bpertama|satu|dua|tiga\b'
        self.regex_dorm_name  = r'\bgenset|annex|bougenville|crystal satu|crystal 1|crystal dua|crystal 2|crystal tiga|crystal 3|crystal|edelweiss|guest house|jasmine satu|jasmine 1|jasmine dua|jasmine 2|jasmine\b'
        
        self.convertWordNumber = wordNum()
        
    def get_dorm_name(self, input_string):
        #Convert input string as lowercase
        input_string = input_string.casefold()
        
        # input_string = re.sub('.', '', input_string)
        
        #List declaration
        collect      = []
        
        #Extract entity email dari input-string
        count = 0
        for match in re.finditer(self.regex_dorm_name, input_string):
            count +=1
            
            # #Mengambil string yang sesuai dengan regex dormitory
            # get_dormName = match.group()
            
            #Convert all textual numbeer to numeric
            get_dormName = self.convertWordNumber.text2int(match.group().casefold())
            
            #Count all specific type in string
            dormName_count = ('<dormName%d>' % count)
            
            dict_dom = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : dormName_count,
                'Value'         : ''+get_dormName
                }
            
            collect.append(dict_dom)
        
        return collect
    
        
def main():
    entity_system_dorm_name = entity_dorm_name()
           
    input_string = 'jasmine satu, annex, Jasmine Satu, jasmine 2.'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_dorm_name.get_dorm_name(input_string)
    print('\nEntity: \n{0}'.format(result_entity))


if __name__ == '__main__' :
      main()