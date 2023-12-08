
from io import TextIOWrapper

class AOCClass():
    infile : TextIOWrapper = None
    def __init__(self) -> None:
        self.infile = None
    
    def load_input(self, file : str = None) -> None:
        self.infile = open(file, 'r', encoding='UTF8') if file else None
    
    def run(self) -> int:
        from math import prod
        cube_dict = {'red' : 12, 'green' : 13, 'blue' : 14}
        min_cubes = []
        impossible_games = list()
        games = list()
        for line in self.infile.readlines():
            line = line.replace('\n','')
            game = int(line.split(':')[0].split(' ')[1])
            games.append(game)
            min_cubes.append({'red' : -1, 'green' : -1, 'blue' : -1})
            subsets = line.split(':')[1].split(';')
            for subset in subsets:
                for cubes in subset.split(','):
                    setg = cubes.strip().split(' ')
                    if cube_dict[setg[1]] < int(setg[0]):
                        impossible_games.append(game)
                    if min_cubes[-1][setg[1]] < int(setg[0]):
                        min_cubes[-1][setg[1]] = int(setg[0])
        impossible_games = list(set(impossible_games))
        
        return sum(games) - sum(impossible_games), sum([prod([v for j,v in i.items()]) for i in min_cubes])

if __name__ == '__main__':
    ac = AOCClass()
    ac.load_input('sample_data.txt')
    print(f"{'sample_data.txt'}: {ac.run()}")
    ac.load_input('input.txt')
    print(f"{'input.txt'}: {ac.run()}")