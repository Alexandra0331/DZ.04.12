# 1. Напишите программу, удаляющую из текста все слова, 
# содержащие "абв". В тексте используется разделитель пробел.
# in
# Number of words: 10

# out
# авб абв бав абв вба бав вба абв абв абв
# авб бав вба бав вба

# in
# Number of words: 6

# out
# ваб вба абв ваб бва абв
# ваб вба ваб бва

# in
# Number of words: -1

# out
# The data is incorrect

txt = input("Введите текст через пробел:\n")
print(f"Исходный текст: {txt}")
find_txt = "абв"
lst = [i for i in txt.split() if find_txt not in i]
print(f'Результат: {" ".join(lst)}')