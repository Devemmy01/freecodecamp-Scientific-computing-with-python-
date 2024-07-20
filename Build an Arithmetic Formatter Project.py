def arithmetic_arranger(problems, display_answers=False):
    if len(problems) > 5:
        return "Error: Too many problems."
    
    first_line = ""
    second_line = ""
    dashes = ""
    results = ""
    
    for i, problem in enumerate(problems):
        parts = problem.split()
        
        if parts[1] not in ["+", "-"]:
            return "Error: Operator must be '+' or '-'."
        
        if not parts[0].isdigit() or not parts[2].isdigit():
            return "Error: Numbers must only contain digits."
        
        if len(parts[0]) > 4 or len(parts[2]) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        if parts[1] == "+":
            answer = str(int(parts[0]) + int(parts[2]))
        else:
            answer = str(int(parts[0]) - int(parts[2]))
        
        width = max(len(parts[0]), len(parts[2])) + 2
        
        if i > 0:
            first_line += "    "
            second_line += "    "
            dashes += "    "
            results += "    "
        
        first_line += parts[0].rjust(width)
        second_line += parts[1] + parts[2].rjust(width - 1)
        dashes += "-" * width
        results += answer.rjust(width)
    
    if display_answers:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes}\n{results}"
    else:
        arranged_problems = f"{first_line}\n{second_line}\n{dashes}"
    
    return arranged_problems

# Test cases
print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
print(arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True))
