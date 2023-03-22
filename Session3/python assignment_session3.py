class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        
    def introduce(self):
        print(f"안녕 난 {self.name} 나이는 {self.age} 키는 {self.height}")
        
    def yell(self):
        print("아?")

class Developer(Person):
    keyboard = '기계식'
    
    def yell(self):
        print("어?")
        
class Designer(Person):
    def __init__(self, name, age, height, disease):
        super().__init__(name, age, height)
        self.disease = disease
    
class Product_Manager(Person):
    def yell(self):
        print("개발자님 여기 오류있어요;;")
        
    def aging(self):
        self.height -=5
        self.age +=2
        print("개발자를 새로 뽑아야하나;;")
        Developer.keyboard = '멤브레인'
        

d1 = Developer("강백호", 17, 188)
d2 = Designer("송태섭", 18, 169, "코로나")
p1 = Product_Manager("서태웅", 17, 183)
d1.introduce()
d1.yell()
d2.introduce()
d2.yell()
p1.introduce()
p1.yell()
p1.aging()
p1.introduce()