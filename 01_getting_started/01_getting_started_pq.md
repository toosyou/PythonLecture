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
## 01. Getting Started

Evan Chang

---

# About me - Evan Chang

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

* **Beautiful** is better than ugly.
* **Explicit** is better than implicit.
* **Simple** is better than complex.
* **Complex** is better than complicated.
* **Readability** counts.

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

# What's Python

![bg left:30% blur grayscale](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/400px-Guido_van_Rossum_OSCON_2006_cropped.png)

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

* 6 HWs, one for each class (20:00 - 21:00).
  * 4 - 5 questions each.
  * you could hand it in the next week.
  * TA will help.

* Team match
  * ~30 people a team
  * ~100 questions
  * Easy / Medium / Hard

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
# :hamster:天竺鼠車車:hamster: PUInt PUInt

![bg opacity:.2](https://p2.bahamut.com.tw/B/2KU/06/ab809378e0d5116c0b861c30c31b3di5.JPG)

---

# 1. 借過:ambulance:借過:ambulance:

![bg opacity:.3](https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/01/21/1/11291372.jpg&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1)

* 車車在高速公路上塞車了，所以他想要跟大家說聲「借過」
* 打開 ![w:70](https://upload.wikimedia.org/wikipedia/commons/7/7e/Spyder_logo.svg) `Spyder`，使用 `print` 印出 `借過🚑借過🚑`
  * 中文跟 🚑 會壞掉的話可以用英文

---

# 2. 站住:raised_hand:站住:raised_hand:

![bg opacity:.3](https://pgw.udn.com.tw/gw/photo.php?u=https://uc.udn.com.tw/photo/2021/01/16/1/11213288.jfif&x=0&y=0&sw=0&sh=0&sl=W&fw=800&exp=3600&w=930&nt=1)

* 警察車車目睹了一場銀行搶案，快叫前面的兩個壞人站住:raised_hand:
1. 使用 `input` 讓警察輸入壞人一號的名字，存入變數 `badguy1`
2. 使用 `input` 讓警察輸入壞人二號的名字，存入變數 `badguy2`
3. 使用 `print` 印出 `{badguy1}站住✋ {badguy2}站住✋`
   * e.g. `Gura站住✋ Ame站住✋`

---

# 3. 好熱:thermometer:好熱:thermometer:

![bg opacity:.3](https://s.newtalk.tw/album/news/526/6007a1165fb16.jpg)

* 太陽好大好大，車車好熱:thermometer:好熱:thermometer:，車上的貓好熱:thermometer:好熱:thermometer:好熱:thermometer:
* 但是溫度計:thermometer:上面寫的是華氏度，寫一個程式將輸入的華氏文度 $F$ 轉換成攝氏度 $C$ 印出來吧
  * $C = \frac{5}{9}\times (F-32)$

---

# 4. 垃圾🗑️垃圾 🗑️

![bg opacity:.2](https://i.ytimg.com/vi/0d4nLXIansU/maxresdefault.jpg)

* 天竺鼠車車在街上做大掃除，他想用最少的垃圾袋將垃圾裝完
* 他有四種垃圾袋：50🗑️，10🗑️，5🗑️，1🗑️
* 請輸入一個整數🗑️的垃圾量，印出最適合的裝法
  ```
  輸入：123
  輸出：50🗑️ * 2
       10🗑️ * 2
        5🗑️ * 0
        1🗑️ * 3
  ```

---

# 5. 披薩:pizza:披薩:pizza:

![bg opacity:.3](https://i0.zi.org.tw/ddm/2021/01/1611688399-5ada021067295a2b0609abf3172ab361.jpg)

* 車車們在比賽誰吃的三角形披薩:pizza:比較大，你能幫車車們算面積嗎
* 輸入三個邊長，請用海龍公式印出面積
$$
\triangle = \sqrt{s(s-a)(s-b)(s-c)}, s =\frac{a + b + c}{2}
$$
```
輸入：3↵ 4↵ 5↵
輸出：🍕6🍕
```

---

# Acknowledgment

* Prof. Chang-Chieh Cheng. National Yang Ming Chiao Tung University, Taiwan
* [Python for Everybody](https://www.py4e.com/)
* [天竺鼠車車](https://www.youtube.com/watch?v=_6TtTRrno3E)