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
## Exercises

Evan Chang

---

# 1. 張氏數列

* 跟費氏數列有一點像
  * 第一個數字為 `69`
  * 第二個數字為 `420`
  * 第三個數字開始為前兩個數字的和
```
69 420 489 909 1398 2307 ...
```

---

# 2. 猜合數遊戲

* 跟猜數字遊戲 和 判斷質數有一點像
* 隨機決定一個 $[1, 100]$ 的合數當答案
* 每輪可以猜最多 $10$ 次
```
剩 10 次！猜 [1, 100]：50
剩 9 次！猜 [1, 49]：25
剩 8 次！猜 [26, 49]：38
喔不，你猜到我的合數了！
```

---

# 3. 更相減損術

* 跟輾轉相除法有一點像
* 記載見於《九章算術》方田章約分術，可以求出一個分數的分子、分母的最大公因數，其步驟如下：
    ```
    約分術曰：可半者半之；不可半者，副置分母、子之數，以少減多，更相
    減損，求其等也。以等數約之。
    ```
  1. `可半者半之` - 兩個數可同時除 $2$ 就除
  2. `不可半者，以少減多，更相減損` - 不停大數減去小數
  3. `求其等也` - 相等就結束

---

# 3. 更相減損術

```
大數 260 | 小數 104
------------------
    130 |       52 <- 可半者半之
     65 |       26 <- 可半者半之
     39 |       26 <- 以少減多
     13 |       26 <- 以少減多
     26 |       13 <- 更相減損
     13 |       13 <- 以少減多，求其等也

答案：2*2*13 = 52
```

---

# 4. 印倒三角形

* 跟印三角形有一點像
* 印出一個 $5$ 層的倒三角形
    ```
    *********
     *******
      *****
       ***
        *
    ```