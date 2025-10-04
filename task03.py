def calculate_tax(salary: int) -> dict:
    if salary <= 5_000_000:
        rate = 0
        rate_str = "0%"
    elif salary <= 10_000_000:
        rate = 0.12
        rate_str = "12%"
    elif salary <= 20_000_000:
        rate = 0.18
        rate_str = "18%"
    else:
        rate = 0.25
        rate_str = "25%"

    tax = int(salary * rate)
    net = salary - tax

    return {"gross": salary, "tax": tax, "net": net, "rate": rate_str}

print(calculate_tax(8_000_000))
# {"gross": 8000000, "tax": 360000, "net": 7640000, "rate": "12%"}

print(calculate_tax(3_000_000))
# {"gross": 3000000, "tax": 0, "net": 3000000, "rate": "0%"}