# global scope

my_global = 10
def fn1():
    local_v = 5
    print("fn1: my_global=", my_global)
    def fn2():
        print("fn2: my_global=", my_global)
        print("fn2: local_v=", local_v)
    fn2()
fn1()
# print("global: my_global=", my_global)
# not possible
# print ("accessing local_v from global scope", local_v)