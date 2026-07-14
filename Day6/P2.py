# File Handling: reading & writing to files on computer

#Writing to a file
#with open('example.text','w') as file:
#    file.write('Hello world!')

#Readin from a file
with open('example.text','r') as file:
    content = file.read()
    print(content)

#re
with open('example.text','r') as file:
    for line in file:
        print(line.strip())