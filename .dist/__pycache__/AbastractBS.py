from abc import ABCMeta, abstractmethod
class Programming(metaclass=ABCMeta):
    @abstractmethod
    def has_oop(self):
        pass    
class Python(Programming):
    def has_oop(self):
        return "Yess" 
class Pascal(Programming):
    def has_oop(self):
        return "No"
  
one = Python()
print(one.has_oop())
