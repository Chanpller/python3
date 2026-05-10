# 定义一个Person类
class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def speak(self, msg):
        print(f'我叫{self.name}， 年龄是{self.age}， 性别是{self.gender}，我想说：{msg}')

# 定义一个Student类（子类、派生类）， 继承自Person类（父类、超类、基类）
class Student(Person):
    def __init__(self, name, age, gender, stu_id, grade):
        # 在子类中，有两种方式去调用父类的初始化方法，来实现对继承属性：name, age, gender 初始化操作
        # 方式1（更推荐）
        super().__init__(name, age, gender)

        # 方式2
        # Person.__init__(self, name, age, gender)

        # 子类独有的属性，需要自己手动完成初始化
        self.stu_id = stu_id
        self.grade = grade

    def study(self):
        print(f'我叫{self.name}，我在努力的学习，争取做到{self.grade}年级的第一名')

        # 方法重写：当子类中定义了一个与父类中相同的方法，那么子类中的方法就会“覆盖”父类的方法

    def speak(self, msg):
        super().speak(msg)
        print(f'我是学生，我的学号是{self.stu_id}，我正在读{self.grade}，我想说：{msg}')

# 创建Student类的实例对象
# s1 = Student('李华', 16, '男', '2025001', '初二')
# print(s1.__dict__)
# print(type(s1))
#
# # 查找speak方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
# # s1.speak('你好')
#
# # print(s1.__dict__)
#
# # 查找study方法的过程：1.实例自身(s1) => 2.Student类 => 3.Person类
# # s1.study()
# print(Student.__dict__)
# s1.speak("好好学习")


p1 = Person('张三', 18, '男')
s1 = Student('李华', 12, '男', '2025001', '初二')

# 方法1：isinstance(instance, Class)，作用：判断某个对象是否为指定类或其子类的实例
print(isinstance(s1, Student))
print(isinstance(p1, Person))
print(isinstance(s1, Person))
print(isinstance(p1, Student))

# 方法2：issubclass(Class1, Class2)，作用：判断某个类是否是另一个类的子类
print(issubclass(Student, Person))
print(issubclass(Person, Student))