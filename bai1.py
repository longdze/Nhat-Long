import os

#thu muc lam viec hien tai
thumucht = os.getcwd()
print('thu muc lam viec hien tai',thumucht)

#chuyen den thu muc
def chuyen_thu_muc():
    thumuc=input('nhap thu muc')
    os.chdir(thumuc)
    print('thu muc lam viec hien tai sau khi chuyen là:')
    print(os.getcwd())

chuyen_thu_muc()

#tạo thư mục
def tao_thu_muc():
    ten = 'nnlt'
    duongdan = "D:/data/"
    path = os.path.join(duongdan,ten)
    mode =0o666
    os.makedirs(path,mode)
    print('thu muc',ten,'duoc tao')

tao_thu_muc()

#Liệt kê tất cả các tập tin và thư mục có trong thư mục ‘My Documents’ trên máy tính của bạn và in ra màn hình
def liet_le_thu_muc():
    nguon = "C:/Users/ACER/Documents/"
    listphantu=os.listdir(nguon)
    print(listphantu)
liet_le_thu_muc()

#kiem tra tap tin va thu muc
def kiem_tra_tt_tm():
    nguon="C:/Users/ACER/Documents/"
    kiemtra=os.path.exists(nguon)
    print("tập tin có trong máy:", kiemtra)
kiem_tra_tt_tm()

#xoa tap tin va thu muc
def xoa_tttm():
    os.remove(os.path.join("D:/data","baitapvn.txt"))
    os.rmdir(os.path.join("D:/data","nnlt"))
    print("da xoa")
xoa_tttm()