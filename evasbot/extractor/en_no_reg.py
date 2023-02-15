# -*- coding: utf-8 -*-
"""
Created on Mon Oct 03 22:25:23 2022

@author: Venisa Tewu
"""
import re

class entity_no_reg:
    
    def __init__(self):
        self.regex =  r'\b(s|S)+\d{8}\b'
        
        
    def get_no_reg(self, input_string):     
        #List declaration
        collect      = [] 
        
        #Extract entity email dari input-string
        count = 0
        for match in re.finditer(self.regex, input_string):
            count += 1
            #Mengambil string yang sesuai dengan regex email
            get_noReg = match.group().casefold()
            
            #Count all specific type in string
            noReg_count = ('<noReg%d>' % count)
            
            dict_email = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : noReg_count,
                'Value'         : ''+get_noReg
                }
            
            collect.append(dict_email) #simpan semua entity yang di ekstrak ke dalam satu list
        return collect


def main():
    entity_system_no_reg = entity_no_reg()
           
    input_string = 'no registrasi saya adalah S21910498'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_no_reg.get_no_reg(input_string)
    print('\nEntity: \n{0}'.format(result_entity))
 
if __name__ == '__main__' :
      main()