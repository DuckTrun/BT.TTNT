import itertools
import re

def generate_truth_table(expression):
    """Tạo bảng chân trị cho biểu thức logic mệnh đề."""
    variables = sorted(set(re.findall(r'\b[A-Z]\b', expression)))

    expr = (expression
            .replace('¬', ' not ')
            .replace('∧', ' and ')
            .replace('∨', ' or ')
            .replace('→', ' <= ')
            .replace('↔', ' == '))

    truth_combinations = list(itertools.product([True, False], repeat=len(variables)))

    truth_table = []
    for combination in truth_combinations:
        values = dict(zip(variables, combination))
        eval_expr = expr
        for var, val in values.items():
            eval_expr = re.sub(rf'\b{var}\b', str(val), eval_expr)
        try:
            result = eval(eval_expr)
        except Exception as e:
            result = f"Error: {e}"
        truth_table.append({**{k: 'T' if v else 'F' for k, v in values.items()}, 'Kết quả': 'T' if result else 'F'})

    return variables, truth_table

def print_truth_table(variables, truth_table):
    """In bảng chân trị."""
    header = variables + ['Kết quả']
    column_widths = {var: max(len(var), 5) for var in header}

    for row in truth_table:
        for var in header:
            column_widths[var] = max(column_widths[var], len(str(row[var])))

    header_line = " | ".join(f"{var:<{column_widths[var]}}" for var in header)
    print(header_line)
    print("-" * len(header_line))

    for row in truth_table:
        row_line = " | ".join(f"{str(row[var]):<{column_widths[var]}}" for var in header)
        print(row_line)


demos = [
    "(A ∨ ¬B) ∧ C",
    "A ∧ (B → C)",
    "(A ↔ B) ∨ ¬C",
    "¬(A ∨ B) ∧ C",
    "(A ∧ B) → (C ∨ ¬A)"
]

for i, demo_expr in enumerate(demos, 1):
    print(f"\nDemo {i}: Biểu thức: {demo_expr}")
    variables, truth_table = generate_truth_table(demo_expr)
    print_truth_table(variables, truth_table)
