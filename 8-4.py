def power_set(s):
  length = len(s)
  result = []
  for i in range(2**length):
    temp_list = list(s)
    new_set = set()
    binary = bin(i)[2:].zfill(length)
    for j in range(length):
      if binary[j] == '1':
        new_set.add(temp_list[j])
    result.append(new_set)
  return result
    

s = {'1','2','3'}
print power_set(s)