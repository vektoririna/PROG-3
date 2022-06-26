"""
    Реализовать программу шифрующую строку, задаваемую пользователем, с помощью
    алгоритма шифрования ROT13
"""


def main():
    str = input('Введите строку ')
    print(rot13(str))


def rot13(str):
    """
        Шифр
    """
    str1 = ""
    for i in str:
        k = ord(i)
        if 65 <= k <= 77 or 97 <= k <= 109:
            k += 13
        elif 78 <= k <= 90 or 109 <= k <= 122:
            k -= 13
        str1 += chr(k)
   return str1
main()