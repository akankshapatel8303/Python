nterms = int(input("Enter the number of terms: "))

result = list(map(lambda x : 2**x, range(1,nterms+1)))

print(result)

for i in range(nterms):
    print(f"The value of 2 raised to power {i} result {result[i]}")