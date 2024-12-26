def count_n_before_comma(sentence):
    count = 0
    for char in sentence:
        if char == ',':
            break
        if char.lower() == 'н':
            count += 1
    return count

# Пример использования функции
sentence_with_comma = "Как дела н, н, да, н!"
result_with_comma = count_n_before_comma(sentence_with_comma)
print(f"Количество букв 'н' до первой запятой: {result_with_comma}")
