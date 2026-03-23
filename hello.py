print("Hallo Welt!")
print()
print("Kleines Einmaleins (1 bis 10):")

for i in range(1, 11):
    row = []
    for j in range(1, 11):
        row.append(f"{i*j:>4}")
    print("".join(row))
