

def Permute( number, spots=0, repeats=0, AddCommasBool = True):
    """
    Takes 'number', fractals it 'spot' number of times, and divides it by the permutation
    of 'repeats'. \n
    Spot and Repeats are optional. If 'spots' left blank, it defaults to 'number' value.
    If 'repeats' is left blank, it skips that step. If AddCommas is true, it will add 
    commas to the output to make it easier to read.
    """
    if not number:
        raise ValueError('number in Permute is not specified')
    if isinstance(number, str):
        number = int(number)
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
