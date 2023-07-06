def is_palindrome_recursive(word, low_index, high_index):
    # Retorne False se nenhuma palavra for passada por parâmetro.
    if len(word) == 0:
        return False
    # Se a palavra tem só uma letra, então já um palindrome.
    elif len(word) == 1:
        return True
    # Se a primeira e a última letra são diferentes, não é um palindrome.
    elif word[low_index] != word[high_index]:
        return False
    # Indica o cruzamento dos index na última substring.
    if low_index >= high_index:
        return True
    else:
        first_caracter = low_index + 1  # Avança um caracter no início.
        last_caracter = high_index - 1  # Recua um caracter no final.
        return is_palindrome_recursive(word, first_caracter, last_caracter)
