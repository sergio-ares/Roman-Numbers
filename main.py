#The function to pass from integer to roman
def intToRoman(num: int):
    symList = [["M",1000],["CM",900],["D",500],["CD",400],["C",100],
    ["XC",90],["L",50],["XL",40],["X",10],["IX",9],["V",5],["IV",4],["I",1]]
    
    res = ""

    for sym, val in symList:
        if num // val:
            count = num // val
            res += (sym * count)
            num = num % val

    return res

#The function to pass from roman to an integer
def romanToInt(s: str):
    numbers = {
        "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
    }
    
    res = 0
    
    for i in range(len(s)):
        if i+1 < len(s) and numbers[s[i]] < numbers[s[i+1]]:
            res -= numbers[s[i]]
        else:
            res += numbers[s[i]]
    
    return res

print("Hello user, this scripts turns roman numbers to integers and integers into roman")
while True:
    action = int(input(f"Input 1 to turn roman into integer | input 2 to turn integer into roman | input 3 to exit the program: "))
    if action == 1:
        roman = input("Input the roman number in CAPS: ")
        print(romanToInt(roman))
    elif action == 2:
        integer = int(input("Input the integer: "))
        print(intToRoman(integer))
    elif action == 3:
        break
    else:
        print("An error occurred with the input provided")