import numpy as np

# среднее время сортировки списка 100 000 случайных чисел таким способом - 0.06
# стандартные средства python позволяют это сделать за 0.7+
def sort_(dat: list):
    return list(np.sort(np.array(dat)))
