# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 22:25:23 2022

@author: Venisa Tewu
"""
import re

class entity_nim:
    
    def __init__(self):
        self.regex =  r'\b(1050)+\d{8}\b'
        
        
    def get_nim(self, input_string):     
        #Convert input string as lowercase
        input_string = input_string.casefold()
        
        #List declaration
        collect      = [] 
        
        #Extract entity email dari input-string
        count = 0
        for match in re.finditer(self.regex, input_string):
            count += 1
            #Mengambil string yang sesuai dengan regex email
            get_nim = match.group() 
            
            #Count all specific type in string
            nim_count = ('<NIM%d>' % count)
            
            dict_email = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : nim_count,
                'Value'         : ''+get_nim
                }
            
            collect.append(dict_email) #simpan semua entity yang di ekstrak ke dalam satu list
        return collect


def main():
    entity_system_nim = entity_nim()
           
    input_string = 'NIM saya yaitu 105021910075'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_nim.get_nim(input_string)
    print('\nEntity: \n{0}'.format(result_entity))
 
if __name__ == '__main__' :
      main()