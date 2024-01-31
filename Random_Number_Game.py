import random

def game1():
    sayi = random.randint(1,10)
    hak = 5
    puan = 0
    puan2 = 100/hak

    while hak > 0:
        tahmin = int(input("Guess: "))
        hak -= 1
        if (tahmin == sayi):
            print("Correct!")
            sayi = random.randint(1,10)
            puan += puan2
        else:
            print(f"Wrong guess. Correct number: {sayi}")
            sayi = random.randint(1,10)
            puan += 0

    print(f"Score: {puan}")
    
def game2():
    sayi = random.randint(1,100)
    hak = 5
    puan = 0 
    
    while hak > 0:
        tahmin = int(input("Guess: "))
        hak -= 1
        if (tahmin == sayi):
            print("Correct!")
            break
        elif (tahmin > sayi):
            print("Down")
        else:
            print("Up")
            
        if (hak == 0):
            print(f"You're done playing. Number held: {sayi}")

def main():
    print("> In the first game, you have to guess the correct number between 1 and 10.")
    print("> In the second game, you have to guess a number from 1 to 100 but this time you will know the direction of the number.")
    game = input("Which game do you want to play?(1/2)")

    if game == "1":
        game1()
    elif game == "2":
        game2()
    else:
        print("ERROR!")
        return main() 

main()   