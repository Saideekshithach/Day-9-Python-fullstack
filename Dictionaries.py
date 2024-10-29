Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#dict{}
a={"name":"Deekshi","year":2024,"month":10}
print(a)
{'name': 'Deekshi', 'year': 2024, 'month': 10}
type(a)
<class 'dict'>
b={4,5,6,7,8}
print(b)
{4, 5, 6, 7, 8}
type(b)
<class 'set'>
a={"course":"python","year":2024,"month":10}
a.keys()
dict_keys(['course', 'year', 'month'])
a.values()
dict_values(['python', 2024, 10])
a.items()
dict_items([('course', 'python'), ('year', 2024), ('month', 10)])
a["course"]
'python'
#accessing items
a={"name":"deekshi","date":29,"month":10,"time":11,"date":29}
b=a.copy()
b
{'name': 'deekshi', 'date': 29, 'month': 10, 'time': 11}
a={"name":"deekshi","date":29,"month":10,"time":11,"date":29}
a.update({"year":2024})
a
{'name': 'deekshi', 'date': 29, 'month': 10, 'time': 11, 'year': 2024}
a.update({"course":"python","place":"vja"})
a
{'name': 'deekshi', 'date': 29, 'month': 10, 'time': 11, 'year': 2024, 'course': 'python', 'place': 'vja'}
a.update({"course":"python"},{"place":"vja"})
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    a.update({"course":"python"},{"place":"vja"})
TypeError: update expected at most 1 argument, got 2
#setdefault(
#setdefault()
a={"year:2025,"month":1}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"year":2025,"month":1}SyntaxError: unterminated string literal (detected at line 1)
   
SyntaxError: invalid syntax
a={"year":2025,"month":1}
   
a.setdefault("name","Deekshi")
   
'Deekshi'
a
   
{'year': 2025, 'month': 1, 'name': 'Deekshi'}
#pop()
   
a={"course:"python","place":"vja"}
   
SyntaxError: unterminated string literal (detected at line 1)
a={"course":"python","place":"vja"}
   
a.pop("place")
   
'vja'
a
   
{'course': 'python'}
#popitem
   
a={"course":"python","place":"vja"}
   
a.popitem()
   
('place', 'vja')
a
   
{'course': 'python'}
#get()
   
a.get("course")
   
'python'
a
   
{'course': 'python'}
a.clear()
   
a
   
{}
#setdefault()
   
a={"year":2025,"month":1}
   
a.setdefault("name","deekshi")
   
'deekshi'
a
   
{'year': 2025, 'month': 1, 'name': 'deekshi'}
a.setdefault("apple","fruit")
   
'fruit'
a
   
{'year': 2025, 'month': 1, 'name': 'deekshi', 'apple': 'fruit'}
a[0]
   
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    a[0]
KeyError: 0
#pop()
   
a={"place":"hyd","year":2025,"month":1}
   
a.pop()
   
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    a.pop()
TypeError: pop expected at least 1 argument, got 0
>>> a.pop(1)
...    
Traceback (most recent call last):
  File "<pyshell#53>", line 1, in <module>
    a.pop(1)
KeyError: 1
>>> a.pop("year")
...    
2025
>>> a
...    
{'place': 'hyd', 'month': 1}
>>> a={"course":"python","place":"codegnan"}
...    
>>> a.popitem("course")
...    
Traceback (most recent call last):
  File "<pyshell#57>", line 1, in <module>
    a.popitem("course")
TypeError: dict.popitem() takes no arguments (1 given)
>>> a,popitem()
...    
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    a,popitem()
NameError: name 'popitem' is not defined
>>> a.popitem()
...    
('place', 'codegnan')
>>> a
...    
{'course': 'python'}
>>> a.clear()
...    
>>> a
...    
{}
