# плюс: выполняет поставленную задачу, может принимать данные типа 2.0 / '2.0' / 2 / '2'
# минусы: более ресурсозатранта
def isEven(value):
    return float(value) % 10 in [0.0, 2.0, 4.0, 6.0, 8.0]


