a=int(input())
n=a%10
sum=0
for i in range(n):
      sum+=a%10
      n=a//10
print(sum)