#Classroom Information Spread Using Binary Tree Traversals
# Binary tree node class representing a student in the classroom
class Student:
    def __init__(self, name):
        self.name = name
        self.left = None  
        self.right = None 


def preorder_traversal(student):
    if student:
        print(student.name, end=' ') 
        preorder_traversal(student.left) 
        preorder_traversal(student.right) 

def inorder_traversal(student):
    if student:
        inorder_traversal(student.left)  
        print(student.name, end=' ')  
        inorder_traversal(student.right) 


def postorder_traversal(student):
    if student:
        postorder_traversal(student.left) 
        postorder_traversal(student.right)  
        print(student.name, end=' ') 

# Create a binary tree structure for the classroom students
def create_classroom():
    student1 = Student("Student1")
    student2 = Student("Student2")
    student3 = Student("Student3")
    student4 = Student("Student4")
    student5 = Student("Student5")

   
    student1.left = student2
    student1.right = student4
    student2.left = student3
    student4.right = student5

    return student1

classroom_root = create_classroom()

# Preorder traversal
print("Preorder news spread (Root -> Left -> Right):")
preorder_traversal(classroom_root)
print("\n")

# Inorder traversal
print("Inorder news spread (Left -> Root -> Right):")
inorder_traversal(classroom_root)
print("\n")

# Postorder traversal
print("Postorder news spread (Left -> Right -> Root):")
postorder_traversal(classroom_root)
print("\n")
