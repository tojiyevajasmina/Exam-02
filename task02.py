def atm_operation(balance: int, action: str, amount: int) -> dict:
    if amount < 0:
        return {"Summa manfiy bo'lishi mumkin emas": None, "balance": balance}
    
    if action == "deposit":
        balance += amount
        return {"balance": balance}
    
    elif action == "withdraw":
        if amount > balance:
            return {"Balans yetarli emas": None, "balance": balance}
        balance -= amount
        return {"balance": balance}
    
    else:
        return {"Noma'lum amal": None, "balance": balance}
    
