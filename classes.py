"""
ООП - стиль прогрпмирования
Класс - фабрика экземпляров
Экземпляр - конкретная реализация объекта
"""


class Player:
    # Класс это переменные + функции
    def __init__(self, name: str, image: str, level: int, hp: int, xp: int) -> None:
        '''
        Конструктор класс
        Вызывается сам после создания эгземпляра
        self - ссылка на сам экземпляр
        Все атрибуты определяются тут!!! 
        '''
        # экземплярный атребут
        self.name = name
        self.image = image
        self.level = level
        self.hp = hp
        self.xp = xp
        self.attack = 1
        self.defence = 1
        self.weapon = Weapon()


class Weapon():
    def __init__(self, name='', attack=1) -> None:
        self.name = name
        if not self.name:
            self.name = 'Кулак'
        self.attack = attack

    def __str__(self) -> str:
        return f'{self.name} ({self.attack})'



            


