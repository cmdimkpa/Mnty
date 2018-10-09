from __future__ import division
import os
global register, program_file, Dir, comment, keywords, arithmetic

Dir = os.getcwd()+"/"
comment = "!"

register = {}
program_file = Dir+"program.mnty"
keywords = ["let","do","print","int","=","float"]
arithmetic = ["+","-","/","*","^","%"]

def uncomment(line):
    pos = None
    try:
        pos = line.index("!")
    except:
        pass
    return line[:pos]

def execute(segment):
    global register
    try:
        components = segment.split(' ')
        vars = [component for component in components if component not in keywords]
        if "let" in segment:
            key = vars[0]
            value = vars[1]
            if "int" in segment:
                register[key] = int(value)
            elif "float" in segment:
                register[key] = float(value)
            else:
                register[key] = str(value)
        elif "do" in segment:
            operation = vars[0]
            result_var = vars[1]
            op = [op for op in arithmetic if op in operation][0]
            operands = operation.split(op)
            if op == "+":
                register[result_var] = register[operands[0]]+register[operands[1]]
            elif op == "-":
                register[result_var] = register[operands[0]]-register[operands[1]]
            elif op == "/":
                register[result_var] = register[operands[0]]/register[operands[1]]
            elif op == "*":
                register[result_var] = register[operands[0]]*register[operands[1]]
            elif op == "^":
                register[result_var] = register[operands[0]]**register[operands[1]]
            elif op == "%":
                register[result_var] = register[operands[0]]%register[operands[1]]
            else:
                pass
        elif "print" in segment:
            var = vars[0]
            print register[var]
    except Exception as e:
        print "CompilerError: %s" % str(e)

p = open(program_file,"rb+")
lines = p.readlines()
p.close()

for line in lines:
    if line:
        code = uncomment(line)
        segments = [segment for segment in code.split(';') if len(segment) > 2]
        if segments:
            map(execute,segments)
