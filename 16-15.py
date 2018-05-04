def mastermind_hits(code, guess):
    n = len(code)
    r1 = 0
    code2, guess2 = [],[]
    hit_list, phit_list = [],[]
    for i in range(n):
        if code[i] == guess[i]:
            r1 += 1
            if code[i] not in hit_list:
                hit_list.append(code[i])
        else:
            code2.append(code[i])        
            guess2.append(guess[i])
    for item in code2:
        if item not in hit_list and item not in phit_list and item in guess2:
            phit_list.append(item)
    print '%d %d\n' %(r1,len(phit_list))
    return r1, len(phit_list)

mastermind_hits("YYBB", "BBYY")
mastermind_hits("BYBB", "BBYY")
mastermind_hits("RGBY", "RGBY")
mastermind_hits("RGBY", "RBGY")
mastermind_hits("RGBY", "RRRR")
mastermind_hits("RRRR", "RBGY")
mastermind_hits("RRYY", "RYGY")
