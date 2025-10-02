#Write a Python Program to Create a Class Set and Get All Possible Subsets 
#from a Set of Distinct Integers.
class MySet:
    def __init__(self, elements):
        self.elements = elements

    def get_subsets(self):
        subsets = [[]]
        for element in self.elements:
            
            subsets += [s + [element] for s in subsets]
        return subsets

s = MySet([1, 2, 3])
print(s.get_subsets())
