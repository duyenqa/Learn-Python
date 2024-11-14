def translateKorean(list, textTranslate):
    for item in list:
        if item.lower() == textTranslate.lower():
            return "Hello"
        elif item.lower() == textTranslate.lower():
            return "Good bye!"
        elif item.lower() == textTranslate.lower():
            return "Thank you"
        elif item.lower() == textTranslate.lower():
            return "Sorry"
        else:
            return "The word does not exist. I can not translate!!!"


def removeOneWordInDictionary(listWord, textTrash):
    listWord.remove(textTrash)
    return listWord


def main():
    select = 0
    wordsDictionary = []

    while select != 4:
        print("---Menu---")
        print("1.Add word")
        print("2.Delete word")
        print("3.View list")
        print("4.Translate word")
        select = int(input("Enter your choice: "))
        if select == 1:
            newWord = input("Enter a new word: ")
            wordsDictionary.append(newWord)
        elif select == 2:
            textTrash = input("Enter a word to remove from dictionary: ")
            newList = removeOneWordInDictionary(wordsDictionary, textTrash)
            print(newList)
        elif select == 3:
            print("---View list word---")
            print(wordsDictionary)
        elif select == 4:
            text = input("Enter a word to translate: ")
            translateWord = translateKorean(wordsDictionary, text)
            print("Translate Korean:")
            print(translateWord)
        else:
            print("The choice is invalid!")
            break

main()