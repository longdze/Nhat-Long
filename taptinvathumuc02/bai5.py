import random as r
def ghi_doc_bai5():
    x=r.choices(range(-1000,1001),k=1000)
    print('danh sách: ',x)
    nguon=input("Nhap ten tap tin: ")
    f=open(nguon,"w")
    btam=[]
    for i in range(10):
        btam.append(i)
    for i in range(100):
        for j in range(10):
            btam[j]=str(x[i*10+j])
        f.write(','.join(btam)+"\n")
    f.close()
    with open(nguon,"r+") as f:
        doc=f.read()
        doc=doc.replace(",", "  ")
        print(doc)
ghi_doc_bai5()