def count_words(text: str) -> dict:
    words = text.lower().split()
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words("salom salom dunyo"))
# {"salom": 2, "dunyo": 1}

print(count_words("Python python PYTHON"))
# {"python": 3}