"""
https://medium.com/@kalanamalshan98/composite-design-pattern-a-beginner-friendly-guide-5590d625f76b
https://chatgpt.com/c/68cf88b7-e750-8323-9695-509f16599717

"""

"""
Problem Statement: Implement a file system similar to os, having functionality such as add files/folders, get file/folder size, remove file/folders
"""

"""
Solution: Here in order to create a file system having above functionality, we can choose composite designnpattern as it allows us to treat objects or group of that objects/composite in a similar manner. 
Here in our case files is an individual object/leaf-node and folders are composition of files and filders, which can be treated uniformly
"""

from abc import ABC, abstractmethod
from typing import List
#Firstly we will have a component interface/abstract class representing files/folders

class IComponent(ABC):
    @abstractmethod
    def get_size(self)->int:pass
    
    @abstractmethod
    def print_structure(self, indent:int)->None:pass


class FileComponent(IComponent):
     
    def get_size(self)->int:
        return 1

    def print_structure(self, indent:int =0)->None:
        print("file")   


class FolderComponent(IComponent):
    def __init__(self):
        self.component:List[IComponent] = []

    def add(self, obj:IComponent)->None:
        if obj not in self.component:
            self.component.append(obj)

    def get_size(self)->int:
        return sum(comp.get_size() for comp in self.component)

    def delete_component(self,obj:IComponent)->None:
        if obj in self.component:
            self.component.remove(obj)

    def print_structure(self, indent:int=1)->None:
        print(f"Folder")
        for c in self.children:
            c.print_structure(indent + 1)
            



# Other example could be maintaining an organization chart(containing employee, Team, sub-team etc) in organization.