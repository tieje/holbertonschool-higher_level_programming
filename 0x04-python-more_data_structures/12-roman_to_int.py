#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_dict_alt = {'IX': 9, 'XC': 90,
                      'CM': 900, 'IV': 4, 'XL': 40, 'CD': 400}
    total = 0
    alt_numbers_list = []
    normal_numbers = []
    if type(roman_string) != str:
        return 0

    def alt_form_check(x): return x[0] in roman_string
    alt_numbers = dict(filter(alt_form_check, roman_dict_alt.items()))
    for i in alt_numbers.items():
        if i[0] in roman_string:
            alt_numbers_list.append(i[1])
            roman_string.replace(i[0], '')
    for i in roman_string:
        normal_numbers.append(roman_dict.get(i))
    total = sum(normal_numbers) + sum(alt_numbers_list)
    return total
