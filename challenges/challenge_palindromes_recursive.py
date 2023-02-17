def is_palindrome_recursive(word, low_index, high_index):
    palavra = word
    tamanho = len(palavra) // 2
    if not palavra:
        return False
    if low_index == tamanho:
        return True
    if palavra[high_index] != palavra[low_index]:
        return False
    else:
        return is_palindrome_recursive(word, (low_index + 1), (high_index - 1))


print(is_palindrome_recursive("AGUA", 0, 3))
