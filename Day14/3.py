lines = []
print("Enter lines of text (type 'STOP' to finish):")
while True:
    line = input()
    if line.upper() == "STOP":  # Stop condition
        break
    lines.append(line.upper())


print("\nCapitalized Lines:")
for line in lines:
    print(line)