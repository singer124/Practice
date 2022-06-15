import numpy
writer = "P1"
player = "P2"
point1 = 0
point2 = 0
valid_letters = 'abcdefghijklmnopqrstuvwxyz'
while point1+point2 < 5:
    l = 0
    guessed_letters = []
    print("Player 1 Points: "+str(point1),"\tPlayer 2 Points: " +str(point2))    
    print(writer+ ", Enter word for " + player +" to guess")
    final_word = input("").lower()
    print("\n\n\n\n\n\n\n\n\n\n\nWord Hidden")
    word = []
    idx_array = []
    placeholder = []
    _ = 0
    i=0
    while _ < len(final_word):
        placeholder.append("_")
        _ += 1
    for x in final_word:
        word.append(x)
    temp = False
    print(*placeholder)
    while temp is False and i < 6:
        print(player + ", Guess a letter")
        letter = input().lower()
        if letter in guessed_letters:
            print("Already Guessed Letter")
            continue
        if len(letter) != 1:
            print("Incorrect Format (Try inputting only 1 letter)")
            continue
        if letter not in valid_letters:
            print("Invalid Character")
            continue
        guessed_letters.append(letter)
        flag = False
        for index, x in enumerate(final_word):
            if x == letter:
                placeholder[index] = letter
                flag = True
        if flag == False:
            i +=1
        print(*placeholder)
        print(f"{i}/6 Incorrect Guesses")
        temp = numpy.array_equiv(word, placeholder)
    if i == 6:
        print(f"Word was {final_word}\n"+writer +" Wins Round!")
        if writer == "P1":
            point1 += 1
        else:
            point2 += 1
    else:
        print(player +" Wins Round!")
        if writer == "P1":
            point2 += 1
        else:
            point1 += 1
    temp = writer
    writer = player
    player = temp
if point1 > point2:
    print("P1 Wins Game!")
else:
    print("P2 Wins Game!")

        
                
            



