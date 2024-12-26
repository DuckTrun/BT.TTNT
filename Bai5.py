from itertools import product
import re

# Hàm tạo bảng chân trị cho các biến
def tao_bang_chan_tri(variables):
    return list(product([True, False], repeat=len(variables)))

# Hàm kiểm tra một biểu thức với giá trị của các biến
def kiem_tra_bieu_thuc(bieu_thuc, values):
    for var, val in values.items():
        # Thay thế biến bằng giá trị True/False
        bieu_thuc = re.sub(fr'\b{var}\b', str(val), bieu_thuc)
    try:
        return eval(bieu_thuc)
    except Exception as e:
        print(f"Lỗi khi đánh giá biểu thức: {bieu_thuc} - {e}")
        return False

# Hàm tìm tất cả các mẫu giá trị
def tim_mau_gia_tri(bieu_thuc):
    # Chỉ lấy các biến là A, B, C
    variables = set(re.findall(r'\b[A-Z]\b', bieu_thuc))
    bang_chan_tri = tao_bang_chan_tri(variables)
    mau_gia_tri_list = []
    
    for row in bang_chan_tri:
        values = dict(zip(variables, row))
        if kiem_tra_bieu_thuc(bieu_thuc, values):
            mau_gia_tri_list.append(values)
    
    return mau_gia_tri_list

# Demo các biểu thức logic mệnh đề
def main():
    # Ví dụ 1
    bieu_thuc_1 = "(A or B) and (not A or C)"
    mau_gia_tri_list_1 = tim_mau_gia_tri(bieu_thuc_1)
    print("Demo 1:")
    print(f"Biểu thức: {bieu_thuc_1}")
    if mau_gia_tri_list_1:
        for values in mau_gia_tri_list_1:
            print({var: val for var, val in values.items()})
    else:
        print("Không có mẫu giá trị nào")

    # Ví dụ 2
    bieu_thuc_2 = "(A and B) or (not B and C)"
    mau_gia_tri_list_2 = tim_mau_gia_tri(bieu_thuc_2)
    print("\nDemo 2:")
    print(f"Biểu thức: {bieu_thuc_2}")
    if mau_gia_tri_list_2:
        for values in mau_gia_tri_list_2:
            print({var: val for var, val in values.items()})
    else:
        print("Không có mẫu giá trị nào")

    # Ví dụ 3
    bieu_thuc_3 = "A and (B or C) and not (A and B)"
    mau_gia_tri_list_3 = tim_mau_gia_tri(bieu_thuc_3)
    print("\nDemo 3:")
    print(f"Biểu thức: {bieu_thuc_3}")
    if mau_gia_tri_list_3:
        for values in mau_gia_tri_list_3:
            print({var: val for var, val in values.items()})
    else:
        print("Không có mẫu giá trị nào")

    # Ví dụ 4
    bieu_thuc_4 = "A or B or C"
    mau_gia_tri_list_4 = tim_mau_gia_tri(bieu_thuc_4)
    print("\nDemo 4:")
    print(f"Biểu thức: {bieu_thuc_4}")
    if mau_gia_tri_list_4:
        for values in mau_gia_tri_list_4:
            print({var: val for var, val in values.items()})
    else:
        print("Không có mẫu giá trị nào")

    # Ví dụ 5
    bieu_thuc_5 = "(A and not B) or (B and not C)"
    mau_gia_tri_list_5 = tim_mau_gia_tri(bieu_thuc_5)
    print("\nDemo 5:")
    print(f"Biểu thức: {bieu_thuc_5}")
    if mau_gia_tri_list_5:
        for values in mau_gia_tri_list_5:
            print({var: val for var, val in values.items()})
    else:
        print("Không có mẫu giá trị nào")

if __name__ == "__main__":
    main()
