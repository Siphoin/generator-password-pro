import sys
import random
import pyperclip

def containsStringOnArray(array, string):
    return [s for s in array if string in s]

def generateRandomSymbol ():
    return chr(random.randint(145, lengthIndexSymbols))


args = sys.argv

helpArgument = '-h'

generateNumbersArgument = '-n'

clipboardArgument = '-c'

indexArgumentLength = 1

lengthIndexSymbols = 255

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

useNumbers = containsStringOnArray(args, generateNumbersArgument)

matchingHelp = containsStringOnArray(args, helpArgument)

clipboard = containsStringOnArray(args, clipboardArgument)

print("\nGenerator Password Pro 1.0\n===========================\nAuthor: Siphon github.com/Siphoin\nLicense: GPL")


if len(matchingHelp) > 0:
    print('-n - generate password with numbers\n-c - copy new generated password to clipboard\n1 argument - count of numbers for new password\n\nExample:\n\n15 -n')
    quit()


else:
    print("\nfor more information write " + helpArgument + "\n")

def generate(count, useNumbers, copyToClipBoard):
    outStr = ''

    for i in range(count):

        symbol = ''

        if len(useNumbers) == 0:
            symbol = generateRandomSymbol()


        if len(useNumbers) > 0:

            n = random.randint(0, 7)
            if n > 3:
                indexNumber = random.randint(0, len(numbers))

                symbol = indexNumber
            else:
                symbol = generateRandomSymbol()
        
        outStr = outStr + str(symbol)

            
    print('Output: ' + outStr)
    if len(clipboard) > 0:
        pyperclip.copy(outStr)
        print('password copped to clipboard!')

def intTryParse(value):
    try:
        return int(value)
    except ValueError:
        return False



length = args[indexArgumentLength]
lengthNumber = int(length)

if intTryParse(length) != lengthNumber:
    print('Error: 1 argument must a contains length password')
    quit()

else:
    generate(lengthNumber, useNumbers, clipboard)
    quit()