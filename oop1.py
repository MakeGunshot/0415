class employee:
    # 生命一个类的变量
    # pay_raise_amount = 1.2
    # 创建一个构造器
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + last +'@email.com'
    # 创建一个方法
    # def fullname(self):
    #     return self.first + self.last
    def new_pay(self):
        return self.pay * self.pay_raise_amount





emp1 = employee('xiaoming','wang',10000)
emp2 = employee('xiaohong','zhang',2000)


# print(emp1.first,emp1.last,emp1.pay,'\n',emp1.email) 
# print(emp2.first,emp2.last,emp2.pay,emp2.email)

#赵老师代码
emp1 = employee("xiaoming","wang",10000)
emp2 = employee("xiaohong",'zhang',20000)
employee.pay_raist_amount = 1.4
print(emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
emp1.pay_raist_amount = 1.5
print("emp1. raise, emp1.newpay0()",emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
emp2.pay_raist_amount = 1.6
print(emp1.new_pay0())
print(emp1.new_pay1())
print(emp2.new_pay0())
print(emp2.new_pay1())
