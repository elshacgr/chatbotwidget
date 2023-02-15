from en_nim import *
from en_date import *
from en_email import *
from en_phone import *
from en_no_reg import *
from en_user_name import *
from en_dorm_name import *
from en_room_number import *
from en_num_of_room import *
from en_bed_position import *
from en_num_of_person import *
from en_floor_position import *

import pandas as pd

#Handling multiple entities
class manage_extractor_entities:
     
    def __init__(self):
        #Stora all found entities that are in the sentence in one list
        self.store_all_entity_found = [] 
        
        self.en_sys_nim            = entity_nim()
        self.en_sys_date           = entity_date()
        self.en_sys_email          = entity_email()
        self.en_sys_phone          = entity_phone()
        self.en_sys_no_reg         = entity_no_reg()
        self.en_sys_user_name      = entity_user_name() 
        self.en_sys_dorm_name      = entity_dorm_name()
        self.en_sys_room_number    = entity_room_number()
        self.en_sys_num_of_room    = entity_num_of_room()
        self.en_sys_bed_position   = entity_bed_position()
        self.en_sys_num_of_person  = entity_num_of_person()
        self.en_sys_floor_position = entity_floor_position()
        
        
    def extract_entity(self, ori_input_user):
        #======================================================================
        #CALL ALL ENTITY BELOW
        #======================================================================
        try:
            #NIM
            get_arr_nim            = self.en_sys_nim.get_nim(ori_input_user)
            
            #Date
            get_arr_date           = self.en_sys_date.date_detector(ori_input_user)
            
            #Email
            get_arr_email          = self.en_sys_email.get_email(ori_input_user)
            
            #Phone
            get_arr_phone          = self.en_sys_phone.get_phone(ori_input_user)
            
            #Nomor Registrasi Mahasiswa
            get_arr_no_reg         = self.en_sys_no_reg.get_no_reg(ori_input_user)
            
            #Inputan user name
            get_arr_user_name      = self.en_sys_user_name.get_user_name(ori_input_user)
            
            #Nama Asrama
            get_arr_dorm_name      = self.en_sys_dorm_name.get_dorm_name(ori_input_user)
            
            #Nomor Kamar Asrama
            get_arr_room_number    = self.en_sys_room_number.get_room_number(ori_input_user)
            
            #Jumlah Kamar Asrama 
            get_arr_num_of_room    = self.en_sys_num_of_room.get_num_of_room(ori_input_user)
            
            #Posisi bed
            get_arr_bed_position   = self.en_sys_bed_position.get_bed_position(ori_input_user)
            
            #Person
            get_arr_num_of_person  = self.en_sys_num_of_person.get_num_of_person(ori_input_user)
            
            #Posisi lantai
            get_arr_floor_position = self.en_sys_floor_position.get_floor_position(ori_input_user)
            
        except Exception as ex:
            print("Error when extract entity: ", ex)
        
        finally:
            #Store in one place
            if self.en_sys_nim is not None: self.store_all_entity_found.extend(get_arr_nim)
            if self.en_sys_date is not None: self.store_all_entity_found.extend(get_arr_date)
            if self.en_sys_email is not None: self.store_all_entity_found.extend(get_arr_email)
            if self.en_sys_phone is not None: self.store_all_entity_found.extend(get_arr_phone)
            if self.en_sys_no_reg is not None: self.store_all_entity_found.extend(get_arr_no_reg)
            if self.en_sys_user_name is not None: self.store_all_entity_found.extend(get_arr_user_name)
            if self.en_sys_dorm_name is not None: self.store_all_entity_found.extend(get_arr_dorm_name)
            if self.en_sys_room_number is not None: self.store_all_entity_found.extend(get_arr_room_number)
            if self.en_sys_num_of_room is not None: self.store_all_entity_found.extend(get_arr_num_of_room)
            if self.en_sys_bed_position is not None: self.store_all_entity_found.extend(get_arr_bed_position)
            if self.en_sys_num_of_person is not None: self.store_all_entity_found.extend(get_arr_num_of_person)
            if self.en_sys_floor_position is not None: self.store_all_entity_found.extend(get_arr_floor_position)  

           
        #Store all entity in pandas Data Frame
        df_allArray = pd.DataFrame(self.store_all_entity_found) # store all entity in pandas Data Frame
        
        # print("number of entity: {0}".format(len(df_allArray.index)))
        
        if len(df_allArray.index) > 0:
            #Sorting by start index as descending
            df_allArray = df_allArray.sort_values(by=['StartIndex'], ascending=False) 
            
            #Reset Index data frame
            df_allArray = df_allArray.reset_index(drop=True) # reset Index data frame ke original order
            print(df_allArray)
            
            # #Get value of each entity
            # final_value = df_allArray["Value"].to_string(index=False)
            # # final_value = df_allArray["Value"]
            # final_value = re.sub(' ', '', final_value)
            # # print(final_value)
            
            #Mark entity
            # Call get_mark_each_entities. Passing ori_input_user and df_allArray
            txt_after_mark = self.get_mark_each_entities(ori_input_user, df_allArray)
            print("Teks mark: ", txt_after_mark)
            
            # Global final_chat
            # Remove all the entity found to be send to machine learning
            final_chat = re.sub("\<.*?\>","",txt_after_mark)
            final_chat = re.sub(r'[^\w\s]','', final_chat)
            final_chat = re.sub(' +', ' ', final_chat)
            # print("final chat: ", final_chat)
            
            # return final_value, final_chat
            
        else:
            # if there's no entity found
            final_chat = ori_input_user;


        return final_chat, df_allArray;


    def get_final_chat(self, input_user):
        
        txt_final_chat, df_entities = self.extract_entity(input_user)

        return txt_final_chat, df_entities;
    
    
    def get_mark_each_entities(self, txt_input_sentence, df_entity_found): 
        
        # print(len(df_entity_found))
        # do looping for replacing type entity to type1 type2 etc in descending order
        for i in range(len(df_entity_found.index)):
            # # print start and end index
            # print(df_entity_found.loc[i, "Entity"], df_entity_found.loc[i, "StartIndex"], df_entity_found.loc[i, "EndIndex"])
            
            # Replace type entity in original input string
            
            txt_input_sentence = txt_input_sentence[:df_entity_found.loc[i, "StartIndex"]] + df_entity_found.loc[i, "Type"] + txt_input_sentence[df_entity_found.loc[i, "EndIndex"]:]

            # print("ini text input:", txt_input_sentence)
            # print("\n\n")
            
        return txt_input_sentence

        
def main():
    system_entity = manage_extractor_entities()
    
    input_string = ', dua kosong satu, dua nol satu, dua ratus satu, 102'
    
    #Extract
    # txt_text_mark = system_entity.extract_entity(input_string) 
    # df_get_result = system_entity.extract_entity(input_string)
    #print(df_get_result)
    
    #Final text
    final_text, df_all_entities = system_entity.get_final_chat(input_string)
    
    print("====================================================================")
    
    # print("\nOriginal input text: \n{0}".format(input_string))
    print("\nFinal text: \n{0}".format(final_text))
    
    # print("FINAL ENTITY RECOGNITION")
    
    # print("====================================================================")
    #print(df_get_result)
    
    
    # #Final value
    # df_get_result = system_entity.get_final_value(input_string)
    # print("Final value: \n{0}".format(df_get_result))

if __name__ == "__main__" :
      main()