import re
from typing import Callable, List

def kiem_tra_cong_thuc(cong_thuc: str, domain: List[int], predicates: dict) -> bool:
    def forall(var: str, subformula: str) -> bool:
        return all(eval(subformula, {**predicates, var: d}) for d in domain)
    
    def exists(var: str, subformula: str) -> bool:
        return any(eval(subformula, {**predicates, var: d}) for d in domain)
    
    cong_thuc = re.sub(r'∀(\w)', r'forall("\1", ', cong_thuc)
    cong_thuc = re.sub(r'∃(\w)', r'exists("\1", ', cong_thuc)
    cong_thuc = cong_thuc.replace(')', ')')
    
    try:
        return eval(cong_thuc, {"forall": forall, "exists": exists, **predicates})
    except Exception as e:
        print(f"Lỗi: {e}")
        return False

def main():
    demo_1 = '∀x (P(x) → Q(x)) ∧ ∃y P(y)'
    domain_1 = [1, 2, 3]
    predicates_1 = {
        "P": lambda x: x > 1,
        "Q": lambda x: x % 2 == 0
    }
    print(f"Demo 1: {demo_1}")
    print(f"Miền giá trị: {domain_1}")
    print("Hàm xác định:")
    print("P(x) = x > 1")
    print("Q(x) = x % 2 == 0")
    demo_1_translated = 'forall("x", "(P(x) <= Q(x))") and exists("y", "P(y)")'
    print(f"Kết quả: {kiem_tra_cong_thuc(demo_1_translated, domain_1, predicates_1)}")

    demo_2 = '∀x (P(x) → Q(x)) ∧ ∃y ¬P(y)'
    domain_2 = [1, 2, 3]
    predicates_2 = {
        "P": lambda x: x < 2,
        "Q": lambda x: x % 2 != 0
    }
    print(f"\nDemo 2: {demo_2}")
    print(f"Miền giá trị: {domain_2}")
    print("Hàm xác định:")
    print("P(x) = x < 2")
    print("Q(x) = x % 2 != 0")
    demo_2_translated = 'forall("x", "(P(x) <= Q(x))") and exists("y", "not P(y)")'
    print(f"Kết quả: {kiem_tra_cong_thuc(demo_2_translated, domain_2, predicates_2)}")

    demo_3 = '∀x (P(x) → Q(x)) ∨ ∃y (P(y) ∧ ¬Q(y))'
    domain_3 = [1, 2, 3]
    predicates_3 = {
        "P": lambda x: x == 2,
        "Q": lambda x: x % 2 == 0
    }
    print(f"\nDemo 3: {demo_3}")
    print(f"Miền giá trị: {domain_3}")
    print("Hàm xác định:")
    print("P(x) = x == 2")
    print("Q(x) = x % 2 == 0")
    demo_3_translated = 'forall("x", "(P(x) <= Q(x))") or exists("y", "P(y) and not Q(y)")'
    print(f"Kết quả: {kiem_tra_cong_thuc(demo_3_translated, domain_3, predicates_3)}")

    demo_4 = '∃x (P(x) ∧ Q(x)) ∧ ∀y P(y)'
    domain_4 = [1, 2, 3]
    predicates_4 = {
        "P": lambda x: x > 0,
        "Q": lambda x: x < 3
    }
    print(f"\nDemo 4: {demo_4}")
    print(f"Miền giá trị: {domain_4}")
    print("Hàm xác định:")
    print("P(x) = x > 0")
    print("Q(x) = x < 3")
    demo_4_translated = 'exists("x", "P(x) and Q(x)") and forall("y", "P(y)")'
    print(f"Kết quả: {kiem_tra_cong_thuc(demo_4_translated, domain_4, predicates_4)}")

    demo_5 = '∀x (P(x) ∨ Q(x)) ∧ ∃y (¬P(y) ∧ Q(y))'
    domain_5 = [1, 2, 3]
    predicates_5 = {
        "P": lambda x: x == 1,
        "Q": lambda x: x == 3
    }
    print(f"\nDemo 5: {demo_5}")
    print(f"Miền giá trị: {domain_5}")
    print("Hàm xác định:")
    print("P(x) = x == 1")
    print("Q(x) = x == 3")
    demo_5_translated = 'forall("x", "P(x) or Q(x)") and exists("y", "not P(y) and Q(y)")'
    print(f"Kết quả: {kiem_tra_cong_thuc(demo_5_translated, domain_5, predicates_5)}")

if __name__ == "__main__":
    main()
