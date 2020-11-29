nim = []
nama = []
asal = []

pilihan = 1
while pilihan != 0 :
    print ("1. masukan data.")
    print ("2. tampilkan data.")
    print ("3. Ubah Nama.")
    print ("4. hapus data.")
    print ("0. exit.")

    pilihan = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if pilihan == 1 :
        masnim = input("masukan nim : ")
        nim.append({'nim' : masnim})
        masnama = input("masukan nama : ")
        nama.append({'nama' : masnama})
        masasal = input("sekolah  asal : ")
        asal.append({'asal' : masasal})
        
        
    elif pilihan == 2 :
        penentu = True
        for i in range (len(nim)) :
            if penentu :
                print ("nim\tnama\tasal")
            print (nim[i]['nim'],'\t',nama[i]['nama'],'\t',asal[i]['asal'])
            penentu = False
            
    elif pilihan == 4 :
        masnama = input("masukan nama : ")
        for i in range (len(nama)) :
            if masnama == nama[i]['nama'] :
                print (i)
                del nim[i]
                del nama[i]
                del asal[i]
                break
    print('')
    print('')
    print('')
