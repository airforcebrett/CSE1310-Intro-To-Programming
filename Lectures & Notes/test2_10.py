def foo1(my_list):
    my_list[1]=10
def foo2(my_list):
    my_list[0]=[10,20,30]
def foo3(my_list):
    my_list.append(40)
def main():
    L=[1,2,3]
    print(L)
    foo1(L)
    print("after foo1: ",L)
    foo2(L)
    print("after foo2:" ,L)
    foo3(L)
    print("after foo3: ",L)
main()
