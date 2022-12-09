def doc_tap_tin_bai2():
    nguon=input("Nhap ten tap tin(nguồn):")
    with open(nguon,"r") as f:
        doc=f.read()
        print(doc)
doc_tap_tin_bai2()