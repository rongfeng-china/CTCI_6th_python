def moveDisks(n,from_stack,to_stack,towers):
  if n == 1:
    v = towers[from_stack].pop()
    print 'move %d from stack %d to stack %d' %(v,from_stack,to_stack)
    if towers[to_stack] == []:
      towers[to_stack].append(v)
    elif v < towers[to_stack][-1]:
      towers[to_stack].append(v)
    else:
      print 'error'
    print towers
  else:
    moveDisks(n-1,from_stack,3-from_stack-to_stack,towers)
    moveDisks(1,from_stack,to_stack,towers)
    moveDisks(n-1,3-from_stack-to_stack,to_stack,towers)
    
  
  


towers = [[5,4,3,2,1],[],[]]
moveDisks(5,0,2,towers)
