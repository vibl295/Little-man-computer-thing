import os

instructionSet = ['add', 'lda', 'sta', 'sub', 'hlt','inp','brp','del']
ACC = 0
pc = 0
memory = [0]
flag = True

def clear():
    if os.name == 'nt':
        os.system('cls')  
    else:
        os.environ['TERM'] = 'xterm'  # Set TERM to 'xterm' for other platforms like macOS and Linux
        os.system('clear')
    
def initialise():
    global memory
    f = open("array.txt", "r")
    a = f.read()
    print('read', a)
    if not a:
        print('empty')

        for i in range(99):
            memory.append(0)
    else:

        memory = a.split('a')
        for i in range(100):
            memory[i] = int(memory[i])
        
        print('previous memory was loaded from secondary storage')
    f.close()
def out():
    global ACC
    global memory
    global pc
    print('program counter', pc)
    print()
    print('accumulator:', ACC)
    print()
    print('memory:')
    for i in range(10):
        print(memory[10 * i:10 * (i + 1)])
def helpp():
    print('BASIC INSTRUCTIONS:')
    print(instructionSet)
    print()
    print()
    print('EXTRA:')
    print('wrt: enter mutiple instructions a time')
    print('del: wipe memory')
    print('')
    input()
def instruction(n, b):
    global ACC
    global memory
    global flag
    print('decoding instruction', n, 'with operand', b)
    if n == 'add':
        ACC = (int(memory[b]) + ACC)
    if n == 'lda':
        ACC = int(memory[b])
    if n == 'sta':
        memory[b] = ACC
    if n == 'sub':
        ACC = ACC - int(memory[b])
    if n == 'inp':
        inp = int(input('enter input'))
        ACC = inp
    if n == 'del':
        memory = [0]
        for i in range(99):
            memory.append(0)
        
    if n == 'hlt':
        flag = False
   
        
def decode(instructionStack):
    clear()
    command = instructionStack.pop()
    if command[:3] in instructionSet:
        if len(command) > 3:
            instruction(command[:3], int(command[4:]))
        else:
            instruction(command[:3],0)
def write():
    global stack

    line = input()
    if line:
        stack.insert(0,line)
        write()
    else:
        print(stack)
        print('running')
def main():
    global stack
    global instructionSet
    global ACC
    global flag
    global pc
    while flag == True:
        clear()
        out()
        pc += 1
        if stack:
            decode(stack)

        else:
            ins = input()
            if ins == 'help':
                helpp()
            if ins == 'wrt':
                print('write code, enter to run')
                write()
            stack.append(ins)
            print(stack)
            decode(stack)
    f = open('array.txt', 'w')
    print('writing')
    for i in range(100):
        print('writing',memory[i])
        f.write(str(memory[i])+'a')
    f.close()
    print('closing')
    clear()


stack = []
initialise()
main()












