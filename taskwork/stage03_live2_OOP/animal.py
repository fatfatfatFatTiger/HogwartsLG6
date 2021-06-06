"""
课后作业

自己写一个面向对象的例子：
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】，
重写父类的__init__方法，继承父类的属性，
添加一个新的属性，毛发 = 短毛，
添加一个新的方法， 会捉老鼠，
重写父类的【会叫】的方法，改成【喵喵叫】
作业上传到自己的 github 仓库中，把 github 仓库地址回复到课程贴中
"""


class Animal:
    age = 5
    gender = "male"

    def __init__(self, name="Tom", color="blue"):
        self.name = name
        self.color = color

    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age}, my gender is {self.gender}, my color is {self.color}")

    def shout(self):
        print(f"{self.name} can shout loudly")

    def run(self):
        name = "Tim"
        print(f"I can run quickly,faster than {name}")


if __name__ == "__main__":
    cat = Animal()
    # 类调用方法
    Animal().introduce()
    # 实例调用方法
    cat.shout()
    # 类修改属性
    Animal.age = 7
    # 实例修改属性
    cat.name = "Bob"
    cat.introduce()
    print("--------------分隔线--------------")
    mouse = Animal("Jerry", "yellow")
    mouse.introduce()
    mouse.run()
    # 实例调用属性
    print(mouse.color)
    # 类调用属性
    print(Animal.gender)


