"""
Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring.
So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.

string_match('xxcaazz', 'xxbaaz') → 3
string_match('abc', 'abc') → 2
string_match('abc', 'axc') → 0
"""

def string_match(a, b):
    a_result = ""
    b_result = ""
    count = 0
    A = ""
    B = ""
    

    if len(a) > len(b):
        A = a[:len(b)]
        for i in range(len(A)):
            a_result = a_result + a[i]
            b_result = b_result + b[i]
            if len(a_result) == len(b_result) == 2:
                if a_result == b_result:
                    count += 1
                    a_result = a_result[1]
                    b_result = b_result[1]
                
                else:
                    a_result = a_result[1]
                    b_result = b_result[1]

            
    elif len(b) > len(a):
        B = b[:len(a)]
        for i in range(len(B)):
            a_result = a_result + a[i]
            b_result = b_result + b[i]
            if len(a_result) == len(b_result) == 2:
                if a_result == b_result:
                    count += 1
                    a_result = a_result[1]
                    b_result = b_result[1]

                else:
                    a_result = a_result[1]
                    b_result = b_result[1]
    else:
        for i in range(len(a)):
            a_result = a_result + a[i]
            b_result = b_result + b[i]
            if len(a_result) == len(b_result) == 2:
                if a_result == b_result:
                    count += 1
                    a_result = a_result[1]
                    b_result = b_result[1]

                else:
                    a_result = a_result[1]
                    b_result = b_result[1]
    return count


print(string_match('he', 'hello'))
