# Learn-Python version 3.12.4

## IDE
* [PyCharm Community Edition version 2024.1.4](https://www.jetbrains.com/pycharm/download/?section=windows) - Version free

## 1.1 Nhập xuất

## Example 1
```python
print("Hello World")
```
Actual result:
```txt
Hello World
```

## Example 2
```python
print("Hello World, \nDuyên")
```
Actual result:
```txt
Hello World, 
Duyên
```

## Example 3
```python
name = input("Tell me your name: ")
print("Hello ", name)
```
Actual result:
```txt
Tell me your name: Duyen
Hello  Duyen
```

## Example 4
```python
numberInteger = int(input("Enter a number: "))
print(numberInteger)
```
Actual result:
```txt
Enter a number: 9
9
```

## Example 5
```python
numberFloat = float(input("Enter a number float: "))
print(numberFloat)
```
Actual result:
```txt
Enter a number: 9.5
9.5
```

## Example 6
```python
name = "Duyen"
age = 30

print(f"Hello {name} ! I'm {age} years old")
```
Actual result:
```txt
Hello Duyen ! I'm 30 years old
9.5
```

## Example 7
```python
n = int(input("Enter a number: "))
print(n % 2 == 0)
```
Actual result 1:
```txt
Enter a number: 5
False
```

Actual result 2:
```txt
Enter a number: 8
True
```

## Example 8
```python
n = int(input("Enter a number: "))
print(n % 3 == 0 and n >= 50 and n <= 100)
```
Actual result 1:
```txt
Enter a number: 75
True
```
## Example 9
Hoán vị 2 số

```python
a = 3
b = 4

a, b = b, a
print("{} {}".format(a,b))
```

Actual result
```txt
4 3
```

## 1.2 Cấu trúc điều kiện

## Example 1
```python
number = int(input("Enter a number: "))
if (number % 2 ==0):
    print(number, 'is even number')
else:
    print(number, 'is odd number')
print("End program!")
```
Actual result 1:
```txt
Enter a number: 8
8 is even number
End program!
```

Actual result 2:
```txt
Enter a number: 5
5 is odd number
End program!
```

## Example 2
```python
math = float(input("Enter a math score: "))
physics = float(input("Enter a physics float: "))
chemistry = float(input("Enter a chemistry float: "))

averageScore = (math + physics + chemistry) / 3

if(averageScore >= 8):
    print(averageScore,"Excellent")
elif(averageScore < 8 and averageScore >= 6.5):
    print(averageScore, "Good")
elif (averageScore < 6.5 and averageScore >= 5.0):
    print(averageScore, "Need to work hard")
elif (averageScore < 5.0 and averageScore >= 3.5):
    print(averageScore, "Bad score")
else:
    print(averageScore, "You must learn again!")
```
Actual result 1:
```txt
Enter a math score: 6.5
Enter a physic float: 7.0
Enter a chemitry float: 8.5
7.333333333333333 Good

```

Actual result 2:
```txt
Enter a math score: 5.0
Enter a physics float: 6.5
Enter a chemistry float: 5.5
5.666666666666667 Need to work hard
```

## Example 3
```python
month = int(input("Enter a month: "))
year = int(input("Enter a year: "))

if month in(1,3,5,7,8,10,12):
    print("Month", month, "has 31 days")
elif month in(4,6,9,11):
    print("Month", month, "has 30 days")
elif month == 2:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("Month", month, " has 29 days")
    else:
        print("Month", month, " has 28 days")
else:
    print("The month is invalid!")
```
Actual result:
```txt
Enter a month: 5
Enter a year: 2024
Month 5 has 31 days
```

## 1.3 Vòng lặp for

## Example 1
```python
for item in range(5):
    print(item)
```
Actual result:
```txt
0
1
2
3
4
```

## Example 2
```python
for item in range(1, 5):
    print(item)
```
Actual result:
```txt
1
2
3
4
```

## Example 3
```python
for item in range(0, 10, 2):
    print(item)
```
Actual result:
```txt
0
2
4
6
8
```

## Example 4
```python
for item in 'Python':
    print(item)
```
Actual result:
```txt
P
y
t
h
o
n
```

## Example 5
```python
for item in ["orange", "apple", "cherry"]:
    print(item)
```
Actual result:
```txt
orange
apple
cherry
```

## Example 6
```python
for item in [11,50,21,56,100]:
    print(item)
```
Actual result:
```txt
11
50
21
56
100
```

## Example 7
S = 1 + 2 + ... + n
```python
n = int(input("Enter a number: "))
s = 0
for i in range(1, n + 1):
    s += i
print(s)
```
Actual result:
```txt
Enter a number: 5
15
```

## Example 8
```python
s = 0
for item in [11,50,21,56,100]:
    s += item
print(f"Result:{s}")
```
Actual result:
```txt
Result:238
```

## 1.4 Vòng lặp while

## Example 1
Nhập số nguyên dương liên tục, nếu nhập số âm sẽ dừng chương trình

```python
n = 1
while True:
    if (n < 0):
        break
    else:
        n = int(input("Enter a number: "))
```
Actual result:
```txt
Enter a number: 5
Enter a number: 0
Enter a number: 12
Enter a number: 34
Enter a number: -1
```
## Example 2
Tạo 1 menu lựa chọn

```python
select = 0
while select != 4:
    print("***** MENU *****")
    print("1.Add item")
    print("2.Read items")
    print("3.Edit item")
    print("4.Delete item")
    select = int(input("Enter a number: "));

    if select == 1:
        print("You have chosen to add items")
    elif select == 2:
        print("You have chosen to read items")
    elif select == 3:
        print("You have chosen to edit items")
    elif select == 4:
        print("You have chosen to delete items")
    else:
        print("The choice is invalid!")
        break
print("End program!")
```
Actual result:
```txt
***** MENU *****
1.Add item
2.Read items
3.Edit item
4.Delete item
Enter a number: 1
You have chosen to add items
***** MENU *****
1.Add item
2.Read items
3.Edit item
4.Delete item
Enter a number: 2
You have chosen to read items
***** MENU *****
1.Add item
2.Read items
3.Edit item
4.Delete item
Enter a number: 5
The choice is invalid!
End program!
```

## Example 3
S = 1 + 2 + ... + n

```python
n = int(input("Enter a number: "))
s = 0
i = 1
while (i <= n):
    s += i
    i+=1
print(s)
```
Actual result:
```txt
Enter a number: 5
15
```

## Example 4
Tổng só lẻ, tổng số chẳn

```python
n = int(input("Enter a number: "))
sumOdd = 0
sumEven = 0
i = 1
while (i <= n):
    if (i % 2 != 0):
        sumOdd += i
    else:
        sumEven += i
    i+=1
print("Sum odd =", sumOdd)
print("Sum even =", sumEven)
```
Actual result:
```txt
Sum odd = 9
Sum even = 6
```

## 1.5 Vòng lặp for lồng nhau

## Example 1
```python
for i in range(2):
    for j in range(1,4):
        print(f"({i},{j})")
print("Done!")
```
Actual result:
```txt
(0,1)
(0,2)
(0,3)
(1,1)
(1,2)
(1,3)
Done!
```

## 1.6 Mảng 1 chiều

## Example 1
Tạo 1 mảng random
```python
import random

n = int(input("Enter the number of elements: "))
arr = [0]*n
for i in range(n):
    arr[i] = random.randrange(0, 101)
print(arr)
```

Actual result:
```python
Enter the number of elements: 10
[100, 52, 33, 11, 85, 61, 82, 57, 21, 7]
```

## Example 2
Thêm vào cuối mảng
```python
numbers = [5,2,1,7,4]
numbers.append(20) 
print(numbers)
```

Actual result:
```python
[5, 2, 1, 7, 4, 20]
```

## Example 3
Thêm vào đầu mảng
```python
numbers = [5,2,1,7,4]
numbers.insert(0,10)
print(numbers)
```

Actual result:
```python
[10, 5, 2, 1, 7, 4]
```

## Example 4
Xóa 1 phần tử trong mảng
```python
numbers = [5,2,1,7,4]
numbers.remove(2)
print(numbers)
```

Actual result:
```python
[5, 1, 7, 4]
```

## Example 5
Xóa 1 phần tử cuối mảng
```python
numbers = [5,2,1,7,4]
numbers.pop()
print(numbers)
```

Actual result:
```python
[5, 1, 7]
```

## Example 5
Xóa tất phần tử trong mảng
```python
numbers = [5,2,1,7,4]
numbers.clear()
print(numbers)
```

Actual result:
```python
[]
```

## Example 6
Kiểm tra phần tử có tồn tại trong mảng hay không ?
```python
n = 9
isExisted = n in [1, 2, 3, 4]
print(n, "is not existed in arr")
```

Actual result:
```python
9 is not existed in arr
```

## Example 7
Tìm số lớn nhất trong mảng

```python
arr = [33,45,18,4,90,55,38,2]
max = min = arr[0]

for item in arr:
    if(item > max):
        max = item
    else:
        min = item
print("Max value: ", max)
print("Min value: ", min)
```

Cách gọn hơn:
```python
print("Max value: ", max([33,45,18,4,90,55,38,2]))
print("Min value: ", min([33,45,18,4,90,55,38,2]))
```

Actual result:
```python
Max value:  90
Min value:  2
```

## Example 8
Đếm tần xuất số xuất hiện
```python
arr = [33,45,18,4,90,55,38,2,18,100]

for item in arr:
    count = arr.count(item)
    print(item, "is displayed", count, "times in list")
```

Actual result:
```txt
33 is displayed 1 times in list
45 is displayed 1 times in list
18 is displayed 2 times in list
4 is displayed 1 times in list
90 is displayed 1 times in list
55 is displayed 1 times in list
38 is displayed 1 times in list
2 is displayed 1 times in list
18 is displayed 2 times in list
100 is displayed 1 times in list
```

## Example 9
Sắp xếp tăng dần

Cách 1:

```python
a = [33,45,18,4,90,55,38,2,18,100]
n = len(a)

for i in range(n):
    for j in range(0, n-i-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
print("Sort ascending:", a)
```

Cách 2: gọn hơn

```python
a = [33,45,18,4,90,55,38,2,18,100]
a.sort()
print("Sort ascending:", a)
```

Actual result:

```python
[2, 4, 18, 18, 33, 38, 45, 55, 90, 100]
```
## Example 10
Sắp xếp giảm đân
```python
a = [33,45,18,4,90,55,38,2,18,100]
a.sort()
a.reverse()
print("Sort descending:", a)
```

Actual result:

```python
Sort ascending: [100, 90, 55, 45, 38, 33, 18, 18, 4, 2]
```

## Example 11
Loại bỏ các phần tử bị trùng nhau trong mảng

```python
numbers = [2,2,4,6,3,4,6,1]
uniques = []

for item in numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)
```

Actual result:
```python
[2, 4, 6, 3, 1]
```

## Author
By Ngô Thị Kim Duyên - 2024
