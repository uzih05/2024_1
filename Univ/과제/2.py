import random

simul = 1000
count = 0

for _ in range(simul):
    if random.randint(1, 6) == 5 :
        count += 1

probability = count / simul

print("주사위를 1000번 던졌을 때 5가 나올 확률:", probability)

