# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 02:53:30 2022

@author: Venisa Tewu & Elshadai Rampengan
"""
import string
import pickle
import joblib
import random
import warnings
warnings.filterwarnings("ignore")
from datetime import datetime

from difflib import SequenceMatcher
from json_parser import json_parser
from dict_resp_scenario import my_dict
from current_datetime import current_datetime
from context_management import context_management
from manage_all_entities import manage_extractor_entities

import pyrebase

# firebase for availability
firebaseAvail = {
    "apiKey": "AIzaSyAp-9JWZDGV58XW-c-Qh6AwesvkHVrt2IQ",
    "authDomain": "availabilitydb.firebaseapp.com",
    "databaseURL": "https://availabilitydb-default-rtdb.firebaseio.com",
    "projectId": "availabilitydb",
    "storageBucket": "availabilitydb.appspot.com",
    "messagingSenderId": "687385392153",
    "appId": "1:687385392153:web:06859f67d41394d0e2a688"
    };

firebaseavail = pyrebase.initialize_app(firebaseAvail)
databaseavail = firebaseavail.database()

# firebase for chat history
firebaseConfig = {
  "apiKey": "AIzaSyDBz8QAajBpjDsgPMHNvih1UNrYBB0_L4k",
  "authDomain": "chatinput.firebaseapp.com",
  "databaseURL": "https://chatinput-default-rtdb.firebaseio.com",
  "projectId": "chatinput",
  "storageBucket": "chatinput.appspot.com",
  "messagingSenderId": "360592263669",
  "appId": "1:360592263669:web:2ed28f1e88342a96b8f8bc"
};
firebasechat = pyrebase.initialize_app(firebaseConfig)
databaseChat = firebasechat.database()


# firebase for user booking information
config= {
    "apiKey": "AIzaSyBwgJsBIV1JAyJcSH6Gn-ugGxsm-gD5diA",
    "authDomain": "chatbotdatabase-ef472.firebaseapp.com",
    "projectId": "chatbotdatabase-ef472",
    "databaseURL": "https://chatbotdatabase-ef472-default-rtdb.firebaseio.com/",
    "storageBucket": "chatbotdatabase-ef472.appspot.com",
    "messagingSenderId": "1031854981385", 
    "appId": "1:1031854981385:web:a45207c42aca8e067cd3d8"
}
firebase = pyrebase.initialize_app(config)
database = firebase.database()

cr_datetime   = current_datetime()
threshold     = 0.70

def preprocess(chat):
    """
    Fungsi yang digunakan untuk melakukan praproses
    """
    #Konversi ke lowercase
    chat = chat.casefold()

    #Menghapus tanda baca
    tandabaca = tuple(string.punctuation)
    chat = ''.join(ch for ch in chat if ch not in tandabaca)

    return chat


def input_user(chat, id_unique_user):
    print("Original chat:", chat)
    print("Unique ID User: {0}".format(id_unique_user));
    #Context always update
    ctm           = context_management(id_unique_user)
    manage_entity = manage_extractor_entities()
    
    # datetime object containing current date and time
    now = datetime.now()
    
    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    
    # original chat
    chat_first = chat;
    
    #NLP
    chat_ori, df_all_entities = manage_entity.get_final_chat(chat)
    # print("Input chat: ", chat_ori)
    print(df_all_entities)
      
    #Praproses machine learning
    chat_ori = preprocess(chat_ori)
    
    #Prediksi intent pakai vektorisasi tf-idf
    vectorizer = joblib.load("./templates/php/trainData/vectorize.pkl")
    chat = vectorizer.transform([chat])

    filename = "./templates/php/trainData/svm.model"
    model = pickle.load(open(filename, 'rb'))
    
    # Prediksi dimulai memakai model yang sudah digenerate
    pred_intent = model.predict(chat)
    
    #Get data intent
    txt_intent = pred_intent[0]
    # print("Text intent: ", txt_intent)
    
    #Get data JSON for check similarity
    path = "./templates/php/trainData/data.json"
    jp = json_parser()
    jp.parse(path)
    df_train = jp.get_dataframe()
    
    #Selecting rows based on condition
    # If intent in dataframe equals to intent in predict
    df_get_intent = df_train[df_train['intents'] == ""+txt_intent]
    # print("List intents in predict tag:", df_get_intent)

    #Get data similarity
    df_get_intent['similarity'] = df_get_intent.apply(lambda x: SequenceMatcher(None, chat_ori, str(x['text_input'])).ratio(), axis=1)
    print(df_get_intent)

    #Get max similarity
    max_sim = df_get_intent['similarity'].max()
    print("Maximal similarity intent: ", max_sim)
    print("ori chat:", chat_ori)
    
    
    # to store every input user in firebase
    pred_chat = txt_intent
    max_sim_chat = max_sim
    dataChat = {"OriginalChat" : chat_first,
                "DateTime"      : dt_string,
                "PredictedIntent" : pred_chat,
                "MaxPrediction" : max_sim_chat
                }
    
    databaseChat.child("chat").push(dataChat)
    

    """
    Chatbot Scenario
    """
    #Check status context user
    if ctm.get_status_book() == "True": #Context true
        
        ctm.set_id(id_unique_user);
     
        #Kalau ada entity save to temporary data
        if len(df_all_entities.index) > 0:
            
            #Save informasi
            df_get_nama         = df_all_entities.loc[df_all_entities["Type"]=="<userName1>"]
            df_get_email        = df_all_entities.loc[df_all_entities["Type"]=="<EMAIL1>"]
            df_get_phone        = df_all_entities.loc[df_all_entities["Type"]=="<PHONE1>"]
            df_get_dorm_name    = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
            df_get_room_num     = df_all_entities.loc[df_all_entities["Type"]=="<noKamar1>"]
            df_get_bed_position = df_all_entities.loc[df_all_entities["Type"]=="<posisiBed1>"]
            
            
            #Jika user input lebih dari satu informasi 
            if len(df_get_nama.index) or len(df_get_email.index) or len(df_get_phone.index) or len(df_get_dorm_name.index) or len(df_get_room_num.index) or len(df_get_bed_position.index) > 0:
                try:
                    ctm.set_name(df_get_nama['Value'].iloc[0])
                except Exception as e: 
                    print("Error set name: ", e)
                        
                try:
                    ctm.set_email(df_get_email['Value'].iloc[0])
                except Exception as e: 
                    print("Error set email: ", e)
                        
                try:
                    ctm.set_phone(df_get_phone['Value'].iloc[0])
                except Exception as e: 
                    print("Error set phone: ", e)
                        
                try:
                    ctm.set_dorm_name(df_get_dorm_name['Value'].iloc[0])
                except Exception as e: 
                    print("Error set dorm name: ", e)
                    
                try:
                    ctm.set_room_num(df_get_room_num['Value'].iloc[0])
                except Exception as e: 
                    print("Error set room number: ", e)
                
                try:
                    ctm.set_posisi_bed(df_get_bed_position['Value'].iloc[0])
                except Exception as e: 
                    print("Error set bed position: ", e)
                
                
            
        """
        Jika ada intent "cancel" selama proses pemesanan
        """
        #Context status cancel menjadi true
        if ctm.get_status_cancel() == "True":
            #If input in pred "yes", all info for booking in temporary file will be remove
            if pred_intent == "yes":
                ctm.set_cancel_answer("yes")
                if ctm.read_cancel_answer() == "yes":
                    respon = "Pemesanan kamu telah dibatalkan.";
                    ctm.set_status_cancel("False")
                    ctm.set_status_book("False")
                    ctm.set_remove_info();
                    ctm.set_remove_ans()
                    
                    return respon
                    
            #If input in pred intent "no", all info for booking in temporary file will be keep
            if pred_intent == "no":
                ctm.set_cancel_answer("no")
                if ctm.read_cancel_answer() == "no":
                    respon = "Baik, pembatalan pesanan gagal";
                    ctm.set_status_cancel("False")
                    ctm.set_remove_ans()
                    
                    return respon
                    
            else:
                return random.choice(my_dict["resp_cancel"])
                
        
        #Check threshold > 0.85
        elif max_sim >= threshold: 
            #Jika ada intent "cancel", context status cancel menjadi true
            if pred_intent == "cancel" or pred_intent =="no":
                ctm.set_status_cancel("True")
                if ctm.get_status_cancel() == "True":
                    #Mengkonfirmasi kembali
                    respon = random.choice(my_dict["resp_cancel"])
                
            else:
                #Check status nama
                if ctm.status_name() == False:
                    # respon = "Oke😊, silahkan masukkan nama mahasiswa.";
                    respon = '<p>Silahkan input nama anda di bawah ini oke</p><form class="msger-inputareaa"><hr width="50%" align="center" > <input type="text" class="msger-inputt" id="textInput" placeholder="Enter your name..."><button id="btn-input-name" type="submit" onClick="inputNamee()"  class="msger-send-btnn"><img src="/static/images/Vector.png"></button></form>' 

                #Check status email
                elif ctm.status_email() == False:
                    respon = "Hi {0} 😊, silahkan masukkan email kamu.".format(ctm.get_name());
                
                #Check status phone
                elif ctm.status_phone() == False:
                    respon = "{0} 😊, silahkan masukkan nomor telepon kamu.".format(ctm.get_name());
                
                #Check status nama asrama
                elif ctm.status_dorm_name() == False:
                    respon = "{0} 😊, silahkan memasukkan nama asrama yang kamu inginkan. <br><br>e.g. : Annex, Edelweiss, Bougenville, Jasmine 1, Jasmine 2 untuk wanita, dan Crystal, Genset, Guest House untuk pria<br><br>Jika kamu ingin melihat setiap asramanya lebih detail, kamu dalam mengakses link dibawah ini: <br> <a href='https://www.google.com/maps/place/Klabat+University/@1.4172798,124.982042,17.65z/data=!4m5!3m4!1s0x32870a95df6309dd:0x21d86e4847556add!8m2!3d1.4175028!4d124.9839744' target='_blank'>Asrama di Universitas Klabat</a>".format(ctm.get_name());
                
                #Check status room number
                elif ctm.status_room_num() == False:
                    respon = "{0}, kamar nomor berapa yang kamu inginkan? <br><br>e.g. : <br>- Annex (101-112) <br>- Edelweiss (101-134, 201-234) <br>- Bougenville (101-104) <br>- Jasmine 1, 2 (101-112, 201-212, 301-312) <br>- Crystal (101-134, 201-234, 1101-1104, 2101-2104) <br>- Genset (101-112) <br>- Guest House (101-106)".format(ctm.get_name());
                
                #Check status posisi bed
                elif ctm.status_posisi_bed() == False:
                    respon = "{0}, posisi tempat tidur mana yang kamu inginkan? Sebelum menentukan pilihan, kamu bisa mengakses link berikut: <br> <a href='https://venisatewu.github.io/index.html' target='_blank'>Visualisasi Kamar Asrama Annex</a>".format(ctm.get_name());
                
                elif ctm.status_posisi_bed() == True:
                    val = ctm.get_dorm_name()
                    room_num = ctm.get_room_num()
                    no_bed = ctm.get_posisi_bed()

                    convert = int(room_num)

                    asrama = databaseavail.child("available").child(val).child(convert).child(no_bed).child("asrama").get()
                    number_room = databaseavail.child("available").child(val).child(convert).child(no_bed).child("no_kamar").get()
                    number_bed = databaseavail.child("available").child(val).child(convert).child(no_bed).child("no_bed").get()
                    status = databaseavail.child("available").child(val).child(convert).child(no_bed).child("status").get()

                    value_asrama = asrama.val()
                    value_number_room = number_room.val()
                    value_number_bed = number_bed.val()
                    value_status = status.val()

                    if ctm.get_dorm_name() == value_asrama and ctm.get_room_num() == value_number_room and ctm.get_posisi_bed()==value_number_bed and value_status== "avail":
                        respon = "Semua informasi telah diperoleh, ketik ya untuk lakukan konfirmasi pemesanan kamar?";
                    
                        # if user confirm yes it means the booking is success
                        if pred_intent == "yes":
                            id_user     = ctm.get_id()
                            name        = ctm.get_name()
                            email       = ctm.get_email()
                            phone       = ctm.get_phone()
                            dorm_name   = ctm.get_dorm_name()
                            room_num    = ctm.get_room_num()
                            posisi_bed  = ctm.get_posisi_bed()

                            data = {"ID"           : id_user,
                                    "Name"         : name, 
                                    "Email"        : email, 
                                    "PhoneNumber"  : phone,
                                    "DormName"     : dorm_name,
                                    "RoomNumber"   : room_num,
                                    "BedPosition"  : posisi_bed
                                    }
                            
                            # database set data into firebase
                            database.child("users").child(name).set(data)
                            # push data into firebase
                            # database.child("users").push(data)
                            
                            # get data from firebase
                            # users = database.child("users").child(name).get()
                            # print(users.val())
                            
                            # Get the specific information from a user to be display
                            id_book = database.child("users").child(name).child("ID").get()
                            name_book = database.child("users").child(name).child("Name").get()
                            email_book = database.child("users").child(name).child("Email").get()
                            no_hp_book = database.child("users").child(name).child("PhoneNumber").get()
                            dorm_name_book = database.child("users").child(name).child("DormName").get()
                            room_num_book = database.child("users").child(name).child("RoomNumber").get()
                            bed_position_book = database.child("users").child(name).child("BedPosition").get()
                            
                            # Display order
                            respon = "Pesananmu telah berhasil!🥳 <br>ID order : {0} <br>Nama : {1} <br>Email : {2} <br>Nomor HP : {3} <br>Asrama : {4} <br>Nomor Kamar : {5} <br>Posisi Tempat Tidur : {6}".format(id_book.val(), name_book.val(), email_book.val(), no_hp_book.val(), dorm_name_book.val(), room_num_book.val(), bed_position_book.val())
                            
                            # Change status available to not avail
                            databaseavail.child("available").child(val).child(convert).child(no_bed).update({"status":"not avail"})
                            
                            
                            ctm.set_status_cancel("False")
                            ctm.set_status_book("False")
                            ctm.set_remove_info();
                            ctm.set_remove_ans();
                            
                            
                        # condition when user already input all the information and when chatbot send confirmation message, user want to cancel it
                        if pred_intent == "cancel" or pred_intent =="no":
                            #Jika ada intent "cancel", context status cancel menjadi true
                            ctm.set_status_cancel("True")
                            if ctm.get_status_cancel() == "True":
                                #Mengkonfirmasi kembali
                                respon = random.choice(my_dict["resp_cancel"])

                    else:
                        # Chatbot check if room is available. If not, this respond will be shown
                        respon = "Maaf, kamar yang kamu inginkan tidak tersedia sekarang ini. Klik link berikut untuk melihat kamar yang tersedia.  <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/annex.php' target='_blank'>Asrama Annex</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/edelweiss.php' target='_blank'>Asrama Edelweiss</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/jasmine1.php' target='_blank'>Asrama Jasmine 1</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/jasmine2.php' target='_blank'>Asrama Jasmine 2</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/bougenville.php' target='_blank'>Asrama Bougenville</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/crystal.php' target='_blank'>Asrama Crystal</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/genset.php' target='_blank'>Asrama Genset</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/guesthouse.php' target='_blank'>Asrama Guest House</a>"
                        ctm.set_status_cancel("False")
                        ctm.set_status_book("True")
                        ctm.set_remove_room();

                return respon
        
        #if user input unrecognize predict (pred_intent < threshold)
        else:
            respon = "Sorry, chatbot tidak bisa respons pertanyaan lain, karena status masih dalam status pemenesanan kamar.";
            
            #Check status nama
            if ctm.status_name() == False:
                # respon = "Oke😊, silahkan masukkan nama mahasiswa";
                respon = '<p>Silahkan input nama anda di bawah ini ya</p><form class="msger-inputareaaa"><hr width="50%" align="center" > <input type="text" class="msger-inputtt" id="textInput" placeholder="Enter your name..."><button id="btn-input-name" type="submit" onClick="inputNameee()"  class="msger-send-btnnn"><img src="/static/images/Vector.png"></button></form>' 
                
            #Check status email
            elif ctm.status_email() == False:
                respon = "Hi {0} 😊, silahkan masukkan email kamu.".format(ctm.get_name());
            
            #Check status phone
            elif ctm.status_phone() == False:
                respon = "{0} 😊, silahkan masukkan nomor telepon kamu.".format(ctm.get_name());
            
            #Check status nama asrama
            elif ctm.status_dorm_name() == False:
                respon = "{0} 😊, silahkan memasukkan nama asrama yang kamu inginkan. <br><br>e.g. : Annex, Edelweiss, Bougenville, Jasmine 1, Jasmine 2 untuk wanita, dan Crystal, Genset, Guest House untuk pria<br><br>Jika kamu ingin melihat setiap asramanya lebih detail, kamu dalam mengakses link dibawah ini: <br> <a href='https://www.google.com/maps/place/Klabat+University/@1.4172798,124.982042,17.65z/data=!4m5!3m4!1s0x32870a95df6309dd:0x21d86e4847556add!8m2!3d1.4175028!4d124.9839744' target='_blank'>Asrama di Universitas Klabat</a>".format(ctm.get_name());
            
            #Check status room number
            elif ctm.status_room_num() == False:
                respon = "{0}, kamar nomor berapa yang kamu inginkan? <br><br>e.g. : <br>- Annex (101-112) <br>- Edelweiss (101-134, 201-234) <br>- Bougenville (101-104) <br>- Jasmine 1, 2 (101-112, 201-212, 301-312) <br>- Crystal (101-134, 201-234, 1101-1104, 2101-2104) <br>- Genset (101-112) <br>- Guest House (101-106)".format(ctm.get_name());
            
            #Check status posisi bed
            elif ctm.status_posisi_bed() == False:
                respon = "{0}, posisi tempat tidur mana yang kamu inginkan? Sebelum menentukan pilihan, kamu bisa mengakses link berikut: <br> <a href='https://venisatewu.github.io/index.html' target='_blank'>Visualisasi Kamar Asrama Annex</a>".format(ctm.get_name());
            
            elif ctm.status_posisi_bed() == True:
                    val = ctm.get_dorm_name()
                    room_num = ctm.get_room_num()
                    convert = int(room_num)
                    no_bed = ctm.get_posisi_bed()

                    asrama = databaseavail.child("available").child(val).child(convert).child(no_bed).child("asrama").get()
                    number_room = databaseavail.child("available").child(val).child(convert).child(no_bed).child("no_kamar").get()
                    number_bed = databaseavail.child("available").child(val).child(convert).child(no_bed).child("no_bed").get()
                    status = databaseavail.child("available").child(val).child(convert).child(no_bed).child("status").get()

                    value_asrama = asrama.val()
                    value_number_room = number_room.val()
                    value_number_bed = number_bed.val()
                    value_status = status.val()

                    if ctm.get_dorm_name() == value_asrama and ctm.get_room_num() == value_number_room and ctm.get_posisi_bed()==value_number_bed and value_status == "avail":
                        respon = "Semua informasi telah diperoleh, ketik ya untuk lakukan konfirmasi pemesanan kamar?";
                    
                        # if user confirm yes it means the booking is success
                        if pred_intent == "yes":
                            id_user     = ctm.get_id()
                            name        = ctm.get_name()
                            email       = ctm.get_email()
                            phone       = ctm.get_phone()
                            dorm_name   = ctm.get_dorm_name()
                            room_num    = ctm.get_room_num()
                            posisi_bed  = ctm.get_posisi_bed()

                            data = {"ID"           : id_user,
                                    "Name"         : name, 
                                    "Email"        : email, 
                                    "PhoneNumber"  : phone,
                                    "DormName"     : dorm_name,
                                    "RoomNumber"   : room_num,
                                    "BedPosition"  : posisi_bed
                                    }
                            
                            # database set data into firebase
                            database.child("users").child(name).set(data)
                            # push data into firebase
                            # database.child("users").push(data)
                            
                            # get data from firebase
                            # users = database.child("users").child(name).get()
                            # # print(users.val())
                            # respon = "Pesananmu telah berhasil!!!! {0}".format(users.val())
                            id_book = database.child("users").child(name).child("ID").get()
                            name_book = database.child("users").child(name).child("Name").get()
                            email_book = database.child("users").child(name).child("Email").get()
                            no_hp_book = database.child("users").child(name).child("PhoneNumber").get()
                            dorm_name_book = database.child("users").child(name).child("DormName").get()
                            room_num_book = database.child("users").child(name).child("RoomNumber").get()
                            bed_position_book = database.child("users").child(name).child("BedPosition").get()

                            # Display order
                            respon = "Pesananmu telah berhasil!🥳 <br>ID order : {0} <br>Nama : {1} <br>Email : {2} <br>Nomor HP : {3} <br>Asrama : {4} <br>Nomor Kamar : {5} <br>Posisi Tempat Tidur : {6}".format(id_book.val(), name_book.val(), email_book.val(), no_hp_book.val(), dorm_name_book.val(), room_num_book.val(), bed_position_book.val())
                            
                            databaseavail.child("available").child(val).child(convert).child(no_bed).update({"status":"not avail"})

                            ctm.set_status_cancel("False")
                            ctm.set_status_book("False")
                            ctm.set_remove_info();
                            ctm.set_remove_ans();

                        # condition when user already input all the information and when chatbot send confirmation message, user want to cancel it
                        if pred_intent == "cancel" or pred_intent =="no":
                            #Jika ada intent "cancel", context status cancel menjadi true
                            ctm.set_status_cancel("True")
                            if ctm.get_status_cancel() == "True":
                                #Mengkonfirmasi kembali
                                respon = random.choice(my_dict["resp_cancel"])
                    
                    else:
                        respon = "Maaf, kamar yang kamu inginkan tidak tersedia sekarang ini. Klik link berikut untuk melihat kamar yang tersedia.  <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/annex.php' target='_blank'>Asrama Annex</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/edelweiss.php' target='_blank'>Asrama Edelweiss</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/jasmine1.php' target='_blank'>Asrama Jasmine 1</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/jasmine2.php' target='_blank'>Asrama Jasmine 2</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/bougenville.php' target='_blank'>Asrama Bougenville</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/crystal.php' target='_blank'>Asrama Crystal</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/genset.php' target='_blank'>Asrama Genset</a> <br> <a href='http://34.128.83.59/elsven_chatbot/available_room/guesthouse.php' target='_blank'>Asrama Guest House</a>"
                        ctm.set_status_cancel("False")
                        ctm.set_status_book("True")
                        ctm.set_remove_room();
    
    else: #Context false. it means not in booking state
        
        """
        Intent "location". User ask location.
        """    
        if ctm.get_status_ask_location() == "True":
            
            # If user ask about dorm name while ask about location (when user don't know the dorm name)
            # lokasi asrama, asrama apa yang diinginkan, asrama apa yang ada, terdapat asrama annex, jasmine 1, dsb, annex, tampilkan lokasi
            if max_sim >= threshold:
                if pred_intent == "asrama":
                    return random.choice(my_dict["resp_asrama"])
                    
                    #Info asrama
            
                    if len(df_all_entities.index) > 0: #Info asrama
                        #Save informasi
                        df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "edelweiss":
                                return random.choice(my_dict["resp_location_edelweiss"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "annex":
                                return random.choice(my_dict["resp_location_annex"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "bougenville":
                                return random.choice(my_dict["resp_location_bougenville"])
                            
                        #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.get_req_dorm_name_not_specific() == "jasmine":
                                return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "jasmine 1":
                                return random.choice(my_dict["resp_location_jasmine_1"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "jasmine 2":
                                return random.choice(my_dict["resp_location_jasmine_2"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "genset":
                                return random.choice(my_dict["resp_location_genset"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "guest house":
                                return random.choice(my_dict["resp_location_guest_house"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "crystal" or ctm.read_req_dorm_name() == "crystal 1" or ctm.read_req_dorm_name() == "crystal 2" or ctm.read_req_dorm_name() == "crystal 3":
                                return random.choice(my_dict["resp_location_crystal"])
                    else:
                        ctm.set_status_ask_location("False") #set/ubah status context di dalam file config menjadi "False"
                        ctm.set_remove_info();
                    
            else:
                ctm.set_status_ask_location("False") #set/ubah status context di dalam file config menjadi "False"
                ctm.set_remove_info();
            
            # If user request dorm name for location without asking dorm name (user already know the dorm name)
            # lokasi asrama, asrama apa yang kamu inginkan, jasmine, tampilkan location
            
            if len(df_all_entities.index) > 0: #Info asrama
                #Save informasi
                df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "edelweiss":
                        return random.choice(my_dict["resp_location_edelweiss"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "annex":
                        return random.choice(my_dict["resp_location_annex"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "bougenville":
                        return random.choice(my_dict["resp_location_bougenville"])
                 
                #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "jasmine":
                        return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 1":
                        return random.choice(my_dict["resp_location_jasmine_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 2":
                        return random.choice(my_dict["resp_location_jasmine_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "genset":
                        return random.choice(my_dict["resp_location_genset"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "guest house":
                        return random.choice(my_dict["resp_location_guest_house"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal" or ctm.read_req_dorm_name() == "crystal 1" or ctm.read_req_dorm_name() == "crystal 2" or ctm.read_req_dorm_name() == "crystal 3":
                        return random.choice(my_dict["resp_location_crystal"])
                else:
                    ctm.set_status_ask_location("False") #set/ubah status context di dalam file config menjadi "False"
                    ctm.set_remove_info();
            else:
                ctm.set_status_ask_location("False") #set/ubah status context di dalam file config menjadi "False"
                ctm.set_remove_info();
    
        
        """
        Intent "room_model"
        """
        if ctm.get_status_ask_room_model() == "True":
            
            #If user ask about dorm name while ask about room model (when user don't know the dorm name)
            # model kamar, asrama apa yang diinginkan, asrama apa yang ada, terdapat asrama annex, jasmine 1, dsb, annex, tampilkan model 
            if max_sim >= threshold:
                if pred_intent == "asrama":
                    return random.choice(my_dict["resp_asrama"])
                    
                    #Info asrama
                    if len(df_all_entities.index) > 0: #Info asrama
                        #Save informasi
                        df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "edelweiss":
                                return random.choice(my_dict["resp_room_model_edelweiss"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "annex":
                                return random.choice(my_dict["resp_room_model_annex"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "bougenville":
                                return random.choice(my_dict["resp_room_model_bougenville"])
                        
                        #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.get_req_dorm_name_not_specific() == "jasmine":
                                return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "jasmine 1":
                                return random.choice(my_dict["resp_room_model_jasmine_1"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "jasmine 2":
                                return random.choice(my_dict["resp_room_model_jasmine_2"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "genset":
                                return random.choice(my_dict["resp_room_model_genset"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "guest house":
                                return random.choice(my_dict["resp_room_model_guest_house"])
                            
                        #If user input crystal only. Not specifically mention crystal 1, crystal 2, or crystal 3
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.get_req_dorm_name_not_specific() == "crystal" or ctm.read_req_dorm_name() == "crystal 1" or ctm.read_req_dorm_name() == "crystal 2" or ctm.read_req_dorm_name() == "crystal 3":
                                return random.choice(my_dict["resp_room_model_crystal"])
        
                    else:
                        ctm.set_status_ask_room_model("False")
                        ctm.set_remove_info();
                            
            else:
                ctm.set_status_ask_room_model("False")
                ctm.set_remove_info();
                # ctm.set_status_ask_room_model("False") #set/ubah status context di dalam file config menjadi "False"
            
            #If user request dorm name for room model witout asking dorm name (user already know the dorm name)
            # model kamar, asrama apa yang kamu inginkan, jasmine, tampilkan model kamar
            if len(df_all_entities.index) > 0: #Info asrama
                #Save informasi
                df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "edelweiss":
                        return random.choice(my_dict["resp_room_model_edelweiss"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "annex":
                        return random.choice(my_dict["resp_room_model_annex"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "bougenville":
                        return random.choice(my_dict["resp_room_model_bougenville"])
                 
                #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "jasmine":
                        return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 1":
                        return random.choice(my_dict["resp_room_model_jasmine_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 2":
                        return random.choice(my_dict["resp_room_model_jasmine_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "genset":
                        return random.choice(my_dict["resp_room_model_genset"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "guest house":
                        return random.choice(my_dict["resp_room_model_guest_house"])
                
                #If user input crystal only. Not specifically mention crystal 1, crystal 2, or crystal 3
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "crystal" or ctm.read_req_dorm_name() == "crystal 1" or ctm.read_req_dorm_name() == "crystal 2" or ctm.read_req_dorm_name() == "crystal 3":
                        return random.choice(my_dict["resp_room_model_crystal"])
                else:
                    ctm.set_status_ask_room_model("False")
                    ctm.set_remove_info();
            else:
                ctm.set_status_ask_room_model("False")
                ctm.set_remove_info();
        
        
        """
        Intent "facility"
        """
        if ctm.get_status_ask_facility() == "True":
            
            #If user ask about dorm name while ask about fasilitas (when user don't know the dorm name)
            # fasilitas, asrama apa yang diinginkan, asrama apa yang ada, terdapat asrama annex, jasmine 1, dsb, annex, tampilkan setiap fasilitas 
            if max_sim >= threshold:
                if pred_intent == "asrama":
                    return random.choice(my_dict["resp_asrama"])
                    
                    #Info asrama
                    if len(df_all_entities.index) > 0: #Info asrama
                        #Save informasi
                        df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "edelweiss":
                                return random.choice(my_dict["resp_facility_edelweiss"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "annex" or ctm.read_req_dorm_name() == "anex":
                                return random.choice(my_dict["resp_facility_annex"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "bougenville" or ctm.read_req_dorm_name() == "bougenvile" or ctm.read_req_dorm_name() == "bugenville" or ctm.read_req_dorm_name() == "bugenvile" or ctm.read_req_dorm_name() == "bougenfille" or ctm.read_req_dorm_name() == "bougenfile" or ctm.read_req_dorm_name() == "bugenfille" or ctm.read_req_dorm_name() == "bugenfile":
                                return random.choice(my_dict["resp_facility_bougenville"])
                        
                        #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.get_req_dorm_name_not_specific() == "jasmine":
                                return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "jasmine 1":
                                return random.choice(my_dict["resp_facility_jasmine_1"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "jasmine 2":
                                return random.choice(my_dict["resp_facility_jasmine_2"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "genset":
                                return random.choice(my_dict["resp_facility_genset"])
                            
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "guest house":
                                return random.choice(my_dict["resp_facility_guest_house"])
                            
                        #If user input crystal only. Not specifically mention crystal 1, crystal 2, or crystal 3
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.get_req_dorm_name_not_specific() == "crystal":
                                return "Di asrama Crystal terbagi menjadi tiga. Crystal 1, Crystal 2, dan Crystal 3. Crystal mankah yang kamu maksud?"
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "crystal 1":
                                return random.choice(my_dict["resp_facility_crystal_1"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "crystal 2":
                                return random.choice(my_dict["resp_facility_crystal_2"])
                        
                        if len(df_get_dm_room_model.index) > 0:
                            ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                            if ctm.read_req_dorm_name() == "crystal 3":
                                return random.choice(my_dict["resp_facility_crystal_3"])
                    else:
                        ctm.set_status_ask_facility("False")
                        ctm.set_remove_info();
            else:
                ctm.set_status_ask_facility("False")
                ctm.set_remove_info();
            
            #If user request dorm name for room model witout asking dorm name (user already know the dorm name)
            # model kamar, asrama apa yang kamu inginkan, jasmine, tampilkan model kamar
            if len(df_all_entities.index) > 0: #Info asrama
                #Save informasi
                df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "edelweiss":
                        return random.choice(my_dict["resp_facility_edelweiss"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "annex" or ctm.read_req_dorm_name() == "anex":
                        return random.choice(my_dict["resp_facility_annex"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "bougenville" or ctm.read_req_dorm_name() == "bougenvile" or ctm.read_req_dorm_name() == "bugenville" or ctm.read_req_dorm_name() == "bugenvile" or ctm.read_req_dorm_name() == "bougenfille" or ctm.read_req_dorm_name() == "bougenfile" or ctm.read_req_dorm_name() == "bugenfille" or ctm.read_req_dorm_name() == "bugenfile":
                        return random.choice(my_dict["resp_facility_bougenville"])
                 
                #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "jasmine":
                        return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine mankah yang kamu maksud?"
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 1":
                        return random.choice(my_dict["resp_facility_jasmine_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 2":
                        return random.choice(my_dict["resp_facility_jasmine_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "genset":
                        return random.choice(my_dict["resp_facility_genset"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "guest house":
                        return random.choice(my_dict["resp_facility_guest_house"])
                
                #If user input crystal only. Not specifically mention crystal 1, crystal 2, or crystal 3
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "crystal":
                        return "Di asrama Crystal terbagi menjadi tiga. Crystal 1, Crystal 2, dan Crystal 3. Crystal manakah yang kamu maksud?"
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal 1":
                        return random.choice(my_dict["resp_facility_crystal_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal 2":
                        return random.choice(my_dict["resp_facility_crystal_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal 3":
                        return random.choice(my_dict["resp_facility_crystal_3"])
                else:
                    ctm.set_status_ask_facility("False")
                    ctm.set_remove_info();
            else:
                ctm.set_status_ask_facility("False")
                ctm.set_remove_info();
            
            
            
                
        # --------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                
        #Check threshold > 0.85
        if max_sim >= threshold:
            
            #Scenario greeting
            if pred_intent == "greeting":
                # respon = '<a href="https://elshacgr.github.io/jasmine-two-room" target="_blank">project homepage</a>' #klik link room
                # return respon
                return random.choice(my_dict["resp_greetings"])
                

            #Scenario thanks
            if pred_intent == "thanks":
                return random.choice(my_dict["resp_thanks"])
                
            #Scenario goodbye
            if pred_intent == "goodbye":
                return random.choice(my_dict["resp_goodbye"])
            
            #Scenario handle "no"
            if pred_intent == "no":
                return random.choice(my_dict["resp_goodbye"])
              
            
            
            """
            Booking
            """
            #Scenario handle pemesanan kamar asrama
            if pred_intent == "booking":
                ctm.set_status_book("True") # set status context di dalam file config
                
                if ctm.get_status_book() == "True":
                   respon = '<p>Silahkan input nama anda di bawah ini</p><form class="msger-inputarea"><hr width="50%" align="center" > <input type="text" class="msger-input" id="textInput" placeholder="Enter your name..."><button id="btn-input-name" type="submit" onClick="inputName()" class="msger-send-btn"><img src="/static/images/Vector.png"></button></form>' 
                   # respon = random.choice(my_dict["resp_booking"])
                   data = 'nama: "Nama Mahasiswa'
                  
                   return respon, data
            
            
            
            """
            Information about dormitory
            """
            #Scenario ask about banyak asrama
            if pred_intent == "asrama":
                respon = random.choice(my_dict["resp_asrama"])
                # print("VamEux: ", respon)
                
            #Scenario ask about rules asrama
            if pred_intent == "rules":
                respon = random.choice(my_dict["resp_rules"])
            
            # if user already input location and the dorm name at the same time
            if pred_intent == "location" and len(df_all_entities.index) > 0 :    
            #If user request dorm name for location witout asking dorm name (user already know the dorm name)
            # lokasi asrama, asrama apa yang kamu inginkan, jasmine, tampilkan location
                #Save informasi
                df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "edelweiss":
                        return random.choice(my_dict["resp_location_edelweiss"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "annex":
                        return random.choice(my_dict["resp_location_annex"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "bougenville":
                        return random.choice(my_dict["resp_location_bougenville"])
                 
                #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "jasmine":
                        ctm.set_status_ask_location("True");
                        return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 1":
                        return random.choice(my_dict["resp_location_jasmine_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 2":
                        return random.choice(my_dict["resp_location_jasmine_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "genset":
                        return random.choice(my_dict["resp_location_genset"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "guest house":
                        return random.choice(my_dict["resp_location_guest_house"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal" or ctm.read_req_dorm_name() == "crystal 1" or ctm.read_req_dorm_name() == "crystal 2" or ctm.read_req_dorm_name() == "crystal 3":
                        return random.choice(my_dict["resp_location_crystal"])
                else:
                    ctm.set_status_ask_location("False") #set/ubah status context di dalam file config menjadi "False"
                    ctm.set_remove_info();
            else:
                ctm.set_status_ask_location("False") #set/ubah status context di dalam file config menjadi "False"
                ctm.set_remove_info();
            
            
            #Scenario ask about location asrama without adding entities
            if pred_intent == "location":
                ctm.set_status_ask_location("True")
                if ctm.get_status_ask_location() == "True":
                    respon = random.choice(my_dict["resp_ask_location"])
            #----------------------------------------------------------------------------------------------------------------------------------------------
                
            #Scenario ask about kapasitas
            if pred_intent == "kapasitas":
                respon = random.choice(my_dict["resp_kapasitas"]) ##
                
            #Scenario handle ask about cara_pesan
            if pred_intent == "cara_pesan":
                respon = random.choice(my_dict["resp_cara_pesan"]) ##
                
            #Scenario handle ask about floor
            if pred_intent == "floor":
                respon = random.choice(my_dict["resp_floor"]) ## 
            
            # Scenario handle ask about dorm room model
            # if user already input drom model and the dorm name at the same time
            if pred_intent=="room_model" and len(df_all_entities.index) > 0:
                
                #If user request dorm name for room model witout asking dorm name (user already know the dorm name)
                    #Save informasi
                df_get_dm_room_model = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "edelweiss":
                        return random.choice(my_dict["resp_room_model_edelweiss"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "annex":
                        return random.choice(my_dict["resp_room_model_annex"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "bougenville":
                        return random.choice(my_dict["resp_room_model_bougenville"])
                 
                #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "jasmine":
                        ctm.set_status_ask_room_model("True");
                        return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 1":
                        return random.choice(my_dict["resp_room_model_jasmine_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 2":
                        return random.choice(my_dict["resp_room_model_jasmine_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "genset":
                        return random.choice(my_dict["resp_room_model_genset"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "guest house":
                        return random.choice(my_dict["resp_room_model_guest_house"])
                
                #If user input crystal only. Not specifically mention crystal 1, crystal 2, or crystal 3
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "crystal" or ctm.read_req_dorm_name() == "crystal 1" or ctm.read_req_dorm_name() == "crystal 2" or ctm.read_req_dorm_name() == "crystal 3":
                        return random.choice(my_dict["resp_room_model_crystal"])
                else:
                    ctm.set_status_ask_room_model("False")
                    ctm.set_remove_info();
            else:
                ctm.set_status_ask_room_model("False")
                ctm.set_remove_info();
                        
            # ask room model without adding entities
            if pred_intent == "room_model":
                ctm.set_status_ask_room_model("True")
    
                if ctm.get_status_ask_room_model() == "True":
                    respon = random.choice(my_dict["resp_ask_model_room"])
                    
            
            #----------------------------------------------------------------------------------------------------------------------#
            #Scenario ask about facility
            # if user already input facility and the dorm name at the same time
            if pred_intent == "facility" and len(df_all_entities.index) > 0 :    
                #Save informasi
                df_get_dm_room_model         = df_all_entities.loc[df_all_entities["Type"]=="<dormName1>"]
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "edelweiss":
                        return random.choice(my_dict["resp_facility_edelweiss"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "annex":
                        return random.choice(my_dict["resp_facility_annex"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "bougenville":
                        return random.choice(my_dict["resp_facility_bougenville"])
                 
                #If user input jasmine only. Not specifically mention jasmine 1 or jasmine 2
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "jasmine":
                        ctm.set_status_ask_facility("True");
                        return "Di asrama Jasmine terbagi menjadi dua. Jasmine 1 dan Jasmine 2. Jasmine manakah yang kamu maksud?"
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 1":
                        return random.choice(my_dict["resp_facility_jasmine_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "jasmine 2":
                        return random.choice(my_dict["resp_facility_jasmine_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "genset":
                        return random.choice(my_dict["resp_facility_genset"])
                    
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "guest house":
                        return random.choice(my_dict["resp_facility_guest_house"])
                
                #If user input crystal only. Not specifically mention crystal 1, crystal 2, or crystal 3
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name_not_specific(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.get_req_dorm_name_not_specific() == "crystal":
                        ctm.set_status_ask_facility("True")
                        return "Di asrama Crystal terbagi menjadi tiga. Crystal 1, Crystal 2, dan Crystal 3. Crystal manakah yang kamu maksud?"
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal 1":
                        return random.choice(my_dict["resp_facility_crystal_1"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal 2":
                        return random.choice(my_dict["resp_facility_crystal_2"])
                
                if len(df_get_dm_room_model.index) > 0:
                    ctm.set_req_dorm_name(df_get_dm_room_model['Value'].iloc[0])
                    if ctm.read_req_dorm_name() == "crystal 3":
                        return random.choice(my_dict["resp_facility_crystal_3"])
                    
                else:
                    ctm.set_status_ask_facility("False") #set/ubah status context di dalam file config menjadi "False"
                    ctm.set_remove_info();
            else:
                ctm.set_status_ask_facility("False") #set/ubah status context di dalam file config menjadi "False"
                ctm.set_remove_info();
                
            if pred_intent == "facility":
                ctm.set_status_ask_facility("True")
                if ctm.get_status_ask_facility() == "True":
                    respon = random.choice(my_dict["resp_ask_facility"])
            
            #----------------------------------------------------------------------------------------------------------------------#
               
           
            """
            Related to dormitory and Unklab
            """
            #Scenario ask about unklab
            if pred_intent == "about_unklab":
                respon = random.choice(my_dict["resp_about_unklab"]) 
            #Scenario ask address unklab
            if pred_intent == "address_unklab":
                respon = random.choice(my_dict["resp_address_unklab"]) 
            #Scenario ask about payments info
            if pred_intent == "payments":
                respon = random.choice(my_dict["resp_payments"])
                
            #Scenario ask about dining
            if pred_intent == "dining":
                respon = random.choice(my_dict["resp_dining"])
                
            #Scenario ask about price
            if pred_intent == "price":
                respon = random.choice(my_dict["resp_price"])
                
            #Scenario ask about kepas_name
            if pred_intent == "kepas_name":
                respon = random.choice(my_dict["resp_kepas_name"]) 

            #Scenario ask about contact_dorm
            if pred_intent == "contact_dorm":
                respon = random.choice(my_dict["resp_contact_dorm"]) 
            
          
            
            
            """
            Chatbot general knowledge
            """
            #Scenario ask about chatbot identity
            if pred_intent == "identity":
                respon = random.choice(my_dict["resp_identity"])
                
            #Scenario ask about chatbot age
            if pred_intent == "age":
                respon = random.choice(my_dict["resp_age"])
                
            #Scenario ask about ability
            if pred_intent == "ability":
                respon = random.choice(my_dict["resp_ability"])
                
            #Scenario ask about language 
            if pred_intent == "language":
                respon = random.choice(my_dict["resp_language"])
            
            #Scenario ask about who the creator
            if pred_intent == "creator":
                respon = random.choice(my_dict["resp_creator"])    
            
            #Scenario ask about what is chatbot
            if pred_intent == "chatbot":
                respon = random.choice(my_dict["resp_chatbot"])
                
            #Scenario ask about what is programming
            if pred_intent == "programming":
                respon = random.choice(my_dict["resp_programming"])
            
                
            
            
            """
            Random chat from user
            """
            #Scenario ask about what is chatbot doing right now
            if pred_intent == "activity":
                respon = random.choice(my_dict["resp_chatbot"])
        
            #Scenario laugh
            if pred_intent == "laugh":
                return random.choice(my_dict["resp_laugh"])
            
            #Scenario jokes
            if pred_intent == "jokes":
                return random.choice(my_dict["resp_jokes"])
            
            #Scenario love
            if pred_intent == "love":
                return random.choice(my_dict["resp_love"])
            
            #Scenario sad
            if pred_intent == "sad":
                return random.choice(my_dict["resp_sad"])
            
            #Scenario sad
            if pred_intent == "happy":
                return random.choice(my_dict["resp_happy"])
            
            #Scenario handle sorry
            if pred_intent == "sorry":
                return random.choice(my_dict["resp_sorry"]) ##
            
            #Scenario handle help
            if pred_intent == "help":
                return random.choice(my_dict["resp_help"])
            
            #Scenario ask about if chatbot alive
            if pred_intent == "alive":
                return random.choice(my_dict["resp_alive"])
            
            #Scenario ask about robot
            if pred_intent == "robot":
                return random.choice(my_dict["resp_robot"])
            
            #Scenario ask about whatsup
            if pred_intent == "whatsup":
                return random.choice(my_dict["resp_whatsup"])
            
            #Scenario ask about motivation
            if pred_intent == "motivation":
                return random.choice(my_dict["resp_motivation"])
            
            #Scenario ask about robot
            if pred_intent == "robot":
                return random.choice(my_dict["resp_robot"])
                
            #Scenario handle negative words
            if pred_intent == "negative":
                respon = random.choice(my_dict["resp_negative"])
            
            if pred_intent == "gender":
                respon = random.choice(my_dict["resp_gender"])
            
            
            
            """
            Current time
            """
            #Scenario handle current time
            if pred_intent == "time":
                respon = cr_datetime.current_waktu()
                
            #Scenario handle current date
            if pred_intent == "date":
                respon = cr_datetime.current_date()
                
            #Scenario handle current day
            if pred_intent == "day":
                respon = cr_datetime.current_day()
                
            #Scenario handle current month
            if pred_intent == "month":
                respon = cr_datetime.current_month()
                
            #Scenario handle current year
            if pred_intent == "year":
                respon = cr_datetime.current_year()
                
                
            #When input user in pred intent "cancel" while booking context false
            if pred_intent == "cancel" or pred_intent == "yes"  or pred_intent == "no":
                respon = random.choice(my_dict["resp_default"])
           
        else:
            respon = random.choice(my_dict["resp_default"])


       
    return respon
            


def get_response(chat):
    x = input_user(chat)
    
    return x

#-------------------------------------------------------------------------------------------------------------------------------------------------


#Rest API using flask
from flask import Flask, render_template, request

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    user_text = request.args.get('msg')
    id_unique = request.args.get('id_unique')
    return input_user(user_text, id_unique)

if __name__ == "__main__":
    app.run()

#------------------------------------------------------------------------------------------------------------------------------------------------

# def main():
#     mo = ""
#     text = get_response(mo)
#     print(text)

# if __name__ == "__main__" :
#         main()