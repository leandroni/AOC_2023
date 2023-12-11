
from io import TextIOWrapper
import re
class AOCClass():
    infile : TextIOWrapper = None
    def __init__(self) -> None:
        self.infile = None
    
    def load_input(self, file : str = None) -> None:
        self.infile = open(file, 'r', encoding='UTF8') if file else None
    
    def run(self) -> int:
        if self.infile:
            repl_dict = {'one' : '1', 'two' : '2', 'three' : '3', 'four' : '4', 'five' : '5',
                         'six' : '6', 'seven' : '7', 'eight': '8', 'nine': '9'}
            data = self.infile.read()
            newlines = []
            for length in [3,4,5]:
                new_data = ''
                for i, charac in enumerate(data):
                    if data[i : i+length] in repl_dict:
                        new_data += charac
                        new_data += repl_dict[data[i : i+length]]
                    new_data += charac
                data = new_data         
            newlines = data.split('\n')
            print(newlines)
            lines = [re.sub('[a-zA-Z\n]','',line) for line in newlines]
            lines = [int(line[0]+line[-1]) for line in lines]
        return sum(lines)

if __name__ == '__main__':
    ac = AOCClass()
    ac.load_input('sample_data.txt')
    print(f"{'sample_data.txt'}: {ac.run()}")
    ac.load_input('input.txt')
    print(f"{'input.txt'}: {ac.run()}")