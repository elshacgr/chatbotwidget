import phonenumbers
import re

class entity_phone:
    def __init__(self):
        # self.regex_phone =  r'\+62\s\d{3}[-\.\s]??\d{3}[-\.\s]??\d{3,4}|\(0\d{2,3}\)\s?\d+|0\d{2,3}\s?\d{6,7}|\+62\s?361\s?\d+|\+62\d+|\+62\s?(?:\d{3,}-)*\d{3,5}\b'
        # self.regex_phone = r'[\d]{3}-[\d]{3}-[\d]{3}'
        # self.regex_phone = r'\+62\d{3}[-\.\s]??\d{3}[-\.\s]??\d{3,4}\b'
        self.regex_phone = r'\b(\+62|62)?[\s-]?0?8[1-9]{1}\d{1}[\s-]?\d{4}[\s-]?\d{2,5}\b'
        
    def get_phone(self, input_string):
        #List declaration
        collect=[]
        
        #Extract entity phone dari input-string
        count = 0
        for match in re.finditer(self.regex_phone, input_string):
            count += 1
            # x =''.join(match.group())
            # print(x)
            
            # #Mengambil string yang sesuai dengan regex
            # get_phone = match.group()
            
            #Default output in value
            national_number = phonenumbers.parse(match.group(), 'ID')
            international_number = phonenumbers.format_number(national_number, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
            # print(international_number)
            value = international_number
            
            #Count all specific type in string
            phone_count = ('<PHONE%d>' % count)
            
            dict_email = {
                'Entity'        : ''+match.group(0),
                'StartIndex'    : match.start(),
                'EndIndex'      : match.end(),
                'Type'          : phone_count,
                'Value'         : ''+value,
                }
            
            collect.append(dict_email) #simpan semua entity yang di ekstrak ke dalam satu list
        
        return collect


def main():
    entity_system_phone= entity_phone()
           
    input_string = 'ini nomor saya 081233333333, +62 8391210312, (0361) 227337, +62812333333'
    print('Input string: \n{0}'.format(input_string))

    result_entity = entity_system_phone.get_phone(input_string)
    print('\nEntity: \n{0}'.format(result_entity))
 
if __name__ == "__main__" :
      main()