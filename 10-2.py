def group_anagrams(letters):
    pairs = [[s,sorted(s)] for s in letters]
    pairs.sort(key=lambda x:x[1])
    print [x[0] for x in pairs]

letters =  ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
group_anagrams(letters)
