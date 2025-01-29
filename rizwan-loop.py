# num=int(input("input the number to print the table: "))
# for k in range(1,5, 4):
#     print (num,"x",k,"=",num*K)

# sum=0
# num=int(input("input the last number of sries: "))
# for k in range (1,num+1):
#     sum=sum+k
#     print("the total is:",sum)
#     print("finished task") 

#program to calculate difference between sum of squares and the number.
number=int (input("enter the number: ")) # 4
sum = 0
for i in range (1,number+1):
    sum = sum + (i *i) # 1*1 + 2*2 + 3*3 + 4*4 - 4 = 26
# 1 + 4+ 9+ 16 = 30 - 4 = 26
ans = sum - number
print("the answer is",ans)