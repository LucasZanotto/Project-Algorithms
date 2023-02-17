def merge_sort(numbers, start=0, end=None):
    if end is None:
        end = len(numbers)
    if (end - start) > 1:
        mid = (start + end) // 2
        merge_sort(numbers, start, mid)
        merge_sort(numbers, mid, end)
        merge(numbers, start, mid, end)


def merge(numbers, start, mid, end):
    left = numbers[start:mid]
    right = numbers[mid:end]

    left_index, right_index = 0, 0

    for general_index in range(start, end):
        if left_index >= len(left):
            numbers[general_index] = right[right_index]
            right_index = right_index + 1
        elif right_index >= len(right):
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        elif left[left_index] < right[right_index]:
            numbers[general_index] = left[left_index]
            left_index = left_index + 1
        else:
            numbers[general_index] = right[right_index]
            right_index = right_index + 1


def is_anagram(first_string, second_string):
    primeira_palavra = list(first_string.lower())
    segunda_palavra = list(second_string.lower())
    merge_sort(primeira_palavra, 0, len(primeira_palavra))
    merge_sort(segunda_palavra, 0, len(segunda_palavra))
    print(primeira_palavra)
    if not primeira_palavra or not segunda_palavra:
        return ("".join(primeira_palavra), "".join(segunda_palavra), False)
    if primeira_palavra == segunda_palavra:
        return ("".join(primeira_palavra), "".join(segunda_palavra), True)
    if primeira_palavra != segunda_palavra:
        return ("".join(primeira_palavra), "".join(segunda_palavra), False)


# print(is_anagram("roMa", "roma"))
# saída: ('amor', 'amor', True)
