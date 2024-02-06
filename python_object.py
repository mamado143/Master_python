# ---- object oriented => Magic Methods --
# Everything in python is object. 
# __init__ Called automatically
# __str__ Gives a human Readable output of the object. 
# __len__ Returns the length of the container. 
# ---------Called when we use the buildin in len() Function on the objet.
# __del__ Called when the object is deleted. 
# 
class Skill:
    '''
    This is the Skill class
    '''
    
    def __init__(self):
        self.skills = ["Html", "Css", "Python"]
        
    def __str__(self):
        return f"this is my skills => {self.skills}"
    def __len__(self):
        return len(self.skills)
    def __del__(self):
        print("Object Deleted")
        
profile = Skill()
print(profile)
print(len(profile))
print(len(profile.skills))
print(profile.skills)
profile.skills.append("PHB")
profile.skills.append("Mysqle")
print(len(profile.skills))
print(profile.skills)
del profile


# profile = Skill()













# print(profile.skills)
# print(profile.__class__)
# my_string = "mido"
# print(type(my_string))
# print(my_string.__class__)
# print(str.upper(my_string))
# print(dir(int))
# print(dir(str))
# print(dir(list))
# print(dir(dict))
# print(dir(set))
# print(dir(tuple))
# print(dir(float))