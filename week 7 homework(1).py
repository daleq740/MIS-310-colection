def get_average():

    # this gets the three scores for the average then calculates it
    score1 = float(input("Enter the score for test 1: "))


    score2 = float(input("Enter the score for test 2: "))


    score3 = float(input("Enter the score for test 3: "))


    average = (score1 + score2 + score3) / 3

    #
    return average


def check_average(average):

    # this shows the average and a message coresponding with the score
    print(f"\nThe average score is: {average:.2f}")


    if average >= 90:
        print("Congratulations you are the best")
    elif average >= 80:
        print("Great job you did good")
    elif average >= 70:
        print("you are average you could do better")
    elif average >= 60:
        print("You almost failed")
    else:
        print(" Please see your instructor and try again you failed.")


def main():

    avg_score = get_average()
    check_average(avg_score)


if __name__ == "__main__":
    main()