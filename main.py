str = "OnlineTutorials2021"

letter = digits = 0

for ch in str:
    if ch.isdigit():
        digits = digits+1

    elif ch.isalpha():
        letter = letter+1

    else:
        pass

print("Count of Digits is: ",digits)
print("Count of Letters is: ",letter)