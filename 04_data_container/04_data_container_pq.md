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

![bg opacity:.3](https://cdn.pocket-lint.com/r/s/660x/assets/images/156343-apps-news-feature-best-suez-canal-memes-image6-sb0tykntw7-jpg.webp?v1)

<!-- _class: lead -->
# Pop Quiz: 
# 長榮的船卡了幾天？

---

# Methods of `list`

* `list()` or `[]` to declare a list.
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
    * Every element `x` will be seen as`key(x)` when sorting.

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
# Exercises

---

# 1. 學妹模擬器

* 上了大學的阿群發現學妹都不想理他
* 於心不忍的你決定要幫他寫一個學妹模擬器
  1. 可以不斷讓阿群**輸入訊息**跟學妹說話
  2. 學妹每次都會隨機回 `恩恩`，`哈哈`，`是喔` ...等話
     * 但是為了不要讓阿群發現，每次回覆不可以跟上次一樣
  3. 等阿群說出 `我喜歡你` 告白後，學妹就會說 `哈哈學長我先去洗澡囉`，程式就結束了

---

# 2. DD黨

![bg opacity:.3](https://img.4gamers.com.tw/ckfinder/images/ALIEN/2021-1/maxresd213efault.jpg?versionId=Kmz4sadnKzhhuFKgyTuOes3KgyKq8eCZ)

* 最近阿群愛上了看 Vtuber，並成為了不折不扣的 DD 黨
* 但是每次 Vtuber 們直播的時候，他都因為打字太慢跟不上聊天室
* 寫個程式自動幫他產生 $20$ 份下面的留言吧：
  ```
  潤羽露西婭我婆！
  兔田佩克拉我婆！
  寶鐘瑪琳我婆！
  噶嗚古拉我婆！
  湊阿庫婭我婆！
  ```

---

# 3. 時間鉗形攻勢

* 阿群朋友被找去打一場仗，但是有些敵人都是倒著走過來的
* 他把他們講的話記錄了起來，發現好像都是迴文
  * 迴文 - palindrome：翻轉後還是保持相同
* 寫一個程式自動判斷一個 `list` 是不是迴文吧
  ```python
  # palindromes
  L = [1, 2, 3, 2, 1]
  L = [1, 2, 1]
  L = [1]

  # not palindromes
  L = [1, 2 ,3]
  ```