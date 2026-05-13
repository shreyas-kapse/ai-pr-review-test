
# hello world function
def greet():
    print("hello world")
    
def add(a:int, b:int):
    return a+b

# multiplication function
def mul(a:int,b:int)->int:
    return a*b

# connect to main server
def connect_to_server(username:str, password:str):
    print("connection to server by using following username and password")
    print("username ", username)
    print("password ",password)
    
username = "admin"
password  = "welcome@123"

greet()
print(add(10,20))
print(mul(10,20))
connect_to_server(username=username, password=password)
