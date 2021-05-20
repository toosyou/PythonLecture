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
## 03. Iteration Statements

Evan Chang

---

# `while`

* Syntax
    ```python
    while statement:
        indented_statements
    ```

* Example
    ```python
    n = int(input('Input a positive integer: '))
    while n > 0:
        print(n)
        n -= 1
    ```

---

# `while`

* More examples
  * `n!`
    ```python
    n = 10
    factorial = 1
    while n > 0: # n, n-1 ... 1
        factorial *= n
        n -= 1
    print('n! is', factorial)
    ```

---

# `while` - `continue` & `break`

```python
while True:
    sentance = input('I\'ll repeat after you: ')
    print(sentance)
    if sentance != 'quit':
        continue
    break
```

---

# `for`