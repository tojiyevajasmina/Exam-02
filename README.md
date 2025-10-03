# Exam 02

---

## **Masala 1: Calculator (Kalkulyator)**

**Funksiya**: `calculate(num1: float, num2: float, operator: str) -> float`

**Talab**: 
- 4 ta asosiy amal: `+`, `-`, `*`, `/`
- Nolga bo'lish xatosini ushlab qoling
- Noto'g'ri operator kiritilsa xato qaytaring
- Natijani 2 kasr xonagacha yaxlitlang

**Test case**:
```python
calculate(15, 3, "/")    # 5.0
calculate(8, 5, "*")     # 40.0
calculate(10, 0, "/")    # Error: Nolga bo'lish mumkin emas
calculate(7, 4, "^")     # Error: Noto'g'ri operator
```

---

## **Masala 2: Simple ATM Simulation**

**Funksiya**: `atm_operation(balance: int, action: str, amount: int = 0) -> dict`

**Talab**:
- 3 ta amal: `deposit`, `withdraw`, `balance`
- Withdraw uchun balans yetarli emasligini tekshiring
- Manfiy summa kiritsa xato qaytaring
- Natija: `balance`

**Test case**:
```python
atm_operation(100000, "deposit", 50000) # 150000

atm_operation(100000, "balance") # 100000
```

---

## **Masala 3: Tax Calculator (Soliq Kalkulyatori)**

**Funksiya**: `calculate_tax(salary: int) -> dict`

**Soliq me'yorlari**:
- 0 - 5,000,000: 0%
- 5,000,001 - 10,000,000: 12%
- 10,000,001 - 20,000,000: 18%
- 20,000,001+: 25%

**Talab**: 
- Natija: `{"gross": int, "tax": int, "net": int, "rate": str}`

**Test case**:
```python
calculate_tax(8_000_000)
# {"gross": 8000000, "tax": 360000, "net": 7640000, "rate": "12%"}

calculate_tax(3_000_000)
# {"gross": 3000000, "tax": 0, "net": 3000000, "rate": "0%"}
```

---

## **Masala 4: FISH Tartibini O'zgartirish**

**Funksiya**: `format_name(full_name: str) -> str`

**Talab**:
- FISH (Familiya Ism Sharif) formatini `Ism Sharif, Familiya` shaklida qaytaring

**Test case**:
```python
format_name("Aliyev Vali G'aniyevich")
# "Vali G'aniyevich, Aliyev"
```

---

## **Masala 5: So'zlar Sonini Hisoblash**

**Funksiya**: `count_words(text: str) -> dict`

**Talab**:
- Matn ichidagi har bir so'z necha marta qatnashganini aniqlang
- Katta-kichik harfni e'tiborga olmang

**Test case**:
```python
count_words("salom salom dunyo")
# {"salom": 2, "dunyo": 1}

count_words("Python python PYTHON")
# {"python": 3}
```

---

## **Masala 6: Baholar Tizimi**

**Funksiya**: `analyze_grades(students: dict) -> dict`

**Talab**:
- O'rtacha bahoni hisoblang
- O'rtachadan yuqori baho olganlarni aniqlang
- Natija: `{"average": float, "above_average": list}`

**Test case**:
```python
analyze_grades({"Ali": 5, "Vali": 4, "Hasan": 5, "Husan": 3})
# {"average": 4.25, "above_average": ["Ali", "Hasan"]}

analyze_grades({"Aziz": 3, "Bobur": 4, "Diyor": 5})
# {"average": 4.0, "above_average": ["Diyor"]}
```

---

## **Masala 7: Mahsulotlar Savatchasi**

**Funksiya**: `calculate_cart(cart: dict) -> int`

**Talab**:
- Har bir mahsulot uchun: narx × miqdor
- Umumiy summani hisoblang

**Test case**:
```python
cart = {
  'non': {'price': 3000, 'quantity': 2},
  'sut': {'price': 8000, 'quantity': 1},
  'olma': {'price': 5000, 'quantity': 5}
}
calculate_cart(cart)  # 37000
```

---

## **Masala 8: Yig'indi va O'rtacha**

**Funksiya**: `calculate_stats(numbers: list) -> dict`

**Talab**:
- Ro'yxatdagi sonlar yig'indisi
- O'rtacha qiymatni hisoblang
- Natija: `{"sum": int, "average": float}`

**Test case**:
```python
calculate_stats([3, 7, 10, -5, -8, 15, 22])
# {"sum": 44, "average": 6.29}

calculate_stats([10, 20, 30])
# {"sum": 60, "average": 20.0}
```

---

## **Masala 9: Eng Katta va Eng Kichik Son**

**Funksiya**: `find_min_max(numbers: list) -> dict`

**Talab**:
- Ro'yxatdagi eng katta sonni toping
- Ro'yxatdagi eng kichik sonni toping
- Natija: `{"max": int, "min": int}`

**Test case**:
```python
find_min_max([3, 7, 10, -5, -8, 15, 22])
# {"max": 22, "min": -8}

find_min_max([100, 50, 200, -10])
# {"max": 200, "min": -10}
```

---

## **Masala 10: Tartiblash**

**Funksiya**: `sort_numbers(numbers: list, reverse: bool = False) -> list`

**Talab**:
- Ro'yxatdagi sonlarni tartiblang
- `reverse=True` bo'lsa kamayish tartibida
- `reverse=False` bo'lsa o'sish tartibida

**Test case**:
```python
sort_numbers([3, 7, 10, -5, -8, 15, 22, 0])
# [-8, -5, 0, 3, 7, 10, 15, 22]

sort_numbers([3, 7, 10, -5], reverse=True)
# [10, 7, 3, -5]
```

---

## **Masala 11: List Operations**

**Funksiya**: `analyze_list(items: list) -> dict`

**Talab**:
- Jami elementlar soni
- Noyob elementlar soni
- Dublikat elementlar ro'yxati
- Eng ko'p takrorlangan element

**Test case**:
```python
analyze_list(["Ali", "Vali", "Ali", 1, 2, 1])
# {
#   "total": 6,
#   "unique": 4,
#   "duplicates": ["Ali", 1],
#   "most_common": "Ali"
# }
```

---

## **Masala 12: Ismlarni Alfavit Bo'yicha Tartiblash**

**Funksiya**: `sort_names(students: list) -> list`

**Talab**:
- Ismlar ro'yxatini alfavit bo'yicha tartiblang
- Katta-kichik harfni e'tiborga olmang

**Test case**:
```python
sort_names(["Ali", "Vali", "Hasan", "Husan", "Aziza"])
# ["Ali", "Aziza", "Hasan", "Husan", "Vali"]

sort_names(["Zara", "Bobur", "Anvar"])
# ["Anvar", "Bobur", "Zara"]
```

---

## **Masala 13: Uzun Ismlar**

**Funksiya**: `filter_long_names(students: list, min_length: int = 5) -> list`

**Talab**:
- Uzunligi `min_length` dan katta bo'lgan ismlarni ajrating

**Test case**:
```python
filter_long_names(["Ali", "Vali", "Hasan", "Husan", "Aziza", "Jasurbek"])
# ["Hasan", "Husan", "Aziza", "Jasurbek"]

filter_long_names(["Ali", "Muhammad", "Jo"], 4)
# ["Muhammad"]
```

---

## **Masala 14: Pattern Matching**

**Funksiya**: `find_pattern(items: list, pattern: str, match_type: str) -> list`

**Match turlari**:
- `"starts"`: Pattern bilan boshlanadi
- `"ends"`: Pattern bilan tugaydi
- `"contains"`: Pattern ichida bor

**Talab**:
- Case-insensitive bo'lsin

**Test case**:
```python
find_pattern(["Ali", "Alisher", "Vali", "Aziz"], "A", "starts")
# ["Ali", "Alisher", "Aziz"]

find_pattern(["Alisher", "Bobur", "Jasur"], "ur", "ends")
# ["Bobur", "Jasur"]

find_pattern(["Python", "Java", "JavaScript"], "java", "contains")
# ["Java", "JavaScript"]
```

---

## **Masala 15: Eng Yuqori Baho**

**Funksiya**: `find_top_students(grades: dict) -> dict`

**Talab**:
- Eng yuqori bahoni toping
- Shu bahoga ega bo'lgan barcha talabalarni qaytaring
- Natija: `{"max_grade": int, "students": list}`

**Test case**:
```python
find_top_students({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5})
# {"max_grade": 5, "students": ["Ali", "Husan"]}

find_top_students({"Aziz": 4, "Bobur": 5, "Diyor": 3})
# {"max_grade": 5, "students": ["Bobur"]}
```

---

## **Masala 16: Bahosi Bo'yicha Sanash**

**Funksiya**: `count_by_grade(grades: dict, target_grade: int) -> dict`

**Talab**:
- Ma'lum bahoga ega talabalar sonini hisoblang
- Ularning ismlarini qaytaring
- Natija: `{"count": int, "students": list}`

**Test case**:
```python
count_by_grade({"Ali": 5, "Vali": 4, "Hasan": 3, "Husan": 5}, 5)
# {"count": 2, "students": ["Ali", "Husan"]}

count_by_grade({"Aziz": 4, "Bobur": 4, "Diyor": 3}, 4)
# {"count": 2, "students": ["Aziz", "Bobur"]}
```

---

## **Masala 17: Musbat Sonlarni Ajratish**

**Funksiya**: `filter_positive(numbers: list) -> list`

**Talab**:
- Dict ichidagi `value` kaliti musbat bo'lgan elementlarni ajrating
- Asl strukturani saqlang

**Test case**:
```python
filter_positive([{'value': -5}, {'value': 10}, {'value': -1}, {'value': 7}])
# [{'value': 10}, {'value': 7}]

filter_positive([{'value': 0}, {'value': 5}, {'value': -3}])
# [{'value': 5}]
```

---

## **Masala 18: Sonlarni Kvadratga Oshirish**

**Funksiya**: `square_values(numbers: list) -> list`

**Talab**:
- Har bir dict ichidagi `value` ni kvadratga oshiring
- Yangi list qaytaring (asl list o'zgarmaydi)

**Test case**:
```python
square_values([{'value': 2}, {'value': 3}, {'value': 4}])
# [{'value': 4}, {'value': 9}, {'value': 16}]

square_values([{'value': -2}, {'value': 5}])
# [{'value': 4}, {'value': 25}]
```

---

## **Masala 19: Eng Uzun Ism**

**Funksiya**: `find_longest_name(names: list) -> str`

**Talab**:
- Ismlar ro'yxatidan eng uzunini toping
- Agar bir nechta bo'lsa, birinchisini qaytaring

**Test case**:
```python
find_longest_name(['Ali', 'Diyor', 'Jasurbek', 'Muhammad'])
# "Jasurbek"

find_longest_name(['Bo', 'Ali', 'Zara'])
# "Zara"
```

---

## **Masala 20: Eng Qisqa Ismli O'quvchi**

**Funksiya**: `find_shortest_name_student(students: list) -> str`

**Talab**:
- Dict'lar ro'yxatidan ismi eng qisqa bo'lgan o'quvchini toping
- Faqat ismni qaytaring
- Agar bir nechta bo'lsa, birinchisini qaytaring

**Test case**:
```python
students = [
    {'name': 'Jasurbek', 'age': 20},
    {'name': 'Diyor', 'age': 19},
    {'name': 'Ali', 'age': 18},
    {'name': 'Muhammad', 'age': 21}
]
find_shortest_name_student(students)  # {'name': 'Ali', 'age': 18}

students2 = [
    {'name': 'Jo', 'age': 19},
    {'name': 'Ali', 'age': 20},
    {'name': 'Bob', 'age': 18}
]
find_shortest_name_student(students2)  # {'name': 'Jo', 'age': 19}
```
