def search_last_occurrence(pat, txt):
    M = len(pat)
    N = len(txt)
    comparisons = 0
    last_index = -1 # ініціалізація -1 якщо підстрічка не знайдена у стрічці і вона за умовчуванням

    # змішення патерну або інш. каж. пошук останього сходження
    for i in range(N - M + 1):
        j = 0
        found = True # ініціалізація зміни для того чи був знайдений паттерн на позиції в тексті за умовчуванням


        while(j < M): # перевірка символа підстрічки з позиції тексту
            comparisons += 1
            if (txt[i + j] != pat[j]):
                found = False
                break
            j += 1

        if found:
            last_index = i

    return last_index, comparisons


if __name__ == '__main__':
    txt = "If you good why you scare about exam? You scare"
    pat = "scare"

    # Function call
    index, comparisons = search_last_occurrence(pat, txt)
    if index != -1:  # якщо патерн знайдено
        print(f"Pattern found at index {index}")
    else:
        print("Pattern not found") # якщо не знайдено
    print(f"Number of comparisons: {comparisons}")

# P.S (N - M + 1) це кілкьість ІТЕРАЦІЇ де N - довжина тексту M - довжина підстрічки