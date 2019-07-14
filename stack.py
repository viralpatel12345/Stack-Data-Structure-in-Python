class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1

    def get_max_size(self):
        return self.__max_size

    def is_full(self):
        if self.__top == self.__max_size-1 :
            return True
        else :
            return False

    def push(self,data):
        if not self.is_full() :
          self.__top+=1
          self.__elements[self.__top]=data
        else :
            print("Stack is Full")
    
    def pop(self) :
        if self.__top!=-1 :
            x=self.__elements[self.__top]
            self.__elements[self.__top]=None
            self.__top-=1
            return x
        else :
            print("Stack is Empty")
        
    
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg

    def display(self) :
        index=self.__top
        while index != -1 :

            print("(",index,")",self.__elements[index],end=" , ")
            index-=1
        print("\n")
        

stack1=Stack(5)
#Push all the required element(s).
stack1.push("Shirt1")
stack1.push("Shirt2")
stack1.push("Shirt3")
stack1.push("Shirt4")
stack1.push("Shirt5")
stack1.display()
print("POP = ",stack1.pop(),"\n")
stack1.display()
print("POP = ",stack1.pop(),"\n")
stack1.display()
print("POP = ",stack1.pop(),"\n")
stack1.display()
print("POP = ",stack1.pop(),"\n")
stack1.display()
print("POP = ",stack1.pop(),"\n")
stack1.display()
print(stack1._Stack__top)