def calculate(string):
    numbers = []
    operators = []
    index_list = []
    for index in range(len(string)):
        if string[index] in '+-*/':
            index_list.append(index)
    
    for i in range(len(index_list)):
        index = index_list[i]
        next_index = 0
        if i == 0:
            numbers.append(int(string[:index]))
        if i == len(index_list) -1 :
            next_index = len(string)
        else:
            next_index = index_list[i+1]
    
        next_number = int(string[index+1:next_index])# int

        op = string[index]
        operators, numbers = compare(op,next_number,operators,numbers)
        
    while operators != []:
        num2 = numbers.pop()
        num1 = numbers.pop()
        op = operators.pop()
        numbers = simple_cal(num1,num2,op,numbers)
    print numbers.pop()


def compare(op,next_number,operators,numbers):
    if operators == [] or (op in '*/' and operators[-1] in '+-'):
        operators.append(op)
        numbers.append(next_number)
    else:
        num2 = numbers.pop()
        num1 = numbers.pop()
        tmp_op = operators.pop()
        
        numbers = simple_cal(num1,num2,tmp_op,numbers)
        
        operators.append(op)
        numbers.append(next_number)
    return operators,numbers
            
def simple_cal(num1,num2,tmp_op,numbers):
    if tmp_op == '+':
        numbers.append(num1+num2)
    elif tmp_op == '-':
        numbers.append(num1-num2)
    elif tmp_op == '*':
        numbers.append(num1*num2)
    else:
        numbers.append(num1/num2)
    return numbers
            
calculate("1+1") 
calculate("0+4") 
calculate("0*7") 
calculate("9*0+1") 
calculate("1+1+1") 
calculate("1+6/5") 
calculate("3+7/8*7") 
calculate("1+11") 
calculate("200+423") 
