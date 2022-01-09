## create a string literal "Hello, @mention!"
```python
"Hello, @donkeyLobster"
```
## print above literal
```python
print("Hello, @donkeyLobster")
```
## move @mention into a variable and turn literal into an f-string
```python
mention = "@donkeyLobster"
print(f"Hello, {mention}")
```
## wrap the whole code into a say_hello function and call it below
```python
def say_hello():
  mention = "@donkeyLobster"
  print(f"Hello, {mention}")
```
If you run this code you will get no output. This happenes because we made a function and put variable assignment and print inside function scope. But now in order to run what is inside the function we actually need to call it.
```python
def say_hello():
  mention = "@donkeyLobster"
  print(f"Hello, {mention}")

say_hello()
```

## make @mention a parameter to a function and pass the string literal value in the call
```python
def say_hello(mention):
  print(f"Hello, {mention}")

user = "@donkeyLobster"
say_hello(user)
```

## change print statement to a return value, return that value to a variable and print the result
```python
def say_hello(mention):
  return f"Hello, {mention}"

user = "@donkeyLobster"
result = say_hello(user)
print(result)
```
