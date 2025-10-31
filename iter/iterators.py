
# my_list = [1,2,3,4,5]
# my_iter = iter(my_list)
#
# while(my_iter):
#     element = next(my_iter)
#     print(element)
#


# numbers =(x for x in range(10**6))
# print(next(numbers))


def divide(x,y):
    print(x/y)

def outer_div(func):
    def inner(x,y):
        if(x<y):
            x,y = y,x
            return func(x,y)
    return inner

divivde1 = outer_div(divide)
divivde1(2,8)


def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitary_argument(*args,**kwargs):
        print("The positional arguments are", args)
        print("the keyword argument are",kwargs)
        function_to_decorate(*args)
    return a_wrapper_accepting_arbitary_argument

@a_decorator_passing_arguments
def function_with_no_argument():
    print("No arguments here")

@a_decorator_passing_arguments
def fun_with_arguments(a,b,c):
    print(a,b,c)

function_with_no_argument()
fun_with_arguments(1,2,3)