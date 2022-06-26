"""
    Создание скрипта для считывания данных справочных логов из текстового
    файла и преобразования их в CSV-формат с последующей записью в новый файл.
"""


def main():
    handle = open('MOCK_DATA.json')
    lines = handle.readlines()
    di = dictionary(lines)
    handle.close()
    new_csv(di)


def dictionary(lines):
    """
        Формирование словаря из файла
    """
    l = []
    for line in lines:
        d = {}
        k = line.find('"')
        line = line+","
        for i in line:
            begin = line.find(":", k)
            if begin != -1:
                end = line.find(",", begin)
                if end != -1:
                    key = line[k:begin].strip(",").strip('"')
                    value = line[begin:end].strip(":").strip("}").strip('"').strip("]").strip("}").strip('"')
                    d.update({key: value})
                    k = end
            else:
                k += 1
        l.append(d)
    return l


def new_csv(di):
    """
        Создание файла в формате CSV
    """
    import csv
    with open('newfile.csv', 'w', newline='') as csvfile:
        fieldnames = ["id", "first_name", "last_name", "email", "gender", "ip_address"]
        cswr = csv.DictWriter(csvfile, fieldnames=fieldnames)
        cswr.writeheader()
        for data in di:
            cswr.writerow(data)


main()