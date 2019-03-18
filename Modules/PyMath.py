import math
from itertools import permutations

def Average( x=[]):
    """
    Takes x list, and returns the average as an int.
    """
    y = 0
    A = 0
    for i in x:
        A += i
    y = A / len(x)
    del A
    return(y)

def Median( x=[]):
    """
    Takes x list, and returns the central number. \n
    Half of the numbers in the list are above the returned number, and half are below.
    """
    Num1 = None
    if len(x) == 3:
        answer = x[1]
        return(answer)
    
    Middle = len(x) // 2
    #
    if len(x) % 2 == 0:
        Num1 = x[Middle - 1]
    Num2 = x[Middle]

    if Num1 != None:
        answer = (Num1 + Num2) / 2
    else:
        answer = Num2
    return(answer)


def Count( x=[]):
    """
    Takes x list, and returns a two dimensional list, the first one contains the original number,
    and the second contains the number of times that number occurs , 
    ordered by how many times each number occurs least to greatest.
    """
    l = [[], []]
    d = {z:x.count(z) for z in x}
    k = d.keys()
    for i in k:
        l[0].append(i)
    v = d.values()
    for i in v:
        l[1].append(i)
    del d, k, v
    return(l)
   
def StandardDeviation( x=[]):
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
       
def Permute( number, spots=0, repeats=0, AddCommasBool = False):
    """
    Takes 'number', fractals it 'spot' number of times, and divides it by the permutation
    of 'repeats'. \n
    Spot and Repeats are optional. If 'spots' left blank, it defaults to 'number' value.
    If 'repeats' is left blank, it skips that step. If AddCommas is true, it will add 
    commas to the output to make it easier to read.
    """
    if spots == 0:
        spots = number
    loopNum=0
    repeatsPerm = 1
    PAnswer=1
    while loopNum < spots:
        PAnswer = PAnswer * (number - loopNum)
        loopNum += 1
    if repeats != 0:
        loopNum = 0
        while loopNum < repeats:
            repeatsPerm = repeatsPerm * (repeats - loopNum)
            loopNum += 1
        answer = PAnswer/repeatsPerm
        return(answer)
    else:
        answer = PAnswer
    if AddCommasBool == True:
        answer = AddCommas(answer)
    return(answer)

def Combination( things, allowedthings, AddCommasBool = True):
    """
    Takes int 'things', and int 'allowedthings', and finds how many combinations ('things'
    divided by allowed things) are possible, and returns the answer as an int. If AddCommas is true, it will add 
    commas to the output to make it easier to read.
    """
    a = Permute(things, allowedthings)
    b = Permute(allowedthings)
    answer = a/b
    del a, b
    if AddCommasBool == True:
        answer = AddCommas(int(answer))
    return(answer)

def PermuteString(x = '', AddCommasBool = True):
    """
    Takes 'x' string, and finds how many possible ways it can be arranged, 
    taking into account double letters. If AddCommas is true, it will add 
    commas to the output to make it easier to read.
    """
    x = x.replace(" ", "")
    x = x.lower()

    answer = []
    tempArray = []
    for i in x:
        tempArray.append(i)
        
    dictVar = {z:tempArray.count(z) for z in tempArray}
    vals = dictVar.values()
    tempArray = []
    tempArray2 = []
    a = 0
    for i in vals:
        t = int(i)
        if i != 1:
            tempArray.append(Permute(t)) 
    for i in tempArray:
        tempArray2.append(Permute(t))
    for i in tempArray2:
        a += t
    try:
        answer = (Permute(len(x)))/a
    except ZeroDivisionError:
        answer = Permute(len(x))
    del tempArray, tempArray2, a

    answer = int(answer)

    if AddCommasBool == True:
        answer = AddCommas(answer)
    return(answer)

def AddCommas(Input):
    output = []
    temp = []
    Loop = 0

    Input = str(Input)

    for i in Input:
        temp.append(i)
    temp.reverse()

    for i in temp:
        if Loop % 3 == 0 and Loop != 0:
            output.append(",")
            output.append(i)
        else:
            output.append(i)
        Loop += 1
    output.reverse()
    output = "".join(output)
    return(output)
