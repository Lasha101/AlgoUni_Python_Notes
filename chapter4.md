# **რა არის გამონაკლისი!**
გამონაკლისი პითონში არის შეცდომა რომელსიც თავს იჩენს პროგრამის აღსრულების დროს და რომელიც წყვეტს პროგრამაში გაწერილი ინსტრუქციების ჯაჭვს. იმის ნაცვლად რომ პროგრამა "გაიჭედოს" პითონი, try/except კონსტრუქციის გამოყენებით, საშუალებას გვაძლევს რომ ვმართოთ შეცდომა ისე რომ პროგრამამ გააგრძელოს ნორმალური ფუნქციონირება.

# **სხვასახვა სტრუქტურის გამონაკლისები**

1)
```
try:
  instruction_1
  instruction_2
  ... ... ...
  last instruction
except Exception:
  print(error_message)
```
თუ ბოლო ინსტრუქცია აღსრულდება კოდის აღსრულება გაწყდება და აღარ მოხდება გამონაკლისის "გასროლა".

2)
```
try:
  instruction_1
  instruction_2
  ... ... ...
  instruction_n
except Exception:
  print(error_message)
else:
  last instruction
```
თუ  instruction_n აღსრულდება, except ბლოკის გამოტოვების შემდეგ აღსრულდება ბოლო ინსტრუქცია.

3)

```
try:
  instruction_1
  instruction_2
  ... ... ...
  instruction_n
except Exception:
  print(error_message)
else:
  last instruction
finally:
  always instruction
```
finally ბლოკის ინსტრუქცია აღსრულდება ნებისმიერ შემთხვევაში იმისგან დაოუკიდებლად რა მოხდება მანამდე try/except ბლოკში.

4)

```
if condition:
  raise Exception
```
ასეთი სახის ჩანაწერი საშუალებას გვაძლევს წამოვწიოთ-გავისროლოთ გამონაკლისი რაღაც პირობის დადგომის შემთცვევაში და პირობის განსაზღვრა აბსოლუტურად ჩვენზეა დამოკიდებული. ამ კონსტრუქციის გამოვენება შეგვიძლია როგორც ცალკე ასევე try/except ერთადაც:

5)

```
try:
  instruction_1
  instruction_2
  if condition:
    raise Exception(error_message)
  ... ... ...
  instruction_n
except Exception as e:
  print(e)
else:
  last instruction
finally:
  always instruction
```
ამ შემთხვევაში e არის ლოკალური ცვლადი რომელიც უზრუნველყოფს შეცდომის შეტყობინების გამობეჭდვას.

6)

რამოდენიმე სვადასხა გამონაკლისის შემთხვევაში შეგვიძლია სხვადასხვა კონსტრუქციები გამოვიყენოთ:

```
try:
  instruction_1
  instruction_2
  ... ... ...
  instruction_n
except Exception_1:
  print(error_message_1)
except Exception_2:
  print(error_message_2)
... ... ... ... ...:
  ... ... ... ... ...
except Exception_n:
  print(error_message_n)
else:
  last instruction
finally:
  always instruction
```
ან 
```
try:
  instruction_1
  instruction_2
  ... ... ...
  instruction_n
except (Exception_1, Exception_2, ... ... ..., Exception_n):
  print(error_message)
else:
  last instruction
finally:
  always instruction
```
# **ხშირად შეხვედრილი გამონაკლისები**

1)
IndentationError

არასწორი ჩანაწერი:
```
def greet():
print("Hello, world!")

greet()
```
სწორი ჩანაწერი:

```
def greet():
    print("Hello, world!")

greet()
```
2)
IndexError

არასწორი ჩანაწერი:
```
my_list = [1, 2, 3]

print(my_list[3])
```
სწორი ჩანაწერი:

```
my_list = [1, 2, 3]

print(my_list[2])
```
3)
KeyError

არასწორი ჩანაწერი:
```
my_dict = {'name': 'Alice'}
print(my_dict['age'])  
```
სწორი ჩანაწერი:
```
my_dict = {'name': 'Alice'}
print(my_dict['name'])  
```
4)
KeyboardInterrupt

უსარულო ციკლი:
```
while True:
    pass  
```
გაშვების შემდეგ გასაჩერებლად დააჭირეთ:

"ctrl + c"

5)
NameError

არასწორი ჩანაწერი:
```
print(x)
```
სწორი ჩანაწერი:
```
x = "Hello, Algouni"

print(x)
```
6)
SyntaxError

არასწორი ჩანაწერი:
```
if True
    print("Hello!")
```
სწორი ჩანაწერი:
```
if True:
    print("Hello!")
```
7)
TypeError

არასწორი ჩანაწერი:
```
x = "hello"
y = 5
print(x + y)
```
სწორი ჩანაწერი:
```
x = "hello"
y = " 5"
print(x + y)
```
8)
ValueError

არასწორი ჩანაწერი:
```
x = int("one hundred twenty-three") 
print(x)
```
სწორი ჩანაწერი:
```
x = int("123") 
print(x)
```
9)
ZeroDivisionError

არასწორი ჩანაწერი:
```
x = 10 // 0

print(x)
```
არასწორი ჩანაწერი:
```
x = 10 // 5

print(x)
```
10)
IOError

არასწორი ჩანაწერი:
```
try:
    file = open('non_existent_file.txt', 'r') 
except IOError:
    print("File not found or can't be opened.")
```
სწორი ჩანაწერი:
```
try:
    file = open('existent_file.txt', 'r') 
except IOError:
    print("File not found or can't be opened.")
```


