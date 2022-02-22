---
marp: true
theme: gaia
_class: lead
paginate: true
backgroundImage: url('https://marp.app/assets/hero-background.jpg')
backgroundColor: #fff

---

![bg left:50% 60%](./figures/python_logo.png)

# **Python Programming**
## 01. Getting Started

Evan Chang

---

# About me - Evan Chang

* ~~NCTU~~ NYCU Computer Science Ph.D. Student
* Data Science / ML / DL
* Python / C / C++ / Java
* toosyou.tw@gmail.com

--- 

# What's Python

![bg left:30%](./figures/Guido_van_Rossum.png)

<- **Guido van Rossum** created it in _1989_.

**Python 2.0** _2000_ - _2020_
**Python 3.x** _2008_ - _now_

---

# What's Python

![bg left:30% blur grayscale](./figures/Guido_van_Rossum.png)

* **Beautiful** is better than ugly.
* **Explicit** is better than implicit.
* **Simple** is better than complex.
* **Complex** is better than complicated.
* **Readability** counts.

---

# What's Python

![bg left:30% blur grayscale](./figures/Guido_van_Rossum.png)

![w:750](./figures/python_arch.png)

--- 

# What's Python

![bg left:30% blur grayscale](./figures/Guido_van_Rossum.pngg)

* Interpreted Language 直譯語言
  * No **Compile** required.
* Dynamic Typed Language 動態語言
  * Type checking in run-time.
  * i.e. type error might occur while executing.

---

# What's Python

![bg left:30% blur grayscale](./figures/Guido_van_Rossum.png)

* Easy to learn.
* Faster to develop.
* Cross-platform.
* **Free packages!**

---
<!-- _class: lead -->

# Pop Quiz:
# Python 2.0 是在哪一年發行的？

---

# Syllabus

1. Environment, Variable, Operation
2. Conditional Statement
3. Loop & Iteration
4. Data Container
5. Functions
6. More Data Container
7. Team Match

---

# Scoring

* 6 HWs, one for each class.
  * 4 - 5 questions each.
  * Upload the source codes to [NYCU E3](https://e3.nycu.edu.tw/).
  * TA will help.

* Team match
  * ~30 people a team
  * ~100 questions
  * Easy / Medium / Hard

---

![bg right:90% fit](./figures/python_logo_large.svg)

---

# Installation

![bg 80% opacity:.2](./figures/AnacondaCIO_Logo.png)

* **Anaconda**
  * Your data science toolkit
  * https://www.anaconda.com/products/individual
    * Python 3.9, 64-Bit Graphical Installer (4xx MB)
    * ![w:50](./figures/windows10_logo.png) > `Anaconda3 (64-bit)` > ![w:50](./figures/anaconda_logo.png)`Anaconda Navigator`
    * ![w:70](./figures/Spyder_logo.svg)`Spyder`

---

![bg 90%](./figures/anaconda_navigator.png)

---

![bg 90%](./figures/spyder.png)

---

# Spyder

* **IDE** for python
  * **I**ntegrated **D**evelopment **E**nvironment
    * 整合開發環境
  * Where to edit and run codes

![bg 90% grayscale opacity:.2](./figures/spyder.png)

---

# Hello, World!

1. ![w:30](./figures/empty_file.png) New File
2. `print('Hello, World!')`
3. Ctrl+s to save the program (you could name it `hello_world.py`)
4. Run ![w:35](./figures/run_button.png)
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

# Constants

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

# Constants
* But how to print single/double quote?
  * `print("single quote:'")` and `print('double quote:"')` works
  * `print('\'')` and `print("\"")` also works
* Special Characters
  * Tab: `\t`
  * Newline: `\n`
  * Beep: `\a`

---

# Constants

* Numerical **constants**
  * `int`, Integer 整數 constant: `420`
  * `float`, Float 浮點數 constant: `199.87`
  * `7e10` means $7 \times 10^{10}$
  * Try it!
    ```python
    print(123)
    print(321.1234567)
    print(9.99e9)
    ```

---

# Arithmetic

* `+ - * /`: `print(1 + 2 / 3)` -> `1.6666666666666665`
* `//` integer division 整數除法: `print(10 // 3)` -> `3`
* `%` modulus 取餘數: `print(10 % 3)` -> `1`
* `**` power: `print(2 ** 10)` -> `1024`

---

# Operator Precedence Rule

1. Parenthesis `()`
2. Power `**`
3. Multiplication, Division, Modulus `*/%`
4. Addition & Subtraction `+-`
5. Left to right

---
<!-- _class: lead -->

# Pop Quiz: 
# `x = 3 + 4 ** 2 / 4 % ( 2 + 1 )`

---

# Variables

* Object with a name that stores data
  * You could choose the name, ~~choose wisely.~~
  * Variables can be reassigned too.
  * Use single `=` to assgin values to variables.
    ```python
    a = 'Hello,'
    b = 69
    c = 10
    c = b / c
    print(a, b, c) # Hello, 69 6.9 
    ```
    * what's the value of `c`?

---

# Variable Names

* Must start with a letter or underscore `_`
* Only letters, numbers and underscore `_`
  * :x: : `2people`, `#sign`, `varable.123`
* Case sensitive 大小寫有差
  * `Sign`, `sign` and `SiGn` are all different variables
* No python keywords
  
---

# Python Keywords

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

# `print`

* Print multiple things at once.
  ```python
  a = 420
  b = 10
  c = a / b
  print(a, 'divided by', b, '=', c) # 420 divided by 10 = 42.0
  ```
  * `a`, `'divided by'`, `b`, `'='` and `c` are arguments 引數 for `print`
  * Note that they are separated by a space.

---

# `print` arguments

* Pass `sep` argument to use different separator.
  ```python
  print(10, 20, 30, sep=', ') # 10, 20, 30
  print(10, 20, 30, sep='\t') # 10      20      30
  ```
* `end` argument to change the ending string.
  ```python
  print(10, 20, 30, end='')
  print(40, 50, 60)
  # 10 20 3040 50 60
  # why?
  ```

---

# `input(prompt_str)`

* Ask the user to input something to the console
  * End with an `Enter`
    ```python
    name = input('Tell me your name:')
    age = input('And your age:')
    print("You're", name, "(", age, ")") # You're Evan ( 18 )
    ```
  * However
    ```python
    print(age + 1) # TypeError: can only concatenate str (not "int") to str
    ```
    * Why?
  
---

# Type Conversion

* `type` will return what type the variable is
  ```python
  print(type(age)) # <class 'str'>
  ```
  * Since `input` return `str`
* Use `int()` to convert object to Integer
  ```python
  age = int(age) # convert to Integer
  print(age + 1, type(age)) # 19 <class 'int'>
  ```
---

# Type Conversion

* Convert it right after `input`
  ```python
  age = int(input('Tell me your age:'))
  print(age + 1)
  ```
  * :warning: Conversion might fail if decimals or texts are inputted.
* Convert to float -> `float()`
* Convert to string -> `str()`
* You get the idea.

---

# Type Conversion

* Integer conversion won't round up
  * `int(3.999)` -> `3`
  * `int(-3.999)` -> `-3`
* `str` convert numbers to strings of number
  * `str(-42)` -> `'-42'`
  * `str(3.999)` -> `'3.999'`

---

# Arithmetic Assignment Operators
* Combine arithmetic operations with assignments
  * `a = a + b` -> `a += b`
  * `a = a - b` -> `a -= b`
  * `a = a * b` -> `a *= b`
  * `a = a / b` -> `a /= b`
  * `a = a % b` -> `a %= b`
  * `a = a ** b` -> `a **= b`
  * `a = a // b` -> `a //= b`

---
<!-- _class: lead -->

# Pop Quiz: 
# 「12345679」猜四個字

---

# Arithmetic Assignment Operators
* Combine arithmetic operations with assignments
  * :warning: The followings are not valid syntax.
    ```python
    a += a += 1
    a += (b += 1)
    ```

---

<!-- _class: lead -->

# Exercises
# 北投香腸人

![bg opacity:.4](./exercises/2022/figures/roger.png)

---

# 北投香腸人

偉大的北投香腸人曾經留下十字箴言，

據傳只要反覆複誦這十個字，就可以抽到傳說中的狗勾肉

![bg opacity:.4](./exercises/2022/figures/roger.png)

---

# 1. 亂講

![bg opacity:.4](./exercises/2022/figures/roger2.png)

* 今天你覺得老師上課在亂講，所以你要印一個「亂講」
* 打開 ![w:70](./figures/Spyder_logo.svg) `Spyder`，使用 `print` 印出 `亂講`
  * 中文會壞掉的話可以用英文

---

# 2. 冷靜

![bg opacity:.4](./exercises/2022/figures/roger3.png)

* 因為你反駁老師，老師太激動了，
* 請輸入老師的名字，後面要他「冷靜」
1. 使用 `input` 輸入老師名字，存入變數 `teeechearrrr`
2. 使用 `print` 印出 `{teeechearrrr} 冷靜`
   * e.g. `TOZY 冷靜`

---

# 3. 真假

![bg opacity:.4](./exercises/2022/figures/roger4.png)

* 你同學跟你講溫度都用華氏，你只好回「真假」再用電腦轉成攝氏度
* 寫一個程式將輸入的華氏溫度 $F$ 轉換成攝氏度 $C$ 印出來
  * $C = \frac{5}{9}\times (F-32)$
```
輸入：50
輸出：真假 10 度喔
```

---

# 4. 有料

![bg opacity:.3](./exercises/2022/figures/toyz.jpg)

* 北投香腸人的朋友 TOZY 最近想買狗牌電動機車
* 但他只有四種硬幣（50, 10, 5, 1）可以付款
* 幫他用最少的硬幣付款吧
* 請輸入一個整數的價格，印出最有料的付法
  ```
  輸入：12699
  輸出：50 * 253
       10 * 4
        5 * 1
        1 * 4
  ```

---

# 5. 中計

![bg opacity:.4](./exercises/2022/figures/taison.jpg)

* 北投香腸人買了一片三角形批薩，發現面積好像怪怪的
* 輸入三個邊長，請用海龍公式印出面積
$$
\triangle = \sqrt{s(s-a)(s-b)(s-c)}, s =\frac{a + b + c}{2}
$$
```
輸入：3↵ 4↵ 5↵
輸出：6 阿中計
```
* [提示](https://www.youtube.com/watch?v=99kJnTr8rwU)

---

# Acknowledgment

* Prof. Chang-Chieh Cheng. National Yang Ming Chiao Tung University, Taiwan
* [Python for Everybody](https://www.py4e.com/)