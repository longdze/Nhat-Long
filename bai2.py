#1
file1=open("D:/data/btvn.txt","r")
print(file1)
#2
file2=open("D:/data/btvn.txt","w")
print(file2)
#3
file3=open("D:/data/lambtvn.txt","r+b")
print(file3)
#4
file4=open("D:/data/lambtvn.txt","r")
print(file4)
#5:đóng tâp tin
file4.close()
#6 Mở tập tin văn bản để đọc bằng cấu trúc câu lệnh
try:
    file6=open("D:/data/btvn.txt","r")
    file6.read()
finally:
    file6.close()
#7 Mở tập tin văn bản để đọc bằng cấu trúc:
with open("D:/data/btvn.txt") as f:
    f.read()
    f.close()
#8
with open("D:/data/btvn.txt","w") as f:
    f.write('xin chao')
    f.write('Bonjour')
    f.write('au revoir')
    f.close()
#9Mở tập tin văn bản Unicode, đọc toàn bộ nội dung của văn bản và in ra màn hình
with open("D:/data/btvn.txt","r") as f:
    a=f.read()
    print(a)
    f.close()
#10 mở tệp nhị phssn
with open("C:/Users/ACER/Pictures/hai van 3011/IMG_4627.JPG","rb") as f:
    b=f.read()
    print(b)