class Dog():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def sit(self):
        print(self.name+'坐着')
    def eat(self):
        print(self.name+'在吃饭')
my_dog=Dog('yoyo','5')
print('小狗的名字是'+my_dog.name)  
print('小狗的年龄是'+my_dog.age) 
my_dog.sit()
my_dog.eat()     
    