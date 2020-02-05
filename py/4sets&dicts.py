#Q1
"""write a function count_vowels() that receives a string. For each word, count how many vowel letters it has.
 As output, print a list of the values calculated for each word.
-   The English vowels are A, E, I, O, U."""
def count_vowels(s):
    l = s.casefold()
    l= s.split()
    z=[]
    e=0
    for word in l:
        x=  l[e].count("a") + l[e].count("i") + l[e].count("e") + l[e].count("o") + l[e].count("u")
        z.append (x)
        e +=1
    return (z)
print(count_vowels("Don't worry, be happy"))#[1, 1, 1, 1]
#Q2
"""Write a function remove_duplicate() that receives a list and returns a new 
list that contains all the elements of the first list without duplicates. 
Don't use sets, use a for loop."""
def remove_duplicate (li):
    l= []
    for a in li:
        if a in l:
            continue
        else:
            l.append(a)          
    return l
my_list = "the player went to the stadium".split()
print(remove_duplicate(my_list))#['the', 'player', 'went', 'to', 'stadium']
#Q3
"""Write an expression in python (a line of code) that takes a list named my_list,
 and removes all the duplicates from it. Keep in mined that the result should be a list as well.
Use set."""
list(set(my_list))
#Q4
"""Write a function print_value() that loops over a dictionary
 and prints the value of every key so that it would print: “The value of key is: value”.
Add a second parameter to the function that receives the message 
you want to print. If no message is added than print the default message above.
For example:
The value of red is: rot
The value green is: green"""
def print_value(dic):
    for i in dic:
        print ("The value of {} is: {}".format(i, dic.get(i)))
{"red":"color", "cat":"animal"}
#Q5
"""Write a function invert_dict() that receives a dictionary that contains unique 
keys and unique values. Create a new dictionary that inverts the keys and values so 
that the values are now the keys and the keys are the new values.
Note that this cannot work in cases where the value is not immutable (e.g. list)."""
def invert_dict(my_dict):
    d={}
    for k, v in my_dict.items():
        d[v]=k
    return d
my_dict = {1: "a", 2:"b", 3:"c"}
print(invert_dict(my_dict))#{'a': 1, 'b': 2, 'c': 3}
#Q6
"""Write a function my_map() that receives another function’s name and a list or tuple as inputs. 
The function returns a list of the results of the input function call on every element in the list."""
def my_map(funk, f):
    k=[]
    for i in f:
        k.append(funk(i))
    return k
print(my_map(int, [0.1, 0.3, 0.5, 0.7, 0.9, 1.1]))#[0, 0, 0, 0, 0, 1]