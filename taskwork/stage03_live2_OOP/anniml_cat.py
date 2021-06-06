
from HogwartsLG6.taskwork.stage3_live2_OOP.animal import Animal


class Cat(Animal):
    gender = "female"

    def __init__(self, name, color):
        super().__init__(name, color)
        self.hair = "short"

    def catch(self):
        mouse = "Dave"
        print(f"I can catch mouse {mouse}")

    def shout(self):
        print(f"{self.name} can meow")


if __name__ == "__main__":
    dd = Cat("dingdang", "white")
    # 调用父类方法
    dd.introduce()
    # 实例调用属性
    print(f"my hair is {dd.hair}")
    # 实例调用方法
    dd.shout()
    # 类调用方法
    Cat("miumiu", "gray").catch()

    # 测试修改内容后通过Pycharm提交到github
