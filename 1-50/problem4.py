#Largest palindrome product

pal = []
for x in range(999, 899, -1):
    for y in range(999, 899, -1):
        prod = x*y
        if int(str(prod)[::-1]) == prod:
            pal.append(prod)

print(max(pal))
