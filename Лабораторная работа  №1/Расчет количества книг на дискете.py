# TODO Найдите количество книг, которое можно разместить на дискете
volume = 1.44
volume_in_kb = volume * 1024
volume_in_b = volume_in_kb * 1024
pages = 100
strings = 50
symbols = 25
volume_per_symbol_b = 4
count = int(volume_in_b //(pages * strings * symbols * volume_per_symbol_b))
print("Количество книг, помещающихся на дискету:", count)
