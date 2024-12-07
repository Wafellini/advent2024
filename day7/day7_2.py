import itertools
from operator import mul
from tqdm import tqdm
calibrations = {}

with open('input1', 'r') as file:
    for line in file:
        result, numbers = line.strip().split(":")
        calibrations[int(result)] = list(map(int, numbers.strip().split()))

def combine(num1, num2):
    return int(str(num1)+str(num2))

symbols = [sum, mul, combine]
valid_calibrations = []
for result, inputs in tqdm(calibrations.items(), desc="Processing Calibrations", unit="calibration"):
    pairs = [[inputs[indx], inputs[indx + 1]] for indx in range(len(inputs)-1)]
    permutations = list(itertools.product(symbols, repeat=len(pairs)))

    for permutation in permutations:
        calculation = 0
        for indx, (nums, operation) in enumerate(zip(pairs, permutation)):
            if indx == 0:
                calculation = operation(nums) if operation == sum else operation(*nums)
            else:
                calculation = operation([calculation, nums[1]]) if operation == sum else operation(calculation, nums[1])
        
        if calculation == result:
            valid_calibrations.append(result) 
            break
        
print(sum(valid_calibrations))