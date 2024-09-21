txt = str(input())  #input txt sebagai kalimat yang ingin diterjemahkan sebagai kunci
key = ""            #inisiasi hasil terjemahan

#Mencari hasil terjemahan
for i in range(len(txt)):                   #Cek setiap karakter pada kalimat
    if txt[i] not in key and txt[i] != " ": #Cek apakah karakter tersebut sudah ada pada key dan memasetikan bukan spasi (" ")
        key += txt[i]                       #Menambahkan karakter pada key
        
print(key)  #Mengeluarkan key sebagai output