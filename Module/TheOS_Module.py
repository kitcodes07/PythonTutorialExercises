import os
"""
#make one directory
os.mkdir("my_first_directory")
print(os.listdir())


#make directories; a directory and another one inside it.
os.makedirs("my_first_directory/my_second_directory")
os.chdir("my_first_directory")
print(os.listdir())

os.makedirs("../my_1st_directory/my_2nd_directory")
os.chdir("../my_1st_directory")
print(os.listdir())


#how to get current working directories
print(os.getcwd())
os.chdir("my_first_directory/my_second_directory")
print(os.getcwd())


#remove a directory
print(os.listdir())
os.chdir("my_first_directory")
print(os.listdir())
os.rmdir("my_second_directory")
print(os.listdir())
os.chdir("../")
print(os.listdir())


#remove directories
os.removedirs("my_1st_directory/my_2nd_directory")


#the above functions can also be done by system function.
returned_value = os.system("mkdir my_1st_directory")
print(returned_value)
"""

########################################################
"""
Exercise 1: OS Module
    Write a function or method called find that takes two arguments called path and dir. 
    The path argument should accept a relative or absolute path to a directory where the search should start, while the dir argument should be the name of a directory that you want to find in the given path. 
    Your program should display the absolute paths if it finds a directory with the given name.

    The directory search should be done recursively. 
    This means that the search should also include all subdirectories in the given path.


    #prep creation of path for test
    os.makedirs("./tree/c/other_courses/cpp")
    os.makedirs("./tree/c/other_courses/python")
    os.makedirs("./tree/cpp/other_courses/c")
    os.makedirs("./tree/cpp/other_courses/python")
    os.makedirs("./tree/python/other_courses/c")
    os.makedirs("tree/python/other_courses/cpp")
"""

#Using chdir
def find(path, dir):
    return_path = os.getcwd()
    os.chdir(path)
    subdirs = os.listdir()
    if len(subdirs) != 0:
        if dir in subdirs:
            print(f"{os.getcwd()}/{dir}")
        for subdir in subdirs:
            find(subdir, dir)

    os.chdir(return_path)

find("./tree", "python")
"""
#Alternative: instead of using chdir, you also use os.path
def find(path, dir):
    path = os.path.abspath(path)
    subdirs = os.listdir(path)
    if dir in subdirs:
        print(f"{path}/{dir}")
    for subdir in subdirs:
        sd_path = os.path.join(path,subdir)
        find(sd_path, dir)

find("./tree", "python")
"""
