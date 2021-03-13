with open('/Users/udaydeshpande/Downloads/VTI/options', 'r') as f:
    strike_sum = 0
    for line in f:
        strs = line.split()
        strike = float(strs[4])
        strike_sum += strike
        print(f'{strike} and {strike_sum} and {strike_sum * 100}')
