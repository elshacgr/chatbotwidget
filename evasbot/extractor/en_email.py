# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:20:03 2022

@author: Venisa Tewu
"""
import re

class entity_email:
    
    def __init__(self):
        self.regex_email =  r'\b[\w.+-]+@[\w-]+\.[\w.-]+\b'
        
    def get_email(self, input_string):     
        #Convert input string as lowercase
        input_string = input_string.casefold()
        
        #List declaration
        collect      = [] 
        
        #Extract entity email dari input-string
        count = 0
        for match in re.finditer(self.regex_email, input_string):
            count += 1
            #Mengambil string yang sesuai dengan regex email
            get_emails = match.group() 
            
            #Count all specific type in string
            email_count = ('<EMAIL%d>' % count)
            
            dict_email = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : email_count,
                'Value'         : ''+get_emails
                }
            
            collect.append(dict_email) #simpan semua entity yang di ekstrak ke dalam satu list
        return collect


def main():
    entity_system_email = entity_email()
           
    input_string = 'ini adalah email saya ven@gmail.com.'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_email.get_email(input_string)
    print('\nEntity: \n{0}'.format(result_entity))
 
if __name__ == '__main__' :
      main()