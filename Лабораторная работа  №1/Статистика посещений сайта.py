users = ['user1', 'user2', 'user3', 'user1', 'user4', 'user2']
stat_websiste ={
    'Общее количество': 0,
    'Уникальные посещения': 0
}
stat_websiste['Общее количество'] = len(users)
stat_websiste['Уникальные посещения'] = len(set(users))

print(stat_websiste)
# TODO Добавьте словарь и замените в нем нулевые значения статисчикой посещений
