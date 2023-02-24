#rock>scissors 1>3
#scissors>paper 3 > 2
#paper>rock 2 >1
counter = [0,0]
while True:
    choice = []
    choice.append(input('player 1 choose weapon: '))
    choice.append(input('player 2 choose weapon: '))
    # gör om till 1,2,3
    for i in range(len(choice)):
        if choice[i] == 'rock':
            choice[i] = 1
        elif choice[i] == 'paper':
            choice[i] = 2
        elif choice[i] == 'scissors':
            choice[i] = 3
        elif choice[i] == 'tsar bomba':
            print('Congratulations player', i+1, 'you found the easter egg and won the game!')
            choice[i] = 5
        else:
            print('Invalid input from player ', i+1)
    #easter egg
    if choice[0] == 5 and choice[1] == 5:
        print('Ulitmate tie')
        counter[0] += 5
        counter[1] += 5
    elif choice[0] == 5:
        print('player 1 got chicken dinner')
        counter[0] += 1
    elif choice[1] == 5:
        print('player 2 got chicken dinner')
        counter[1] += 1
    else:
        # om palyer 1 valt rock
        if choice[0] == 1:
            if choice[1] == 1:
                print('Tie')
            elif choice[1] == 2:
                counter[1] += 1
                print('player 2 wins')
            elif choice[1] == 3:
                counter[1] += 1
                print('player 1 wins')
        # om palyer 1 valt paper
        if choice[0] == 2:
            if choice[1] == 1:
                counter[0] += 1
                print('player 1 wins')
            elif choice[1] == 2:
                print('Tie')
            elif choice[1] == 3:
                counter[1] += 1
                print('player 2 wins')
        #om palyer 1 valt scissors
        if choice[0] == 3:
            if choice[1] == 1:
                print('player 2 wins')
                counter[1] += 1
            elif choice[1] == 2:
                counter[0] += 1
                print('player 1 wins')
            elif choice[1] == 3:
                print('Tie')
    print()
    quit = input('Play again? (y/n) ')
    if quit == 'n':
        break
print('Score: ')
print('p1: ', counter[0], '| p2: :', counter[1])
