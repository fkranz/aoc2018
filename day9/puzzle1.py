import sys 

players = int(sys.argv[1])
marbels = int(sys.argv[2])

scores = [0]*players
circle = [0,1]
curr = 1

for i in range(2,marbels+1):
    if i % 23 == 0:
        scores[(i-1)%players] += i
        curr = (curr - 7) % len(circle)
        removepos = curr
        scores[(i-1)%players] += circle.pop(removepos)
    else:
        insertpos = (curr + 1) % len(circle) + 1
        if insertpos == len(circle):
            circle.append(i)
        else:
            circle.insert(insertpos,i)
        curr = insertpos

print("Highscore is:", max(scores))