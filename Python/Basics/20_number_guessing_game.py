from random import randint

play_again = True
# print(number)
while play_again:
    number = randint(1,1000)
    guess = -1
    n=0
    while guess != number:
        guess = int(input("Enter number: "))
        n+=1
        if guess == number: 
            print(f"YAYYY...!!! you got it in {n} guesses")
            break
        print(f"{'guess HIGHER' if guess < number else 'guess LOWER'}")
    play = input("\nwanna play again? (y/n)")
    if play.lower() not in 'yesssyep':
        play_again = False
print("******************\nTHANK YOU..!! hope you had a great time!!\n******************\n")