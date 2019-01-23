# Problem 1:
# # #
# # # Create a function with the variable below. After you create the variable do the instructions below that.
# # #
# # # arrayForProblem2 = ["Kenn", "Kevin", "Erin", "Meka"]
# # # a) Print the 3rd element of the numberList.
# # #
# # #     b) Print the size of the array
# # #
# # # c) Delete the second element.
# # #
# #     d) Print the 3rd ele
from typing import List


def main():
    problem4()


# ///////////////////////////////////////////////////////////////////////////////

# def problem1():
#
#     nam = ["Kenn", "Kevin","Erin", "Meka"]
#
#     print(nam[2])
#     print(len(nam))
#     nam.remove("Erin")
#     print(nam[2])


# ///////////////////////////////////////////////////////////////////////////////

# Problem 2:
#
# We will keep having this problem until EVERYONE gets it right without help
#
# Create a function that has a loop that quits with ‘q’. If the user doesn't enter 'q', ask them to input another string.
#
# def problem2():
#     uI = ""
#     userInputPrint = ""
#
#     while(uI != 'q'):
#         userInputPrint += uI + "\n"
#         uI = input("Input string here")
#         print(userInputPrint)
# //////////////////////////////////////////////////////////////////////////////////

# Create a function that contains a collection of information for the following. After you create the collection do the instructions below that.
#
# Jonathan/John
# Michael/Mike
# William/Bill
# Robert/Rob
# def problem3():
#
#     phonebook = {
#             "Jonathan":'John',
#             "Michael":'Mike',
#             "William":'Bill',
#             "Robert":'Rob'
#     }
#     print(phonebook)
#     print(phonebook['William'])


# ///////////////////////////////////////////////////////////////////////////

# Problem 4:
#
# Create an array of 5 numbers. Using a loop, print the elements in the array reverse order. Do not use a function

# def problem4():
#     nam = [1,2,3,4,5]
#     for eachEl in range(len(nam)-1,-1,-1):
#         print(nam[eachEl])

# //////////////////////////////////////////////////////////////////////////////
# Problem 5:
#
# Create a function that will have a hard coded array then ask the user for a number.
# Use the userInput to state how many numbers in an array are higher, lower, or equal to it.
def problem5():
    list = [1,2,3,4,5]
    input("Please pick a number from 1 thru 4")
if __name__ == '__main__':
    main()