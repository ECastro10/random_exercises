import time
import random as r




def timer(time_limit, start):

    timeLoop = True
    Sec = 0
    Min = 0

    timeLoop = start
    while timeLoop:
        if Min == time_limit:
            break
        Sec += 1
        print(str(Min) + " Mins " + str(Sec) + " Sec ")
        time.sleep(1)
        if Sec == 60:
            Sec = 0
            Min += 1
            print(str(Min) + " Minute")

def choose_activity_and_rep(exercises_dictionary):
    temp_choice = r.choice(list(exercises_dictionary))
    temp_reps = r.randint(2, exercises_dictionary[temp_choice] + 1)

    activity_and_reps = "Time to do {0} {1}!".format(temp_reps, temp_choice)

    return activity_and_reps


def main():
    print("THIS IS THE EXERCISE TIMER.\nARE YOU READY?\n")

    target_minutes = int(input("Longest number of minutes between exercises? >> "))
    print("\nA few questions to build the program\n")
    pushups = int(input("Max number of pushups in an interval? >> "))
    situps = int(input("Max number of situps in an interval? >> "))
    ab_roller = int(input("Max number of ab roller reps in an interval? >> "))
    jumping_jacks = int(input("Max number of jumping jacks in an interval? >> "))
    mountain_climbers = int(input("Max number of mountain climbers in an interval? >> "))
    exercise_dict = {"pushups": pushups, "situps": situps, "ab rollers": ab_roller, "jumping jacks": jumping_jacks,
                     "mountain climbers": mountain_climbers}

    start = input("Would you like to begin Timing? (y/n): ")

    while start != "y" and start != "n":
        print("incorrect input\n")
        start = input("Would you like to begin Timing? (y/n): ")

    while start == "y":
        temp_time = r.randint(1, target_minutes)
        timer(temp_time, start)
        print(choose_activity_and_rep(exercise_dict))
        start = input("Would you like to begin Timing? (y/n): ")

        while start != "y" and start != "n":
            print("incorrect input\n")
            start = input("Would you like to begin Timing? (y/n): ")

    print("I hope you enjoyed this and I am glad you exercised today!\nHave a nice day!")
    exit()
while 1 == 1:
    main()



