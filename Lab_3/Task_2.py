# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, delimiter = ','):
    group1 = set(participants_first_group.split(delimiter))
    group2 = set(participants_second_group.split(delimiter))
    recurring_participants = group1 & group2
    return sorted(recurring_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

common = find_common_participants(participants_first_group, participants_second_group, delimiter = '|')
print(common)