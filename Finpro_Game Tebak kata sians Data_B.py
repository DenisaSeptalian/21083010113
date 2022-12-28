#!/usr/bin/env python
# coding: utf-8

# In[1]:

import random
import sys
import time
import os
print()
def main(kata):
    parsekata = list(kata)
    panjangkata = len(parsekata)
    progress = None
    tertebak = False
    telahdipilih =[]
    #print(parsekata)
    ()
    print(f'''
                                   +=====================================+
                                   | Welcome to game kosakata sains data |
                                   +=====================================+
                                                 |||||||||
                                   +=====================================+
                                   <<< Masukan Huruf pertama dari clue >>>
                                   +=====================================+
        ''')
    langkah = 0
    while not tertebak:
        print('Ayo kerjakan', Nama,',', 'Tebak kata berdasarkan topik berisi %d huruf.' % panjangkata, end='')
        huruftebakan = input('silahkan Tebak 1 huruf: ')
        
        jmlhtebakan = hitunginput(huruftebakan)
        if jmlhtebakan == 1: # jika input hanya 1 huruf S: cek huruf sudah pernah di pilih
            cek1hdipilih = sudahdipilih(telahdipilih,huruftebakan)
            if cek1hdipilih:
                print('Anda sudah menebak huruf %s ini' % huruftebakan)
                print(join(progress))
                continue #langsung langkah berikutnya
            else:
                telahdipilih.append(huruftebakan)
            # E: cek huruf sudah pernah dipilih
            # S: cek jika huruf tebakan ada dalam kata
            cekada = cektebakan(parsekata,huruftebakan)
            if cekada:
                progress = progreskata(parsekata,progress,huruftebakan)
                print(join(progress))
            else:
                print('worng!!! tidak ada Huruf ini dikata kunci', huruftebakan)
                print(join(progress))
        # E: cek jika huruf tebakan ada dalam kata
        # S: cek jika huruf sudah berhasil tertebak
        selesai = cekselesai(progress)
        if not selesai: 
            print('kata ''%s'' tertebak dalam %d percobaan.' % (join(parsekata),langkah))
            skor = 100
            if panjangkata-1 == langkah:
                print('Skor=', skor)
                print(langkah)
                print(f'''
                                   +=====================================+
                                   |Selamat anda Berhasil menyelesaiakan!|
                                   +=====================================+
                                                   |||||||||
                                   +=====================================+
                                   |      <<< Skor kredit {skor}  >>>       |
                                   +=====================================+
                ''')
            else:
                skor -= langkah*10 
                print('skor=', skor)
            tertebak = True
            #E: cek jika huruf sudah berhasil tertebak
        else: #jika input lebih dari 1 huruf
            if jmlhtebakan == 0: #tidak ada input
                print('Tidak ada input, harus memasukan 1 huruf.')
                print(join(progress))
            else: #kondisi input lebih dari satu, tebakan langsung
                langsung = tebaklangsung(parsekata,huruftebakan)
            if langsung == True: # jika tebakan langsung benar
                print('BERHASIL')
                print('kata ''%'' tertebak dalam %d langkah.' % (join(parsekata),langkah))
                tertebak = True
            else: #tebakan langsung salah
                print('<<<<<<<<<<<<<<<<<<<<<< kamu berhasil melengkapi satu huruf', Nama, 'Lanjutkan!!!>>>>>>>>>>>>>>>>>>>>>>')
                print(join(progress))
            langkah +=1
            
def Pilihan():
    print('Silahkan Pilih Topik Kata di bawah :')
    print('1.Excel')
    print('2.Database')
    print('3.python')
    print('4.statistika')
    print('5.Data')
    
def Excel(): #library kata ke 1
    katakata = ['cell','row','grafik','column','worksheat','tabel','range','charts','merge','average']
    kataterpilih = random.choice(katakata)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clue Huruf pertama Adalah >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(kataterpilih[0])
    main(kataterpilih)

def Database(): #Library kata ke 2
    katakata = ['atribute','mysql','server','claude','query','field','insert','forirgnkey','primarykey','dbms']
    kataterpilih = random.choice(katakata)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clue Huruf pertama Adalah >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(kataterpilih[0])
    main(kataterpilih)

def python(): #Library kata ke 3
    katakata = ['code','syntax','coment','whitespace','library','input','output','looping','string','integer',]
    kataterpilih = random.choice(katakata)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clue Huruf pertama Adalah >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(kataterpilih[0])
    main(kataterpilih)

def statistika(): #Library kata ke 4
    katakata = ['kuantitatif','kualitatif','kovarians','varians','korelasi','distribusi','hipotesis','linear','sccaterplot','sampel']
    kataterpilih = random.choice(katakata)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clue Huruf pertama Adalah >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(kataterpilih[0])
    main(kataterpilih)

def Data(): #Library kata ke 5
    katakata = ['numnerik','visualisasi','database','dataset','analyst','Enginer','scientist','python','spss','tablue',]
    kataterpilih = random.choice(katakata)
    print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< Clue Huruf pertama Adalah >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
    print(kataterpilih[0])
    main(kataterpilih)
    
def mengetik(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(random.random() * 0.05)
mengetik('''
                                    +=========================================+
                                    |Masukan Data Diri Anda Pada kolom Dibawah|
                                    +=========================================+
        ''')
print()
Nama = input ("Masukan nama  :")
skills = input ("Gelar         :")
print("Hello", skills, Nama,",","Ayo Bermain game tebak kata sains Data....!!!")
mengetik('''
                                    +=========================================+
                                    <<<<<<<<<<<<<RULES OF THE GAME>>>>>>>>>>>>>
                                    +=========================================+
        ''')
def rules(r):
    for b in r + '\n':
        sys.stdout.write(b)
        sys.stdout.flush()
        time.sleep(random.random() *0)
mengetik('''            -------------------------------------------------------------------------------------
            |1.Memilih Topik yang diinginkan                                                     |
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------
            |2.Jawaban menebak kata harus dimasukan per huruf                                    |
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------
            |3.Apabila Percobaan pertama salah maka sistem akan langsung mengeluarkan pemain     |
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------
            |4.Perhitungan skor akan sempurna apabila melakukan penebakan sebanyak variabel kata |
            |  dan akan dikurangi apabila percobaan melibihi variabel huruf                      |
            -------------------------------------------------------------------------------------
            -------------------------------------------------------------------------------------
            |5.clue akan diberikan sesuai jenis topik dan akan hilang ketika mulai               |
            -------------------------------------------------------------------------------------
                                                
                                              <<<<<<<<<<<<< Kosakata >>>>>>>>>>>>>

            Excel       : 'cell','row','grafik','column','worksheat'
			  'tabel','range','charts','merge','average'

            Databse     : 'atribute','mysql','server','claude','query'
	                  'field','insert','forirgnkey','primarykey','dbms'

            python      : 'code','syntax','coment','whitespace','library'
			  'input','output','looping','string','integer'

            Statistika  : 'kuantitatif','kualitatif','kovarians','varians','korelasi'
			  'distribusi','hipotesis','linear','sccaterplot','sampel'

            Data        : 'numnerik','visualisasi','database','dataset','analyst'
			  'Enginer','scientist','python','spss','tablue'
                                  
        ''')
print()

def cektebakan(parsekata,huruftebakan = None): #mengecek huruf  pada list
    if huruftebakan in parsekata:
        return True
    else:
        return False

def hitunginput(huruftebakan): #menghitung jumlah input tebakan
    count = 0
    for i in huruftebakan:
        count += 1
    return count

def progreskata(parsekata,progress,huruftebakan = None): #fungsi tebak persatukata
    if progress == None: #tampilan awal kata akan tertutup semua *
        progress = []
        for i in parsekata:
            progress.append('*')
            
    for i in (i for i,x in enumerate(parsekata) if x == huruftebakan) :
        progress[i] = str(huruftebakan) #ubah tanda * jadi huruf
        
    return progress
def tebaklangsung(parsekata,huruftebakan): #fungsi tebakan langsung
    kata = ''.join(parsekata)
    tebak = ''.join(huruftebakan)
    
    if kata == tebak:
        return True
    else:
        return False
def cekselesai(progress): #cek progres tebakan
    ada = -1
    for i in (i for i,x in enumerate(progress) if x == '*'):
        ada = i
        
    if ada != -1:
        return True
    else:
        return False

def join(kata): #mengabungkan isi list
    kata = ''.join(kata)
    return kata

def sudahdipilih(baghuruf,pilihan): #fungsi cek huruf yg sudah terpilih
    ada = -1
    for i in (i for i,x in enumerate(baghuruf) if x == pilihan):
        ada = i
        
    if ada != -1:
        return True
    else:
        return False
Pilihan()
pilih = int(input('Pilih satu Topik koskata,Hanya memasukan nomer topik :  '))

if pilih == 1:
    os.system('clear')
    Excel()
elif pilih == 2:
    os.system('clear')
    Database()
elif pilih == 3:
    os.system('clear')
    python()
elif pilih == 4:
    os.system('clear')
    statistika()
elif pilih == 5:
    os.system('clear')
    Data()

