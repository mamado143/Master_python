''' 
cleanWord - This function
parma word - string
return - string
'''
def cleanWord(word):
    if len(word) == 1:
        return word
    print(f"print start function {word}")

    if word[0] == word[1]:
            print(f"Print before condiotn {word}")
            return cleanWord(word[1:])
    print(f"Print after condiotn {word}")
        
    return word[0] + cleanWord(word[1:])

print(cleanWord("wwwooorrrrlllllddd"))