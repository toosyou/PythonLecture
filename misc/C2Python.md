---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
backgroundColor: #fff

---

![bg left:50% 60%](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png)

# **Python Programming**
## From C to python

Evan Chang

---

# About me - 張逸群, Evan Chang

* ~~NCTU~~ NYCU Computer Science Ph.D. Student
* Data Science / ML / DL
  * [Cardio Tool](http://cardiotool.miplab.org)
* Python / C / C++ / Java
* toosyou.tw@gmail.com

--- 

# What's Python

![bg left:30%](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/400px-Guido_van_Rossum_OSCON_2006_cropped.png)

<- **Guido van Rossum** created it in _1989_.

**Python 2.0** _2000_ - _2020_
**Python 3.x** _2008_ - _now_

---

# What's Python

![bg left:30% blur grayscale](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/400px-Guido_van_Rossum_OSCON_2006_cropped.png)

* Zen of python
  * **Beautiful** is better than ugly.
  * **Explicit** is better than implicit.
  * **Simple** is better than complex.
  * **Complex** is better than complicated.
  * **Readability** counts.
  * ... etc
* `import this` to see more

---

# What's Python

![bg left:30% blur grayscale](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/400px-Guido_van_Rossum_OSCON_2006_cropped.png)

![w:750](https://miro.medium.com/max/603/1*oUPhgu1G22fxhl8L6g3YCg.png)

--- 

# What's Python

![bg left:30% blur grayscale](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/400px-Guido_van_Rossum_OSCON_2006_cropped.png)

* Interpreted Language 直譯語言
  * No **Compile** required.
* Dynamic Typed Language 動態語言
  * Type checking in run-time.
  * i.e. type error might occur while executing.

---

# Why Python?

![bg left:30% blur grayscale](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/400px-Guido_van_Rossum_OSCON_2006_cropped.png)

* Easy to learn.
* Faster to develop.
* Cross-platform.
* **Free packages!**

* Porting to `C++` is complicated but possible.
  * [Link](https://docs.python.org/3/extending/embedding.html)

---

# Syllabus

1. Environment, Variable, Operation
2. Conditional Statement
3. Loop & Iteration
4. Data Container
5. Functions
6. Class, Inheritance

---

![bg right:90% fit](https://www.python.org/static/community_logos/python-logo-inkscape.svg)

---

# Installation

![bg 80% opacity:.2](http://ijstokes-public.s3.amazonaws.com/dspyr/img/AnacondaCIO_Logo)

* **Anaconda**
  * Your data science toolkit
  * https://www.anaconda.com/products/individual
    * Python 3.8, 64-Bit Graphical Installer (4xx MB)
    * ![w:50](https://cdn.icon-icons.com/icons2/1508/PNG/512/windows_104558.png) > `Anaconda3 (64-bit)` > ![w:50](https://img-blog.csdnimg.cn/20190601140812391.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MzIzOTQ0MA==,size_16,color_FFFFFF,t_70)`Anaconda Navigator`
    * ![w:70](https://upload.wikimedia.org/wikipedia/commons/7/7e/Spyder_logo.svg)`Spyder`

---

![bg 90%](https://www.anaconda.com/imager/assetsdo/Products/Product-Screenshots/5736/navigator-screenshot_680db6b6f11f9cc710dd7defae241cd3.png)

---

![bg 90%](https://upload.wikimedia.org/wikipedia/commons/1/1b/Spyder-windows-screenshot.png?download)

---

# Spyder

* **IDE** for python
  * **I**ntegrated **D**evelopment **E**nvironment
    * 整合開發環境
  * Where to edit and run codes

![bg 90% grayscale opacity:.2](https://upload.wikimedia.org/wikipedia/commons/1/1b/Spyder-windows-screenshot.png?download)

---

# Hello, World!

1. ![w:30](https://d338t8kmirgyke.cloudfront.net/icons/icon_pngs/000/000/288/original/file-empty.png) New File
2. `print('Hello, World!')`
3. Ctrl+s to save the program (you could name it `hello_world.py`)
4. Run ![w:35](https://icons.iconarchive.com/icons/oxygen-icons.org/oxygen/256/Actions-arrow-right-icon.png)
5. See the output in the bottom right panel!
6. ~~Now you know python~~

---

# How not to write code - comments

* Single-line comments start with `#`
* Multiple lines comments start and end with `'''` or `"""`
* Computer won't see comments. Write whatever you want!
  ```python
  # This is a single line comment
  '''This is a
      multiple lines comment
  '''
  """ so is this one """
  ```

---

# String

* `'Hello, World!'` is a `str`, string 字串 **constant**
  * `'str'`, `"str"`, `'''str'''` and `"""str"""` are all the same in python
  * Try it!
    ```python
    print('Hello, Wrold!')
    print("Hello, World!")
    print('''Hello, World!''')
    print("""Hello, World!""")
    ```

---

# String (Cont')

* But how to print single/double quote?
  * `print("single quote:'")` and `print('double quote:"')` works
  * `print('\'')` and `print("\"")` also works
* Special Characters
  * Tab: `\t`
  * Newline: `\n`
  * Beep: `\a`

---

# String (Cont')

* String concatenation
    ```python
    print('aaa' 'bbb')   # 'aaabbb'
    print('aaa' + 'bbb') # 'aaabbb', same by slower
    ```
* String replication
    ```python
    print('give me ' * 5) # give me give me give me give me give me
    ```

---

# Data type

| Data Type | Examples                                |
| --------- | --------------------------------------- |
| `int`     | -2, -1, 0, 1, 2, 3, 4, 5                |
| `float`   | -1.25, -1.0, --0.5, 0.0, 0.5, 1.0, 1.25 |
| `str`     | 'a', 'aa', 'aaa', 'Hello!', '11 cats'   |
| `bool`    | True, False                             |
| `None`    |                                         |

* Note: `--0.5` is actually `0.5`

---

# Data type (cont')

* Types are also considered as **objects**
  * Data type conversions are done by **object constructors**

```python
a = 55555
s = str(a)        # convert to a string, '55555'
b = int('66666')  # A integer with value 66666
c = float(b)      # 66666.0
```

---

# Variables

* Reserved words

```
False	def	if	raise
None	del	import	return
True	elif	in	try
and	else	is	while
as	except	lambda	with
assert	finally	nonlocal	yield
break	for	not	
class	from	or	
continue	global	pass
```

---

# Variables(Cont')

* No need for declaring types
  ```python
  a = 999
  b = 'a string'
  c = str(999) # '999'
  ```
* Variables with `_` prefix are considered **unuseful**.
  ```python
  _tmp = '123' # _tmp should not be used again
  _, a = some_function() # the first return value doesn't matter
  ```

---

# `print` & `input`

```python
name = input('Tell me your name: ')
age = int(input('Tell me your age: ')) # convert to integer

print(name, age) # Evan 18
print(name, age, sep=', ', end=' - ') # Evan, 18 - 
print('Your name is {}, and your age is {}'.format(name, age)) # format string
```

---

# Logical operations

| Operator | Meaning                  |
| -------- | ------------------------ |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |
| `<`      | Less than                |
| `>`      | Greater Than             |
| `<=`     | Less than or Equal to    |
| `>=`     | Greater than or Equal to |

---

# Logical operations (cont')

```python
42 == 42            # True
40 == 42            # False

'hello' == 'hello'  # True
'hello' == 'Hello'  # False

42.0 == 42          # True
42 == '42'          # True
```

---

# `is`

* Check if two variables point to the same object.

```python

a = 99999
b = 99999
print(a is b) # False

# however
a = 99
b = 99
print(a is b) # True, why?
```

---

# `is` (cont')

* Some constant values are kept as the **default objects**.
  * **Integers in [-5, 256]**.
  * [Strings](https://github.com/satwikkansal/wtfpython#-strings-can-be-tricky-sometimes) without some character.
  * Depends on the interpreter implementation.

---

# `is` (cont')
```python
a = 10
b = 10
c = a + 1
'''
                                        a
                                        |
                                        V
default objects: [-5][-4] ... [0] ... [10][11] ... [255][256]
                                        ^   ^
                                        |   |
                                        b   c
'''
```

---

# `and`, `or`, `not`

* In python, boolean statements are prettier.
  * `&&` -> `and`
  * `||` -> `or`
  * `!`  -> `not`

---

# `and`, `or`, `not`

* In python, boolean statements are prettier.
  ```python
  print(2 + 2 == 4 and not 2 + 2 == 5 or 3 != 3) # True
  ```

---

# `if`, `else`, `elif`

```python
name = 'Bob'
age = 30
if name == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
else:
    print('You are neither Alice nor a little kid.')
```

* Note: **indent matters in python**

---

# `while`

```python
name = str() # empty string
while name != 'Evan':
    name = input('Who are you again? ')
```

* Note: there's no `do while` in python
  ```python
  name = str() # empty string
  while True:
      name = input('Who are you again? ')
      if name == 'Evan':
          break
  ```

---

# `for`

* `range(n)` -> `0, 1, 2 ... n-1`
* `range(start, end)` -> `start, start+1, ... end-1`
* `range(start, end, step)`
  * every `step` elements from `start` to `end`

```python
for i in range(5):
    print(i, end=', ') # 0, 1, 2, 3, 4,

for i in range(3, 8, 2):
    print(i, end=', ')   # 3, 5, 7, 
```

---

# `list`

* A container for **ordered** objects.
* Elements can have **different types**.
* Random access; index starts from **$0$**.

```python
L = [5, 4, 3, 2, 1, 0]
print(L[0])                 # 5

L[0] = L[1] + L[2]
print(L[0])                 # 7
print(L)                    # [7, 4, 3, 2, 1, 0]
```

---

# Indexing of `list`

* Index starts from $0$
* `list[i]`: the $i$-th element.
* `list[i: j]`: elements from $i$ to $j-1$ th
* `list[i: j: k]`: Every $k$ elements of from $i$ to $j-1$ th

---

# Indexing of `list`

```python
L = [0, 1, 2, 3, 4, 5]
print(L[3])                     # 3
print(L[1:6])                   # [1, 2, 3, 4, 5]
print(L[1:6:2])                 # [1, 3, 5]

print(L[:-3])                   # [0, 1, 2]
print(L[3:])                    # [3, 4, 5]
print(L[:])                     # [0, 1, 2, 3, 4, 5]
print(L[::-1])                  # [5, 4, 3, 2, 1, 0]
```

---

# Methods of `list`

* `list()` or `[]` to declare a empty list.
* `list.append(x)` to add `x` to the end of the list.
* `list.extend(another_list)` to extend the list with another list.
* `list.insert(i, x)` to insert `x` to index `i`
* `list.remove(x)` to remove (**the first**) `x` from the list.
* `list.clear()` to remove all the elements.
* `len(L)` returns the length of the list `L`
* `x in L` checks if `x` exists in `L`

---

# Methods of `list`

* `list.sort(key=None, reverse=False)` to sort the list
  * `key` specifies the key function
    * Every element `x` will be seen as`key(x)` when sorting.
* `list.reverse()` to revert the list
  * Equivalent to `list = list[::-1]`
* `list.copy()` returns a copy of the list

---

# Methods of `list`

* `del` to remove elements from the list

```python
L = ['do', 'not', 'work', 'just', 'relax']
del L[1]
print(L)  # ['do', 'work', 'just', 'relax']

del L[2:]
print(L)  # ['do', 'work']

del L[:]  # equivalent to L.clear()
print(L)  # []
```

---

# `for` & `list`

* A list can be passed to a `for` loop

```python
animals = ['cat', 'dog', 'bird', 'dinosaur']
for ani in animals:
    ani += 's'
    print('{} in the zoo!'.format(ani))
print(animals) # ['cat', 'dog', 'bird', 'dinosaur'], why?
```

---

# Immutable vs Mutable

* Immutable objects' value **cannot** be changed after creating.
  * `int`, `float`, `str`, `tuple`...
* Mutable objects' can.
  * `list`, `set`, `dict`...
---

# Immutable vs Mutable

* Immutable
  ![](https://www.maxlist.xyz/wp-content/uploads/2021/01/Immutable-1024x192.jpg)
* Mutable
  ![](https://www.maxlist.xyz/wp-content/uploads/2021/01/mutable-object-list-1024x170.jpg)

---

<!-- _class: lead -->
# Let's take a break and exercise

---

# Bubble Sort - C++

```c
int i, j, temp;
Boolean exchanged = true;

for (i=0; exchanged && i<len-1; i++){
  exchanged = false;
  for (j=0; j<len-1-i; j++){ 
    if (arr[j] > arr[j+1]){
      temp = arr[j];
      arr[j] = arr[j+1];
      arr[j+1] = temp;
      exchanged = true; 
    }
  }
}
```

---

# `tuple`

* Just like a `list` but cannot be changed
* `tuple()` or `()` to declare one
  * Even `v1, v2` will be treated as tuple

```python
a = (1, 2, 3)
b = (4, )       # (4) will be treated as int
c = 5, 6        # a tuple too

print(a, b, c)  # (1, 2, 3) (4,) (5, 6)

a[0] = 5        # TypeError: 'tuple' object does not support item assignment
```

---

# `tuple` & swap

* We could use a tuple to **swap values**

```python
a = 10
b = 20
c = [30, 40]  # list

a, b = b, a   # left and right side are both tuples
print(a, b)   # 20 10, swapped

a, b = c      # list can also distribute values
print(a, b)   # 30 40
```

---

# `dict`

* Use `dict()` or `{}` to declare an empty dictionary
* `values`, `keys` and `items` functions to get elements

```python
student = {
    'id': '0756021',
    'name': 'Evan',
    'age': 18,
}

student['id'] = '0756099'                     # change the id
student['gender'] = 'male'                    # add a new record
print(student['age'], student['gender'])      # 18 male
```

---

# `dict`

* Use `dict()` or `{}` to declare an empty dictionary
* `values`, `keys` and `items` functions to get elements

```python
student = {
    'id': '0756021',
    'name': 'Evan',
    'age': 18,
}

print(student.values()) # dict_values(['0756021', 'Evan', 18])
print(student.keys())   # dict_keys(['id', 'name', 'age'])

for key, value in student.items():
    print('{}: {}'.format(key, value))
```

---

# Functions

* Syntax

```python
def get_a_student(name, gender, age=18):
    return {'name': name, 'gender': gender, 'age': age}

def hello_world():
    print('hello, world!')
    # return nothing

print(hello_world()) 
# hello, world! 
# None, why?
```

---

# Functions (cont')

* Immutable parameters will be copied
* **Mutable** ones will be passed as **references**

```python
def change_int(i):
    i = -999

def change_list(L):
    L[0] = -999

value, a_list = 199, [299]
change_int(value)
change_list(a_list)
print(value, a_list)        # 199 [-999]
```

---

# Functions (cont')

* `tuple` can be returned, allowing multiple return values

```python
def get_max(L):
    maximum = -9999
    index_maximum = -1
    for i in range(len(L)):
        if L[i] > maximum:
            index_maximum = i
            maximum = L[i]
    return index_maximum, maximum # return both index and value

index_maximum, maximum = get_max([9, 3, 7]) # 0, 9
```

---

# `class`

* Instead of `this`, python uses `self`
  * `self` prefix is **always** needed to access memeber func/variables

```python
class MyObject:
    def __init__(self, x, y): # constructor, where to define member variables
        self.x = 30
        self.y = 40
        print(x, y) # different from self.x and self.y

    def __del__(self): # destructor, not used very often in python
        print('bye')

obj = MyObject(10, 20) # 10 20
```

---

# `import` - `include` in python

```python
import numpy # import numpy package

numpy.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

```python
import numpy as np # rename numpy to np

np.arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

```python
from numpy import arange

arange(10) # array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
```

---

<!-- _class: lead -->
# Some Fancy Python Stuffs.

---

# `enumerate` & `zip`

```python
names = ['Evan', 'Bob', 'Alice']
ages = [18, 20, 22]

for i, name in enumerate(names):
    print(i, name, end=', ') # 0 Evan, 1 Bob, 2 Alice,

for name, age in zip(names, ages):
    print(name, age, end=', ') # Evan 18, Bob 20, Alice 22,
```

---

# One Liners

```python
a, b = 10, 30
a, b = b, a                               # swapped

# single line if-else
maximum = a if a > b else b               # 30

# list declaring
one_to_ten = [i+1 for i in range(10)]     # [1, 2, ... 10]
odds = [i for i in range(11) if i%2 == 1] # [1, 3, 5, 7, 9]
identity_matrix = [[1 if i == j else 0 for i in range(3)] for j in range(3)]
# [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
```

---

# Acknowledgment

* Prof. Chang-Chieh Cheng. National Yang Ming Chiao Tung University, Taiwan
* [Python for Everybody](https://www.py4e.com/)
* [cheatsheet](https://www.pythoncheatsheet.org/#Lists)