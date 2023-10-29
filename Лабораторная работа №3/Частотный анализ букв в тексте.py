# TODO Напишите функцию find_common_participants

def find_common_participants(s1,s2, dev=','):

    result = list(set(s2.split(dev)).intersection(set(s1.split(dev))))
    result.sort()
    return result
participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group,participants_second_group,dev='|'))