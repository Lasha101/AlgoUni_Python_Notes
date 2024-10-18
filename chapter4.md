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











