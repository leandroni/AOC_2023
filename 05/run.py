
from io import TextIOWrapper
import re
from math import prod

class AOCClass():
    infile : TextIOWrapper = None
    def __init__(self) -> None:
        self.infile = None
    
    def load_input(self, file : str = None) -> None:
        self.infile = open(file, 'r', encoding='UTF8') if file else None
    
    def convert_to_array(self, line : str) -> list:
        return [int(i) for i in list(filter(None, line.split(" ")))]
    
    def run(self) -> int:
        lines = self.infile.readlines()
        if len(lines) == 0:
            return -1
        map = {}
        type = None
        for line in lines:
            line = line.replace("\n","")
            if 'seeds:' in line[0:7]:
                seeds = self.convert_to_array(line.split(":")[1])
            elif 'map:' in line:
                type = line.split(" ")[0]
                map[type] = []
            elif len(line) == 0:
                type = None
            elif type:
                map[type].append(self.convert_to_array(line))
        
        # Start search:
        current_item = 'seed'
        while current_item != 'location':
            for key, items in map.items():
                if current_item in key.split("-")[0]:
                    #print(f">>{current_item}")
                    new_seeds = []
                    current_item = key.split("-")[2]
                    for seed in seeds:
                        flag = None
                        for ranges in items:
                            if seed >= ranges[1] and seed<= (ranges[1]+ranges[2]):
                                #print(f"For seed {seed} we found it in the {ranges} for {key}")
                                flag = ranges[0] + (seed - ranges[1])
                        new_seeds.append(flag if flag else seed)
                    seeds = new_seeds[:]
        return min(seeds)
    
    def run_2nd(self) -> int:
        lines = self.infile.readlines()
        if len(lines) == 0:
            return -1
        map = {}
        type = None
        for line in lines:
            line = line.replace("\n","")
            if 'seeds:' in line[0:7]:
                seeds = self.convert_to_array(line.split(":")[1])
            elif 'map:' in line:
                type = line.split(" ")[0]
                map[type] = []
            elif len(line) == 0:
                type = None
            elif type:
                map[type].append(self.convert_to_array(line))
        
        # Start search:
        current_item = 'seed'
        while current_item != 'location':
            for key, items in map.items():
                if current_item in key.split("-")[0]:
                    print(f">>{current_item}")
                    new_seeds = []
                    current_item = key.split("-")[2]
                    for index in range(0, len(seeds), 2):
                        temp_seeds = {}
                        start_seed = seeds[index]
                        end_seed   = seeds[index] + seeds[index+1]
                        flag = False
                        for ranges in items:
                            start_new_seed = ranges[0]
                            start_old_seed = ranges[1]
                            headroom       = ranges[2]
                            if start_seed < start_old_seed and end_seed >= start_old_seed and end_seed < start_old_seed + headroom:
                                # ....XXXXX
                                temp_seeds[start_old_seed] = [start_new_seed, end_seed - start_old_seed]
                            if start_seed >= start_old_seed and start_seed < start_old_seed + headroom and end_seed >= start_old_seed + headroom:
                                temp_seeds[start_seed] = [start_new_seed + (start_seed - start_old_seed), start_old_seed + headroom]
                            if start_seed >= start_old_seed and end_seed < start_old_seed + headroom:
                                temp_seeds[start_seed] = [start_new_seed + (start_seed - start_old_seed), end_seed - start_seed]
                        temp_seeds = dict(sorted(temp_seeds.items()))
                        print(f"Start at {start_seed} end at {end_seed}: {end_seed - start_seed}")
                        items_count = 0
                        for source, destination_arr in temp_seeds.items():
                            if start_seed < source:
                                new_seeds.append(start_seed)
                                new_seeds.append(source - start_seed)
                                items_count += source - start_seed
                            new_seeds.append(destination_arr[0])
                            new_seeds.append(destination_arr[1])
                            items_count += destination_arr[1]
                            start_seed = destination_arr[0] + destination_arr[1]
                        if end_seed > source + destination_arr[-2]:
                            new_seeds.append(destination_arr[-1] + destination_arr[-2])
                            new_seeds.append(end_seed - source)
                            items_count += end_seed - source
                            start_seed = start_seed + end_seed - source
                        if items_count < seeds[index+1]:
                            new_seeds.append(start_seed)
                            new_seeds.append(end_seed - start_seed)
                        print(f">> {new_seeds}")
                    seeds = new_seeds[:]
        print(seeds)
        return min(seeds)

if __name__ == '__main__':
    ac = AOCClass()
    ac.load_input('sample_data.txt')
    print(f"{'sample_data.txt'}: {ac.run()}")
    ac.load_input('sample_data.txt')
    print(f"{'sample_data.txt'}: {ac.run_2nd()}")
    ac.load_input('input.txt')
    print(f"{'input.txt'}: {ac.run()}")
    ac.load_input('input.txt')
    #print(f"{'input.txt'}: {ac.run_2nd()}")
    