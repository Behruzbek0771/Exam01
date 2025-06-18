matn = input("Matn kiriting: ")
unli_harflar = "aeiou"
count = 0
for harf in matn.lower():
    if harf in unli_harflar:
            count += 1
print(f"Unli harflar soni: {count}")