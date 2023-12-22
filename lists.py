#!/usr/bin/env python3

# Created by: Noah Smith
# Created on: Dec 18th, 2023
# This program asks the user repeatedly to enter a mark between 0 and 100
# When the user enters -1, the loop stops
# then it finds and displays the average of those marks


def calc_average(list_marks):
    # Initialize sum
    sum = 0

    # Use for in loop to calculate sum
    for a_num in list_marks:
        sum += a_num

    # Calculate average
    average = sum / len(list_marks)

    # Return average
    return average


def main():
    # Create empty list
    list_of_marks = []

    # Get marks
    for counter in range(0, 100000):
        a_num = input("Enter a mark: ")
        try:
            a_num_int = int(a_num)
            if a_num_int < 0 or a_num_int > 100:
                if a_num_int == -1:
                    break
                else:
                    print("{} is not a valid mark.".format(a_num_int))
            else:
                list_of_marks.append(a_num_int)
        except:
            print("{} is not an integer".format(a_num))

    # Function call
    average = calc_average(list_of_marks)

    # Display the average
    print("")
    print("The average is {:.2f}.".format(average))


if __name__ == "__main__":
    main()
