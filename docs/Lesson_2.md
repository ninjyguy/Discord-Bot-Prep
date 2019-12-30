# String Manipulation
## Let's compare strings
```python
first_one = "ONE"
second_one = "one"
third_one = " One "
fourth_one = "one"
fifth_one = "One"
```
## compare first and second
```python
print(first_one == second_one)
```
## compare second and fourth
```python
print(second_one == fourth_one)
```
## compare third and fifth
```python
print(third_one == fifth_one)
```
## lets clean up "   /chatbot do dishes   "
```python
print("   /chatbot do dishes   ".strip())
```
You can also take off the left or right spaces with .lstrip or .strip
```python
print("   /chatbot do dishes   ".lstrip())

print("   /chatbot do dishes   ".rstrip())
```
## lower case a string
```python
print("/CHATBOT DO DISHES".lower())
```
## upper case a string
```python
print("/chatbot do dishes".upper())
```
## split a string to get individual words in it
```python
print("!play rock".split(" ")[1])
```
## find if string starts with "/chatbot"
```python
not_important = "This string is not important."
very_important = "/chatbot This is very important to capture"
```
If (Variable) starts with /chatbot, then...
```python
if not_important.startswith("/chatbot"):
    print("This string starts with /chatbot")
else:
    print("This string does not start with /chatbot")

if very_important.startswith("/chatbot"):
    print("This string starts with /chatbot")
else:
    print("This string does not start with /chatbot")
```
# find if a substring is IN a string
```python
good_one = "This string is very good for you."
bad_one = "This string is terribly bad for you."
```
If variable contains the word (good/bad), then...
```python
if "good" in good_one:
    print("This string is all good")
else:
    print("This string is bad")

if "bad" in bad_one:
    print("This string is bad")
else:
    print("This string is all good")
```