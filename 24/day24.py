# not working in time
import sys

infile = sys.argv[1] if len(sys.argv) > 1 else '24.in'
data = list(map(lambda x:x.split(' '), open(infile).read().strip().split('\n')))
print(data)

def compiler(program, inputs):
    inputs = inputs.copy()
    variables = {x: 0 for x in "wxyz"}
    for instruction in program:
        if instruction[0] == "inp":
            variables[instruction[1]] = inputs.pop(0)
            continue
        operator, a, b = instruction
        b = variables[b] if b in variables else int(b)
        if operator == "add":
            variables[a] += b
        if operator == "mul":
            variables[a] *= b
        if operator == "div":
            variables[a] = variables[a] // b
        if operator == "mod":
            variables[a] = variables[a] % b
        if operator == "eql":
            variables[a] = int(variables[a] == b)

    return variables["z"] == 0


def count_down():
    for x in range(99_999_999_999_999, 0, -1):
        if "0" not in str(x):
            yield x

for num in count_down():
    print(f'Checking {num}')
    inputs = [int(x) for x in str(num)]
    if compiler(data, inputs):
        break

print("Part 1:", num)
