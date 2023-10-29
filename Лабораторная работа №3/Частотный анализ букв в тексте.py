# TODO  Напишите функцию count_letters
def count_letters(s):
    dictionary = {}
    stroka = ''.join(s.lower().split())
    for i in stroka:
        if i.isalpha():
            if i  not in dictionary:
                dictionary[i] = 0
            dictionary[i] += 1
    return dictionary





# TODO Напишите функцию calculate_frequency
def calculate_frequency(s):
    dictionary = count_letters(s)
    keys = list(dictionary)
    result = {}
    for i,k in enumerate(dictionary):
        summary = sum(dictionary.values())
        result[keys[i][0]] = f"{(dictionary[k] / summary):.2f}"
    return result
main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте
for key, value in calculate_frequency(main_str).items():
    print(key+':',value)