# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:21:52 2022

@author: Venisa Tewu
"""

import configparser
import os.path
import shutil

class context_management:
    
    def __init__(self, id_user_unique):
        self.status = False;
        
        self.id_user = id_user_unique;
        print("Context Management Unique ID User: {0}".format(self.id_user));
        
        self.file_config_id = "./static/config/config_file_{0}.ini".format(self.id_user);
        if os.path.exists(self.file_config_id):
            print("So ada file config id.");
        else:
            print("Belum ada file config id.");
            shutil.copy2("./static/config/config_file.ini", self.file_config_id);
       
    """
    Context status booking
    """
    #Set status for booking
    def set_status_book(self, txt_status):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        info_context["status_book"] = txt_status;
        self.status = txt_status;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #Get status for booking
    def get_status_book(self): #get
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        return info_context["status_book"];

    
    """
    Information for booking
    """
    #2. Set/update status "id"
    def set_id(self, txt_id):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["id"] = txt_id;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #3. Get name from config_name
    def get_id(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["id"];
    
    ### 1. Check status "name"
    def status_name(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        if len(info_context["name"]) > 0:
            return True;
        else:
            return False;
    
    #2. Set/update status "name"
    def set_name(self, txt_name):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["name"] = txt_name;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #3. Get name from config_name
    def get_name(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["name"];
    
    ### 1. Check status "email"
    def status_email(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        if len(info_context["email"]) > 0:
            return True;
        else:
            return False;
    #2. Set/update status "email"
    def set_email(self, txt_email):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["email"] = txt_email;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #3. Get email from config_name
    def get_email(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["email"];
        
    ### 1. Check status "nomor hp"
    def status_phone(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        if len(info_context["phone"]) > 0:
            return True;
        else:
            return False;
    
    #2. Set/update status "nomor hp"
    def set_phone(self, txt_phone):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["phone"] = txt_phone;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
            
    #3. Get name from config_name
    def get_phone(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["phone"];
    
    ### 1. Check status "nama asrama"
    def status_dorm_name(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        if len(info_context["dorm_name"]) > 0:
            return True;
        else:
            return False;
    
    #2. Set/update status "nama asrama"
    def set_dorm_name(self, txt_nama_asrama):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["dorm_name"] = txt_nama_asrama;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
            
    #3. Get name from config_name
    def get_dorm_name(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["dorm_name"];
      
    ### 1. Check status "posisi bed"
    def status_room_num(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        if len(info_context["room_num"]) > 0:
            return True;
        else:
            return False;
    
    #2. Set/update status "posisi bed"
    def set_room_num(self, txt_room_number):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["room_num"] = txt_room_number;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #3. Get room number from config_name
    def get_room_num(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["room_num"];
    
    ### 1. Check status "posisi bed"
    def status_posisi_bed(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        if len(info_context["posisi_bed"]) > 0:
            return True;
        else:
            return False;
    
    #2. Set/update status "posisi bed"
    def set_posisi_bed(self, txt_posisi_bed):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["posisi_bed"] = txt_posisi_bed;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #3. Get room number from config_name
    def get_posisi_bed(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        return info_context["posisi_bed"];
     
         
     
    """
    Context status cancel
    """
    #Set status for booking
    def set_status_cancel(self, txt_status):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_cancel"]
        info_context["status_cancel"] = txt_status;
        self.status = txt_status;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #Get status for booking
    def get_status_cancel(self): #get
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_cancel"]
        return info_context["status_cancel"];
    
    def set_cancel_answer(self, txt_dorm_name):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_cancel"]
        info_context["cancel_answer"] = txt_dorm_name;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    def read_cancel_answer(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_cancel = config_obj.get("context_cancel", "cancel_answer")
        return info_cancel
    
    def set_remove_ans(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_cancel"]
        info_context["cancel_answer"] = "";
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile) 
    
    
    
    """
    Remove all information in get info book when cancel
    """
    #Remove all info when cancel
    def set_remove_info(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["name"] = "";
        info_context["email"] = "";
        info_context["phone"] = "";
        info_context["dorm_name"] = "";
        info_context["room_num"] = "";
        info_context["posisi_bed"] = "";
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)        
    def set_remove_room(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_book"]
        info_context["dorm_name"] = "";
        info_context["room_num"] = "";
        info_context["posisi_bed"] = "";
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)        

    
    """
    Context status ask about dorm room model
    """
    #Set status ask about room
    def set_status_ask_room_model(self, txt_status):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        info_context["status_ask_room_model"] = txt_status;
        self.status = txt_status;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #Get status ask about room
    def get_status_ask_room_model(self): #get
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        return info_context["status_ask_room_model"];


    
    """
    Context status ask about location dormitory
    """
    #Set status ask about room
    def set_status_ask_location(self, txt_status):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        info_context["status_ask_location"] = txt_status;
        self.status = txt_status;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #Get status ask about location
    def get_status_ask_location(self): #get
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        return info_context["status_ask_location"];    

    
    """
    Context status ask about dormitory facility
    """
    #Set status ask about room
    def set_status_ask_facility(self, txt_status):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        info_context["status_ask_facility"] = txt_status;
        self.status = txt_status;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
    
    #Get status ask about room
    def get_status_ask_facility(self): #get
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["context_management"]
        return info_context["status_ask_facility"];

    
    """
    Information for ask about dorm room model
    """
    #Set status ask about room
    def set_req_dorm_name_not_specific(self, txt_dorm_name):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_asrama"]
        info_context["req_dorm_name_not_specific"] = txt_dorm_name;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
        
    #Get dorm name after set req dorm name not specific already satisfied in req_dorm_name_not_specific on config_file
    def get_req_dorm_name_not_specific(self): #get
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_asrama"]
        return info_context["req_dorm_name_not_specific"];
    
    def set_req_dorm_name(self, txt_dorm_name):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_context = config_obj["get_info_asrama"]
        info_context["req_dorm_name"] = txt_dorm_name;
        #Write changes back to file
        with open(self.file_config_id, 'w') as configfile:
            config_obj.write(configfile)
        
    def read_req_dorm_name(self):
        config_obj = configparser.ConfigParser()
        config_obj.read(self.file_config_id)
        info_dorm_name = config_obj.get("get_info_asrama", "req_dorm_name")
        return info_dorm_name
    

        
# def main():
#     ctm = context_management()
    
# #     # ctm.set_status("False")
# #     # ctm.display_status();
# #     # sts_name = ctm.status_name()
# #     # sts_email = ctm.status_email()
# #     # sts_phone = ctm.status_phone()
# #     # sts_dorm_name = ctm.read_status_cancel()
# #     ctm.set_status_ask_room_model("False")
#     x = ctm.get_id()
#     print(x)

    
# #     # print("status name: ", sts_name)
# #     # print("status email: ", sts_email)
# #     # print("status nomor hp: ", sts_phone)
# #     print("name: ", x)
# #     # ctm.status = False
# #     # ctm.turn_on_context();
# #     # print(ctm.status)


# if __name__ == "__main__" :
#       main()