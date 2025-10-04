from rich.console import Console
console = Console()

def calculate(num1, num2, operator) -> float:

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            console.print("Nolga bo'lish mumkin emas",style = 'bold red')
            return 
        result = num1 / num2
    else:
        console.print("Noto'g'ri operator",style = 'bold red')
        return 

    return round(result, 2)

print(calculate(15, 3, "/"))   # 5.0
print(calculate(8, 5, "*"))     # 40.0
print(calculate(10, 0, "/"))    # Error: Nolga bo'lish mumkin emas
print(calculate(7, 4, "^"))     # Error: Noto'g'ri operator