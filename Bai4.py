import re
from itertools import product

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
    except SyntaxError as e:
        print(f"Lỗi cú pháp trong biểu thức: {bieu_thuc} - {e}")
        return False

# Hàm tự động chứng minh
def tu_dong_chung_minh(premises, conclusion):
    variables = set()
    for premise in premises:
        variables.update(set(filter(str.isalpha, premise)))
    variables.update(set(filter(str.isalpha, conclusion)))

    bang_chan_tri = tao_bang_chan_tri(variables)
    for row in bang_chan_tri:
        values = dict(zip(variables, row))
        if all(kiem_tra_bieu_thuc(p, values) for p in premises) and not kiem_tra_bieu_thuc(conclusion, values):
            return False
    return True

# Demo các mệnh đề
def main():
    # Ví dụ 1
    premises_1 = ["P <= Q", "Q <= R"]
    conclusion_1 = "P <= R"
    print("Demo 1:")
    print(f"Premises: {premises_1}")
    print(f"Conclusion: {conclusion_1}")
    print(f"Kết quả: {'Đúng' if tu_dong_chung_minh(premises_1, conclusion_1) else 'Sai'}")

    # Ví dụ 2
    premises_2 = ["A and B", "B or C"]
    conclusion_2 = "A"
    print("\nDemo 2:")
    print(f"Premises: {premises_2}")
    print(f"Conclusion: {conclusion_2}")
    print(f"Kết quả: {'Đúng' if tu_dong_chung_minh(premises_2, conclusion_2) else 'Sai'}")

    # Ví dụ 3
    premises_3 = ["not A or B", "not B or C"]
    conclusion_3 = "not A or C"
    print("\nDemo 3:")
    print(f"Premises: {premises_3}")
    print(f"Conclusion: {conclusion_3}")
    print(f"Kết quả: {'Đúng' if tu_dong_chung_minh(premises_3, conclusion_3) else 'Sai'}")

    # Ví dụ 4
    premises_4 = ["P <= Q", "not Q"]
    conclusion_4 = "not P"
    print("\nDemo 4:")
    print(f"Premises: {premises_4}")
    print(f"Conclusion: {conclusion_4}")
    print(f"Kết quả: {'Đúng' if tu_dong_chung_minh(premises_4, conclusion_4) else 'Sai'}")

    # Ví dụ 5
    premises_5 = ["P and not Q", "Q or R"]
    conclusion_5 = "P and R"
    print("\nDemo 5:")
    print(f"Premises: {premises_5}")
    print(f"Conclusion: {conclusion_5}")
    print(f"Kết quả: {'Đúng' if tu_dong_chung_minh(premises_5, conclusion_5) else 'Sai'}")

if __name__ == "__main__":
    main()
