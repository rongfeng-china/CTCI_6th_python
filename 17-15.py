class Trie:
    def __init__(self,wordList):
        self.root = {}
        self.end = '\n'
        for word in wordList:
            self.add(word)

    def add(self,word):
        node = self.root 
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node[self.end]=self.end
    
    def containWord(self,word):
        node = self.root
        for letter in word:
            if letter not in node:
                return False
            else:
                node = node[letter]
        if self.end in node:
            return True
        return False

def getLongest(words):
    result = ''
    trie = Trie(words)
    for word in words:
        if madeOfOthers(word,trie):
            if len(word) > len(result):
                result = word
    return result

def madeOfOthers(word,trie):
    n = len(word)
    node = trie.root
    for i in range(n):
        letter = word[i]
        if letter not in node:
            return False
        node = node[letter]
        if trie.end in node:
            if madeOfOthers(word[i+1:],trie) or trie.containWord(word[i+1:]):
                return True
    return False


              
words = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker', 'giantwordthatisntomadeofothers']
print getLongest(words)

