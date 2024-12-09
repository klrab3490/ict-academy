
percentage = int(input("Enter the percentage : "))
if (percentage>=35):
    print("Passed")
    if percentage >= 90:
        print("Medical College")
    elif percentage >= 70:
        print("Engineering")
    else:
        print("Arts")
else:
    print("Failed")
