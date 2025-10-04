def find_min_max(numbers: list) -> dict:
    return {
        "max": max(numbers),
        "min": min(numbers)
    }
print(find_min_max([3, 7, 10, -5, -8, 15, 22]))
# {"max": 22, "min": -8}

print(find_min_max([100, 50, 200, -10]))
# {"max": 200, "min": -10}
