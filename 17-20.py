import heapq,random
def process(arr):
    heap1 = []
    heap2 = []
    median = None

    for i,n in enumerate(arr):
        if median == None or n > median:
            heapq.heappush(heap2,n)
        else:
            heapq.heappush(heap1,-n)
        while len(heap1) > len(heap2):
            n1 = heapq.heappop(heap1)
            heapq.heappush(heap2,-n1)
        while len(heap2) > len(heap1) + 1:
            n2 = heapq.heappop(heap2)
            heapq.heappush(heap1,-n2)

        heap1Top = heap1[0] if len(heap1) > 0 else 0 
        heap2Top = heap2[0] if len(heap2) > 0 else 0
        if len(heap1) == len(heap2):    
            median = (-heap1Top + heap2Top)/2.0
        else:
            median = heap2Top

        #print heap1,heap2,median
    return median

#arr  = [random.randint(0, 20000) for i in range(2000)]
#process(arr)


arr = [5,6,8,2,1,10,39,3]
result = process(arr)
print result
