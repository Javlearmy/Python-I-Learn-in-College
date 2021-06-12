def HaiInput(dataKOMPLIT):
    print("\n")
    while True:
        dataNAMA=str(input("Masukan nama : "))
        dataNIM=str(input("Masukan NIM : "))
        dataJURUSAN=str(input("Masukan JURUSAN : "))
        dataKOMPLIT[dataNIM]=dataNAMA,dataJURUSAN
        breakerInput=str(input("lanjut?? tekan Y : "))
        print("\n")
        if breakerInput!="Y":
            break
    return dataKOMPLIT

def HaiBank(dataKOMPLIT):
    print("\n")
    print("DAFTAR DATA : [NIM / NAMA / JURUSAN] ")
    print (dataKOMPLIT)

def HaiSorted(dataKOMPLIT):
    print("before sorted : ",dataKOMPLIT.items())
    dataKOMPLIT=(sorted(dataKOMPLIT.items()))
    print("after sorted : ",dataKOMPLIT)

def HaiSearch(dataKOMPLIT):
    print("\n")
    hasil=False
    targetstr=str(input("DATA Target : "))
    for nim,namaNjurusan in dataKOMPLIT.items():
        print("\n")
        if targetstr in nim:
            hasil=True
            print("Data ditemukan : ",hasil)
            print(nim,namaNjurusan)
        elif targetstr in namaNjurusan[0]:
            hasil=True
            print("Data ditemukan : ",hasil)
            print(nim,namaNjurusan)
        elif targetstr in namaNjurusan[1]:
            hasil=True   
            print("Data ditemukan : ",hasil)  
            print(nim,namaNjurusan)
        else:
            print("Data ditemukan : ",hasil)
    
    
def main():
    print("\n")
    dataKOMPLIT={}
    while True:
        print("\n")
        print("Selamat datang di aplikasi Saku Mahasiswa UDINUS \n 1). INPUT DATA \n 2). DAFTAR DATA \n 3). URUTKAN DATA \n 4). CARI DATA \n 5). EXIT")
        AKSI=int(input("Pilih kegiatan anda : "))
        if AKSI==1:
            HaiInput(dataKOMPLIT)
        elif AKSI==2:
            HaiBank(dataKOMPLIT)
        elif AKSI==3:
            HaiSorted(dataKOMPLIT)
        elif AKSI==4:
            HaiSearch(dataKOMPLIT)
        else:
            break
        
main()
    

    
