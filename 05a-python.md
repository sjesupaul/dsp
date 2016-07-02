# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Tuples and lists are both data structures which hold collections of objects. Tuples can hold objects which have different purposes, whereas lists hold similar objects. Tuples are immutable whereas lists, by default, are mutable in python. Tuples will work as keys in dictionaries because it makes sense to create a new instance for each new key and they will not need to be edited.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> Lists and sets are both data structures which hold collections of objects, however lists are ordered and can have morethan one element with the same value, and sets are unordered and each element must be unique. 
For example, if we wanted to keep a sequence of people who won a round in a game, we could use a list, since the same person may win multiple rounds, and the order is important to know which player won in which round.

>> `wins = [‘Max’, ‘Leia’, ‘Harley’, ‘Moki’, ‘Max’, ‘Mika’]`

>> If we wanted to store ID numbers of students in a course, it would make sense that a ID number should not occur more than once, and the order of the collection is not too relevant, so we could use a set.

>> `student_id = {2893, 3287, 8098, 1567, 4873, 2873}`

>> Sets use hash tables to store their values so finding elements is much quicker than lists, which are essentially arrays.

---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> Lambda functions are similar to ‘def’ function definitions, but are anonymous and perform operations on parameters assigned to a variable. It can be used for iterable objects like lists or string, where it performs the operations on each item in your iterable, so that you don’t have to use a `for` loop. For example if we wanted to sort a list of tuples based on the second value in each tuple, we could say:
 
>> `sorted([(2, 2, 7), (6, 3, 5), (3, 4, 9), (1, 7, 2)], key=lambda t: t[1])`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehension is a way to create and modify lists quickly and concisely. They’re written in a mathematical format so they’re used for lists in which some operation had been performed on each element. For example, we could create a list of the powers of two from 0 to 9, by executing either of these lines:

>> `[2**x for x in range(10)]`, or

>> `map(lambda x: 2**x, range(10))`

>> Or we could create a list of numbers divisible by 3 in a given range, 15 to 75:

>> `[x for x in range(15,75) if x % 3 == 0]`, or

>> `filter(lambda x: x % 3 == 0, range(15,75))`

>> Filter only adds a value to a list if the given condition is met, however, map performs a given operation on every element in the list. 

>> We could also create a set which holds pairs of even values 0 to 12 with their cubes:

>> `set([(x,x**3) for x in range(0,12) if x%2==0])`

>> Or a dictionary with values from 0 to 15 with the remainder of their division by 5:

>> `{x : x%5 for x in range(15)}`

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)




