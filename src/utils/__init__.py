
import random

LIST_NINE = [1,2,3,4,5,6,7,8,9]
def get_random_nine_list():
    _list = [i for i in range(1,10)]
    random.shuffle(_list)
    return _list