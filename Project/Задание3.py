def remove_duplicates(word):
    seen = set()  # Множество для отслеживания уже встреченных букв
    result = []   # Список для формирования нового слова

    for char in word:
        if char not in seen:
            result.append(char)
            seen.add(char)

    return ''.join(result)

# Пример использования
word = "исскуство"
new_word = remove_duplicates(word)
print(new_word)  
