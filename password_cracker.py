import hashlib as hl

def main():

    #read file of passwords to crack and store in an array
    passwordFile = input("Enter path to passwords to hash file (absolute if not in same directory): ")
    passwordFileOpen = open(passwordFile, 'r')
    passwordsToCrack = []

    #this for loop assumes that the format of the input is username:hashed_password:other_stuff
    for word in passwordFileOpen:
        passwordsToCrack.append(word.split(":")[1])

    #read /usr/share/dict/words -- done
    #this is the absolute path for a macbook pro running mojave (need to change if found elsewhere)
    allEnglishWords = open("/usr/share/dict/words", 'r')
    allEnglishWordsArray = []

    for word in allEnglishWords:
        strippedWord = word.strip('\n')
        allEnglishWordsArray.append(strippedWord)

    for word in passwordsToCrack:
        if anyWordInWordlist(allEnglishWordsArray, word):
            print("Found")
        elif fourDigitWord(word):
            print("Found")
        elif anyDigit(word):
            print("Found")
        else:
            print("Password not cracked: ", word)

    #sevenCharWord("goodbye", "185f05649820601edfe7dd63faab71c87fd9e87705ca99a064bc8bc3d4086f3e")
    #fourDigitWord("ec20ce5a859f49142d0bed196700d3d0b5abde609e1d8dbf56807f25fcf28275")
    #anyDigit("7618f66753db7ec069c83ed8c197708e1402396774f60961065addd678933871")
    #anyWordInWordlist(allEnglishWordsArray, "ecb0c1f0173573feb4008eb19c81ee07c5d2289047de87e63c43bda9aae3fa3c")
    #fiveCharWord("altos", "2110aef73f190ea123486807f41e6896c40412052c7fa23c84a758c89bc504c8")

    allEnglishWords.close()
    passwordFileOpen.close()

## takes a 5 char word and a hashed password and checks if the word has 'a' or 'l' changing them to '@' and '1'
## repspectively
def fiveCharWord(fiveChar, hashedPW):

    if 'a' in fiveChar or 'l' in fiveChar:
        aTranslated = fiveChar.replace('a', '@')
        aTranslatedHashed = hl.sha256(aTranslated.encode())
        if aTranslatedHashed.hexdigest() == hashedPW:
            print(aTranslated)
            return True
        lTranslated = fiveChar.replace('l', '1')
        lTranslatedHashed = hl.sha256(lTranslated.encode())
        if lTranslatedHashed.hexdigest() == hashedPW:
            print(lTranslated)
            return True
        alTranslated = fiveChar.replace('a', '@').replace('l', '1')
        alTranslatedHashed = hl.sha256(alTranslated.encode())
        if alTranslatedHashed.hexdigest() == hashedPW:
            print(alTranslated)
            return True
    return False

## takes a 7 letter word, capitalizes the first letter and adds a number 0-9 to the end and compares to the
## given hash password. prints password if found and returns true, otherwise returns false
def sevenCharWord(sevenChar, hashedPW):

    for i in range(10):
        sevenCharPlusNumber = sevenChar.capitalize() + str(i)
        sevenCharPlusNumberHashed = hl.sha256(sevenCharPlusNumber.encode())
        if sevenCharPlusNumberHashed.hexdigest() == hashedPW:
            print(sevenCharPlusNumber)
            return True
    return False

## takes a wordlist and a hashed password and hashes all words in the wordlist. also calls the
## sevenCharWord and fiveCharWord function to possibly save time by consolidating searches
## prints the word if found and returns true, otherwise returns false
def anyWordInWordlist(wordList, hashedPW):

    for word in wordList:
        if len(word) == 7:
            if sevenCharWord(word, hashedPW):
                return True
        if len(word) == 5:
            if fiveCharWord(word, hashedPW):
                return True
        wordHashed = hl.sha256(word.encode())
        if wordHashed.hexdigest() == hashedPW:
            print(word)
            return True
    return False

## takes a hashed password and checks all numbers from 0 - 999999. prints password if found and returns true,
## otherwise returns false
def anyDigit(hashedPW):

    for i in range(999999, -1, -1):
        numberToHash = str(i)
        hashedNumber = hl.sha256(numberToHash.encode())
        if hashedNumber.hexdigest() == hashedPW:
            print(numberToHash)
            return True;
    return False



## takes a hashed password and checks all numbers from 1000-9999 with chars '*, !, ~, #' in any permutation
## at the beginning. prints password if found and returns true, otherwise return false
def fourDigitWord(hashedPW):

    possibleCombinationOfSymbols = ['*', '~', '!', '#',
                                     "*~", "*!", "*#", 
                                     "~*", "~!", "~#",
                                     "!*", "!~", "!#",
                                     "#*", "#~", "#!",
                                     "*~!", "*~#", "*!~",
                                     "*!#", "*#~", "*#!",
                                     "~*!", "~*#", "~!*",
                                     "~!#", "~#*", "~#!",
                                     "!*~", "!*#", "!~*",
                                     "!~#", "!#*", "!#~",
                                     "#*~", "#*!", "#~*",
                                     "#~!", "#!*", "#!~",
                                     "*~!#", "*~#!", "*!~#",
                                     "*!#~", "*#~!", "*#!~",
                                     "~*!#", "~*#!", "~!*#",
                                     "~!#*", "~#*!", "~#!*",
                                     "!*~#", "!*#~", "!~*#",
                                     "!~#*", "!#*~", "!#~*",
                                     "#*~!", "#*!~", "#~*!",
                                     "#~!*", "#!*~", "#!~*"]

    for i in range(9999, 999, -1):
        for symbol in possibleCombinationOfSymbols:
            numberPlusSymbol = symbol + str(i)
            numberPlusSymbolHashed = hl.sha256(numberPlusSymbol.encode())
            if numberPlusSymbolHashed.hexdigest() == hashedPW:
                print(numberPlusSymbol)
                return True
    return False

    
main()
