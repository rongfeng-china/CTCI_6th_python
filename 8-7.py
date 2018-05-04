def permutation(string):
  n = len(string)
  result = []
  if n == 1:
    result.append(string)
  else:
    value = permutation(string[0:n-1])
    for item in value:
      new_items = insert(item,string[n-1])
      result+=new_items
        
  return result
        
def insert(item,v):
  values = []
  for i in range(len(item)+1):
    first = item[0:i]
    second = item[i:]
    values.append(first+v+second)
  return values
        
string = "abcd"
print permutation(string)