# for i in range(1,10):
#     for j in range(1,i+1) :
#         print(f"{j} * {i} = {j*i}",end="  ")
#     print("\n")


# a,b = map(int,input().split(" "))
# for i in range(a,b+1) :
#     count = 0
#     for j in range(2,i) :
#         if (i % j == 0):
#             count = 1
#             break
#     if count == 0:
#         print(i)

# n = int(input())
# sum = 0
# mu = 1
# zi = 2
# for i in range(1,n+1):
#     sum += zi /mu;
#     tem = zi;
#     zi = zi +mu
#     mu = tem
# print(sum)

# # include <stdio.h>
# int main ()  {
# 	int num ;
# 	scanf ("%d",&num);
# 	int cnt = 0;
# 	int cnt2 = num;
# 	int nums[num];
# 	int sum =0;
# 	while(cnt2 > 0 ) {
# 		printf("input a num");
# 		scanf("%d",nums[cnt]);
# 		cnt ++;
# 		sum += nums[cnt];
# 		cnt2 --;
# 	}
# 	printf("%d\n",sum);
# }

num = int(input())
cnt = 0;
cnt2 = num
nums = []
sum = 0
while cnt2 > 0:
    print("input a num")
    nums.append(int(input()))
    cnt += 1
    sum += nums[cnt]
    cnt2 -= 1
print(sum)
