#%%
import re 
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = [] 
        self.parent = None 
    
    def add_child(self,child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent 
        while p:
            level += 1 
            p = p.parent 
        return level 
    
    def print_tree(self,data_type):
        spaces = ' ' * self.get_level() * 3 
        prefix = spaces + "|__" if self.parent else ""
        string = self.data 
        name,designation = string.split(" ",1)
        if data_type == "both":
            print(prefix + self.data)
        elif data_type == "name":
            print(prefix + name)
        elif data_type == "designation":
            print(prefix + designation)
        else:
            raise KeyError("That word is not permitted.")
        if self.children:
            for child in self.children:
                child.print_tree(data_type)

#%%
def build_tree():
    root = TreeNode("rudgh99 (CEO)")

    management = TreeNode("manager1 (CTO)")
    management1 = TreeNode("manager2 (teamchief)") 
    management1.add_child(TreeNode("manager3 (cloud manager)"))

    
    
    service = TreeNode("service1 (HR Head)")
    service.add_child(child = TreeNode("service2 (product service)"))
    service.add_child(child = TreeNode("service3 (store service)"))

    management.add_child(management1)
    root.add_child(management)
    root.add_child(service)
    root.print_tree(data_type="designation")

if __name__ == "__main__":
    build_tree()

#%%
