# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 23:41:22 2022

@author: Venisa Tewu
"""

import re

class entity_user_name:
    
    def __init__(self):
        self.user_name =  r'\"(.*?)\"'
        
    def get_user_name(self, input_string):     
        #List declaration
        collect      = [] 
        
        #Extract entity email dari input-string
        count = 0
        for match in re.finditer(self.user_name, input_string):
            count += 1
            #Mengambil string yang sesuai dengan regex email
            get_emails = match.group() 
            get_emails = re.sub('"',"", get_emails)
            
            #Count all specific type in string
            email_count = ('<userName%d>' % count)
            
            dict_email = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : email_count,
                'Value'         : ''+get_emails
                }
            
            collect.append(dict_email) #simpan semua entity yang di ekstrak ke dalam satu list
        return collect


# def main():
#     entity_system_user_name = entity_user_name()
           
#     input_string = 'nama saya "Venisa", teman "Elsha"'
#     print('Input string: \n{0}'.format(input_string))

#     result_entity = entity_system_user_name.get_user_name(input_string)
#     print('\nEntity: \n{0}'.format(result_entity))
 
# if __name__ == "__main__" :
#       main()