#写一个函数，把罗马数字转化为整数。输入为 1 到 3999之间的任意数字
def roman_to_int(src):
    convert_map = {
        'I':1,
        'V':5,
        'X':10,
        'L':50,
        'C':100,
        'D':500,
        'M':1000
    }
    roman = src.upper()[::-1]
    prew = 0
    lst = []
    for x in roman:
        i = convert_map[x]
        if i < prew:
            lst.append(-1 * i)
        else:
            lst.append(i)
        prew = i
    return sum(lst)
print(roman_to_int('MCMLXXXVII'))