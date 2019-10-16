def simple_assembler(program):
    registers = dict()
    x = 0
    while x < len(program):
        com = program[x].split()
        if com[0] == "mov":
            if com[2].isalpha():
                registers[com[1]] = registers[com[2]]
            else: registers[com[1]] = int(com[2])
        elif com[0] == "inc":
            registers[com[1]] += 1
        elif com[0] == "dec":
            registers[com[1]] -= 1
        elif com[0] == "jnz":
            if (com[1].isdigit() and int(com[1])) or (com[1].isalpha() and registers[com[1]]):
                x += int(com[2]) - 1
        x += 1
    return registers