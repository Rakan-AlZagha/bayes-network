#
# Author: Rakan AlZagha
# Date: 5/7/2021
#
# Assignment: Project #3
# Comments: All good!
#

import random

#
# Function: main
# Purpose: drive the queries and generate main menu
# Parameters: N/A
#

def main():
    print("Would you like to specify how many samples to generate? ('Y' or 'N')\n*If no, default of 100,000 samples will be used for queries.")
    sample_choice = input("--> ")
    if(sample_choice == 'Y'):
        print("\nEnter number of samples to generate:")
        samples = int(input("--> "))
        print()
    elif(sample_choice == 'N'):
        print()
        samples = 100000
    print("Please enter the query you would like to run:\n")
    print("1. In general, how likely is the Hare to win?")
    print("2. Given that is it coldWet, how likely is the Hare to win?")
    print("3. Given that the Tortoise won on the short course, what is the probability distribution for the Weather?")
    print("4. Exit!")
    while(main_menu(samples) != False):
        print("Please input next query or exit:")
        continue

#
# Function: main_menu()
# Purpose: take user input and call query function
# Parameters: N/A
#

def main_menu(samples):
    choice = int(input("--> "))
    if(choice == 1):
        question_one(samples)
        print()
    elif(choice == 2):
        question_two(samples)
        print()
    elif(choice == 3):
        question_three(samples)
        print()
    else:
        print("Exiting...")
        return False

#
# Function: print_status()
# Purpose: for each run, we can see what probability toggles which variable to true (for testing)
# Parameters: N/A
#

def print_status(course_short, course_long, cold_wet, hot, nice, slow_hare, med_hare, fast_hare, slow_tort, med_tort, fast_tort):
    print("Course short: ", course_short, "\nCourse long: ", course_long, "\nCold: ", cold_wet, "\nHot: ", hot, "\nNice: ", nice)
    print("Slow Hare: ", slow_hare, "\nMed Hare: ", med_hare, "\nFast Hare: ", fast_hare, "\nSlow Tort: ", slow_tort, "\nMed Tort: ", med_tort, "\nFast Tort: ", fast_tort)

#
# Function: probability_generator()
# Purpose: generate random probabilites for each query
# Parameters: N/A
#

def probability_generator():
    random_prob = random.uniform(0, 1)
    random_prob = round(random_prob, 2)
    return random_prob

#
# Function: question_one()
# Purpose: generate a probability for q1, run prior sampling
# Parameters: N/A
#

def question_one(samples):
    win_count = 0
    total_samples = 0
    for i in range(samples):
        total_samples += 1
        if(prior_sampling() == True):
            win_count += 1
    probability_hare_win = win_count/total_samples
    print("The probability of a Hare win is:", round(probability_hare_win * 100, 2), "%")

#
# Function: question_two()
# Purpose: generate a probability for q2, run rejection sampling
# Parameters: N/A
#

def question_two(samples):
    win_count = 0
    total_samples = 0
    for i in range(samples):
        evidence, hare_win = rejection_sample_one()
        if(evidence == True):
            total_samples += 1
        if(hare_win == True and evidence == True):
            win_count += 1
    probability_hare_win = win_count/total_samples
    print("Given that is it coldWet, the probability of the Hare winning is:", round(probability_hare_win * 100, 2), "%")

#
# Function: question_two()
# Purpose: generate a probability for q3, run rejection sampling
# Parameters: N/A
#

def question_three(samples):
    total_samples = 0
    cold_count = 0
    hot_count = 0
    nice_count = 0
    for i in range(samples):
        evidence, cold_wet, hot, nice = rejection_sample_two()
        if(evidence == True):
            total_samples += 1
            if(cold_wet == True):
                cold_count += 1
            if(hot == True):
                hot_count += 1
            if(nice == True):
                nice_count += 1
    cold_dist = cold_count / total_samples
    hot_dist = hot_count / total_samples
    nice_dist = nice_count / total_samples
    
    print("Given that the Tortoise won on the short course, the probability distribution for the Weather is:\n")
    print("ColdWet\t\tHot\t  Nice")
    print("-------------------------------")
    print(round(cold_dist * 100, 2), "%\t      ", round(hot_dist * 100, 2), "%\t ", round(nice_dist * 100, 2), "%")

#
# Function: prior_sampling()
# Purpose: for each run, we run prior sampling and return when the hare wins
# Parameters: N/A
#

def prior_sampling():
    hare_win = False
    course_short, course_long = course()
    cold_wet, hot, nice = weather()
    slow_hare, med_hare, fast_hare = hare_perf(course_short, course_long, cold_wet, hot, nice)
    slow_tort, med_tort, fast_tort = tortoise_perf(course_short, course_long, cold_wet, hot, nice)
    hare_win = hare_wins(slow_hare, med_hare, fast_hare, slow_tort, med_tort, fast_tort)
    return hare_win

#
# Function: rejection_sample_one()
# Purpose: for each run, we run rejection sampling and return when cold_wet is true
# Parameters: N/A
#

def rejection_sample_one():
    evidence = False
    hare_win = False
    course_short, course_long = course()
    cold_wet, hot, nice = weather()
    slow_hare, med_hare, fast_hare = hare_perf(course_short, course_long, cold_wet, hot, nice)
    slow_tort, med_tort, fast_tort = tortoise_perf(course_short, course_long, cold_wet, hot, nice)
    hare_win = hare_wins(slow_hare, med_hare, fast_hare, slow_tort, med_tort, fast_tort)
    if(cold_wet == True):
        evidence = True
    return evidence, hare_win

#
# Function: rejection_sample_two()
# Purpose: for each run, we run rejection sampling and return true when the tort wins and the course is short
# Parameters: N/A
#

def rejection_sample_two():
    evidence = False
    hare_win = False
    course_short, course_long = course()
    cold_wet, hot, nice = weather()
    slow_hare, med_hare, fast_hare = hare_perf(course_short, course_long, cold_wet, hot, nice)
    slow_tort, med_tort, fast_tort = tortoise_perf(course_short, course_long, cold_wet, hot, nice)
    hare_win = hare_wins(slow_hare, med_hare, fast_hare, slow_tort, med_tort, fast_tort)
    if(hare_win == False and course_short == True):
        evidence = True
    else:
        evidence = False
    return evidence, cold_wet, hot, nice

#
# Function: course()
# Purpose: take probability and toggle course as short or long
# Parameters: N/A
#

def course():
    course_short, course_long = False, False
    probability = probability_generator()
    #print(probability)
    if(probability <= .5):
        course_short = True
    else:
        course_long = True
    return course_short, course_long

#
# Function: weather()
# Purpose: take probability and toggle weather as cold, hot, or nice
# Parameters: N/A
#

def weather():
    cold_wet, hot, nice = False, False, False
    probability = probability_generator()
    #print(probability)
    if(probability <= .3):
        cold_wet = True
    elif(probability > .3 and probability <= .5):
        hot = True
    else:
        nice = True
    return cold_wet, hot, nice
#
# Function: hare_perf()
# Purpose: for each run, generate what the hare's performance is
# Parameters: N/A
#

def hare_perf(course_short, course_long, cold_wet, hot, nice):
    slow_hare, med_hare, fast_hare = False, False, False
    probability = probability_generator()
    #print(probability)
    if(course_short == True):
        if(cold_wet == True):
            if(probability <= .5):
                slow_hare = True
            elif(probability > .5 and probability <= .8):
                med_hare = True
            else:
                fast_hare = True
        elif(hot == True):
            if(probability <= .1):
                slow_hare = True
            elif(probability > .1 and probability <= .3):
                med_hare = True
            else:
                fast_hare = True
        else:
            if(probability <= .0):
                slow_hare = True
            elif(probability > .0 and probability <= .2):
                med_hare = True
            else:
                fast_hare = True
    if(course_long == True):
        if(cold_wet == True):
            if(probability <= .7):
                slow_hare = True
            elif(probability > .7 and probability <= .9):
                med_hare = True
            else:
                fast_hare = True
        elif(hot == True):
            if(probability <= .2):
                slow_hare = True
            elif(probability > .2 and probability <= .6):
                med_hare = True
            else:
                fast_hare = True
        else:
            if(probability <= .1):
                slow_hare = True
            elif(probability > .1 and probability <= .4):
                med_hare = True
            else:
                fast_hare = True
    return slow_hare, med_hare, fast_hare

#
# Function: tortoise_perf()
# Purpose: for each run, generate the tort's performance
# Parameters: N/A
#    

def tortoise_perf(course_short, course_long, cold_wet, hot, nice):
    slow_tort, med_tort, fast_tort = False, False, False
    probability = probability_generator()
    #print(probability)
    if(course_short == True):
        if(cold_wet == True):
            if(probability <= .2):
                slow_tort = True
            elif(probability > .2 and probability <= .5):
                med_tort = True
            else:
                fast_tort = True
        elif(hot == True):
            if(probability <= .4):
                slow_tort = True
            elif(probability > .4 and probability <= .9):
                med_tort = True
            else:
                fast_tort = True
        else:
            if(probability <= .3):
                slow_tort = True
            elif(probability > .3 and probability <= .8):
                med_tort = True
            else:
                fast_tort = True
    if(course_long == True):
        if(cold_wet == True):
            if(probability <= .2):
                slow_tort = True
            elif(probability > .2 and probability <= .6):
                med_tort = True
            else:
                fast_tort = True
        elif(hot == True):
            if(probability <= .2):
                slow_tort = True
            elif(probability > .2 and probability <= .7):
                med_tort = True
            else:
                fast_tort = True
        else:
            if(probability <= .4):
                slow_tort = True
            elif(probability > .4 and probability <= .8):
                med_tort = True
            else:
                fast_tort = True
    return slow_tort, med_tort, fast_tort

#
# Function: hare_wins()
# Purpose: for each run, generate if the hare won
# Parameters: N/A
#

def hare_wins(slow_hare, med_hare, fast_hare, slow_tort, med_tort, fast_tort):
    hare_win = False
    probability = probability_generator()
    #print(probability)
    if(slow_hare == True):
        if(slow_tort == True):
            if(probability <= .5):
                hare_win = True
        elif(med_tort == True):
            if(probability <= .1):
                hare_win = True
        else:
            if(probability <= .0):
                hare_win = True
    elif(med_hare == True):
        if(slow_tort == True):
            if(probability <= .8):
                hare_win = True
        elif(med_tort == True):
            if(probability <= .5):
                hare_win = True
        else:
            if(probability <= .2):
                hare_win = True
    else:
        if(slow_tort == True):
            if(probability <= .9):
                hare_win = True
        elif(med_tort == True):
            if(probability <= .7):
                hare_win = True
        else:
            if(probability <= 0.5):
                hare_win = True
    return hare_win

if __name__ == "__main__":
    main()
