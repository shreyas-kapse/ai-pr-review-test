
# hello world method
def greet():
    print("hello world")

# addition method 
def add(a:int, b:int):
    return a+b

# multiplication method 
def mul(a:int,b:int)->int:
    return a*b

# connect to main server
def connect_to_server(username:str, password:str):
    print("connection to server by using following username and password")
    print("username ", username)
    print("password ",password)
    return {"success ": True}

# configs    
username = "admin"
password  = "welcome@123"
port = 8080

greet()
print(add(10,20))
print(mul(10,20))


print(connect_to_server(username=username, password=password))
