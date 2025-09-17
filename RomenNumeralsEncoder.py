inp = int(input("Değer giriniz: "))


def romentoint(num:int) -> str:
    if not isinstance(num,int):
        raise TypeError("You must enter an integer.")
    if (num<1 and num>3999):
        raise ValueError("Number must be between 1 and and 3999.(both included)")

    vals = [(1000,'M'),(900,'CM'),
            (500,'D'),(400,'CD'),
            (100,'C'),(90,'XC'),
            (50,'L'),(40,'XL'),
            (10,'X'),(9,'IX'),
            (5,'V'),(4,'IV'),
            (1,'I')]
    res = []

    for value,symbol in vals:
        if (num == 0):
            break
        
        count = num // value
        if count: # means if not equals to zero.
            res.append(symbol*count)
            num -= value*count
    return "".join(res)

print(romentoint(inp))