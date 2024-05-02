1.寫程式計算 1 ~ 100 中的所有奇數和

sum = 0 
for x in range(1, 101): 
    if x % 2 != 0:
        sum = sum + x 

print(sum) 
print('中四乙 409012387 林姵筠')


2.

sum = 0 
for x in range(1, 101): 
    if x % 2 == 0:
        continue
    sum = sum + x 

print(sum) 
print('中四乙 409012387 林姵筠')


3.

sum = 0
for x in range (1,101,2):
    sum = sum + x
    
print(sum)
print('中四乙 409012387 林姵筠')