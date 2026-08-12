def main():
    x = 1
    y = 2
    z = 0

    print ("x ",x)
    print ("y ",y)
    print ("z ",z)

    x,y,z  = foo(x,y)

    print ("x ",x)
    print ("y ",y)
    print ("z ",z)


def foo(x,y):

    x = 0
    y = 0
    z = x + y

    return x,y, z

     
if __name__ == "__main__":
    main()