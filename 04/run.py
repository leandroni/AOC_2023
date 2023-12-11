
from io import TextIOWrapper
import re
from math import prod

class AOCClass():
    infile : TextIOWrapper = None
    def __init__(self) -> None:
        self.infile = None
    
    def load_input(self, file : str = None) -> None:
        self.infile = open(file, 'r', encoding='UTF8') if file else None
    
    
    def run(self) -> int:
        lines = self.infile.readlines()
        points = 0
        for line_number, line in enumerate(lines):
            card = line.split(":")[0]
            win_num, raf_num = line.split(":")[1].split("|")[0].strip().split(' '), line.split(":")[1].split("|")[1].strip().split(' ')
            win_num, raf_num = list(filter(None, win_num)), list(filter(None, raf_num))
            number_matches = len([value for value in win_num if value in raf_num])
            points += 1 * 2 ** (number_matches-1) if number_matches > 1 else number_matches
        return points
    
    def run_2nd(self) -> int:
        lines = self.infile.readlines()
        cards = dict(zip(range(1, len(lines)+1),[1 for _ in range(1, len(lines)+1)]))
        for line_number, line in enumerate(lines):
            card = int(line.split(":")[0].split(' ')[-1])
            win_num, raf_num = line.split(":")[1].split("|")[0].strip().split(' '), line.split(":")[1].split("|")[1].strip().split(' ')
            win_num, raf_num = list(filter(None, win_num)), list(filter(None, raf_num))
            number_matches = len([value for value in win_num if value in raf_num])
            for i in range(1, 1+number_matches):
                cards[card+i] += cards[card]
        print(sum([cards[card] for card in cards]))
        return -1

if __name__ == '__main__':
    ac = AOCClass()
    ac.load_input('sample_data.txt')
    print(f"{'sample_data.txt'}: {ac.run()}")
    ac.load_input('sample_data.txt')
    print(f"{'sample_data.txt'}: {ac.run_2nd()}")
    ac.load_input('input.txt')
    print(f"{'input.txt'}: {ac.run()}")
    ac.load_input('input.txt')
    print(f"{'input.txt'}: {ac.run_2nd()}")
    