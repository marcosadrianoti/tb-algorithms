def is_anagram(first_string, second_string):
    first_st = merge_sort_string(first_string.lower())
    second_st = merge_sort_string(second_string.lower())
    if first_st == second_st and len(first_st) != 0 and len(second_st) != 0:
        return (first_st, second_st, True)
    return (first_st, second_st, False)


def merge_sort_string(string):
    if len(string) <= 1:
        return string

    half = len(string) // 2
    left_half = merge_sort_string(string[:half])
    right_half = merge_sort_string(string[half:])

    ordered_string = ""
    id_left_half = 0
    id_rigth_half = 0

    while id_left_half < len(left_half) and id_rigth_half < len(right_half):
        if left_half[id_left_half] < right_half[id_rigth_half]:
            ordered_string += left_half[id_left_half]
            id_left_half += 1
        else:
            ordered_string += right_half[id_rigth_half]
            id_rigth_half += 1

    ordered_string += left_half[id_left_half:]
    ordered_string += right_half[id_rigth_half:]

    return ordered_string
