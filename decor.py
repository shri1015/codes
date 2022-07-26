#def func1(msg):
 #   print(msg)

# func1("hii")
# func2 = func1
# func2("hii")

# inner function

def func():
    print("this is first function")
    def func1():
        print("this is first child function")
    def func2():
        print("this is second child function")

    func1()
    func2()

func()