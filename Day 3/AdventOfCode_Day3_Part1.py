# add up all part numbers
# any number adjacent to a symbol also diagonally is a part number
# every line is 140 characters long


with open('input.txt', 'r') as f:
    inputText = f.read()
    
inputText = inputText.split('\n')

special = ['`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|','\',':',';',""",''','<',',','>','?','/']

