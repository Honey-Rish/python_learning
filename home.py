Python 3.10.4 (tags/v3.10.4:9d38120, Mar 23 2022, 23:13:41) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
list=[1,3,0.3,'cherry']
print(list)
[1, 3, 0.3, 'cherry']
print(list[2])
0.3
print(list[1:3])
[3, 0.3]

print(list.append(10))
None

list[0]=25
print(list)
[25, 3, 0.3, 'cherry', 10]
