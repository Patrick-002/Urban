n = int(input())
result = ''
for i in range(1, 21):
    for j in range(i+1, 21):
        if n % (i + j) == 0:
            result += str(i) + str(j)
print(result)
print(int(result) == 13141911923282183731746416515614713812911)  # сравнение пароля для 20