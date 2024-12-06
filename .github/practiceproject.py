
# def joke_recognition():
#     Joke = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
#     user_input = input ("What do you want?:")
#     if "joke" in user_input:
#         print (Joke)
#     else:
#         print ("Sorry! I only tell jokes")


# def double_num():
#     while True:
#         user_num = int(input ("Enter a number to double it:"))
#         if user_num < 100:
#             user_num = user_num * 2
#             print (user_num)
#         else:
#             print ("enter a number less than 100")
#             break

# def space_ship ():       
#     for i in range (10, 0, -1):
#         print (i)
#     print ("LIFT OFF")
# space_ship()

# import random
# def guess_num ():
#     while True:
#         guess: int = random.randint (1, 99)
#         user_input = int(input("Guess the number:"))
#         if user_input < guess:
#             print ("Your guess is too low")
#         elif user_input > guess:
#             print ("Your guess is too high")
#         else:
#             print (f"Congrats! The number was {guess}")
#             break
# guess_num()

# import random
# N_NUMBERS: int = 10
# MIN_VALUE: int = 1
# MAX_VALUE: int = 100
# def main():
#     for _ in range(N_NUMBERS):  
#         print(random.randint(MIN_VALUE, MAX_VALUE), end=" ")    
# if __name__ == '__main__':
#     main()

# import random
# num_rounds = 5
# def high_low ():
#     print ("Welcome to high low game")
#     your_score = 0
#     for i in range(num_rounds):
#         print ("round", i + 1)
#         comp_number = random.randint(1,100)
#         player_number = random.randint(1,100)
#         print (f"Your number is {player_number}")
#         user_ans = input ("Guess your number is high or low from the computer number:")
#         higher_and_correct = user_ans == "higher" and player_number > comp_number
#         lower_and_correct = user_ans == "lower" and player_number < comp_number
#         if higher_and_correct or lower_and_correct:
#             print ("Wow! Your guess was right")
#             your_score += 1
#         else:
#             print("Oooops You lost, the computer number was", comp_number)
#         print ("your score is now", your_score)
#     print("Thanks for playing")
# high_low()
        
# def weight_calculator ():
#     print ("Let's calculate your weight on other planets")
#     user_weight = int(input("Enter your weight in kg on earth:"))
#     user_planet = input ("On which planet you want to calculate your weight on?:").lower()
#     if user_planet == "mars" or user_planet == "mercury":
#         mars_weight = user_weight * 0.38
#         print (mars_weight, "kg")
#     elif user_planet == "venus":
#         venus_weight = user_weight * 0.91
#         print (venus_weight,"kg")
#     elif user_planet == "jupiter":
#         jupiter_weight = user_weight * 2.34
#         print (jupiter_weight,"kg")
#     elif user_planet == "saturn":
#         saturn_weight = user_weight * 1.06
#         print (saturn_weight,"kg")
#     elif user_planet == "uranus":
#         uranus_weight = user_weight * 0.92
#         print (uranus_weight,"kg")
#     elif user_planet == "neptune":
#         neptune_weight = user_weight * 1.19
#         print (neptune_weight,"kg")
#     else:
#         print ("Invalid information")
# weight_calculator()
