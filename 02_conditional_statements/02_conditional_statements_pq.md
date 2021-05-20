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
## 02. Conditional Statements

Evan Chang

---

# Conditional Statements?

![bg right:40%](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.0-9/16426270_1850797695203024_3694001626865080011_n.jpg?_nc_cat=105&ccb=3&_nc_sid=730e14&_nc_ohc=0OYME0s2i54AX8MqgRF&_nc_ht=scontent-tpe1-1.xx&oh=48c95c9097d4ae3b5fa968301b45fdf2&oe=60600166)

* Bring an umbrella if it rains.
* Fat if 起Ｏ雞
* ~~Skip classes if they're boring.~~

---

# Boolean Values

![bg left:30%](https://upload.wikimedia.org/wikipedia/commons/6/6c/George_Boole.jpg)

* Only two possible values: `False` and `True`
* Use `bool()` to convert a variable to a boolean
  * `0`, `None` or empty -> `False`
  * otherwise -> `True`
  ```python
  eat_cheogajip     = True
  become_slim       = bool(0)           # False
  become_slim       = bool(None)        # False
  become_fat        = bool(999)         # True
  but_it_feels_good = bool('yesyesyes') # True
  ```

---

# Comparison Operators

* `>`, `<` Greater/Less than
* `>=`, `<=` Greater/Less than or equal to
* **`==` Equal to**
* **`!=` Not equal to**

```python
x = 1
y = 2
print(1 == 1)   # True
print(1 != 2)   # False
print(1 >= 2)   # False
print(x < y)    # True
z = (x == y)    # False, does z = x == y work? why?
```

---
<!-- _class: lead -->

# Pop Quiz: 
# 什麼變數型態只有 `True` 或 `False`?

---

# Logical Operators

* `x and y`, return `True` if x and y are both `True`
* `x or y`, return `False` if x and y are both `False`
* `not x`, return `True` if x is `False`

```python
eat_cheogajip = True
eat_KFC = True
become_slim = not (eat_cheogajip or eat_KFC) # False

print((eat_cheogajip or eat_KFC) and become_slim) # False
```

---

# Logical Complements

* `not (x and y) == (not x) or (not y)`
* `not (x or y)  == (not x) and (not y)`

---

# Logical Complements

* Venn Diagram (文氏圖)
    ![](https://imgur.com/9yZRfMh.jpg)
    * [靈魂繪師](https://sketch.io/sketchpad/)
  
---

<!-- _class: lead -->

# Pop Quiz: 
#### `( (True and False) or (not (False or False)) ) and True`

---

```python
# Operator Precedence
1. :=
2. lambda
3. if – else
4. or
5. and
6. not x
7. in, not in, is, is not, <, <=, >, >=, !=, ==
8. |
9. ^
10. &
11. <<, >>
12. +, -
13. *, @, /, //, %
14. +x, -x, ~x
14. **
14. await x
15. x[index], x[index:index], x(arguments...), x.attribute
16. (expressions...), [expressions...], {key: value...}, {expressions...}
```

---

# Identity Operators
* `x is y` return `True` if `x` and `y` is the same object.
* There's also `x is not y` for checking if they are different objects

```python
x = 3
y = 4
print(x is y)       # False
print(x is not y)   # True
print(not(x is y))  # True
```

---

# Identity Operators
* **However**, python creates one object for each number in [-5, 256].
* But not for number < -5 or > 256

```python
a = 10
b = 10
x = 257
y = 257

print(a is b, x is y)     # True False, why?
```

---

# Identity Operators

* Default objects
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

# Identity Operators

* Not default objects
```python
x = 257
y = 257

'''
x -> [Integer with value 257]
y -> [Integer with value 257]
'''
```

* Takeaway: **DON'T compare integers by `is`**

---

# Identity Operators

* Something similar occurs when using `is` to compare `string`s

```python
a = 'AAAAA'
b = 'AAAAA'

x = 'cheogajip is good'
y = 'cheogajip is good'

print(a is b, x is y) # True False, why?
```
* [Why?](https://github.com/satwikkansal/wtfpython?fbclid=IwAR3nXrCEFisfEMhVU5WTcLcOEFN7LQlicVAiy1V3YdXRMVl5fw9p_1MwhPo#-strings-can-be-tricky-sometimes)
* Takeaway: **DON'T compare strings by `is`**

---

# `if` statement

* Do something `if` the condition is `True`
* Syntax
  ```python
  if some_condition:
      indented_statements
  ```
* Example
  ```python
  dinner = input('What do you want to eat? ')
  if dinner == 'cheogajip' or dinner == 'KFC':
      print('FAT!')
  ```

---

# `if` and `else`
* Do something if no conditions are `True` in `if`
* Syntax
  ```python
  if some_condition:
      indented_statements
  else:
      another_indented_statements
  ```

---

# `if` and `else`
* Do something if no conditions are `True` in `if`
* Example
  ```python
  dinner = input('What do you want to eat? ')
  if dinner == 'cheogajip' or dinner == 'KFC':
      print('FAT!')
  else:
      print('Good!')
  ```

---

# `if`, `elif` and `else`

* `elif` stands for `else` + `if`
* Syntax
  ```python
  if some_condition:
      indented_statements
  elif another_condition:
      another_indented_statements
  else:
      yet_another_indented_statements
  ```

---

# `if`, `elif` and `else`

* Example
  ```python
  dinner = input('What do you want to eat? ')
  if dinner == 'cheogajip' or dinner == 'KFC':
      print('FAT!')
  elif dinner == 'chicken breast':
      print('Excellent!')
  else:
      print('Good!')
  ```

---

# `if`, `elif` and `else`

* Example - scoring system

```python
score = int(input('Input Score: '))           #    start
if score >= 90:                               #      ↓
    print('A!')                               # [score >= 90?]  -> A!
elif score >= 70:                             #      ↓
    print('B!')                               # [score >= 70?]  -> B!
elif score >= 60:                             #      ↓
    print('C!')                               # [score >= 60?]  -> C!
else:                                         #      ↓
    print('F!')                               #      F!
```

---

# Nested `if`, `elif` and `else`

```python
teacher_nice = input('Is the teacher nice? ') #   start
score = int(input('Input Score: '))           #     ↓
if teacher_nice == 'yes':                     # [teacher_nice == 'yes'] -> A++!
    print('A++!')                             #     |
else:                                         #     L -> [score >= 90?]  -> A!
    if score >= 90:                           #                ↓
        print('A!')                           #          [score >= 70?]  -> B!
    elif score >= 70:                         #                ↓
        print('B!')                           #          [score >= 60?]  -> C!
    elif score >= 60:                         #                ↓
        print('C!')                           #                F!
    else:
        print('F!')
```

---

<!-- _class: lead -->
# Before we continue
![bg right:60%](https://i.imgur.com/AsngJfx.png)


---

# `try` and `except`

* Sometimes codes will give us errors.
  ```python
  x = 'not an integer'
  x = int(x)
  '''
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  ValueError: invalid literal for int() with base 10: 'not a integer'
  '''
  ```
* How to prevent programs from crashing?

---

# `try` and `except`
* Syntax
    ```python
    try:
        do_something
    except SomeException:
        handle_exception
    ```
* `ValueError` is one type of build-in exception.
  * Also `KeyError`, `IndexError`, `KeyboardInterrupt`, `ZeroDivisionError` ...etc.

---

# `try` and `except`

* Example
  ```python
  weight = input('Input your weight: ')
  try:
      weight = int(weight)
      print('You weight', weight, 'kg')
  except ValueError:
      print('Input Integer plz!')
  ```

---

# `try` and `except`

* Catch multiple exceptions
  ```python
  try:
      cost = int(input('Dinner, how much? '))
      n_people = int(input('People, how many? '))
      print('Each should pay', cost / n_people)
  except ValueError:
      print('Please input integers!')
  except ZeroDivisionError:
      print('There is no one ????')
  ```

---

# `try` and `except`

* How to find the correct exception?
  * Try it and see the error messages!
* Too lazy? Simply ignore it!
  ```python
  try:
      int('Not a integer')
  except:
      print('Oops, there is something wrong!')
  ```
  * This catches every exception.
    * However, it may reduce **readability** and **reliability**.

---

# :warning: Indentation :warning:

* Python **cares** about indentation.
  * Inconsistent indentation might causes problems.
    ```python
    if True: # always proceed
        print('Ahoy!Ahoy!Ahoy!Ahoy')  # 4 spaces
      print('踊るAhoy!に見るAhoy!')     # 2 spaces
    '''
      File "test.py", line 3
    print('踊るAhoy!に見るAhoy!')     # 2 spaces
                                         ^
    IndentationError: unindent does not match any outer indentation level
    '''
    ```
---

# :warning: Indentation :warning:

* Python **cares** about indentation.
  * Mixing `Tab ↹` and 4 `Space`s also causes problems.
    * And you can't even see it.
    * Modern IDEs prevent this by replace `Tab ↹` with 4 `Space`s automatically.

---

<!-- _class: lead -->
# Exercises

---

# 1. 起Ｏ雞

![bg opacity:.2](https://miemie.tw/wp-content/uploads/%E9%AB%98%E9%9B%84%E8%B5%B7%E5%AE%B6%E9%9B%9E-1-1.jpg)

* 起Ｏ雞實在太好吃了，以至於阿群每次都會點太多吃不完，請寫一個程式警告阿群吧！
  1. 請使用者輸入一個浮點數 $T$，代表阿群今天餓了幾個小時
  2. 使用以下公式計算阿群的食量 $F$ （隻雞）
     $$
     F = \frac{T}{10} + \frac{1}{4}
     $$
  3. 讓阿群輸入一個浮點數 $C$，代表想要點的隻數
  4. 若 $C>F$ 則印出 `你才吃不完`，反之印出 `胖`

---

# 2. 起Ｏ雞 2

![bg opacity:.2](https://alina00.com/wp-content/uploads/2016/10/%E8%B5%B7%E5%AE%B6%E9%9B%9E.jpg)

* 承上題，有時候阿群會輸入奇怪的東西，那就代表他餓到語無論次了，印個東西讓他醒醒腦吧！
  * 請使用 `try` 跟 `except` 處理輸入無法被轉成浮點數的錯誤
  * 如果無法轉成浮點數，印出下面的訊息並結束程式吧
    ```
    觀自在菩薩, 行深般若起Ｏ雞多時, 照見五蘊皆雞, 度一切苦厄.
    起Ｏ雞, 起不異雞, 雞不異起, 起即是雞, 雞即是起; 受想行識, 亦復如是.
    起Ｏ雞, 是諸法雞相: 不生不滅, 不垢不淨, 不增不減.
    是故空中無雞, 無受想行識, 無眼耳鼻舌身意,
    無雞聲香味觸法, 無眼界乃至無意識界,
    無無明, 亦無無明盡; 乃至無老死, 亦無老死盡.
    無苦集滅道, 無智亦無得.
    ```
---

# 3. 火鍋

![bg opacity:.3](https://cdn.psee.io/4908f44a-0697-4ee7-b90d-5892716679dd.png)

* 阿統面臨財務危機，被迫兼差打工，他決定用骰子來決定打工地點
  1. 請阿統輸入骰出來的數字，如果該數字
     1. 大於六或小於一，印出 `台中哪個屁孩站出來說啊！！你只是個小丑R！`
     2. 一到六
        1. 奇數 —— 阿統決定要去辛酸火鍋店打工，印出 `RRRRRR一代一代一代`
        2. 偶數 —— 阿統決定要去公館擺攤，請印出下頁的決定
   
---

<!-- _class: lead -->

![bg opacity:.3](https://i.ytimg.com/vi/vUvKjM73x9A/hqdefault.jpg)

```
他們是人欸😡😡那你叫警察🤬🤬來叫他們滾嘛🤭🤭他們是人😭😭
他們是人🤔🤔你禮貌的說😳😳好我們現在大家不要擠在這邊😀😀
那他們要不要走他們的事🙃🙃我怎麼控制他們我請問你😔😔
他們是不是你的粉絲嘛😤😤我不知道👐👐我不知道👐👐
我說真的不知道🙌🙌🙌不要笑👈不要笑👉不要笑👇
```
---

# 4. 肝膽香皂

![bg opacity:.4](https://cdn.ready-market.com/101/9816a644//Templates/pic/soap.png?v=3b4ef92f)

* 阿莎最近著迷於製作人工肥皂，但他始終搞不清楚原理
  ![](https://wikimedia.org/api/rest_v1/media/math/render/svg/529faff0c03a891c96bfd517c20730771f17efba)
  * 其中 R 基有三種可能的形式：$C_{17}H_{33}$, $C_{15}H_{31}$, $C_{17}H_{35}$
  * 讓阿莎各別輸入 $C$ 及 $H$ 的數量，並僅使用**一個** `if` 判斷是否是可用的 R 基吧
  * :warning:注意：$C$ 及 $H$ 的量可以是 $K$ 個 R 基總和
    

---

# 5. 彬彬姐泡湯

![bg opacity:.15](https://s.yimg.com/ny/api/res/1.2/E8DexpEjOPp3D6cMOJ4FsA--/YXBwaWQ9aGlnaGxhbmRlcjt3PTk2MA--/https://s.yimg.com/os/creatr-uploaded-images/2021-02/4f4584f0-7705-11eb-997f-92146e0fd5fb)

* 彬彬姐在二二八時，去由布院泡了「只有今天限定」的限時湯屋
* 她不禁好奇今年是不是閏年，明天會不會是 2/29 呢
  * 請彬彬姐輸入今年的西元年份 $Y$，輸出是不是閏年吧，閏年規則：
    1. $Y$ 非 $4$ 的倍數 -> 平年
    2. $Y$ 為 $4$ 的倍數，但非 $100$ 的倍數 -> 閏年
    3. $Y$ 為 $100$ 的倍數，但非 $400$ 的倍數 -> 平年
    4. $Y$ 為 $400$ 的倍數 -> 閏年
* [提示](https://youtu.be/uoqJy_AEt-E)

---

# Acknowledgment

* Prof. Chang-Chieh Cheng. National Yang Ming Chiao Tung University, Taiwan
* [Python for Everybody](https://www.py4e.com/)