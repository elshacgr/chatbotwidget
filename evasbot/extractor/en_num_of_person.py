# -*- coding: utf-8 -*-
"""
Created on input_stringn Sep 19 02:23:43 2022

@author: Venisa Tewu
"""

import re
# from ordinal2num_test import *
from word2num_test import *
import word2num_test

class entity_num_of_person:
    
    def __init__(self):
        self.units      = 'nol|pertama|satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan|sepuluh|seratus' #tambah yang sebutan 'dua nol satu' atau 'dua kosong satu'
        self.scales     = 'belas|puluh|ratus|ribu|juta|miliar|triliun' 
        
        self.person = r'\bteman saya|adik saya|saya|student|students|kita|mama|papa|kaka|oma|opa|tamang|orang|ade\b'
        
        self.convertWordNumber = wordNum()
        
        
    def get_num_of_person(self, input_string):     
        # pattern_1 = '('+self.units+')'
        # pattern_2 = '('+self.units+'|'+self.scales+')'
        # space = '\s'
        # all_pattern = '('+pattern_1+space+pattern_2+space+pattern_2+space+pattern_2+space+pattern_2+')|'+'('+pattern_1+space+pattern_2+space+pattern_2+space+pattern_2+')|'+'('+pattern_1+space+pattern_2+space+pattern_2+')|'+'('+pattern_1+space+pattern_2+')|'+'('+pattern_1+')' #one words
        # orang = '('+self.person+')'
        # pattern = '('+all_pattern+space+orang+')|'+'('+orang+')'
        
        #Change all input string to lowercase
        input_string = input_string.casefold()
        
        #List declaration
        collect = []
        
        #Convert untuk extract entity dari full-strin
        count = 0
        for match in re.finditer(self.person, input_string):
            count +=1
            # get_num_of_person = self.convertWordNumber.text2int(match.group().casefold())
            
            #Mengambil string yang sesuai dengan regex email
            get_jumlahPerson = match.group()
            
            #Count all specific type in string
            person_count = ('<PERSON%d>' % count)
           
            dict_dom = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : person_count,
                'Value'         : ''+get_jumlahPerson
                }
            
            collect.append(dict_dom)
      
        # jumlah = len(re.findall(self.person, input_string))
        # print('Jumlah entity person:', jumlah)
        
        return collect
       
        #Convert untuk ditampilkan di full-string
        # input_string = input_string.replace(',', ' ,') #jadi koma displit dulu sebulum dipanggil untuk ditampilkan hasil convert ke dalam string
        # curstring = self.convertWordNumber.text2int(input_string) #ERROR atau #JADI tapi harus split koma:,
        # curstring = curstring.replace(' ,', ',') #setelah berhasil diconvert, sambungkan kembali komanya ke string atau convert angka (ketempat semula)
        # print('\n')
        # print('Output: ', curstring)
   

def main():
    entity_system_person = entity_num_of_person()
           
    input_string = 'pesan kamar untuk saya, teman saya juga adik saya'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_person.get_num_of_person(input_string)
    print('\nEntity: \n{0}'.format(result_entity))

if __name__ == '__main__' :
      main()