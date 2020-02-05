#Q1
"""word is a variable containing a string.
Write an expression that produces the char located second to last in word. 
Don't use the print function function"""
word[len(word)-2]
#Q2
"""word is a variable containing a sting.
Write an expression that produces the word first three letters.
Don't use the print function."""
word[0:3]
#Q3
"""N is some big number. We have created the variable my_nums by:
my_nums = list(range(N))
1. Slice the list to return every third element starting from the second element. Print your answer.
2. Print the descending list of my_nums using slicing. 
Think which function would you use to answer part 2 (don't need to submit this)."""
print(my_nums[1:len(my_nums):3])
my_nums.reverse()
print(my_nums)
#OR
print(my_nums[1::3])
print(my_nums[::-1])
#Q4
"""Create a list L1 of numbers from 1 to 5. Use range.
Create a new list L2 with the elements: five, four, three, two, one
Use list methods to add the word ’six’ to L1
Add L2 to L1. 
Print L1.
Switch the positions of elements five and 5 in L1.
print a new list that has every second element of L."""
L1 = list(range(1, 6))
L2 = ['five', 'four', 'three', 'two', 'one']
L1.append('six')
L1.extend(L2)
print(L1)
L1[4], L1[-5] = L1[-5], L1[4]
print(L1[1::2])
#Q5
"""Write an expression that produces the index of the second occurrence of 𝚜𝟸 in 𝚜𝟷.
If 𝚜𝟸 does not occur twice in 𝚜𝟷, the expression should produce -𝟷. 
you should allow overlapping occurrences of 𝚜𝟸."""
s1.find(s2, s1.find(s2) + 1)
#Q6
"""Given a list of names names_list, print the names 
separated by comma and space. Please use a string to answer."""
print(', '.join(names_list))
#Q7
"""Write a script that asks a user to enter a temperature in Celsius.
You should convert it to Fahrenheit and print back the answer.
Use input() function."""
val =float(input("Enter your value: "))
val*=1.8
val+=32
val=round(val,2)
print(val)