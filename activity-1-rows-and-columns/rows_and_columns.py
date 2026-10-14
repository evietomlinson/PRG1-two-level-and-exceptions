scores = [[78, 81, 84],
          [55, 54, 62],
          [89, 71, 90]]

print(scores[1][2]) #62
print(len(scores)) #3
print(len(scores[0])) #3
print(scores[1])

for row in scores: 
    print(row[0])

print("---")

for row in scores:
    print(row)

print(sum(scores[1]))

print("---")

for row in scores:
    for mark in row:
        print(mark)
