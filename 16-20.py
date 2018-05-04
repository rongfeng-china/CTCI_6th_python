def t9_words(digits,trie,letters):
    for digit in digits:
        result = []
        for item in letters[int(digit)]:
            result.append(

trie = {'a':{'b':{'a':{'c':{'u':'s'}}}},'t':{'r':{'e':'e'}},'u':{'s':{'e':'d'}}}
digits =  "222287"
letters = {2:['a','b','c'],3:['d','e','f'],4:['g','h','i'],5:['j','k','l'],6:['m','n','o'],7:['p','q','r','s'],8:['t','u','v'],9:['w','x','y','z']}
result =t9_words(digits,trie,letters,'',[])

digits = "8733"
