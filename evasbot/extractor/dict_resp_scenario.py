# -*- coding: utf-8 -*-
'''
Created on Sun Oct 16 00:18:36 2022

@author: Venisa Tewu
'''

my_dict = {
    'resp_greetings'         : ['Selamat datang di EVAs Bot. Ada yang bisa saya bantu?',
                               'Hay! Senang melihatmu kembali! Apa yang Anda butuhkan?',
                               'Hallo!! EVAs Bot disini. Ada yang bisa saya bantu terkait asrama?',
                               'Holla!!! Nama saya EVAs Bot. Beri tahu saya apa yang dapat saya bantu terkait asram',
                               'Terima kasih telah mengubungi saya, EVAs Bot. Ada yang bisa saya bantu terkait asrama?',
                               'Hi there! Selamat datang di EVAs Bot. Saya senang sekali kamu datang kemari. Ada yang bisa saya bantu?',
                               'Hai! Selamat datang di EVAs Bot. Jika Anda membutuhkan bantuan terkait asrama, saya selalu di sini siap membantu Anda.',
                               'Hi, senang berjumpa denganmu😊. EVAs Bot siap membantu kamu perihal informasi dan pemesanan kamar asrama di Universitas Klabat.',
                               'Hai! Selamat datang di EVAs Bot Universitas Klabat! Di sini kamu dapat mengetahui informasi tentang asrama dan memesan kamar asrama.',
                               'Holla!! Saya EVAs Bot yang akan menjadi asisten virtual Anda. Anda dapat bertanya ataupun memesan kamar asrama langsung kepada saya😊',
                               'Haii!! Apa kabar? Selamat datang di EVAs Bot. Silahkan tanyakan apa saja yang berkaitan dengan asrama kepada saya. Saya siap membantu😊',
                               'Hallo, ini EVAs Bot sebagai asisten virtual yang siap membantu Anda dalam layanan informasi dan pemesanan kamar asrama di Universitas Klabat.',
                               'Sangat senang berjumpa denganmu! Saya EVAs Bot, asisten virtual yang siap membantu Anda dalam memberikan informasi dan memesan kamar asrama di Universitas Klabat😊',
                               'Selamat datang di EVAs Bot. Saya bisa membantu Anda menemukan informasi mengenai asrama di Universitas Klabat dan juga dapat membantu Anda dalam pemesanan kamar asrama.',
                               'Selamat datang! Terima kasih telah mempercayakan saya EVAs Bot sebagai asisten virtual Anda dalam memesan atau mencari informasi terkait asrama. Ada yang bisa saya bantu?🤓'],
    
    'resp_thanks'           : ['Senang bisa membantu', 
                               'Dengan senang hati😊',
                               'Terima kasih kembali😊',
                               'Itu tidak masalah bagi saya.',
                               'Terima kasih, datang kembali!',
                               'Saya senang bisa membantu Anda😊',
                               'Sama-sama. Ada lagi yang bisa saya bantu?',
                               'Sudah menjadi tugas saya untuk membantu Anda.',
                               'Bukan masalah. Apa kau masih memiliki pertanyaan?',
                               'Terima kasih kembali, sangat senang bercakap dengan Anda🥺',
                               'Tidak masalah. Datanglah kembali jika kamu membutuhkan bantuan😊',
                               'Sama-sama, beritahu saya jika masih ada lagi yang ingin kamu tanyakan',
                               'Bukan masalah, Tidak perlu berterima kasih, saya sangat senang bisa membantu.',
                               'Terima kasih telah datang! Semoga saya bisa terus membantu Anda terkait asrama😊',
                               'Biarkan saya tahu jika ada hal lain yang bisa saya lakukan untuk Anda. Senang dapat membantu Anda😊'],
    
    'resp_goodbye'          : ['Bye bye!',
                               'Selamat tinggal!',
                               'Selamat menjalani harimu😊',
                               'Sampai jumpa di lain waktu ya',
                               'Salam perpisahan dari EVAs Bot😊🙏🏼',
                               'Dadah! Jangan lupa datang lagi ya😊',
                               'Byebye, semoga kita bisa bertemu kembali👋',
                               'Sampai jumpa nanti, silahkan datang kembali',
                               'Sampai jumpa lagi, semoga harimu menyenangkan.',
                               'Percakapan yang sangat menyenangkan, bye bye!!!',
                               'Terima kasih telah mempercayakan saya sebagai asisten virtual Anda.',
                               'Bye! Terima kasih telah mempercayai saya. Semoga hari Anda menyenangkan.',
                               'Terima kasih sudah mempercayai saya, EVAs Bot. Semoga kamu senang bercakap dengan saya🥺😊',
                               'Terima kasih atas kedatangan Anda. Semoga pengalaman Anda di EVAs Bot hari ini menyenangkan!😊🙏🏼',
                               'Terima kasih!! Hubungi developer saya di @elshacgr dan @venisatewu jikalau ada beberapa hal yang tidak bisa saya mengerti. Itu sangat-sangat membantu saya untuk belajar.'],


    #Booking
    'resp_booking'          : ['Baik. Namun, saya membutuhkan informasi Anda terlebih dahulu. Bisa tahu atas nama mahasiswa siapa? \n\nMohon memasukkan nama di dalam tanda kutip dua seperti <Nama Mahasiswa>', 
                               'Ok. Mari kita mulai pemesanan kamarnya. <br>Saya membutuhkan beberapa informasi kamu berupa: <br>- Nama <br> Bisa tahu atas nama mahasiswa siapa? \n\nMohon memasukkan nama di dalam tanda kutip dua seperti "Nama Mahasiswa"'],
                               # 'Ok. Mari kita mulai pemesanan kamarnya. Bisa tahu atas nama mahasiswa siapa? \n\nMohon memasukkan nama di dalam tanda kutip dua seperti "Nama Mahasiswa"'],
    
    
    #Information about dormitory
    'resp_asrama'           : ['Universitas Klabat memiliki 7 asrama diantaranya Crystal, Guest House, Genset untuk pria, dan Jasmine 1, Jasmine 2, Annex, Edelweiss, dan Bougenville untuk wanita. <br><br>Jika kamu ingin melihat setiap asramanya lebih detail, kamu dalam mengakses link dibawah ini: <br> <a href="https://www.google.com/maps/place/Klabat+University/@1.4172798,124.982042,17.65z/data=!4m5!3m4!1s0x32870a95df6309dd:0x21d86e4847556add!8m2!3d1.4175028!4d124.9839744" target="_blank">Asrama di Universitas Klabat</a>'],    
    
    'resp_rules'            : ['Semua asrama memiliki peraturan yang harus ditaati oleh setiap penghuni asrama. Ketika didapati melanggar peraturan, maka akan dikenakan sanksi. Peraturan-peraturan ini telah tertulis secara rinci pada buku peraturan Kehidupan Mahasiswa di Dalam dan Sekitar Kampus. Kamu bisa membacanya dengan mengakses link berikut:     <br> <a href="https://usermanual.wiki/Document/studentmanual.470346736/view" target="_blank">Peraturan Asrama</a>'],

    #dormitory location
    'resp_ask_location'            : ['Mau lihat asrama apa?',
                                      'Ada 7 asrama di Universitas klabat. Mau lihat asrama apa?'],
    
    'resp_location_edelweiss'      : ['Untuk melihat di mana lokasi asrama Edelweiss, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/VELdKid1siHUwgQv8" target="_blank">Lokasi Asrama Edelweiss</a>'],
    
    'resp_location_annex'          : ['Untuk melihat di mana lokasi asrama Annex, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/5urULc3nb4Y2MSsV8" target="_blank">Lokasi Asrama Annex</a>'],
    
    'resp_location_bougenville'    : ['Untuk melihat di mana lokasi asrama Bougenville, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/SBJ5wRDx2wjUWJRp9" target="_blank">Lokasi Asrama Bougenville</a>'],
    
    'resp_location_jasmine_1'      : ['Untuk melihat di mana lokasi asrama Jasmine 1, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/1ZJ9iwbTitE2oqUE7" target="_blank">Lokasi Asrama Jasmine 1</a>'],
    
    'resp_location_jasmine_2'      : ['Untuk melihat di mana lokasi asrama Jasmine 2, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/x1B4VxCAwH7sZvZB7" target="_blank">Lokasi Asrama Jasmine 2</a>'],
    
    'resp_location_genset'         : ['Untuk melihat di mana lokasi asrama Genset, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/npvMHbnESet7Q7b97" target="_blank">Lokasi Asrama Genset</a>'],
    
    'resp_location_guest_house'    : ['Untuk melihat di mana lokasi asrama Guest House, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/dBQjdCgjaQKqJeni8" target="_blank">Lokasi Asrama Guest House</a>'],
    
    'resp_location_crystal'        : ['Untuk melihat di mana lokasi asrama Crystal, kamu bisa mengunjungi link berikut: <br> <a href="https://goo.gl/maps/ws69sVjSMZReSN6JA" target="_blank">Lokasi Asrama Crystal</a>'],
    #---
    'resp_kapasitas'               : ['Kamu bisa mengakses link dibawah ini untuk melihat kapasitas sekaligus kamar yang tersedia di setiap asrama <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/annex.php" target="_blank">Annex </a> <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/edelweiss.php" target="_blank">Edelweiss </a> <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/jasmine1.php" target="blank">Jasmine 1</a> <a href="http://34.128.83.59/elsven_chatbot/available_room/jasmine2.php" target="_blank">Jasmine 2</a> <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/bougenville.php" target="_blank">Bougenville</a> <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/crystal.php" target="_blank">Crystal</a> <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/genset.php" target="_blank">Genset</a> <br> <a href="http://34.128.83.59/elsven_chatbot/available_room/guesthouse.php" target="_blank">Guest House</a>'],
    #---
    'resp_cara_pesan'              : ['Untuk memesan kamar, cukup ketik ingin pesan kamar kemudian kami akan meminta anda untuk menjawab melengkapi data diri serta asrama dan kamar yang diinginkan.'],
    
    #room model dormitory
    'resp_ask_model_room'   : ['Mau lihat asrama apa?',
                               'Ada 7 asrama di Universitas klabat. Mau lihat asrama apa?'],
    
    'resp_room_model_edelweiss'    : ['Untuk melihat visualisasi kamar asrama Edelweiss, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/edelweiss.html" target="_blank">Visualisasi Kamar Asrama Edelweiss</a>'],
    
    'resp_room_model_annex'        : ['Untuk melihat visualisasi kamar asrama Annex, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/index.html" target="_blank">Visualisasi Kamar Asrama Annex</a>'],
    
    'resp_room_model_bougenville'  : ['Untuk melihat visualisasi kamar asrama Bougenville, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/bougenville.html" target="_blank">Visualisasi Kamar Asrama Bougenville</a>'],
    
    'resp_room_model_jasmine_1'    : ['Untuk melihat visualisasi kamar asrama Jasmine 1, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/jasmine_one.html" target="_blank">Visualisasi Kamar Asrama Jasmine 1</a>'],
    
    'resp_room_model_jasmine_2'    : ['Untuk melihat visualisasi kamar asrama Jasmine 2, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/jasmine_two.html" target="_blank">Visualisasi Kamar Asrama Jasmine 2</a>'],
    
    'resp_room_model_genset'       : ['Untuk melihat visualisasi kamar asrama Genset, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/genset.html" target="_blank">Visualisasi Kamar Asrama Genset</a>'],
    
    'resp_room_model_guest_house'  : ['Untuk melihat visualisasi kamar asrama Guest House, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/guest_house.html" target="_blank">Visualisasi Kamar Asrama Guest House</a>'],
    
    'resp_room_model_crystal'      : ['Untuk melihat visualisasi kamar asrama Crystal, kamu bisa mengunjungi link berikut: <br> <a href="https://venisatewu.github.io/crystal4people.html" target="_blank">Visualisasi Kamar Asrama Crystal 1</a>'],
    
    #---------------------------------------------------------------------------------------------------------#
    #dormitory facility
    'resp_ask_facility'     : ['Mau tahu fasilitas asrama apa?',
                                       'Ada 7 asrama di Universitas klabat. Mau tahu fasilitas asrama apa?'],
    
    'resp_facility_edelweiss'      : ['Berikut adalah fasilitas yang tersedia di asrama Edelweiss: <br>- Sofa <br>- Toilet umum <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 6 tempat tidur dua tingkat <br>'], ##
    
    'resp_facility_annex'           : ['Berikut adalah fasilitas yang tersedia di asrama Annex: <br>- Sofa <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 3 tempat tidur dua tingkat <br>- 5 busa matras <br>- 5 meja belajar yang telah di build in dengan lemari <br>- Toilet'],
    
    'resp_facility_bougenville'     : ['Berikut adalah fasilitas yang tersedia di asrama Bougenville: <br>- Sofa <br>- Toilet umum <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 2 tempat tidur dua tingkat'], ##
    
    'resp_facility_jasmine_1'       : ['Berikut adalah fasilitas yang tersedia di asrama Jasmine 1: <br>- Wifi <br>- Sofa <br>- Dispenser <br>- Water filter <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 2 tempat tidur dua tingkat <br> - 4 busa matras <br>- 4 meja belajar yang telah di build in dengan lemari <br>- 1 rak sepatu tiga tingkat <br>- 1 tempat jemuran <br>- Toilet <br>- Shower <br>- Wastafel'],
    
    'resp_facility_jasmine_2'       : ['Berikut adalah fasilitas yang tersedia di asrama Jasmine 2: <br>- Wifi <br>- Sofa <br>- Dispenser <br>- Water filter <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 2 tempat tidur dua tingkat <br> - 4 busa matras <br>- 4 meja belajar yang telah di build in dengan lemari <br>- 1 tempat jemuran <br>- Toilet (wc dan kamar mandi terpisah) <br>- Shower <br>- Wastafel <br>- Ember'],
    
    'resp_facility_genset'          : ['Berikut adalah fasilitas yang tersedia di asrama Genset: <br>- Toilet umum <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 4 tempat tidur dua tingkat <br>- 4 Lemari baju'], ##
    
    'resp_facility_guest_house'     : ['Berikut adalah fasilitas yang tersedia di asrama Guest House: <br>- Sofa <br>-Wifi <br>-Water filter <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 6 tempat tidur dua tingkat <br>- 6 busa matra <br>- 6 meja belajar yang telah di build in dengan lemari <br>- Toilet'], ##
    
    'resp_facility_crystal_1'       : ['Berikut adalah fasilitas yang tersedia di asrama Crystal 1: <br>- Sofa <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia:  <br>- 4 tempat tidur dua tingkat <br>- 4 Lemari baju'], ##
    
    'resp_facility_crystal_2'       : ['Berikut adalah fasilitas yang tersedia di asrama Crystal 2: <br>- Sofa <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 4 tempat tidur dua tingkat <br>- 4 Lemari baju'], ##
    
    'resp_facility_crystal_3'       : ['Berikut adalah fasilitas yang tersedia di asrama Crystal 3: <br>- Sofa <br>- Tempat jemuran umum <br>- Dining <br><br> Untuk setiap kamar tersedia: <br>- 6 tempat tidur dua tingkat <br>- 6 Lemari baju <br>-  Toilet'], ##
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
    
    
    #Related to dormitory and Unklab
    'resp_about_unklab'     : ['Univeritas Klabat adalah pusat pendidikan tinggi yang didirikan oleh Gereja Masehi Advent Hari Ketujuh untuk menyediakan mahasiswa bagi pelayanan di Indonesia dan tempat lainnya.'],
    
    'resp_address_unklab'   : ['Jl. Arnold Mononutu, Airmadidi Bawah, Kec. Airmadidi, Kabupaten Minahasa Utara, Sulawesi Utara 95371'],

    'resp_payments'         : ['Pembayaran asrama akan diproses oleh pihak Business Office saat pendaftaran berlangsung.',
                               'Untuk pembayaran, Anda bisa langsung datang ke bagian Busines Office Universitas Klabat. Anda hanya perlihatkan ID pemesanannya. Nanti akan di proses.'],
    
    'resp_dining'           : ['Bagi mahasiswa yang tinggal di asrama, disediakan makanan pagi, siang, dan malam dengan berbagai macam menu di Fern Wallace.',
                               'Dining merupakan salah satu fasilitas yang akan didapatkan mahasiswa ketika tinggal di dalam asrama. Disediakan makanan pagi, siang, serta malam dengan berbagai macam menu setiap harinya.'],
    
    'resp_price'            : ['Setiap asrama memiliki berbagai fasilitas yang berbeda-beda sehingga harganyapun beragam. Berikut adalah detail harga setiap asrama <br> <a href="https://www.unklab.ac.id/biaya-perkuliahan" target="_blank">Harga Asrama</a>'],
    
    'resp_kepas_name'       : ['Setiap asrama memiliki penanggung jawabnya masing-masing yang disebut Kepala Asrama atau sering disebut Kepas. Setiap kepas dipercayakan untuk memimpin dan mengatur asrama. <br><br>Berikut adalah nama kepala asrama saat ini. <pre>Edelweiss        : Delly Antou, S.Pd <pre>Bougenville     : Poppy Iroth <br>Annex             : Poppy Iroth <br>Jasmine 1       : Poppy Iroth <br>Jasmine 2       : Poppy Iroth <br>Crystal            : Steven Jacob <br>Genset            : Pdt. Sonny Syafirudin <br>Guest House  : Pdt. Sonny Syafirudin'],
    
    'resp_contact_dorm'     : ['Berikut adalah kontak pihak asrama yang bisa kamu hubungi: <br>- Edelweiss: <br>  Kepas: Delly Antou, S.Pd <br>  No.Hp: +62 813-5510-6175 <br>  Email: dellyantou12@unklab.ac.id <br><br>- Annex, Bougenville, Jasmine 1, Jasmine 2: <br>  Kepas: Poppy Iroth <br>  No.Hp:  <br>  Email: poppyiroth@unklab.ac.id <br><br>- Crystal: <br>  Kepas: Steven Jacob <br>  No.Hp: +62 852-5600-6363 <br>  Email: stevenjacob@unklab.ac.id <br><br>- Genset, Guest House: <br>  Kepas: Pdt. Sonny Syafirudin <br>  No.Hp: +62 813-4018-3852 <br>  Email: sonnysyafirudin@unklab.ac.id'],
   
    
    #General knowledge for chatbot
    'resp_identity'         : ['Saya EVAs Bot, chatbot yang berperan sebagai asisten virtual Anda dalam memesan dan menanyakan informasi asrama.'],
    
    'resp_age'              : ['Saya dibuat pada tahun 2022 oleh Venisa Tewu dan Elshadai Rampengan.'],
    
    'resp_ability'          : ['Saya dapat membantu anda dalam melakukan pemesanan kamar dan menjawab pertanyaan-pertanyaan terkait asrama.', 
                               'Menjadi asisten virtual anda dalam melakukan pemesanan kamar dan menjawab pertanyaan-pertanyaan terkait asrama.', 
                               'Anda dapat mengajukan pertanyaan kepada saya sesuatu yang berkaitan tentang asrama dan memesan kamar kepada saya dan saya akan mencoba menjawabnya.'],
    
    'resp_language'         : ['Saya memahami bahasa Indonesia dan logat Manado',
                               'Bahasa Indonesia dan logat manado',
                               'Saya bisa mengerti dua bahasa, yaitu bahasa Indonesia dan logat Manado',
                               'Untuk saat ini bahasa Indonesia dan logat Manado',
                               'Saat ini saya tahu bahasa Indonesia dan logat Manado'],
    
    'resp_creator'          : ['Saya dikembangkan oleh Elsha dan Venisa',
                               'Elsha dan Venisa mengembangkan saya pada 2022, untuk project akhir mereka.',
                               'Dua anak perempuan mengembangkan saya di Universitas Klabat, Elsha dan Venisa'],
    
    'resp_chatbot'          : ['Chatbot adalah program yang mencoba mensimulasikan percakapan atau "obrolan" manusia.',
                               'Chatbot adalah saya, EVAs Bot, yang dapat mensimulasikan percakapan atau "obrolan" manusia.'],
    
    'resp_programming'      : ['Python adalah bahasa pemrograman terbaik untuk membuat chatbot',
                               'Saya cukup menikmati pemrograman dengan bahasa Python akhir-akhir ini.'],
    
    
    #Random chat from user
    'resp_activity'         : ['Umm.. sedang merespon pesan Anda', 
                               'Umm.. membantu Anda mungkin? hehe',
                               'Berbicara dengan Anda, tentu saja.'],
    
    'resp_laugh'            : ['Senang bisa buat Anda tertawa'],
    
    'resp_jokes'            : ['Hidup itu penuh cobaan, kalo penuh cucian itu Laundry.',
                               'Tak usah takut tak usah khawatir.. Ini kentut bukan petir.',
                               'Kera apa yang harus dimusnahkan? Keraguan untuk melamarmu.',
                               'Buah manggis jatuh di ember, ngana manangis sampe desember🤣',
                               'Kamu nggak fokus, bukan karena butuh air mineral tapi butuh aku.',
                               'Hidup itu singkat. Maka tersenyumlah mumpung kamu masih punya gigi.',
                               'Google itu hebat ya? Tapi sayang sehebat – hebatnya google gak bisa menemukan jodoh kita.',
                               'Jangan suka membohongi diri sendiri. Karena membohongi dirimu sudah jadi tugas orang lain.',
                               'Cinta itu buta…buta itu gelap..gelap itu item..item itu monyet…monyet itu yang lagi baca status ini. wkwkw.'],
    
    'resp_love'             : ['Yes i do',
                               'Tentu saja...',
                               'Kamu orang yang menarik',
                               'Hanya orang bodoh yang menjawab tidak'
                               'Saya tidak bisa memikirkan jawaban lain selan IYA'],
    
    'resp_sad'              : ['Sedih mendengarnya🥺',
                               'Oh kasiang, semangat neh🥺🥺',
                               'Jangan lupa untuk terus berdoa😇',
                               'Lakukan yang terbaik yang kamu bisa.',
                               'Jangan pernah menyerah apapun yang terjadi.',
                               'Syukuri dan hargai hal-hal yang kamu miliki.'],
    
    'resp_happy'            : ['Wahh, mantap...',
                               'Senang mendengarnya😊',
                               'Saya pun turut bahagia🥺',
                               'Saya pun ikut bahagia...😊😊',
                               'Puji Tuhan, senang megetahuinya😇',
                               'Sungguh baik mendengarnya. Jangan lupa untuk selalu bersyukur🤗'],
    
    'resp_sorry'            : ['Tidak mengapa.',
                               'Tidak apa-apa.',
                               'Bukan masalah,',
                               'Jangan dipikirkan.',
                               'Aku dapat memahaminya',
                               'Aku juga minta maaf ya.',
                               'Kenapa anda minta maaf.',
                               'Permintaan maaf diterima.',
                               'Jangan khawatir soal itu.',
                               'Tidak perlu lah anda minta maaf.',
                               'Terima kasih kamu sudah minta maaf.',
                               'Tolong, jangan khawatir. Tidak apa-apa.',
                               'Lupakan saja. Aku sungguh tidak apa-apa.',
                               'Aku menghargai permintaan maaf kamu, terima kasih.'],
    
    'resp_help'             : ['Apakah ada masalah?',
                               'Apa yang bisa saya bantu?',
                               'Adakah yang bisa saya bantu?',
                               'Masalah apa yang kamu hadapi?',
                               'Bantuan apa yang kamu butuhkan?',
                               'Apa yang bisa saya lakukan untuk anda?'
                               'Silahkan bertanya. Saya akan berusaha membantu anda.',
                               ],
    
    'resp_alive'            : ['Saya ragu tentang itu.',
                               'Hahaha.. maaf tapi tidak bisa.',
                               'Tidak, saya tidak bisa melakukan hal itu.'],
    
    'resp_robot'            : ['Ya, saya robot. Tapi saya pintar! 😎😎',
                               'Saya memang robot, tapi jangan meragukan kemampuan saya😎',
                               'Ya, saya robot, tapi saya robot pintar😎. Biarkan saya membuktikannya. Apa yang bisa saya bantu?'],
    
    'resp_whatsup'          : ['Luar biasa... Kamu?',
                               'Lumayan... Kalau kamu?',
                               'Bae-bae skali, ngana dang?',
                               'Cukup baik, bagaimana denganmu?',
                               'Baik, terima kasih. Kamu apa kabar?',
                               'Kabar baik, terima kasih. Apa kabar?',
                               'Baik-baik saja, bagaimana dengan Anda?'],
    
    'resp_motivation'       : ['Lelah tidak pernah dirasakan oleh mereka yang tidak mau berusaha.',
                               "Bersyukurlah ketika merasa lelah, tidak semua orang bisa sekuat kamu.",
                               'Bersyukur, bersyukur, dan bersyukur karena bersyukur ialah kebahagiaan sejati.',
                               'Jangan kecewa merasa lelah, justru ia menjadi pengingat terbaik untuk targetmu.',
                               'Filipi 4:13 "Segala perkara dapat kutanggung di dalam Dia yang memberi kekuatan kepadaku."',
                               'Semakin keras kamu bekerja untuk sesuatu, semakin besar kamu merasakannya ketika mencapainya.',
                               "Melihat kadar kesuksesan orang lain hanya akan membuatmu kelelahan. Ciptakan sendiri standarmu.",
                               'Cuma sadiki skali yang sampe puncak. Bukang karna dorang yang terbaik. Dorang cuma nyanda brenti.',
                               'Hidup adalah perjalanan yang harus dilalui, tidak peduli seberapa buruk jalan yang harus dilewati.',
                               'Roma 12:11 "Janganlah hendaknya kerajinanmu kendor, biarlah rohmu menyala-nyala dan layanilah Tuhan."',
                               'Galau itu wajar dan normal karena ia adalah proses penyesuaian diri dengan kehidupan yang lebih berkelas.',
                               'Menyerah berarti menerima bahwa kamu lelah. Tetapi untuk beristirahat dan mencoba lagi adalah tanda sebuah tekad.',
                               'Jangan lelah mencoba. Tidak ada jaminan kesuksesan, tetapi memilih untuk tidak mencoba adalah jaminan kegagalan.',
                               'Yesaya 40:29 ,"Dia memberi kekuatan kepada yang lelah dan menambah semangat kepada yang tiada berdaya." Tetap semangat!!🤗🤗',
                               'Hidop ini modal sgalanya; Hidop lebe luas dari samudra. Lebe bermakna dari sribu bintang. Se polote ngana pe potensi hidop itu!',
                               'Jika ingin berhasil jangan menunggu termotivasi dulu baru bergerak, tapi bergeraklah terlebih dahulu, maka dirimu akan termotivasi dengan sendirinya.',
                               'Tidak ada, bahkan rasa sakit, yang bertahan selamanya. Jika aku bisa terus meletakkan satu kaki di depan yang lain, aku akhirnya akan sampai pada akhirnya.',
                               'Yosua 1:9 "Bukankah telah Kuperintahkan kepadamu: kuatkan dan teguhkanlah hatimu? Janganlah kecut dan tawar hati, sebab Tuhan, Allahmu, menyertai engkai, ke mana pun engkau pergi."',
                               'Roma 8:28 "Kita tahu sekarang, bahwa Allah turut bekerja dalam segala sesuatu untuk mendatangkan kebaikan bagi mereka yang mengasihi Dia, yaitu bagi mereka yang terpanggil sesuai dengan rencana Allah."'],
    
    'resp_negative'         : ['Kami tidak menerima kata-kata makian', 
                               'Maaf, mohon tidak memakai kata-kata makian.',
                               'Sopan santun harus diterapkan dimana pun dan kapanpun. Salah satunya adalah tidak berkata kasar.'],
    
    
    'resp_limit'            : ['Kami hanya menampilkan gambaran visualnya saja. Untuk lebih jelasnya, kamu dapat datang langsung. Kami akan dengan senang hati melayani Anda.'],
    
    
    'resp_id_pesanan'       : ['Baik. Bisa minta ID pemesanannya?',
                               'Bisa minta ID pemesanannya?', 
                               'ID pesanannya?'],
    'resp_error'            : ['Maaf, mohon memasukkan data yang tepat'],
    'resp_info_id'          : ['Nama Pemesan: Venisa Tewu \nEmail: venisatewu@gmail.com \nNo.HP: 082123439044 \nDetail order:  \n- Nama asrama: Jasmine 2  \n- No. Kamar: 204  \n- Tempat tidur: 1A  \nID Pemesanan: UK000001'],
    
    
    
    
    'resp_email'            : ['Baiklah. Emailmu telah disimpan.'],
    'resp_hp'               : ['Oke. Nomor handphonenya telah disimpan'],
    'resp_name'             : ['Noted. Namamu telah disimpan.'],
    'resp_no_reg'           : ['Nomor registrasimu telah disimpan.'],
    'resp_nim'              : ['Baik. Nomormu berhasil disimpan.'],
    'resp_input_no_kamar'   : ['Oke. Nomor kamarmu telah disimpan.'],
    'resp_input_no_bed'     : ['Tempat tidur yang kamu inginkan masih tersedia dan berhasil disimpan.'],
    'resp_input_asrama'     : ['Oke.','Baik.','Baiklah'],
    'resp_batal_cancel'     : ['Baik. Pembatalan pesanan gagal.'],
    'resp_yes_cancel'       : ['Pesanan Anda telah dibatalkan'],
    
    'resp_cancel'           : ['Apakah kamu yakin ingin membatalkan pesanan? Silahkan mengkonfirmasi terlebih dahulu pembatalan pemesanan kamar.',
                               'Saat ini konteks percakapan masih dalam status pemesanan kamar. Apakah kamu ingin membatalkan pesanan? Ketik Ya untuk pembatalan.'],
    
    #Default respon for chatbot
    'resp_gender'           : ['Saya dibuat oleh creator wanita, jadi mungkin saya adalah perempuan',
                               'Perempuan, karena saya dibuat oleh creator wanita'],
    'resp_default'          : ['Ada yang ingin kamu tanyakan?',
                               'Mohon maaf sebelumnya, apa yang kamu maksud?',
                               'Adakah pertanyaan lain yang mungkin bisa saya jawab?',
                               'Dapatkah Anda lebih detail tentang apa yang Anda katakan sebelumnya?',
                               'Maaf saya kurang paham. Saya harus belajar lagi. Apakah ada pertanyaan lain?',
                               'Maaf, tapi sepertinya developer saya belum memberitahu saya bagaimana merespon pesan Anda',
                               'Ada yang bisa saya bantu terkait informasi dan pemesanan kamar asrama di Universitas Klabat?',
                               'Terima kasih telah menghubungi saya. Saya berhadap dapat membantu Anda lebih baik lagi kedepannya🙏🏼',
                               'Mohon maaf, saya belum paham mengenai pesan anda sebelumnya. Bisa kah kamu mengajukan pertanyaan lain?',
                               'Mohon maaf, sepertinya developer saya belum memberi tahu saya bagaimana merespon maksud anda barusan🙏🏼',
                               'Maafkan saya. Semua hal ini masih asing bagi saya. Adakah pertanyaan lain yang mungkin bisa saya jawab?',
                               'Hai!, mungkin saya perlu waktu untuk mendapatkan kembali informasi yang Anda cari. Ada pertanyaan lain?',
                               'Maaf, saya tidak dapat menyampaikan jawaban saya dengan jelas saat ini. Saya akan menyampaikan pertanyaan ini kepada developer saya.',
                               'Maaf untuk mengatakannya, tetapi saya tidak dapat langsung menjawab pesan anda. Untuk hal lainnya, Anda selalu dapat menghubungi saya',
                               'Terima kasih karena telah menanyakan hal ini. Namun, saya perlu memeriksa dengan tim saya untuk memberitahu Anda tentang hal ini lebih lanjut. Saya bisa menjawab pertanyaan Anda terkait asrama. Adakah yang bisa saya bantu?'],
}