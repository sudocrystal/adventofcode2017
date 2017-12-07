import fileinput

total = 0

for line in fileinput.input(files="input.txt"):
    words = [sorted(w) for w in line.split()]
    total += 1
    for word in words:
        if words.count(word) > 1:
            total -= 1
            break
    
print(total)
