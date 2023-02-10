def ApplyLSystem(string, rule1, rule2, n):
    if (n <= 0):
        return string
    else:
        for i in range(n):
            string = string.replace(rule1, rule2)
        return string


def DrawLSystem(theturtle, thestring):
    for i in range(len(thestring)):
        if (thestring[i] == 'F'):
            theturtle.forward(10)
        elif (thestring[i] == '+'):
            theturtle.right(60)
        else:
            theturtle.left(60)
