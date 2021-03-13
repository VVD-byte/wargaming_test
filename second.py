# Представление о кольцевом буфере получено из статьи
# https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BB%D1%8C%D1%86%D0%B5%D0%B2%D0%BE%D0%B9_%D0%B1%D1%83%D1%84%D0%B5%D1%80


# Плюсы - можно сделать итератор
# Минусы -
class FifoOne:
    """
    Использование
    a = FifoOne(5)
    a.add(1)
    a.add(2)
    b = iter(a)
    for i in b:
        ...
    """
    def __init__(self, _len: int):
        """
        :param _len: Длина буфера
        """
        self.fifo = [None for i in range(_len)]
        self.history = []
        self.now = 0

    def __iter__(self):
        """
        :return: итератор
        """
        return self

    def __next__(self):
        """
        :return: следующее значение
        """
        dat = [i for i in self.fifo if i != None]
        if self.now + 1 < dat.__len__():
            self.now += 1
            return dat[self.now]
        else:
            self.now = 0
            return dat[self.now]

    def add(self, value):
        """
        :param value: Значение для добавления в буфер
        :return: None
        """
        if self.history.__len__() != 0:
            self.fifo[(self.history[0] + 1) % self.fifo.__len__()] = value
            self.history.insert(0, (self.history[0] + 1) % self.fifo.__len__())
        else:
            self.fifo[0] = value
            self.history.append(0)
        if self.history.__len__() > self.fifo.__len__():
            self.history.pop()

    def pop(self):
        """
        :return: None
        удаляет самое старое значение
        """
        if self.history:
            self.fifo[self.history.pop()] = None


# Плюсы -
# Минусы -
class FifoSec:
    def __init__(self, _len: int):
        self.fifo = [None for i in range(_len)]
        self.history = []
        self.now = 0

    def __str__(self):
        return self.fifo

    def pop(self):
        if self.history:
            self.fifo[self.history.pop()] = None

    def add(self, value):
        if self.history.__len__() != 0:
            self.fifo[(self.history[0] + 1) % self.fifo.__len__()] = value
            self.history.insert(0, (self.history[0] + 1) % self.fifo.__len__())
        else:
            self.fifo[0] = value
            self.history.append(0)
        if self.history.__len__() > self.fifo.__len__():
            self.history.pop()

    def next(self):
        try:
            dat = [i for i in self.fifo if i != None]
            if self.now + 1 < dat.__len__():
                self.now += 1
                return dat[self.now]
            else:
                self.now = 0
                return dat[self.now]
        except:
            return None
