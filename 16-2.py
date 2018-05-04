class TextBook:
    def __init__(self,f_name):
        f = open(f_name,'r')
        lines = f.readlines()
        self.total_words = 0
        self.dict = {}
        for line in lines:
            words = line.strip('\n').split(" ")
            self.total_words += len(words)
            for word in words:
                #print (word)
                if word in self.dict:
                    self.dict[word] += 1
                else:
                    self.dict[word] = 1

    def word_frequency( self, word):
        if word in self.dict:
            return 1.0*self.dict[word]/self.total_words
        else:
            return 0


f_name = "16-2.txt"
    
TB1 = TextBook(f_name)
print TB1.total_words
print TB1.word_frequency("umbrella")
