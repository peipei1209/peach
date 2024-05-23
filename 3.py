1.請寫一個函式 compare_value(x, y)，比較參數 x 和 y 的大小，若 x 大於 y 則回傳 1；若 x 等於 y 則回傳 0；若 x 小於 y 則回傳 -1。

def compare_value(x, y):
    if x > y:
        return 1
    elif x == y:
        return 0
    else:
        return -1
print(compare_value(6, 8))    
print(compare_value(8, 8))
print(compare_value(8, 6))



2.請撰寫一個程式，呼叫一個自訂的函式 f(x, n)，計算一個整數 x 的 n 次方。

def f(x, n):
    return x ** n
print (f(3, 4))



3. 請寫一個 `is_odd(x)` 函式，檢查輸入的參數 `x` 是不是奇數。如果 `x` 是奇數則回傳 `Ture`；若 `x` 不是奇數則回傳 `False`。

def is_odd(x):
    if x % 2 == 1:
        return True
    else:
        return False
print(is_odd(13))
print(is_odd(96))


或

def is_odd(x):
    return x % 2 == 1

中四乙 409012387 林姵筠