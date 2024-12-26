import re

def is_valid_expression(expression):
    """Kiểm tra biểu thức logic có hợp lệ không."""
    
    valid_chars = re.compile(r'^[A-Z()¬∧∨→↔ ]+$')
    
    open_parens = expression.count('(')
    close_parens = expression.count(')')
    return bool(valid_chars.match(expression)) and open_parens == close_parens

def evaluate_expression(expression, values):
    """Tính giá trị của biểu thức logic với các biến."""
    
    expr = expression.replace('¬', ' not ').replace('∧', ' and ').replace('∨', ' or ')
    expr = expr.replace('→', ' <= ').replace('↔', ' == ')  
    
    for var, val in values.items():
        expr = re.sub(rf'\b{var}\b', str(val), expr)  
    try:
        
        return eval(expr)
    except Exception as e:
        return f"Lỗi khi tính giá trị biểu thức: {e}"


def main():
    
    demos = [
    {"expression": "(A ∧ B) → (¬C)", "values": {"A": True, "B": False, "C": True}},
    {"expression": "(A ∨ ¬B) ↔ C", "values": {"A": False, "B": True, "C": True}},
    {"expression": "A ∧ (B ∨ C)", "values": {"A": True, "B": False, "C": True}},
    {"expression": "¬A ∧ (B → C)", "values": {"A": False, "B": True, "C": False}},
    {"expression": "(A ∨ B) → (¬C)", "values": {"A": True, "B": True, "C": False}},
]

    for i, demo in enumerate(demos, 1):
        expr = demo["expression"]
        values = demo["values"]

        print(f"\nDemo {i}:")
        print(f"Biểu thức: {expr}")
        print(f"Giá trị biến: {values}")
        
        if is_valid_expression(expr):
            print("Biểu thức hợp lệ.")
            result = evaluate_expression(expr, values)
            print(f"Kết quả: {result}")
        else:
            print("Biểu thức không hợp lệ.")

if __name__ == "__main__":
    main()
