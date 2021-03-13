with open('/Users/udaydeshpande/Downloads/VTI/puts1', 'r') as f:
  sum = 0.0
  for line in f:
    sum = sum + float(line)
    print(sum)


