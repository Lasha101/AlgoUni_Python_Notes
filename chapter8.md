# **რას გულისხმობს ობიექტზე მიმართული პროგრამირება?!**
ობიექტზე მიმართული პროგრამირება გულისხმობს ისეთი კოდის წერას რომელიც ორგანიზებულია კლასების მიხედვით შექმნილი ობიექტების ირგვლივ.

# **რა არის კლასი?!**
ზოგადი წარმოდგენის დონეზე კლასი არის ყალიბივით, რომელიც აერთიანებს ამ ყალიბის მიხედვით შექმნილ ნივთებს თუმცა ნივთები თავის მხრივ შეიძლება განსხვავდებოდნენ ერთმანეთისგან. კლასი არის ნიმუშივით რომლის მიხედვითაც შვენ შეგვიძლია შევქმნათ კონკრეტული ობიექტები.
პითონში კლასი არის ინკაფსულაციის საშუალება. ინკაფსულაცია შეგვიძლია გავიგოთ როგორც გამოცალკევება-კაფსულაში მოქცევა, ლაპარაკია მონაცემების და ფუნქციონალის გამოცალკევებაზე. 

```
class MyClass:
  ...
    data
  ...
    functions
```
კლასის შექმნა შეგვიძლია class ქივორდის გამოყენებით.

# **რა არის ობიექტი?!**
ობიექტი არის კლასის ინსტანციაციის შედეგად შექმნილი ინსტენსი ანუ კლასის სტრუქტურის კონკრეტული განხორციელება-კლასის კერძო შემთხვევა.
ობიექტი = ინსთენსს.
```
my_class = MyClass()
```
ინსტანციაციის შედეგად შევქმენით my_class ობიექტი.

# **რა არის ატრიბუტი?!**
ატრიბუტი არის მონაცემი რომელიც ახასიათებს კლასს ან ამ კლასის მიხედვით შექმნილ ობიექტს.
კლასის ატრიბუტი არის კლასის ცვლადი როგორც ველი რომლისთვის მინიჭებული მნიშვნელობის ცვლილებაც ცვლის ამ კლასის მიხედვით შექმნილი ყველა ობიექტის მდგომარეობას, ხოლო ინსთენს ატრიბუტი არის ინსთენს ცვლადი როგორც ველი რომლისთვის მინიჭებული მნიშვნელობის ცვლილებაც ცვლის ამ კლასის მიხედვით შექმნილი კონკრეტული ობიექტის მდგომარეობას
კლასის და ინსთენს ატრიბუტები:
```
class MyClass:
  class_attribute = data_1
  ...
    instance_attribute = data_2
  ...
  functions
```
class_attribute არის კლასის ატრიბუტი ხოლო instance_attribute არის ობიექტის ატრიბუტი. კლასში ობიექტისთვის ატრიბუტების მისანიჭებლად უნდა განვსაზღვროთ ფუნქცია "def __ init __(self):" რომლის სქოუფშიც შეგვიძლია გავწეროთ ინსთენსის ცვლადები "self" სიტყვის გამოყენებით:
```
class MyClass:
  class_attribute = data
  def __ init __(self, data_1, data_2, data_3, ...):
    self.attribute_1 = data_1
    self.attribute_2 = data_2
    self.attribute_3 = data_3
    self.attribute_... = ...
  ...
  functions
```
"def __ str __(self):" ფუნქციის განსაზღვრით ჩვენ შეგვიძლია კლასს სტრინგის სახით დავაბრუნებინოთ ჩვენთვის სასურველი ინფორმაცია:
```
class MyClass:
  class_attribute = data
  def __ init __(self, data_1, data_2, data_3, ...):
    self.attribute_1 = data_1
    self.attribute_2 = data_2
    self.attribute_3 = data_3
    self.attribute_... = ...

  def __ str __(self):
    return f"{self.attribute_1} is first attribute of instance"
  ...
  functions

my_class = MyClass(3, 2, 1)
print(my_class) # დაიპრინტება იქნება "3 is first attribute of instance"
```

"self" სიტყვა შეგვიძლია ჩავანაცვლოთ ჩვენთვის სასურველი სიტყვით თუმცა ნებისმიერ შემთხვევაში ეს სიტყვა პირველ პარამეტრად უნდა იყოს გადაცემული 
__ init __ ფუნქციისთვის! რაც შეეხება 

# **რა არის მეთოდი?!**
მეთოდი არის კლასში ჩაშენებული ფუნქცია-ფუნქციონალი. ეს შეიძლება იყოს კლასის მეთოდი, ინსთენსის მეთოდი ან სტატიკური მეთოდი.
ინსთენს მეთოდი შეგვიძლია განვსაზღვროთ როგორც უბრალო ფუნქცია იმ გასხვავებით რომ პირველ პარამეტრად აუცილებლად უნდა გადავცეთ იგივე სიტყვა რაც გადავეცით __ init __() ფუნქციას! ამ შემთხვევაში ლაპარაკია "self" სიტყვაზე:
```  
class MyClass:
  class_attribute = data
  def __ init __(self, data_1, data_2, data_3):
    self.attribute_1 = data_1
    self.attribute_2 = data_2
    self.attribute_3 = data_3
  ...
  def instance_method(self):
    return self.attribute_1 + self.attribute_2 + self.attribute_3

my_class = MyClass(3, 2, 1)
print(my_class.instance_method()) # დაიპრინტება "6"
```
# **რა არის თვისებები-properties და დეკორატორი?!**
თვისებები არიან მეთოდები რომლებიც გამოიყურებიან ატრიბუტებივით. თვისებებს ვიყენებთ მაშინ როცა გვჭირდება ატრიბუტზე დამატებითი ლოგიკის გაწერა ან ატრიბუტის დასეთვა.
დეკორატორი არის საშუალება რომ ფუნქციაზე, მეთოდზე ან კლასზე დავამატოთ ფუნქციონალი ისე რომ არ შევცვალოთ მათი კოდი.
ამ შემთხვევაში განვიხილოთ @property დეკორატორი:
```  
class MyClass:
  class_attribute = data
  def __ init __(self, data_1, data_2):
    self.attribute_1 = data_1
    self.attribute_2 = data_2
  @property
  def instance_method(self):
    return self.attribute_1 * self.attribute_2

my_class = MyClass(3, 5)
print(my_class.instance_method) # დაიპრინტება "15"
```
დეკორატორის ნიშანი არის "@", დეკორატორი საშუალებას გვაძლევს მონაცემს მეთოდის საშუალებით ჩავწვდეთ ისე როგორც ატრიბუტს.
@property დეკორატორის გამოყენებით ჩვენ შეგვიძლია ატრიბუტები ვაქციოთ "only read" ატრიბუტებად.
```  
class MyClass:
  class_attribute = data
  def __ init __(self, data_1):
    self.attribute_1 = data_1

my_class = MyClass(3)
print(my_class.attribute_1) # დაიპრინტება "3"
my_class.attribute_1 = 5
print(my_class.attribute_1) # დაიპრინტება "5"
```
გამოვიყენოთ @property რომ ატრიბუტი გადავაქციოთ მხოლოდ წაკითხვად ატრიბუტად, იდულისხმება რომ შეუძლებელი გახდება ატრიბუტის მოდიფიცირება:

```
class MyClass:
  class_attribute = data
  def __ init __(self, data_1):
    self._attribute_1 = data_1
  @property
  def instance_method(self):
    return self._attribute_1

my_class = MyClass(3)
print(my_class.attribute_1) # დაიპრინტება "3"
my_class.attribute_1 = 5 # Raises: AttributeError: can't set attribute
```
იმისთვის რომ ისევ შევძლოთ ატრიბუტის მოდიფიცირება გამოვიყენოთ @setter დეკორატორი:
```
class MyClass:
  class_attribute = data
  def __ init __(self, data_1):
    self._attribute_1 = data_1
  @property
  def instance_method(self):
    return self._attribute_1

  @instance_method.setter
  def instance_method(self, value):  # Setter for instance_method
        if value <= 0:
            raise ValueError("value must be positive!")
        self._attribute_1 = value  # Update the attribute if valid

my_class = MyClass(3)
print(my_class.attribute_1) # დაიპრინტება "3"
my_class.attribute_1 = 5 
print(my_class.attribute_1) # დაიპრინტება "5"
my_class.attribute_1 = -4 # Raises: ValueError: value must be positive!
```

# **რა არის @classmethod-ი და @staticmethod-ი?!**
@classmethod-ი არის კლასში ინკაფსულირებული მეთოდი რომელიც ეკუთვნის კლასს და არა რომელიმე ინსტანციას. @classmethod-ის და "cls" სიტყვის გამოყენებით ჩვენ შეგვიძლია ვიმოქმედოთ კლასის ატრიბუტზე ანუ შევცვალოთ კლასის მდგომარეობა:

```
class MyClass:
  class_attribute = value 

  @classmethod
  def class_method(cls, new_value):
    cls.class_attribute = new_value

my_class = MyClass()
print(my_class.class_attribute) # დაიპრინტება vlaue
my_class.class_method(new_value)
print(my_class.class_attribute) # დაიპრინტება new_vlaue
```
"cls" სიტყვა გამოიყენება იგივე დანიშნულებით კლასის მიმართ როგორითაც "self" სიტყვა ინსთენსის მიმართ, ანუ მისი გამოყენებით მეთოდს შეუძლია ჩაწვდეს კლასის ატრიბუტებს.

@staticmethod-ი არის კლასში ინკაფსულირებული მეთოდი რომელიც არც კლასის მდგომარეობაზე ახდენს გავლენას და არც ინსთენსზე!!! ამ შემთხვევაში დაისმის შეკითხვა: რატომ არის ის იმპლემენტირებული კლასში?
მარტივი პასუხია რომ: შინაარსობრივად დაკავშირებულია კლასთან.
```
class MyClass:
  class_attribute = value 

  @classmethod
  def class_method(cls, new_value):
    cls.class_attribute = new_value
  
  @staticmethod
  def static_method(var, var_1):
    return var + var_1

my_class = MyClass()
print(my_class.class_attribute) # დაიპრინტება vlaue
my_class.class_method(new_value)
print(my_class.class_attribute) # დაიპრინტება new_vlaue

print(my_class.static_method(int(3), int(2)) დაიპრინტება "5"
```
# **რა არის მემკვიდრეობითობა?!**

მემკვიდრეობითობა გულისხმობს კლასის შექმნას სხვა კლასის საფუძველზე, სხვა კლასს ეწოდება მბობელი კლასი რომლისგანაც შვილ კლასს გადაეცემა მშობელი კლასის ატრიბუტები და მეთოდები, შვილ კლასს შეუძლია უბრალოდ გამოიყენოს ისინი, დაუმატოს მათ თავისი მონაცემები და ფუნქციონალი ან საერთოდ შეცვალოს ისინი.
მშობელი კლასი:
class ParentClass:
  class_attribute = data
  def __ init __(self, data_1):
    self.instance_attribute = data_1 

  def instance_method(self):
    return self.instance_attribute * self.instance_attribute
  
  @classmethod
  def class_method(cls):
    return cls.class_attribute * cls.class_attribute
  
class ChildClass(ParentClass):
  ...

my_class = ChildClass()
print(my_class.class_method) # დაბეჭდავს data * data -ს შედეგს
```




