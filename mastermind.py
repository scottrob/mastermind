import random


colors = ['red', 'yellow', 'green', 'blue', 'purple', 'orange']


secret_code = []
i = 0
while i < 4:
   color = random.randint(0,5)
   secret_code.append(colors[color])
   i = i + 1
print ('Secret: ', secret_code)

correct_location = 0
guess_number = 1
while (correct_location != 4):
    # Set up loop variables
    correct_location = 0
    correct_matches = 0
    copy_secret_code = secret_code[:]
    guess = []
    print ('Guess:', guess_number)

    i = 0
    while i < len(secret_code):
      print ('Enter a color from:')
      print (colors)
      color = input()
      guess.append(color)
      i = i + 1

    # correct_location
    i = 0
    while i < len(guess):
      if guess[i] ==  copy_secret_code[i]:
        correct_location = correct_location  +  1
        copy_secret_code[i] = 'X'
        guess[i] = 'Y'
      i = i + 1

    # Partial correct_location
    i = 0
    while i < len(guess):
      j = 0
      while j < len(copy_secret_code):
        if guess[i] ==  copy_secret_code[j]:
          correct_matches = correct_matches +  1
          copy_secret_code[j] = 'X'
          guess[i] = 'Y'
        j = j + 1
      i = i + 1
    #print response
    print (correct_matches, '..', correct_location)
    if correct_location ==  4:
        print ('You guessed it in')
        print (guess_number)
    guess_number = guess_number + 1
