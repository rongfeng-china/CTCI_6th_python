def minProduct(a,b):
  if a <= b:
    return minProductHelper(a,b)
  else:
    return minProductHelper(b,a)
    
def minProductHelper(a,b):
  if a == 0:
    return 0
  if a == 1:
    return b 
  
  h = a >> 1 
  half_result = minProductHelper(h,b)
  if a%2 == 1:
    return half_result+half_result+b 
  else:
    return half_result+half_result
    
    
print minProduct(31,35)
print 31*35