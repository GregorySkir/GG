#Q1
"""Write a function name c_to_f that receives a temperature in Celsius as an argument.
Return the temperature in Fahrenheit.
do not use the input() function."""
def c_to_f(val):
    val*=1.8
    val+=32
    val=round(val,2)
    return(val)
print(c_to_f(0))#32.0
#Q2
"""Write a function name words_lengths that receives a sentence 
(an argument of a long string containing multiple words). 
The function returns a list of the lengths of the words.
- You should use split() to transform the string into a list of these words.
- You should initialize your list"""
def words_lengths(s1):
    li1=s1.split()
    i=0
    l2=[]
    while i < len(li1):
        l2.append(len(li1[i]))
        i+=1
    return (l2)
print(words_lengths("Good evening and good night"))#[4, 7, 3, 4, 5]
#Q3 FLAGS LETTERS
"""Write three loops that print sequences of letters in the following way (one for each loop):"""
import string
letters = string.ascii_lowercase
i=0
j=len(letters)
while i<j:
    print(letters[i:j])
    i+=1
i=0
j=len(letters)
while i<j:
    print(letters[i:j])
    j-=1
i=0
j=len(letters)
while i<j:
    print(letters[i:j])
    j-=1
    i+=1
#Q4
"""Write a function that checks if this song is true: 
Roses are red, violets are blue, sugar is sweet, and so are you.
The function name should be color_song. It receives 3 arguments: 
the color of a rose, the color of a violet, and the taste of sugar. 
If everything is according to the song then return True. Else return False."""
def color_song( cor, cov, shugar):
    if cor=='Red' and cov=='Blue' and shugar=='Sweet':
        return(True)
    else:
        return(False)
print(color_song('Red', 'Blue', 'Sweet'))#True
#Q5
"""Write the function rps_game(player1, player2) that receives
two hand gestures, rock, paper or scissor, one for each player.
Return a variable that contains the name of the winner (player1 or player2) and a congratulations message.
if they choose the same gesture then return a variable that contains 
an empty string and the message: It’s a draw! 
Remember the rules: Rock beats scissors; scissors beats paper; paper beats rock."""
def rps_game(player1, player2):
    if player1=='rock' and player2=='scissors':
        return('1')
        print('congratulations')
    if player1=='rock' and player2=='paper':
        return('2')
        print('congratulations')
    if player1=='paper' and player2=='scissors':
        return('2')
        print('congratulations')
    if player1=='paper' and player2=='rock':
        return('1')
        print('congratulations')
    if player1=='scissors' and player2=='rock':
        return('2')
        print('congratulations')
    if player1=='scissors' and player2=='paper':
        return('1')
        print('congratulations')
    if player1==player2:
        print('It’s a draw!')        
        return("draw")
print(rps_game('rock', 'paper')[0])#2
#Q6
"""Write the function guess_my_number that receives as an argument some number between 1-100.
Ask the user to guess the number until it is a match.
Print to the user if the guessed number is too high or too low.
Return the number and some congratulation message when the user found the number."""
def guess_my_number(num):
    while True:
        num2=int(input('guess the number 1-100 '))
        if num2>num:
            print('too high')
        elif num2<num:
            print('too low')
        else:
            return(num,'congratulation')
        break
print(guess_my_number(37)[0])#input 50 25 37 expected 37
#OR
def guess_my_number(num):
    # num = randint(1,101)
    guess_num = int(input("Please enter a number between 1 to 100: "))
    while num != guess_num:
        if num < guess_num:
            guess_num = int(input("Too high, guess again: "))
        else:
            guess_num = int(input("Too low, guess again: "))
    else:
        return num, "Well Done"