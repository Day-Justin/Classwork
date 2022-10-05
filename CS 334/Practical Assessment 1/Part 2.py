import random

B = random.randint(2,3)
cut_points = []
for i in range(B):
    cut_points.append(random.random())
    cut_points.sort()

print(B)
print(cut_points)