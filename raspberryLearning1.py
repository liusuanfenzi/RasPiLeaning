#Task1:
print("Hello world")

#Task2:
def Fibonacci(n):
    if(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("输入斐波那契的项数："))
print(Fibonacci(n))
        
#Task3:
class myList:
    #初始化函数是两个下划线（严肃。
    def __init__(self):
        self.l1=list()#创建当前对象
        print("Successfully instancing!")
    #在列表末追加元素
    def add(self,element):
        self.l1.append(element)
    #删除指定元素
    def remove(self,element):
        self.l1.remove(element)
    #删除指定位置元素
    def delete(self,index):
        self.l1.pop(index)
    #清空列表
    def clear(self):
        self.l1.clear()
    #在指定位置插入元素
    def insert(self,index,element):
        self.l1.insert(index,element)
    #升序排序
    def asscendingSort(self):
        self.l1.sort()
    #逆置列表
    def reverse(self):
        self.l1.reverse()
    #打印列表
    def print(self):
        print(self.l1)

#实例化
ll=myList()
for i in range(1,10):
    ll.add(i)
# ll.asscendingSort()
# ll.print()
# ll.add(99)
# ll.print()
# ll.remove(99)
# ll.print()
# ll.clear()
# ll.print()
ll.delete(7)
ll.print()