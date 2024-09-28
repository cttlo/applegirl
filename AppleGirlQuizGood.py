#!/usr/bin/env python
# coding: utf-8

# In[15]:


#All rights reserved, the intellectual property of KYRA MEIER
#contact kyraprmeier@gmail.com
#09/23/2024
#for Apple Girl Zine (2024), Charlotte Alarie

total_score = 0 #initiate total score
welcome_input = input("Hello there! Welcome to this lyric quiz created exclusively for Apple Girl Zine subscribers. The category is: Apple (2024) by Charli XCX. Are you ready to begin?") #send welcome message and initiate quiz
welcome_input = welcome_input.strip().lower() #convert input to lowercase to avoid potential issues

if welcome_input.startswith("y"): #allow program to accept "yass" "yess" "ya" etc.
    question_1_input = input("Question 1 of 3 (easy): Did the apple fall far from the tree? (answer yes or no) ") #get user input for Q1
    question_1_input = question_1_input.strip().lower()  
    
    if question_1_input == "no":
        print("Correct!")
        total_score += 1 #add to total score
    else:
        print("Incorrect :(")

    question_2_input = input("Question 2 of 3 (medium): What color did the apple turn?") #get user input for Q2
    question_2_input = question_2_input.strip().lower()  
    
    if question_2_input in ("yellow and green","yellow or green","yellow green","green yellow","yellow","green"): #account for potential lyric variations
        print("Correct!")
        total_score += 1
    else:
        print("Incorrect :(")

    question_3_input = input("Question 3 of 3 (hard): Why is the apple rotten right to the core? ") #get user input for Q3
    question_3_input = question_3_input.strip().lower()

    accepted_responses = [ #define accepted answers
        "from all the things passed down from all the apples coming before",
        "from all the things passed down",
        "all the things passed down",
        "the things passed down",
        "things passed down",
        "from all the apples coming before",
        "all the apples coming before",
        "the apples coming before",
        "apples coming before",
    ]    

    if question_3_input in accepted_responses:
        print("Correct!")
        total_score += 1
    elif question_3_input == "you think you just fell out of a coconut tree? you exist in the context of all in which you live and what came before you":
        print("Ur so cheeky >;) Take an extra point!")
        total_score += 2
    else:
        print("Incorrect :(")

    #formulate personalized outputs based on test score
    if total_score > 3:
        output = "Thank you for completing the quiz <3. Based on your results, you received a bonus score of {0}/3 and are permitted to DRIVE ALL NIGHT. Trop cool!".format(total_score)
    elif total_score == 3:
        output = "Thank you for completing the quiz <3. Based on your results, you received a perfect score of {0}/3 and are permitted to DRIVE ALL NIGHT. Amazing!".format(total_score)
    elif total_score == 2:
        output = "Thank you for completing the quiz <3. Based on your results, you received a passing score of {0}/3 and are permitted to DRIVE ALL NIGHT. Yay!".format(total_score)
    else:
        output = "Thank you for completing the quiz <3. Based on your results, you received a failing score of {0}/3 and are not permitted to DRIVE ALL NIGHT. Try again next time!".format(total_score)

    print(output)

else:
    print("Bye bye!")


# In[ ]:




