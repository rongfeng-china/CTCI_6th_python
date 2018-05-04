class Trie:
    def __init__(self,words):
        self.root = {}
        self.end = '*'
        for word in words:
            self.add(word)
        
    def add(self,word):
        node = self.root
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end] = self.end

    def contrainWord(self,word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            node = node[letter]
        if self.end in node:
            return True
        return False

def multiSearch(T,b):
    trie = Trie(T)
    result = []
    #print trie.contrainWord('ppi')
    for i in range(len(b)):
        for j in range(i+1,len(b)+1):
            word = b[i:j]    
            if trie.contrainWord(word):
                if word not in result:
                    result.append(word)
                else:
                    break

    return result
 
T = ['is', 'ppi', 'hi', 'sis', 'i', 'ssippi']
b = 'mississippi'
result = multiSearch(T, b)
print result
