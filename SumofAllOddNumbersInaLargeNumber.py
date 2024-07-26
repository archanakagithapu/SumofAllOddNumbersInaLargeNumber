'''num = int(input())
sum = 0

while num != 0:
    digit = num % 10
    if digit % 2 != 0:
        sum += digit
    num //= 10

print(sum)'''


num = input()
oddList=['1','3','5','7','9']
sum = 0

for i in num:
    if i in oddList:
        sum += int(i)
print(sum)
