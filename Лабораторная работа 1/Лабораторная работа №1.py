# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Attack_Helicopter:
    def __init__(self, machine_weight: float, lifting_capacity: float, cargo_mass: float):
        """
        Создание и подготовка к работе объекта "Боевой вертолет"

        :param machine_weight: Масса вертолета
        :param lifting_capacity: Грузоподъемность

        Примеры:
        >>> helicopter = Attack_Helicopter(500, 400, 0)  # инициализация экземпляра класса
        """
        if not isinstance(machine_weight, (int, float)):
            raise TypeError("Масса вертолета должна быть типа int или float")
        if machine_weight <= 0:
            raise ValueError("Масса вертолета должна быть положительным числом")
        self.machine_weight = machine_weight

        if not isinstance(lifting_capacity, (int, float)):
            raise TypeError("Грузоподъемность должна быть int или float")
        if lifting_capacity < 0:
            raise ValueError("Грузоподъемность не может быть отрицательным числом")
        if lifting_capacity > machine_weight:
            raise ValueError("Вертолет - не муравей, больше своего веса поднять не может")
        self.lifting_capacity = lifting_capacity

        if not isinstance(cargo_mass, (int, float)):
            raise TypeError("Масса груза в отсеке должна быть int или float")
        if cargo_mass < 0:
            raise ValueError("Масса груза в отсеке не может быть отрицательным числом")
        if cargo_mass > lifting_capacity:
            raise ValueError("Вертолет - не волшебник, больше, чем значение грузоподъемности, поднять не может")
        self.cargo_mass = cargo_mass
    def is_empty_cargo(self) -> bool:
        """
        Функция которая проверяет загружен ли грузовой отсек вертолета

        :return: Есть ли на борту вертолета груз

        Примеры:
        >>> helicopter = Attack_Helicopter(500, 400, 0)
        >>> helicopter.is_empty_cargo()
        """
        ...

    def add_weight_to_helicopter(self, weight: float) -> None:
        """
        Добавление груза в отсек.
        :param weight: Масса добавляемого груза

        :raise ValueError: Если масса груза превышает допустимую грузоподъемность, то вызываем ошибку

        Примеры:
        >>> helicopter = Attack_Helicopter(500, 400, 0)
        >>> helicopter.add_weight_to_helicopter(200)
        """
        if not isinstance(weight, (int, float)):
            raise TypeError("Масса груза должна быть типа int или float")
        if weight < 0:
            raise ValueError("Добавляемая масса должна быть положительным числом")
        ...

    def remove_weight_from_cargo(self, unloadable_weight: float) -> None:
        """
        Извлечение груза из грузового отсека.

        :param unloadable_weight: Масса извлекаемого груза
        :raise ValueError: Если масса извлекаемого груза превышает массу груза в отсеке,
        то возвращается ошибка.

        :return: Масса реально извлеченного груза

        Примеры:
        >>> helicopter = Attack_Helicopter(500, 400, 300)
        >>> helicopter.remove_weight_from_cargo(200)
        """
        if not isinstance(unloadable_weight, (int, float)):
            raise TypeError("Масса груза должна быть типа int или float")
        if unloadable_weight < 0:
            raise ValueError("Извлекаемая масса должна быть положительным числом")
        ...

class Student:
    def __init__(self, last_name: str, diploma: dict):
        """
        Создание и подготовка к работе объекта "Студент"

        :param last_name: Фамилия студента
        :param diploma: Словарь, в котором содержаться названия дисциплин и оценки по ним

        Примеры:
        >>> student = Student('Петров', {"Химия":4,"Физика":3})  # инициализация экземпляра класса
        """
        if not isinstance(last_name, str):
            raise TypeError("Фамилия студента должна быть типа str")
        if last_name is None:
            raise ValueError("Каждый студент должен иметь фамилию")
        self.last_name = last_name

        if not isinstance(diploma, dict):
            raise TypeError("Список дисциплин и оценок по ним должен хранится в dict")
        for key in diploma.keys():
            if not type(key) is str:
                raise TypeError("Названия дисциплин должны содержаться в str")
        for value in diploma.values():
            if not type(value) is int:
                raise TypeError("Оценки по дисциплинам должны быть числом. Зачеты в сделку не входили.")
            if not 2 <= value <= 5:
                raise ValueError("Как его до сих пор не отчислили?")
        self.diploma = diploma

    def get_average(self) -> float:
        """
        Функция которая находит средний балл по дисциплинам

        :return: Значение среднего бала

        Примеры:
        >>> student = Student('Петров', {"Химия":4,"Физика":3})
        >>> student.get_average()
        """
        ...

    def is_scholarship_worthy(self, diploma: dict) -> bool:
        """
        Проверка на то, достоин ли студент стипендии, или нет. Для получения стипендии, надо, чтобы среди оценок были только 4 и 5.


        :return: Являются ли все оценки из зачетки 4 и 5.

        Примеры:
        >>> student = Student('Петров', {"Химия":4,"Физика":3})
        >>> student.is_scholarship_worthy(student.diploma)
        """
        for value in diploma.values():
            if not type(value) is int:
                raise TypeError("Оценки по дисциплинам должны быть числом. Зачеты в сделку не входили.")
            if not 2 <= value <= 5:
                raise ValueError("Как его до сих пор не отчислили?")
        ...

class Printer:
    def __init__(self, printing_volume: tuple, volumetric_flow: float):
        """
        Создание и подготовка к работе объекта "3Д принтер"

        :param printing_volume: Кортеж из 3 размеров рабочей зоны станка в мм (длинна, ширина, высота)
        :param volumetric_flow: Объемный расход принтера - количество пластика в см^3, который
         станок может выкладывать на стол в минуту


        Примеры:
        >>> printer = Printer((300,300,400),15)  # инициализация экземпляра класса
        """
        if not isinstance(printing_volume, tuple):
            raise TypeError("Рабочая зона станка должна быть представлена 3 размерами в формате tuple")
        if len(printing_volume) != 3 :
            raise ValueError("Рабочая зона представляется 3 размерами")
        self.printing_volume = printing_volume

        if not isinstance(volumetric_flow, (int, float)):
            raise TypeError("Объемный расход должно быть int или float")
        if volumetric_flow < 0:
            raise ValueError("Количество пластика выкладываемого на стол в минуту не может быть отрицательным числом")
        self.volumetric_flow = volumetric_flow

    def is_in_size(self, model_size: tuple) -> bool:
        """
        Функция которая проверяет пометиться ли модель с габаритами model_size на стол станка

        :param model_size: Кортеж из 3 размеров модели по осям в мм (длинна, ширина, высота)
        :return: Помещается ли модель на стол

        Примеры:

        >>> printer = Printer((300,300,400),15)
        >>> printer.is_in_size((150,150,150))
        """
        if not isinstance(model_size, tuple):
            raise TypeError("Габариты модели должны быть представлены 3 размерами в формате tuple")
        if len(model_size) != 3 :
            raise ValueError("Габариты модели представляются 3 размерами")

        ...

    def calculate_time(self, model_size: tuple, volumetric_flow: float) -> None:
        """
        Расчет времени печати модели по ее объему и объемному расходу станка.

        :param model_size: Кортеж из 3 размеров модели по осям в мм (длинна, ширина, высота)
        :param volumetric_flow: Объемный расход принтера - количество пластика в см^3, который
         станок может выкладывать на стол в минуту


        Примеры:
        >>> printer = Printer((300,300,400),15)
        >>> printer.calculate_time((150,150,150), printer.volumetric_flow)
        """
        if not isinstance(model_size, tuple):
            raise TypeError("Габариты модели должны быть представлены 3 размерами в формате tuple")
        if len(model_size) != 3:
            raise ValueError("Габариты модели представляются 3 размерами")
        if not isinstance(volumetric_flow, (int, float)):
            raise TypeError("Объемный расход должно быть int или float")
        if volumetric_flow < 0:
            raise ValueError("Количество пластика выкладываемого на стол в минуту не может быть отрицательным числом")
        ...


if __name__ == "__main__":
    doctest.testmod() # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
