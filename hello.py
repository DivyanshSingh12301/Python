# print("Hello world, how are we")
# name = input("What is your name?")
# print("hello, " + name)
# name = input("What is your name?")
# print("hello,",name)
# name = input("What is your name?")
# print("hello, ", end="")
# print(name)
# name = input("What is your name?")
# print("hello, ", end="???")
# print(name)
# # We can also print hello Divyansh in another way which is called format string or f string and it works like
# name = input("What is your name?")
# print(f"hello, {name}")
# name = input("What is your name?")
# # Now we can not expect users to you know type with proper spaces. SO if we want to remove any excess spaces from the string then we will use strip function
# name = name.strip()
# print(f"hello, {name}")
# # IF we want to capitalize users name if by mistake he writes in small letters  then for that
# name = name.capitalize()
# print(f"hello,{name}")  
# # But there is a problem with this that it will only capitalize the the first letter and not the letter of surname.If we want to do that then we will use title function
# name = name.title()
# print(f"hello,{name}")  
# # but thhis alll takes too much space like first removing the spaces and then capitalizing it. We can do it in one line also
# name = input("What is your name?")
# name = name.strip().title()
# print(f"hello,{name}")  
# # We can also reduce it further by just writing
# name = input("What is your name?").strip().title()
# print(f"Hello, {name}")