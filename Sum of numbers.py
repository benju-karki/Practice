###number = int(input("Let's do the sum of numbers. Tell me any number and i will give you summ of all numbers till n: "))
# total_sum= number* ((number+1)//2)
# print (total_sum) ###

### we can do this same problem by using loop
sum =0  
number = int(input("Enter the number.  "))
for i in range(1, number+1):
    sum= sum +i

print(sum)
