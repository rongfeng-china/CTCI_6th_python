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
  previous = ''
  for i in range(len(item)+1):
    if i == len(item):
        current = v
    else:
        current  =  item[i]
    if current == previous and current == v:
        continue
    else:
        first = item[0:i]
        second = item[i:]
        values.append(first+v+second)
        previous = current
  return values
        
string = "aab"
print (permutation(string))
