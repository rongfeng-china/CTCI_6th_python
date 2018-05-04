    def __init__(self,capacity):
        self.capacity = capacity
        self.size = 0
        self.lru_index = ''
        self.dictionary = {}
        self.mru_v = -1
        self.ages = []

    def add(self,key,value):
        if key in self.dictionary:
            value = self.dictionary[key][1]
            self.dictionary[key] = [self.mru_v + 1,value]
        elif self.size < self.capacity:
            self.dictionary[key] = [self.mru_v + 1,value]
            self.size += 1
        else:
            self.update(key,value)
        self.mru_v += 1
        self.ages  = [(i,self.dictionary[i][0]) for i in self.dictionary]

    def update(self,key,value):
        dict2 = sorted(self.dictionary.iteritems(), key = lambda x:x[1][0])
        dict2.pop(0)
        self.dictionary =  dict(dict2)
        self.dictionary[key] = [self.mru_v + 1,value]
        
    def lookup(self,key):
        if key in self.dictionary:
            v = self.dictionary[key][1]
            self.add(key,v)
            return v
        else:
            return None
    
cache = LRUCache(4)
cache.add('food',  'lasagna')
cache.add('drink', 'orange juice')
cache.add('color', 'green')
cache.add('dance', 'bachata')
print cache.ages

cache.add('sport', 'ultimate')
print cache.ages

print cache.lookup('dance')
print cache.ages

print cache.lookup('food')
print cache.ages

cache.add('spice', 'paprika')
print cache.ages 

print cache.lookup('drink')
print cache.ages 

print cache.lookup('color')
print cache.ages 
