#Q1
"""Create the class Person:
a. The class should have the following attributes: name, job, salary, gender with a default value 'male'.
gender should receive 'male' of 'female'
b. During the initialization, if the gender is female than change the salary to 72% of the original salary.
a.     Write a method ‘give_raise’ that receives a percent argument (default it to 0.1).
 Update the property salary by adding to it the percent raise of the original salary.
c. Write the __repr__ and __str__ methods. The method __repr__ should return be unambiguous and 
return “Person(name, job, salary, gender)” for the specific instance. The method “__str__ should be 
readable and return a text that presents the person."""
class Person():
     def __init__(self, name, job, salary, gender='male'):
        self.name=name
        self.job=job
        self.salary=salary
        self.gender=gender
        if self.gender=='female':
            self.salary=0.72*self.salary

     def get_raise(self, percent=0.1):
        self.salary=(1+percent)*self.salary

     def __repr__(self):
        r= [self.name, self.job, self.salary, self.gender]
        return r

     def __str__(self):
        s=self.name+" "+ self.job+" "+ self.salary+" "+ self.gender
        return s
mickey = Person('Mickey Mouse', 'Detective', 1000)
mickey.get_raise(0.2)
print(mickey.salary)#1200.0
#Q2
"""a. Create a subclass Manager of class Person.
b. Update the method give_raise to include a bonus (also as input with default value 0.1).
The method would update the new salary, to be the old salary plus the raise plus the bonus 
calculated over the old salary."""
class Manager(Person):
    def __init__(self, name, job, salary, gender='male'):
        super().__init__(name, job, salary, gender='male')

    def get_raise(self, percent=0.1, bonus=0.1):
        self.salary=self.salary+percent*self.salary+bonus*self.salary
donald = Manager('Donald Duck', 'sailor', 500, 'male')
donald.get_raise(0.1, 0.2)
print(donald.salary)#650.0
#Q3
"""Create a subclass Student of class Person:
a. Add two new attributes: 'courses' that would represent courses the student mastered; 'degree' that would indicate if the student has a degree (should be True or False).
b. Write a method 'learned_course' that would receive a name of a course the student learned. If this is a new course then add it to courses.
c. Write a method 'did_finished_degree' that checks if degree is True. If it is False but the student took enough courses (5 and more) then change the degree to True. The method returns True or False.
* Please make sure that you know how to create an instance."""
class Student(Person):
    def __init__(self, name, job, salary, gender, courses, degree=False):
        super().__init__(name, job, salary, gender)
        self.courses=courses
        self.degree=degree

    def learned_course(self, course):
        set(self.courses).add(course)
    
    def did_finished_degree(self):
        if self.degree==True:
            return self.degree
        elif len(self.courses)>=5:
            self.degree=True
            return self.degree
        else:
            return self.degree
belle = Student('Belle', 'Princess', 0, 'female', ['Introduction to Data Science', 'Hairdressing'])
print(belle.did_finished_degree())#      False      
#Q4
"""Write a list comprehension expression that would return the length of each element in a sequence.
The expression would receive the sequence seq.
To help you out:
A FOR loop works as:

for (set of values to iterate):

    if (conditional filtering):

        output_expression()
The same gets implemented in a simple List Comprehension construct in a single line as:
[output_expression() for(set of values to iterate) if(conditional filtering)]."""
[len(x) for x in seq]
seq = "Hello, how are you? would you tell me your name?".split()#[6, 3, 3, 4, 5, 3, 4, 2, 4, 5]
#Q5
"""Write the same task as a lambda function. Use map. 
The expression would receive the sequence seq.
That is, use: 
list(map(lambda your_expression, your_sequence))"""
list(map(lambda seq : len(seq), seq))
seq = "Hello, how are you? would you tell me your name?".split()#[6, 3, 3, 4, 5, 3, 4, 2, 4, 5]
#Q6
"""Write a list comprehension that would transform a list of numbers to a list of strings.
The list would receive the sequence seq."""
list(map(lambda seq : str(seq), seq))
seq = [12, 14, 5.3, 4]#['12', '14', '5.3', '4']
#Q7
"""Write a list comprehension that would only return numbers that are divided by 2 and 3. 
The expression would receive the sequence seq."""
list(filter(lambda seq: (seq%3 == 0) and (seq%2==0), seq))
seq = range(20)#[0, 6, 12, 18]
#Q8
"""Write a list comprehension that would return a list of characters that are different from a specific letter.
The expression would receive the sequence seq and letter char.
- use if"""
list(filter(lambda seq: (char!=seq) , seq))
seq = "Hello, how are you? would you tell me your name?"
char = 'a'#['H', 'e', 'l', 'l', 'o', ',', ' ', 'h', 'o', 'w', ' ', 'r', 'e', ' ', 'y', 'o', 'u', '?', ' ', 'w', 'o', 'u', 'l', 'd', ' ', 'y', 'o', 'u', ' ', 't', 'e', 'l', 'l', ' ', 'm', 'e', ' ', 'y', 'o', 'u', 'r', ' ', 'n', 'm', 'e', '?']
#Q9
"""Write an expression that takes a string as input and return the string with vowels removed. 
Use list comprehension + join.
The expression would receive the sequence seq."""
"".join(list(filter(lambda seq: (seq!='A') and (seq!='E') and (seq!='I') and (seq!='O') and (seq!='U') and (seq!='a') and (seq!='e') and (seq!='i') and (seq!='o') and (seq!='u') , seq)))
seq = "Hello, how are you? would you tell me your name?"#Hll, hw r y? wld y tll m yr nm?
#OR
''.join([x for x in seq if x not in 'AUOIEauoie'])
