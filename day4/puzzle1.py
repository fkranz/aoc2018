import sys
sleepingTimes = {}


file = open(sys.argv[1])
hour = []
guardID = -1
sleep = -1
wake = -1
for line in sorted(file):
    if "begins shift" in line:
        sleepingTimes[guardID] = hour
        guardID = int(line.split(' ')[3].replace("#",""))
        if guardID not in sleepingTimes:
            hour = [0]*60
        else:
            hour = sleepingTimes[guardID]
    elif "falls asleep" in line:
        sleep = int(line.split(' ')[1].split(":")[1].replace("]",""))
    elif "wakes up" in line :
        wake = int(line.split(' ')[1].split(":")[1].replace("]",""))
        for i in range(sleep,wake):
            hour[i] += 1

maxSleep = 0
mostSleepy = -1

for key,value in sleepingTimes.items():
    sleep = sum(value)
    if sleep > maxSleep:
        maxSleep = sleep
        mostSleepy = key

maxi = -1
minute = -1
for k,i in enumerate(sleepingTimes[mostSleepy]):
    if i > maxi:
        maxi = i
        minute = k

print(minute,mostSleepy)
print("Result:", minute*mostSleepy)
file.close()