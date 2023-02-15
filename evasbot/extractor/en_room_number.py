# -*- coding: utf-8 -*-
"""
Created on input_stringn Sep 19 02:15:09 2022

@author: Venisa Tewu
"""

import re
from word2num_test import *
import word2num_test

class entity_room_number:
    
    def __init__(self):
        self.units2            = 'nol|kosong|ratus'
        self.units3            = 'satu|dua|tiga|empat|lima|enam|tujuh|delapan|sembilan'
        self.teens             = 'belas'
        self.tens              = 'puluh'
        self.scales            = 'ribu'
        self.ordinal_scales    = 'seribu'
        self.ordinal_teens     = 'sebelas'
        self.ordinal_tens      = 'sepuluh'
        self.ordinal_scale     = 'seratus'
        self.number            = r'\b[1-9][0][1-9]|[1-9][1][1-9]\b'
        self.room              = r'\bkamar|bilik|room|ruangan\b'

        self.convertWordNumber = wordNum()
        
        
    def get_room_number(self, input_string):          
        units_1      = '('+self.units3+')' #[satu-sembilan]
        units_2      = '('+self.units3+'|'+self.units2+')' #[nol|kosong|ratus] 
        teens        = '('+self.teens+')' # [belas]
        tens         = '('+self.tens+')' # [puluh]
        scales       = '('+self.scales+')' # [ribu]
        ord_scales   = '('+self.ordinal_scales+')' # [seribu]
        ord_teens    = '('+self.ordinal_teens+')' # [sebelas]
        ord_tens     = '('+self.ordinal_tens+')' # [sepuluh]
        ord_scale    = '('+self.ordinal_scale+')' # [seratus]
        
        number       = '('+self.number+')' # [1-9][0][1-0]|[1-9][1][1-9]
        kamar        = '('+self.room+')' # [bilik, kamar,room,ruangan]
        space        = '\s'
    
         #Pattern
        pattern_1    = '('+units_1+space+scales+space+ord_scale+space+units_1+')' #[satu-sembilan] [ribu] [seratus] [satu-sembilan]
        pattern_2    = '('+ord_scales+space+ord_scale+space+units_1+')' #[seribu] [seratus] [satu-sembilan]
        pattern_3    = '('+units_1+space+units_2+space+units_1+space+tens+space+units_1+')' #[satu-sembilan] [nol|kosong|ratus] [satu-sembilan] [puluh] [satu-sembilan]
        pattern_4    = '('+units_1+space+units_2+space+units_1+space+teens+')' #[satu-sembilan] [nol|kosong|ratus] [satu-sembilan] [belas]
        pattern_5    = '('+units_1+space+units_2+space+units_1+')' #[satu-sembilan] [nol|kosong|ratus] [satu-sembilan]
        pattern_6    = '('+units_1+space+units_2+space+ord_tens+')' #[satu-sembilan] [nol|kosong|ratus] [sepuluh]
        pattern_7    = '('+units_1+space+units_2+space+ord_teens+')' #[satu-sembilan] [nol|kosong|ratus] [sebelas]
        pattern_8    = '('+ord_scale+space+ord_tens+')' #[seratus] [sepuluh]
        pattern_9    = '('+ord_scale+space+ord_teens+')' #[seratus] [sebelas]
        pattern_10   = '('+ord_scale+space+units_1+space+tens+space+units_1+')' #[seratus] [satu-sembilan] [puluh] [satu-sembilan]
        pattern_11   = '('+ord_scale+space+units_1+space+tens+')' #[seratus] [satu-sembilan] [puluh]
        pattern_12   = '('+ord_scale+space+units_1+space+teens+')' #[seratus] [satu-sembilan] [belas]
        pattern_13   = '('+ord_scale+space+units_1+')' #[seratus] [satu-sembilan]
        
        #Pattern for recognize number of room
        pattern_1th  = '('+pattern_1+')|'+'('+pattern_2+')|'+'('+pattern_3+')|'+'('+pattern_4+')|'+'('+pattern_5+')|'+'('+pattern_6+')|'+'('+pattern_7+')|'+'('+pattern_8+')|'+'('+pattern_9+')|'+'('+pattern_10+')|'+'('+pattern_11+')|'+'('+pattern_12+')|'+'('+pattern_13+')'
        pattern_2nd  = '('+kamar+space+pattern_1+')|'+'('+kamar+space+pattern_2+')|'+'('+kamar+space+pattern_3+')|'+'('+kamar+space+pattern_4+')|'+'('+kamar+space+pattern_5+')|'+'('+kamar+space+pattern_6+')|'+'('+kamar+space+pattern_7+')|'+'('+kamar+space+pattern_8+')|'+'('+kamar+space+pattern_9+')|'+'('+kamar+space+pattern_10+')|'+'('+kamar+space+pattern_11+')|'+'('+kamar+space+pattern_12+')|'+'('+kamar+space+pattern_13+')'
        pattern_3rd  = '('+number+')'
        pattern_4th  = '('+kamar+space+number+')' 
        
        all_pattern  = '('+pattern_1th+')|'+'('+pattern_2nd+')|'+'('+pattern_3rd+')|'+'('+pattern_4th+')'
        #Change all input string to lowercase
        input_string = input_string.casefold()
        
        #List declaration
        collect      = []
        
        #Convert untuk extract entity dari full-string
        count = 0
        display = re.finditer(all_pattern, input_string)
        for match in display:
            count +=1
            
            # Replace 'nol' and 'kosong' to 'ratus'
            def replace_all(text, dic):
                for i, j in dic.items():
                    text = text.replace(i, j)
                return text
            zero_dict = { 'kosong': 'nol', 'nol': 'ratus'}
            replace_zero = replace_all(match.group(), zero_dict)
            # print("zero_dict:", replace_zero)

            #Convert all textual number to numeric
            get_roomNum = self.convertWordNumber.text2int(replace_zero.casefold())
            
            #Count all specific type in string
            roomNum_count = ('<noKamar%d>' % count)
            
            #Remove kamar/bilik/room/ruangan
            #Remove room-dict from entity to put in Value (take only value)
            val = re.sub(kamar , '', get_roomNum)
            value = val.replace(' ', '')

            def replace_tens(text, dic):
                for i, j in dic.items():
                    text = text.replace(i, j)
                return text
            tens_dict = { '1020': '120', '1021':'121', '1022':'122', '1023':'123', '1024':'124', '1025':'125', '1026':'126', '1027':'127', '1028':'128', '1029':'129',
                          '2020': '220', '2021':'221', '2022':'222', '2023':'223', '2024':'224', '2025':'225', '2026':'226', '2027':'227', '2028':'228', '2029':'229',
                          '3020': '320', '3021':'321', '3022':'322', '3023':'323', '3024':'324', '3025':'325', '3026':'326', '3027':'327', '3028':'328', '3029':'329',
                          '1030': '130', '1031':'131', '1032':'132', '1033':'133', '1034':'134', '1035':'135', '1036':'136', '1037':'137', '1038':'138', '1039':'139',
                          '2030': '230', '2031':'231', '2032':'232', '2033':'233', '2034':'234', '2035':'235', '2036':'236', '2037':'237', '2038':'238', '2039':'239',
                          '3030': '330', '3031':'331', '3032':'332', '3033':'333', '3034':'334', '3035':'335', '3036':'336', '3037':'337', '3038':'338', '3039':'339',
                        }
            value = replace_tens(value, tens_dict)
            
            dict_dom = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : roomNum_count,
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
    entity_system_noKamar = entity_room_number()
           
    input_string = '101, dua ratus satu, seratus sebelas, dua ratus dua belas, tiga ratus dua belas, dua ribu seratus satu, dua ribu dua ratus satu, satu kosong satu, satu nol satu'
    print('Input: \n{0}'.format(input_string))
    
    result_entity = entity_system_noKamar.get_room_number(input_string)
    print('\nEntity: \n{0}'.format(result_entity))
 

if __name__ == "__main__" :
      main()