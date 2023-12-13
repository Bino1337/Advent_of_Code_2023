#textdatei auslesen
#    jede zeile einzeln nacheinander auslesen und
#    funktion anwenden
#
#funktion
#    von links nach rechts abgehen und erste zahl die
#    erkannt wird in variable first speichern
#    
#    von rechts nach links abgehen und erste zahl in
#    variable second speichern
#    
#    variablen zusammenfügen und in eine liste
#    
#    summe aller variablen   



file1 = open("example.txt", "r")



data = file1.read()

wordToDigit = {'one':'1', 'two':'2', 'three':'3',
               'four':'4', 'five':'5', 'six':'6',
               'seven':'7', 'eight':'8', 'nine':'9'}

for key in wordToDigit.keys():
    data = data.replace(key, wordToDigit[key])
    
# replaces written out digits with its numeric counterpart


codes = data.split("\n")
file1.close()
    
# reads file and makes a list with all codes

tempText = []
firstNum = 0
secondNum = 0
bothNum = []
listBothNum = []
sumNum = 0
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

for i in range(len(codes)):
    tempText = codes[i]
# iterates over the whole list line by line

    for j in range(len(tempText)):
        
        if tempText[j] in number:
            firstNum = tempText[j]
            break
# searches for first digit

    for k in range(len(tempText)):
        if tempText[len(tempText)-k-1: len(tempText)-k] in number:
            secondNum = tempText[len(tempText)-k-1]
            break
#searches for second digit
        
    bothNum.append(firstNum)
    bothNum.append(secondNum)
    bothNum = "".join(bothNum)
    
    
    sumNum += int(bothNum)
    
# joins both numbers and converts to int and makes sum of all numbers in the list

    firstNum = 0
    secondNum = 0
    bothNum = []
    
print(sumNum)

#solution: 54203

    
    



