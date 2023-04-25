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
## 04. Data Container

Evan Chang

---

<!-- _class: lead -->
# Data Container 
# 
# 
# 
# 
# 

![bg opacity:.5](https://cdn.pocket-lint.com/r/s/660x/assets/images/156343-apps-news-feature-best-suez-canal-memes-image6-sb0tykntw7-jpg.webp?v1)

---

<!-- _class: lead -->
# `list`

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
print(L[:])                     # [0, 1, 2, 3, 4, 5], same as L
print(L[::-1])                  # [5, 4, 3, 2, 1, 0]
print(L[4:1:-1])                # [4, 3, 2]
```

---

<!-- _class: lead -->
# Pop Quiz: 
```python
L = [0, 1, 2, 3, 4, 5]

print(L[::2])
```

---

# Methods of `list`

* `list()` or `[]` to declare an empty list.
* `list.append(x)` to add `x` to the end of the list.
* `list.extend(another_list)` to extend the list with another list.

```python
L1 = list()
L2 = [2, 3]
L3 = ['X', 'Y', 'Z']

L1.append(1)        # [1]
L1.extend(L2)       # [1, 2, 3]
L1.extend(L3)       # [1, 2, 3, 'X', 'Y', 'Z']
print(L1)
```

---

# Methods of `list`

* Try it!
  * Use `L1`, `L2` and `L3` to generate `L4`
```python
L1 = ['A', 'B', 'C']
L2 = [1, 2, 3]
L3 = ['O', 'X']
L4 = ['A', 'B', 'C', 1, 'O',
      'A', 'B', 'C', 1, 'X',
      'A', 'B', 'C', 2, 'O',
      'A', 'B', 'C', 2, 'X',
      'A', 'B', 'C', 3, 'O',
      'A', 'B', 'C', 3, 'X']
```

---

# 2D `list`

* A list of lists.

```python
L = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(L[0])                 # [1, 2, 3]
print(L[0][1])              # 2
```

* 3D `list` is also possible. List of lists of lists.

---

# Methods of `list`

* `list.insert(i, x)` to insert `x` to index `i`
* `list.remove(x)` to remove (**the first**) `x` from the list.
* `list.clear()` to remove all the elements.
* `len(L)` to get the length of the list `L`

```python
L = ['A', 'B', 'C', 1, 2, 3]
L.insert(6, 'A')
print(L, len(L))    # ['A', 'B', 'C', 1, 2, 3, 'A'] 7
L.remove('A')
print(L, len(L))    # ['B', 'C', 1, 2, 3, 'A'] 6
L.clear()
print(L, len(L))    # [] 0
```

---

# Methods of `list`

* What if there's nothing to remove?
  * Exception
  ```python
  L = ['A', 'B', 'C']
  L.remove('D')           # ValueError: list.remove(x): x not in list
  ```
* Try it!
  * use `try/except` to append `L` with `x` if `x` is not in `L`

---

# Methods of `list`

* `list.index(x)` to find the index of **(the first)** `x` in the list
  ```python
  L = ['A', 'B', 'C', 1, 2, 3, 'C']

  L.index('C')          # 2
  L.index('D')          # ValueError: 'D' is not in list
  ```

---

# `in` / `not in`

* `x in list` / `x not in list`
  * Check if `x` exists in the list
  ```python
  FIR = ['Faye', 'REAL', 'IAN']
  if 'Lydia' not in FIR:
      FIR.remove('Faye')
      FIR.append('Lydia')
  ```

---

# `is` & `is not`
* `L1 is L2` / `L1 is not L2`
  * Check if `L1` and `L2` is the same object

  ```python
  L1 = [1, 2, 3]
  L2 = [1, 2, 3]
  print(L1 is L2)       # False, why?

  L2 = L1
  print(L1 is L2)       # True, why?

  L2[0] = 999
  print(L1)             # [999, 2, 3], why?
  ```

---

# `==` & `!=`

* `L1 == L2` / `L1 != L2`
  * Check if the two lists are equal

```python
L1 = [1, 2, 3]
L2 = [1, 2, 3]
print(L1 == L2)       # True

L2 = L1
print(L1 == L2)       # True
```


---

# Methods of `list`

* `list.sort(key=None, reverse=False)` to sort the list
  * `key` specifies the key function
    * Every element `x` will be seen as `key(x)` when sorting.

  ```python
  L = [123, 32, 1, 1234567]
  L.sort()
  print(L)                  # [1, 32, 123, 1234567]

  L.sort(reverse=True)
  print(L)                  # [1234567, 123, 32, 1]

  L.sort(key=str)
  print(L)                  # [1, 123, 1234567, 32], why?
  ```

---

# Methods of `list`

* `list.reverse()` to revert the list
  * Equivalent to `list = list[::-1]`
* `list.copy()` returns a copy of the list
```python
L1 = [1, 2, 3]
L2 = L1
L3 = L1.copy()

print(L2 is L1, L3 is L1) # True False, why?

L2[0] = 69
L3[0] = 420
print(L1)                 # [69, 2, 3], why?
```

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

<!-- _class: lead -->
# `tuple`

---

# `tuple`

* A tuple is also a data container to store a set of data objects
* Similar to `list`, using an index to access an item of a tuple

```python
t = (1, 'two', [3, 4, 5])
print(t[0]) # 1
print(t)    # (1, 'two', [3, 4, 5])

t2 = 6, 7, 8
t3 = t, t2, (1, ) # (1, ) is a tuple with one element
``` 

---

# `tuple`

* `tuple` is immutable
  * Cannot change the value of an element
  * Cannot add or remove elements
  * Cannot sort or reverse

```python
t = 1, 2, 3
t[0] = 69420 # TypeError: 'tuple' object does not support item assignment
```

---

# `tuple`

* A tuple/list can be distributed to several variables.
  * The number of variables must match the number of elements in the tuple/list

```python
one, too, therr, fore, faife = 1, 2, 3, 4, 5
print(one, too, therr, fore, faife) # 1 2 3 4 5
```

---

# `enumerate`

* A function to get the index and the value of an iterable object
  * `enumerate(iterable, start=0)`
  * `start` specifies the starting index

```python
L = ['A', 'B', 'C', 'D']
for i, x in enumerate(L): # (i, x) is a tuple (index, value)
    print(i, x) 
# 0 A
# 1 B
# 2 C
# 3 D
```

---

# `zip`

* A function to combine two or more iterables into a list of tuples
  * `zip(iterable1, iterable2, ...)`
  * The length of the result is the length of the shortest iterable

```python
L1 = [28, 30, 32, 34]
L2 = ['A', 'B', 'C', 'D']

for x, y in zip(L1, L2):
    print(x, y)
# 28 A
# 30 B
# 32 C
# 34 D
```

---

<!-- _class: lead -->
# Exercises

---

# 1. 六千

* 某島國最近要發六千塊給他們的國民，
* 但為了維持效率，他們決定從北邊開始發，
* 請寫一個程式輸入一些 x 座標，請依照 x 座標由小到大印出。
```python
輸入： 9↵ 1↵ 7↵ 4↵ 3↵ 10↵ 5↵ 6↵ 2↵ 8↵ 
輸出： 1 2 3 4 5 6 7 8 9 10
```

![bg opacity:0.2](./figures/rich.jpg)

---

# 2. 緬甸的購物清單

* 阿靜最近想去緬甸旅遊購物，
* 請幫他寫一個購物清單系統吧！

```python
輸入：   買↵ 包包↵
        買↵ 鞋子↵
      不買↵ 包包↵
        買↵ 彩券↵
      結束↵
輸出：鞋子 彩券
```

![bg opacity:0.2](./figures/kk.jpg)

---

# 3. 傑寶模擬器

![bg opacity:0.2](./figures/robot_dancing.gif)

* 知名實況主 Rager 覺得最近觀眾數實在太少了
* 因此希望你幫他寫一個機器人，讓他可以用來當作聊天室
  1. 可以讓 Rager 不斷 **輸入訊息**
  2. 機器人每次都會依序回 `真假`，`確實`，`冷靜`，`亂講`，`有料` ...等
  3. 等 Rager 說出 `下播拉`，機器人就會回 `機油好難喝`，程式就結束了

---

# 4. エクスプロージョン

* 阿惠每天只能放一次名為 エクスプロージョン 的法術
* 為了確保每次都能命中，阿惠必須要先用內積計算他跟敵人的夾角
* 請寫一個程式，計算兩個向量的內積吧！

```python
a = [1, 2, 3]
b = [10, 20, 30]
輸出： 140
```

![bg opacity:0.3](./figures/Megumin.png)

---

# Acknowledgment

* Prof. Chang-Chieh Cheng. National Yang Ming Chiao Tung University, Taiwan
* [Python for Everybody](https://www.py4e.com/)