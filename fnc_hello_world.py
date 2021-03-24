def hello_world(params):
    for param in range(0,params):
        print("{}. Hello World!".format(param+1))

inp_number = int(input())
hello_world(inp_number)