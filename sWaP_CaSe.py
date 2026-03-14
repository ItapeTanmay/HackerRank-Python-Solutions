"""

"""

def swap_case(s):
    op=""
    for ch in s:
        if ch.isupper():
            op+=ch.lower()
        else:
            op+=ch.upper()
    return op

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)