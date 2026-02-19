# import numpy as np

# x= np.random.randint(100)

# geuss= int(input("enter a number:"))

# while geuss!=x:
#     if geuss>x:
#         print("number is higher, enter again.")
#     else:
#         print("number is lower, enter again.")
    
#     geuss = int(input("Enter a number: "))

# print("you are right")

        

import numpy as np

x = np.random.randint(100)

while True:
    geuss_input = input("Enter a number between 0 and 99: ")

    if geuss_input.isdigit():          # checks that input is numeric
        geuss = int(geuss_input)
        break
    else:
        print("❌ Please enter a valid number.")
while geuss != x:
    if geuss > x:
        print("Your guess is higher, try again.")
    else:
        print("Your guess is lower, try again.")

    while True:
        geuss_input = input("Enter a number: ")
        if geuss_input.isdigit():
            geuss = int(geuss_input)
            break
        else:
            print("❌ Please enter a valid number.")

print("🎉 You are right!")