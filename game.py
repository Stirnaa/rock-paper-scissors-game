human_turn = input ('Input human turn: ')
computer_turn = input('Input computer turn: ')
if computer_turn == human_turn: 
    print('Draw!')
if human_turn == 'rock' and computer_turn == 'scissors':
    print('human wins!')
elif human_turn == 'paper' and computer_turn == 'rock':
    print('human wins!')    
elif human_turn == 'scissors' and computer_turn == 'paper':
    print('human wins!')
else: print('Computer wins!')
