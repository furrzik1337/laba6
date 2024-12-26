# Дано предложение
sentence = "Сколько же здесь букв и?"

# Подсчет количества букв "и"
count = 0
for char in sentence:
    if char.lower() == 'и':
        count += 1

# Вывод результата
print(f"Количество 'и': {count}")
