# **რა არის ტესტირება?**
ტესტირება გულისხმობს ფუნქციებად ჩაშლილი კოდის ფუნქციებისთვის შესაბაშისი ტესტ-ფუნქციების წერას, რომლებიც ამოწმებენ აბრუნებენ თუ არა ფუნქციები ტესტ-ფუნქციების მიერ ნავარაუდებ აუთფუთს მოცემული ინფუთისთვის.

# **ფაილური სტრუქტურა pytest-ისთვის**
pytest-ი არის პითონის ბიბლიოთეკა რომელიც გვეხმარება ჩვენი კოდის გატესტვაში, საუბარია პატარ-პატარა ტესტების ავტომატურად გაშვებაზე მოცემული ფაილური სტრუქტურის ფარგლებში:
```
Your_Testing_Folder
  -> your_code_file.py
  -> test_your_code_file.py
```
ფოლდერში გვაქვს ფაილი რომლშიც ფუნქციებად ჩაშლილი კოდი გვიწერია და იმავე ფოლდერში ჩვენი ფაილის გვერდით გვაქვს ტესტ-ფაილი რომელშიც გამტესტავი ფუნქციები გვაქვს გაწერილი.

code_file.py:
```
def my_function_1(var):
  instruction_1(... var ...)
  instruction_2(... instruction_1 ...)
    instruction_3(var ... instruction_2)
      return instruction_3

def my_function_2():
  var = input("Enter your value: ")
  instruction_1(... var ...)
  instruction_2(... instruction_1 ...)
    instruction_2(var ... instruction_3)
      return instruction_2

def my_function_3(my_var as my_function_1(var))):
  if not my_var.isdigit():
    raise Exception
  return instruction_1(int(my_var())

def main():
  user_input = input("Enter your value: ")
  my_var = my_function_1(user_input)
  print(my_function_2())
  new_var = my_function_3(my_var)
  print(f"The result for given value is {new_var}")

if __name__=="__main__":
  main()
```
test_code_file.py:
```
from code_file import my_function_1, my_function_2, my_function_3

def test_my_function_1():
  assert my_function_1(var as concret value_1) == result_1
  assert my_function_1(var as concret value_2) == result_2
  assert my_function_1(var as concret value_3) == result_3

from unittest.mock import patch

def test_my_function_2():
  mock_answer = value as simulated value ramplacing input's returned value within the function's scope
  with patch('builtins.input', return_value=2):
  result = my_function_2()
  assert result == 4

import pytest

def test_my_function_3():
  with pytest.raises(Exception):
    my_function_3(1.5)
    my_function_3("half")
    my_function_3("Hi!")
```
!!! ჩვენი კოდის ფაილიდან ჩვენს გამტესტავ ფაილში აუცილებლად უნდა დავაიმპორტოთ ყველა ის ფუნქცია რომლის გატესტვასაც ვაპირებთ

!!! აუცილებლად უნდა დავაინსტალიროთ და ტესტ-ფაილში დავაიმპორტოთ ყველა ის საშუალება რასაც ტესტებში გამოვიყენებთ

!!! ტესტ ფუნქციის გასაზღვრისას ფუნქციის სახელწოდებაში აუცილებლად უნდა ფიგურირებდეს სიტყვა "test" რომ pytest-მა შეძლოს მათი პოვნა და გაშვება

!!! ტესტ ფუნქციის განსაზღრისას ფუნქციის სხეულში(სქოუფში) გაწერილი ტესტ-ქეისებს pytest-ი აღიქვამს როგორც ერთ ტესტს, უმჯობესია თუ სხვადასხვა სახის ტესტ-შემთხვევებს სხვადასხვა ტესტ-ფუნქციებში დავაჯგუფებთ ასეთნაირად ტესტი უფრო გასაგები გახდება და ერორის პოვნაც გაგვიადვილდება!

ცალ-ცალკე განვიხილოთ my_function_1, my_function_2 და my_function_3-ის გატესტვის შემთხვევები pytest მოდულის გამოყენებისას
pytest მოდული ძალიან მოსახერხებელია პატარ-პატარა ტესტების წერისას

my_function_1-ის შემთხვევაში განვსაზღვრავთ test_my_function_1 ფუნქციას test_code_file.py-ში და სქოუფში "assert" ქივორდის გამოყენებით ვეძახით code_file.py-დან დაიმპორტებულ my_function_1-ს და არგუმენტად გადავცემთ კონკრეტულ მნიშვნელობას და ორმაგი ტოლობის მარჯვენა მხარეს ვუწერთ შედეგს რომლის დაბრუნებასაც ფუნქციისგან ველოდებით იმ შემთხვევაში როცა ფუნქცია გამართულად მუშაობს. ამ შემთხვევაში ლაპარაკი გვაქვს ისეთი ფუნქციის გატესტვაზე რომელიც რაიმეს აიღებს ინფუთად და რაიმეს დაგვიბრუნებს აუთფუთად!


my_function_2-ის შემთხვევაში განვსაზღვრავთ test_my_function_2 ფუნქციას test_code_file.py-ში. იმის გათვალისწინებით რომ ფუნქცია ინფუთად არაფერს ღებულობს დაგვიჭირდება mock მოდულიდან patch() ფუნქციის დაიმპორტება, რომლის გამოყენებითაც მოვახდენთ ფუნქციის სქოუფში გამოძახებული input() ფუნქციის მიერ დაბრუნებული შედეგის სიმულაციას my_function_2-ის და "assert" ქივორდის გამოყენებით გავაკეთებთ შედარებას my_function_2-ის დაბრუნებულ შედეგს და ნავარაუდებ შედეგს შორის. ამ შემთხვევაში ლაპარაკი გვაქვს ისეთი ფუნქციის გატესტვაზე რომელიც ინპუთად არაფერს ღებულობს მაგრამ აბრუნებს აუთფუთს!


my_function_3-ის შემთხვევაში განვსაზღვრავთ test_my_function_3 ფუნქციას test_code_file.py-ში. იმის გათვალისწინებით რომ ფუნქციამ არასწორი ინფუთის შემთხვევაში Exception-ზე უნდა გავიდეს დაგვიჭირდება pythest მოდულის ფუნქციის დაიმპორტება, რაც with გამოყენებით საშუალებას მოგვცემს შევამოწმოთ გადის თუ არა my_function_3 Exception-ზე არასწორი ინფუთის შემთხვევაში. ლაპარაკი გვაქვს მომხმარებლის მხრიდან ფუნქციისთვის არასწორი ტიპის მნიშვნელობის გადაცემაზე!




