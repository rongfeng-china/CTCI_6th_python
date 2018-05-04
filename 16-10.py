class P:
    def __init__ (self,by,dy=None):
        self.birth_year = by
        self.death_year = dy

def most_living_people(people):
    dict = {}
    for person in people:
        if person.birth_year in dict:
            dict[person.birth_year] += 1
        else:
            dict[person.birth_year] =  1
        if person.death_year != None:
            if person.death_year in dict:
                dict[person.death_year+1] -= 1
            else:
                dict[person.death_year+1] = -1
    dict = sorted(dict.items(), key = lambda x: x[0])
    #print dict
    result = 0
    tmp_year, tmp_result =0, 0
    for item in dict:
        tmp_result += item[1]
        if tmp_result > result:
            result = tmp_result
            tmp_year = item[0]
    return tmp_year
        
    

people=[P(1907,1942),P(1909,1982),P(1933,1967),P(1912,1954),P(1980),P(1988)]
result = most_living_people(people)
print result
