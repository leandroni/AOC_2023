
from io import TextIOWrapper
import re
from math import prod

class AOCClass():
    infile : TextIOWrapper = None
    def __init__(self) -> None:
        self.infile = None
    
    def load_input(self, file : str = None) -> None:
        self.infile = open(file, 'r', encoding='UTF8') if file else None
    
    def get_indices(self, line : str):
        return [index for index, character in enumerate(line) if character.isdigit()]
        
    def has_symbol(self, line : str, index : int, only_star : bool = False):
        prev = max(index - 1, 0)
        next = min(index + 1, len(line) - 1)
        nline = re.sub('[\d.\n]','',line[prev: next+1]) if not only_star else re.sub('[^*]','',line[prev: next+1])
        return len(nline) > 0

    def run(self) -> int:
        lines = self.infile.readlines()
        numbers = []
        for line_number, line in enumerate(lines):
            prev_line = max(line_number - 1, 0)
            next_line = min(line_number + 1, len(lines)-1)
            indices = self.get_indices(line)
            prev_ind    = -999
            part_number = ''
            flag = False
            for index in indices:
                if index == prev_ind + 1:
                    part_number += line[index]
                else:
                    if flag:
                        numbers.append(int(part_number))
                    flag = False
                    part_number = line[index]
                if self.has_symbol(lines[prev_line], index) or self.has_symbol(line, index) or self.has_symbol(lines[next_line], index):
                    flag = True    
                prev_ind = index
            if flag:
                numbers.append(int(part_number))
        return sum(numbers)
    
    def run_2nd(self) -> int:
        lines = self.infile.readlines()
        numbers = {}
        stars   = {}
        for line_number, line in enumerate(lines):
            prev_line = max(line_number - 1, 0)
            next_line = min(line_number + 1, len(lines)-1)
            indices = self.get_indices(line)
            prev_ind    = -999
            start_index = -999
            part_number = ''
            flag = False
            
            for index, character in enumerate(line):
                if character == '*':
                        stars[(line_number, index)] = 0
            
            for index in indices:
                if index == prev_ind + 1:
                    part_number += line[index]
                else:
                    if flag:
                        numbers[(line_number, start_index, prev_ind)] = int(part_number)
                    flag = False
                    part_number = line[index]
                if (self.has_symbol(lines[prev_line], index, only_star=True) or self.has_symbol(line, index, only_star=True) or self.has_symbol(lines[next_line], index, only_star=True)) and not flag:
                    flag = True
                    start_index = index
                prev_ind = index
            if flag:
                numbers[(line_number, start_index, prev_ind)] = int(part_number)
        return_product = 0
        for index, (star_line, star_position) in enumerate(stars):
            counter = []
            for (num_line, num_start, num_end), number in numbers.items():
                if star_line in [num_line - 1, num_line, num_line + 1]:
                    if star_position in range(num_start - 1, num_end + 1 + 1):
                        counter.append(number)
            if len(counter) > 1:
                return_product += prod(counter)
        return return_product
                    

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
    