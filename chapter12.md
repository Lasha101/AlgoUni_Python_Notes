# **რელაციური მონაცემთა ბაზები, SQLite, SQL**
რელაციური მონაცემთა ბაზა (RDB) არის მონაცემთა ბაზის ტიპი, რომელიც ინახავს და აორგანიზებს მონაცემებს ცხრილებში. ეს ცხრილები შედგება სვეტებისგან და მწკრივებისგან.

რიგები-მწკრივები წარმოადგენენ ჩანაწერებს კონკრეტული ობიექტის მონაცემების შესახებ.
სვეტები-ველები განსაზღვრავენ მონაცემთა ტიპს, როგორიცაა "სახელი/გვარი" ან/და "დაბადების თარიღი", ისინი წარმოადგენენ კოლონების სათაურებს.
რელაციურ მონაცემთა ბაზების შემთხვევაში მიღებულია ზოგადი მიდგომა რომ მონაცემები გავანაწილოთ სხვადასხვა პატარ-პატარა სპეციალიზებულ ცხრილებში რომლებიც ერთმანეთთან დაკავშირებულნი არიან ეგრეთ წოდებული გასაღებების გამოყენებით. 
ცხრილებს შორის კავშირს ეწოდება რელაციები.
აღნიშნული მიდგომა უზრუნველყოფს მონაცემების უკეთ ორგანიზებას და ზრდის მათ მიმართ განხორციელებული მანიპულაციების პერფორმატიულობას.

# **მონაცემთა ბაზა-SQLite**
SQLite-ი არის პითონში ჩაშენებული მსუბუქი რელაციური მონაცემთა ბაზა, იგი ძალიან მოსახერხებელია პატარა პროექტებისთვის, იმპლემეტირებულია C-ში და შესაბამისად ძალიან სწრაფია.

# **SQL-Structured Query Language**
რელაციურ მონაცემთა ბაზებს ჩაშენებული აქვთ მექანიზმი რომელიც საშუალებას გვაძლევს რომ მოვახდინოთ მონაცემების მანიპულაცია SQL-ის გამოყენებით. SQL-ი არის დეკლარატიული პარადიგმის პროგრამირების ენა, რაც გულისხმობს იმას რომ გააჩნია საკუთარი სინტაქსი რომლის გათვალისწინებითაც ჩვენ რელაციურ მონაცემთა ბაზას ვთხოვთ რის გაკეთებაც გვინდა მაგრამ არ ვაძლევთ კონკრეტულ ინსტრუქციებს დავალების შესასრულებლად. 

# **CRUD ოპერაციები**
- C for Create
- R for Read
- U for Update
- D for Delete

CREATE ბრძანებით ჩვენ შეგვიძლია შევქმნათ ცხრილი-მაგიდა მონაცემთა ბაზაში:
```
CREATE TABLE users (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);
```
... ... ...

READ = SELECT ბრძანებით ჩვენ შეგვიძლია ამოვიღოთ ცხრილიდან ჩვენთვის სასურველი მონაცემები:
```
SELECT * FROM users;
```
... ... ...

UPDATE ბრძანებით ჩვენ შეგვიძლია ნაწილობრივ შევცვალოთ ჩვენთვის სასურველი მონაცემები:
```
UPDATE users
SET age = 30
WHERE id = 1;
```
... ... ...

DELETE ბრძანებით ჩვენ შეგვიძლია წავშალოთ როგორც ჩვენთვის სასურველი რიგი-ჩანაწერი ცხრილიდან ასევე ყველა ჩანაწერი:
```
DELETE FROM users
WHERE id = 1;
```
... ... ...


```
DELETE FROM users;
```

ეს კონფიგურაცია აადვილებს მონაცემთა ორგანიზებას, ამოღებას და ანალიზს SQL-ის (Structured Query Language) გამოყენებით.

