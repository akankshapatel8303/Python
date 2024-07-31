#Solution 1

#print("The numbers divisible by 13 are: ")
# for i in range(1, 100):
#     if i % 13 ==0:
#         print(i)

#Solution 2

l = [23, 36, 889, 54, 89, 34, 378]
result = list(filter(lambda x: x%18==0, l))
print(result)