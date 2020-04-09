import math

def stat_calc(input_list):
    return 'I am incomplete!!! :`('

def average( x=[]):
    """
    Takes x list, and returns the average as an int.
    """
    y = 0
    A = 0
    for i in x:
        if i is None:
            continue
        A += i
    y = A / len(x)
    del A
    return(y)

def median( x=[]):
    """
    Takes x list, and returns the central number. \n
    If there are an even number of items, it returns the average of the middle two.\n
    Half of the numbers in the list are above the returned number, and half are below.
    """
    Num1 = None
    if len(x) == 3:
        answer = x[1]
        return(answer)
    Middle = len(x) // 2
    if len(x) % 2 == 0:
        Num1 = x[Middle - 1]
        Num2 = x[Middle]
        answer = (Num1 + Num2) / 2
    elif len(x) % 2 != 0:
        answer = x[Middle]
    return(answer)


def count(x=[]):
    """
    Takes x list, and returns a two dimensional list, the first one contains the original number,
    and the second contains the number of times that number occurs , 
    ordered by how many times each number occurs least to greatest.
    """
    loop_num = 0
    list_keys = []
    list_values = []
    output = []
    y = []
    for i in x:
        y.append(i)
    y.sort()
    d = {z:y.count(z) for z in y}
    k = d.keys()
    v = d.values()
    for i in k:
        list_keys.append(i)
    for i in v:
        list_values.append(i)
    while loop_num < len(list_keys): 
            output.append(str(list_keys[loop_num])+ ':' + str(list_values[loop_num]))
            loop_num += 1
    del d, k, v, list_keys, list_values, loop_num
    return(output)
   
def count_two(x=[]):
    """
    Takes x list, and returns two lists, the first one contains the original number,
    and the second contains the number of times that number occurs, 
    ordered by how many times each number occurs least to greatest.
    """
    y = []
    for i in x:
        y.append(i)
    y.sort()
    diction = {z:y.count(z) for z in y}
    return(diction)

def standard_deviation( x=[]):
    """
    Takes x list, and returns an int the equals the average amount that the numbers deviate from the Average. 
    """
    z = []
    tempnum = 0
    for i in x:
        tempnum += i
    deviationAverage = tempnum/len(x)
    tempnum = 0
    for i in x:
        z.append(pow((i - deviationAverage), 2))
    for i in z:
        tempnum += i
    answer = tempnum / len(z)
    answer = math.sqrt(answer)
    del z, tempnum
    return(answer)

if __name__ == '__main__':
    x = [5, 5, 10, 10, 15, 56, 22, 27]
    print(count(x))