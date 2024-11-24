Joke = "Here is a joke for you! Sophia is heading out to the grocery store. A programmer tells her: get a liter of milk, and if they have eggs, get 12. Sophia returns with 13 liters of milk. The programmer asks why and Sophia replies: 'because they had eggs"
user_input = input ("What do you want?:")
def joke_recognition():
    if "joke" in user_input:
        print (Joke)
    else:
        print ("Sorry! I only tell jokes")
joke_recognition()

