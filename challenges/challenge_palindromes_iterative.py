def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    for id in range(0, len(word)//2):
        left_caracter = word[id]
        rigth_caracter = word[(id + 1) * -1]
        if left_caracter != rigth_caracter:
            return False
    return True
