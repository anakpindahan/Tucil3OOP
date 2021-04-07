from queue import PriorityQueue

#fungsi fungsi

def jarak(a, b):
    return ((a[0]-b[0])**2 + (a[1] - b[1])**2)**0.5


#################################################


# Baca file
print("Silahkan masukkan nama file: ")
f = input()
fFile = open(f, "r")
N = int(fFile.readline())
dictPlace = {}
for _ in range(N):
    x, y, place = fFile.readline().split(" ")
    dictPlace[_] = [float(x), float(y), place[:-1]]

adjMat = []
for line in fFile.readlines():
    adjMat.append([float(x) for x in line.split(" ")])

#print(adjMat)

#menampilkan indeks, koordinat dari tiap simpul
print("indeks, data simpul (x, y, nama simpul)")
for i in dictPlace:
    print(i, ": ",  dictPlace[i])

###################################################


coordinate = dictPlace
matriksKetetanggaan = adjMat


# masukkan indeks kota asal (diasumsikan input sesuai, tidak ada yang diluar indeks yang diberikan)
asal = int(input("masukkan indeks tempat asal: "))
# masukkan indeks kota tujuan (diasumsikan input sesuai, tidak ada yang diluar indeks yang diberikan)
tujuan = int(input("masukkan indeks tempat tujuan: "))

#hitung jarak garis lurus dari setiap kota ke kota tujuan dan simpan di sebuah array
jarakLurusSetiapTempatKeTujuan = [jarak(coordinate[i], coordinate[tujuan]) for i in range (len(coordinate))]





#Algoritma A*

# Step 1, bikin simpul terbuka dan tertutup dengan awal simpul buka adalah start node
simpulBuka = PriorityQueue() #priorityQueue yang prioritasnya adalah jarak terkecil terlebih dahulu dengan nilai berupa jalur yang dilewati
simpulBuka.put((jarakLurusSetiapTempatKeTujuan[asal], [asal]))



# Step 2, Kalau simpul bukanya kosong, maka tidak ada jalan dari asal ke tujuan.
stop = False
jarak = 0
while (not stop):
    if (simpulBuka.empty()):
        stop = True
        print("tidak ada jalur yang menghubungkan asal dan tujuan")

    #step 3, ambil node yang paling kecil, masukin ke simpul Tutup
    else: 
        t = simpulBuka.get()
        #print("Proses: ", t) #jika ingin melihat prosesnya
        #step 4, jika ujung jalur merupakan simpul tujuan, maka selesai. ambil jarak dan jalurnya
        if(t[1][len(t[1])-1]== tujuan):
            stop = True
            jarak = t[0]
            jalur = t[1]
         #step 5, jika ujung jalur bukan tujuan,
        else: #masukkan setiap anak dari simpul yang nilai f nya terkecil ke open list
            ujungjalur = t[1][len(t[1]) - 1]
            #copy jalur
            for i in range(0, len(coordinate)):
                a = []
                for j in range(0, len(t[1])):
                    a.append (t[1][j])
                
                if (matriksKetetanggaan[i][ujungjalur] != 0): #merupakan anak jika mempunyai jarak dengan ujung jalur
                    a.append(i)
                    nilai = t[0] - jarakLurusSetiapTempatKeTujuan[ujungjalur] + matriksKetetanggaan[i][ujungjalur] +  jarakLurusSetiapTempatKeTujuan[i]
                    simpulBuka.put((nilai, a)) # step 6, ekspansi simpul terbuka

print("\nJarak terpendek adalah: ", jarak, " meter")
print('')
print("jalurnya adalah:")

for i in jalur:
    print (coordinate[i][2])





