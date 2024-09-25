n = int(input())         #input jumlah id sepatu yang terkena virus

enshoes = [None]*100     #inisiasi id sepatu yang terkena virus/enkripsi
reshoes = [""]*100       #inisiasi id sepatu yang sudah dipulihkan/dekripsi
match = 0                #inisisasi pasangan sepatu

for i in range(n):
    enshoes[i] = str(input()) #input id sepatu yang terenkripsi
    
    #memulihkan id sepatu:
    for j in range(len(enshoes[i])):
        if enshoes[i][j].isdigit() or enshoes[i][j].isupper(): #jika karakter di id sepatu yang terenkripsi merupakan angka atau huruf kapital
            reshoes[i] += enshoes[i][j]                        #maka karakter tersebut dimasukkan pada variabel id sepatu yang sudah didekripsi

#mencari jumlah sepatu yang berpasangan:
for i in range(n):
    for j in range(i+1, n):
        if (f"{reshoes[i][:-1]}" == f"{reshoes[j][:-1]}") and (f"{reshoes[i][-1]}" != f"{reshoes[j][-1]}"): #jika angka pada ukuran sepatu sama dan huruf kapital berbeda(L/R)
            match += 1                                                                                      #maka menambah jumlah sepatu yang berpasangan
            reshoes[j] = "0"                                                                                #dan mengganti salah variabel yang berpasangan sehingga tidak terhitung
            reshoes[i] = "0"                                                                                #kembali pada perulangan berikutnya
       
print(match) #output hasil jumlah sepatuyang berpasangan