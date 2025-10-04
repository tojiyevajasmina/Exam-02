def filter_long_names(students: list, min_length: int = 5) -> list:
    return [name for name in students if len(name) > min_length]
    
print(filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"]))
# ["Hasan", "Husan", "Aziza", "Jasurbek"]

print(filter_long_names(["Ali", "Muhammad", "Jo"], 4))
# ["Muhammad"]