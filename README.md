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
