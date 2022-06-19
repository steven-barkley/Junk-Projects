# Mock Exam 3 code
print()
#Introduction and Purpose statement
intro = input("Welcome to the Mock Exam. Please enter your first name here: ")
print()
print("{}, please take this Mock Exam seriously and good luck!".format(intro))
# Point accumulation out of 50

#input statements are lowercased or ints

# 15 to 17 questions

# if statements, using in for the string
score = 0
print()
question1 = input(""" List_name[a:b] will return the portion
 of list_name starting ____ the index a and ending ____ the
 index b. Enter after, with or before """).lower()
if "with" and "before" in question1:
    score = score + 4
print()
question2 = input("""  If my_list = ["circle", "square",
"triangle", "rectangle"], which of the following modifications
to my_list will make it equal ["circle", "square", "triangle",
"line", "rectangle"]?Enter the function name and index number """).lower()
if "insert" and "three" or "3" in question2:
    score = score + 3
print()

question3 = input("Explain how to find the length of a list? ").lower()
if question3 == "len()" or "len function":
    score = score + 3
print()
question4 = input("""fisted = [ “Punch”, “Kick”, “Jab”]
print(fisted[0])
print(fisted[1:])
print(fisted[1][0])
What will be printed from the last print statement? """)
if question4 == "K":
    score = score + 4
print()
question5 = input("""Type the correct sentence number 1,2,3, or 4.

1. Mutable objects like lists or dictionaries are mutable
because the data stored within them is unchangeable in Memory.

2. Mutable objects like tuples or dictionaries are mutable
because the data stored within them is changeable in Memory.

3. Mutable objects like lists or dictionaries are mutable
because the data stored within them is changeable in Memory.

4. Immutable objects like strings or dictionaries are immutable
because the data stored within them is unchangeable in Memory. """)
if question5 == "3":
    score = score + 3
print()
question6 = input("""Which is an example of list cloning?
Type the correct number.
alist = [0,4,12,7,9]
blist = [12, 15, 17, 20]
1.clist = blist + alist
2.dlist = alist * 2
3.elist = alist
4.flist = list(blist)
 """).lower()
if question6 == "4" or "four" or "fourth":
    score = score + 4
print()
question7 = input("""Functions which take lists as arguments and
change them during execution are called modifiers and the changes
they make are called side effects. Passing a list as an argument
actually passes a reference to the list, not a copy of the list.
Since lists are mutable, changes made to the elements referenced
by the parameter change the same list that the argument is referencing.

Read carefully and enter: "True" or "False"
""")
if question7 == "True":
    score = score + 3
print()
question8 = input("""Which function will produce this output:
[2,3,4,5,6,7,8,9,10,11,12,13,14] ?
1.
def mystuff(stuff):
    mylist = []
    for i in range(1,stuff,2):
        mylist.append(i)
    return(mylist)

print(mystuff(15))

2.
def mystuff(stuff):
    mylist = []
    for i in range(2,stuff,1):
        mylist.append(i)
    return(mylist)

print(mystuff(15))
 """)
if question8 == "2":
    score = score + 4
print()
question9 = input("""What is the difference between a list
and a dictionary?

1. Lists are mapped and dictionaries are indexed.
2. Dictionaries are immutable and use maps.
3. Lists use [] and Dictionaries use ().
4. Dictionaries are indexed by keys and lists by sequence.
 """)
if question9 == "4" or "fourth" or "four":
    score = score + 3
print()
question10 = input("""What will output from the following?
Enter the number of your anwer.

tomatos = [4,24,12,8,9]
mystuff = {tomatos : 55}
mystuff[tomatos] = mystuff[tomatos] + 1
print(len(mystuff)==5)
1. True
2. False
3. Error
4. 56
 """)
if question10 == "3" or "three" or "third":
    score = score + 3
print()
question11 = input("""Which print statement will produce 'stuff' 1,2,3 or 4?
yesSir = [ "captain", "Battle", "ship",["admiral","stuff"]]
print(yesSir[3][::-1])
print(yesSir[3][-1][:])
print(yesSir[3][0])
print(yesSir[3][-1][1:])
 """)
if question11 == "2" or "two" or "second":
    score = score + 3
print()
question12 = input("""Is the follow output correct? Enter 'True' or 'False':
order_of_oper = ["Parenthesis","Exponents",
"Multiplication", "Division","Addition","Substraction","Relational",
"Logical"]

priority = dict(enumerate(order_of_oper))

print(priority)

Output ____
{1: 'Parenthesis', 2: 'Exponents', 3: 'Multiplication', 4: 'Division',
5: 'Addition', 6: 'Substraction', 7: 'Relational', 8: 'Logical'}
 """)
if question12 == "False" or "false" or 'F' or 'f':
    score = score + 3
print()
question13 = input("""Which method will change the value of 'apples' to 75?
fruits = { "apple" : 50 , "banana" : 100 }
1. fruits['apple'] == 75
2. fruits['apple'] = fruits['apple'] + 75
3. fruits['apple'] = fruits['apple'] + 25
4. fruits['apple'] += 75
 """)
if question13 == "3" or "three" or "third" or "3.":
    score = score + 4
print()
question14 = input(""" Explain how to find a total of the dictionary 'inventory'.
inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
Name the function and operator(s) you would use.
 """)
if "+" or "plus" or "add" or "addition" and "get" in question14:
    score = score + 3
print()
question15 = input("""Which is the primary method to format an object's values
 __str__ or __repr__? Type '2' for __str__ and '1' for __repr__ """)
if question15 == "2":
    score = score + 3
print()
#Print Name and score
if score >= 45:
    print("Congratulations, {} you aced the Mock Exam with a score of {}".format(intro,score))
elif 45 > score > 40:
    print("Congratulations, {} you scored {} I think you are ready for the real thing!".format(intro,score))
elif 40 > score > 35:
    print("You almost made the cut, {} just missed one or two in the Mock Exam".format(intro,score))
else:
    print("{}, you can do better, study and try again.".format(intro,score))

print ("Thank you for participating in the MOCK EXAM.")
