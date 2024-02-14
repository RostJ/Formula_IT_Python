class Part:

    """ Базовый класс детали на производстве. """

    def __init__(self, material: str, weight: float) -> None:
        """
                        Создание и подготовка к работе объекта "Деталь"

         :param material: Строка с указанием типа материала, из которого изготовлена деталь
         :param weight: Вес детали в кг, указанный при помощи числа с плавающей точкой   """


        if not isinstance(material, str):
            raise TypeError("Материал задается типом 'строка' даже если состоит исключительно из цифр")
        if len(material) == 0:
            raise ValueError("Необходимо задать материал")
        self.material = material

        if not isinstance(weight, float):
            raise TypeError("Вес должен быть представлен в виде числа формата float")
        if weight < 0:
            raise ValueError("Вес не может быть отрицательным числом")
        self.weight = weight

    def set_material(self, new_material: str) -> None:
        """
                Метод осуществляет замену материала детали.

        :param new_material: Новый материал

        :raise TypeError: Если материал указан не в том формате - будет вызвана ошибка
        :raise ValueError: Если параметр не указан, будет вызвана ошибка, ведь у детали обязан быть материал


            """
        if not isinstance(new_material, str):
            raise TypeError("Материал должен задаваться при помощи str")
        if len(new_material) == 0:
            raise ValueError("Необходимо указать материал")
        self.material = new_material


    def set_weight(self, new_weight: float) -> None:
        """
                Метод осуществляет замену веса детали.

        :param new_weight: Новый вес детали

        :raise TypeError: Если вес указан не в том формате - будет вызвана ошибка
        :raise ValueError: Если параметр не указан или отрицателен, будет вызвана ошибка, ведь у детали обязан быть вес


            """
        if not isinstance(new_weight, float):
            raise TypeError("Вес должен задаваться при помощи str")
        if new_weight <= 0:
            raise ValueError("Необходимо указать вес")
        self.weight = new_weight

    def __str__(self) -> str:
        return f"Материал {self.material}. Вес {self.weight}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(material={self.material!r}, weight={self.weight!r})"


class Shaft(Part):

    """ Подкласс детали - Вал """

    def __init__(self, material: str, weight: float, diameter: float, length: float) -> None:
        """
                                Создание и подготовка к работе объекта "Вал"

                 :param material: Строка с указанием типа материала, из которого изготовлена деталь
                 :param weight: Вес детали в кг, указанная при помощи числа с плавающей точкой
                 :param diameter: Диамтер детали в мм, указанный при помощи числа с плавающей точкой
                 :param length: Длина детали в мм, указанная при помощи числа с плавающей точкой  """

        super().__init__(material=material, weight=weight)

        if not isinstance(diameter, float):
            raise TypeError("Диаметр должен быть представлен в виде числа формата float")
        if diameter < 0:
            raise ValueError("Диаметр не может быть отрицательным числом")
        self.diameter = diameter

        if not isinstance(length, float):
            raise TypeError("Длина должна быть представлена в виде числа формата float")
        if length < 0:
            raise ValueError("Длина не может быть отрицательным числом")
        self.length = length

    def set_material(self, new_material: str) -> None:
        """
                        Метод осуществляет замену материала детали.

                :param new_material: Новый материал

                :raise TypeError: Если материал указан не в том формате - будет вызвана ошибка
                :raise ValueError: Если параметр не указан, будет вызвана ошибка, ведь у детали обязан быть материал


                    """
        super().set_material(new_material=new_material)

    def set_weight(self, new_weight: float, keep_diameter: bool, keep_length: bool) -> None:
        """
                Метод осуществляет замену веса детали.

        :param new_weight: Новый вес детали
        :param keep_diameter: При замене веса, диаметр детали останется тем же (если это возможно) - изменится длина
        :param keep_length: При замене веса, длина детали останется той же (если это возможно) - изменится диаметр

        :raise TypeError: Если вес или указатель (keep_...) указан не в том формате - будет вызвана ошибка
        :raise ValueError: Если параметр не указан или отрицателен, будет вызвана ошибка, ведь у детали обязан быть вес


            """
        if not isinstance(new_weight, float):
            raise TypeError("Вес должен задаваться при помощи str")
        if not isinstance(keep_length, bool):
            raise TypeError("Указатель сохранения длины должен быть представлен в виде bool")
        if not isinstance(keep_diameter, bool):
            raise TypeError("Указатель сохранения диаметра должен быть представлен в виде bool")
        if new_weight <= 0:
            raise ValueError("Необходимо указать вес")


    def __str__(self):
        return f"Материал {self.material}. Вес {self.weight}. Диаметр {self.diameter}. Длина {self.length}."

    def __repr__(self):
        return f"{self.__class__.__name__}(material={self.material!r}, weight={self.weight!r}, " \
               f"diameter={self.diameter!r}, length={self.length!r})"

if __name__ == "__main__":
    # Write your solution here
    part = Part('Сталь',2.00)
    shaft = Shaft('Алюминий', 3.25, 15.00, 250.00)
    print(part)
    print(shaft)
    print()
    print(part.__repr__())
    print(shaft.__repr__())
    # изменяем материал
    part.set_material('Бронза')
    shaft.set_material('Титан')
    print(part.__repr__())
    print(shaft.__repr__())
    pass
