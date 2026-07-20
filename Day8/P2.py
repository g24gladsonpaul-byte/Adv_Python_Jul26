# Context Manager
# Context Manager like a hotel room
# You check in (setup)
# You stay int he room (the code block)


#File Handing
#file = None
#try:
#    file = open('example.txt','r')
#    content = file.read()
#    print(content)
#finally:
#    if file:
#        file.close()


#Multiple context managers
with open('example.txt','r') as input_file, open('output.txt','w') as output_file:
    content = input_file.read()
    output_file.write(content.upper())
