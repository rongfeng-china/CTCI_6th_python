def magicFast(arr):
  start_index, end_index = 0, len(arr)-1
  while start_index <= end_index:
    mid_index = int((start_index+end_index)/2)
    if arr[mid_index]< mid_index:
      start_index = mid_index + 1 
    elif arr[mid_index]> mid_index:
      end_index = mid_index - 1 
    else:
      return mid_index
  return -1

def magicFastNotDistinct(arr,start_index,end_index):
  if start_index > end_index:
    return -1
  lists = []
  mid_index = (int(start_index+end_index)/2)
  v = arr[mid_index]
  left, right = -1,-1
  if arr[mid_index] < mid_index:
    ## left side
    if v >= start_index:
      left = magicFastNotDistinct(arr,start_index,v)
    ## right side
    if mid_index+1 <=end_index:
      right = magicFastNotDistinct(arr,mid_index+1,end_index)
    
  elif arr[mid_index] > mid_index:
    ## left side
    if mid_index-1 >= start_index:
      left = magicFastNotDistinct(arr,start_index,mid_index-1)
    ## right side
    if v <= end_index:
      right = magicFastNotDistinct(arr,v,end_index)
  
  else:
    lists.append(mid_index)
    left = magicFastNotDistinct(arr,start_index,mid_index-1)
    right = magicFastNotDistinct(arr,mid_index+1,end_index)
    
  if left != -1:
    lists = lists+left
  if right != -1:
    lists = lists+right
  
  return lists
  
arr1 = [-40,-20,-1,1,2,3,5,7,9,12,13]
print magicFast(arr1)
arr2 = [-10,-5,2,2,2,3,4,7,9,9,13]
print magicFastNotDistinct(arr2,0,len(arr2))