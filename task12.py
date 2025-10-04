def sort_names(names):
    return sorted(names, key=lambda name: name.lower())

print(sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"]))
# ["Ali", "Aziza", "Hasan", "Husan", "Vali"]

print(sort_names(["Zara", "Bobur", "Anvar"]))
# ["Anvar", "Bobur", "Zara"]