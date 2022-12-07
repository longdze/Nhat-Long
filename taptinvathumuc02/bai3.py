def them_ki_tu_vao_chuoi_b3():
    nguon=input("Nhap ten tap tin (nguon):")
    chuoi=input("Nhập vào chuỗi muốn thêm :")
    with open(nguon,"a") as f:
        f.write(chuoi)

them_ki_tu_vao_chuoi_b3()