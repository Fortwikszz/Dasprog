src = str(input())              #input string yang berisi karakter-karakter
len = int(input())              #input panjang karakter yang dihasilkan
pick = input().split(" ")       #input karakter yang diakses dari variabel src

out = ""                        #inisiasi output yang akan dikeluarkan

for i in range(len):
    out += src[int(pick[i])]    #menambahkan karakter yang dipilih dari src ke dalam variabel out

print(out)                      #mengeluarkan out sebagai output