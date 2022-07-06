n = 6
names = ["Tom", "Jones", "Jerry", "Jane", "Lisa", "Susan"]
scores = [10, 11, 12, 13, 11, 10]

together = []

for i in range(0, n):
    together.append([names[i], scores[i]])

print(together)

together.sort(key=lambda scores: scores[1])

print(together)

minScore = together[0][1]
print(minScore)


def findSecondLowest(list):
    for i in range(0, n):
        if list[i][1] != minScore:
            return list[i][1]


secondLowest = findSecondLowest(together)
print(secondLowest)

for i in range(0, n):
    if together[i][1] == secondLowest:
        print(together[i][0])
