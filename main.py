# A*
'''
- Sebuah bilangan N menyatakan banyak simpul
- N buah koordinat setiap simpul dan nama setiap simpul
- Adjacency Matrix berukuran N x N

'''
'''
2
3 4 Medan
28 8 Baubau
0 3
3 0
'''
# Baca file
print("Silahkan masukkan nama file: ")
f = input()
fFile = open(f, "r")
N = int(fFile.readline())
dictPlace = {}
for _ in range(N):
    x, y, place = fFile.readline().split(" ")
    dictPlace[_] = [int(x), int(y), place[:-1]]

adjMat = []
for line in fFile.readlines():
    adjMat.append([int(x) for x in line.split(" ")])

print(dictPlace)
print(adjMat)
# Algoritma