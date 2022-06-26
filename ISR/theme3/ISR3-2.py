"""
    Разработка сценария  с реализацией операции поиска подстроки в тексте.
"""


def main():
    input_str = input("Введите строку для поиска: ")
    searchable_str = input("Введите строку, по которой мы ищем: ")
    firstN = 0
    choice = None
    while choice != '4':
        print('1 - поиск первого вхождения подстрки')
        print('2 - замена первой подстроки')
        print('3 - найти все вхождения подстроки')
        print('4 - для выхода')
        choice = input("Сделайте  выбор (1..4) ")
        if choice == '1':
            firstN = search_str(input_str, searchable_str)
            print('Положение первого вхождения искомой строки: ', firstN)
        if choice == '2':
            print(rep_str(input_str, searchable_str))
        if choice == '3':
            print('Искомые строки находятся на следующих позициях')
            print(alle_str(firstN, input_str, searchable_str))


def search_str(what="", where=""):
    """
        Поиск первого вхождения подстроки
    """
    return where.find(what)


def rep_str(what="", where=""):
    """
        Замена подстроки
    """
    replace_str = input("Строка для замены: ")
    newStr = where.replace(what, replace_str)
    return newStr


def alle_str(N, what="", where=""):
    """
        Поиск всех подстрок
    """
    i = N
    lst = []
    while i < len(where):
        k = where.find(what, i)
        lst.append(k)
        i = len(what) + k
    return lst


main()