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



file1 = open("input.txt", "r")

data = file1.read()

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
    
    for j in range(len(tempText)):
        
        if tempText[j] in number:
            firstNum = tempText[j]
            break
    for k in range(len(tempText)):
        if tempText[len(tempText)-k-1: len(tempText)-k] in number:
            secondNum = tempText[len(tempText)-k-1]
            break
    bothNum.append(firstNum)
    bothNum.append(secondNum)
    bothNum = "".join(bothNum)
    
    #listBothNum.append(bothNum)
    
    sumNum += int(bothNum)
    
    firstNum = 0
    secondNum = 0
    bothNum = []
    
print(sumNum)
    
    
      
            
    
    



