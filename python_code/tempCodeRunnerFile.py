import random
secret = random.randint(1,99)
guess = 0
tries = 0
print "AHOY! I'm the Dread Pirate Roberts, and I have a secret!"
print "It is a number from 1 to 99, I'll give you 6 tries. "
while guess = secret and tries < 6:
    guess = input("what's yer guess?")
    if guess < secret:
        print(Too low,ye scurvy dog!)
    elif guess > secret:\
        print("Too high, landlubber!")
    
    tries = tries + 1

if guess = secret:
    print("avast! You got it! forund my secret, you did!")
else:
    print("No more guesses！ Better luck next time， matay")