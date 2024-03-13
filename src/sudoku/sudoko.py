import utils
import random
class Sudoku:
    def __init__(self):
        self.data = []

    def generate_sudoku(self):
        # shuffle;
        self.data = []
        for i in range(9):
            self.data.append([])
        first = utils.get_random_nine_list()
        b = first[3:]
        random.shuffle(b)
