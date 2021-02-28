from toy_project.toy_package.toy_module import toy_function, ToyClass

def run():
    """runs an example using the toy_function and ToyClass
    """
    l=["a", "b", "c"]
    d=dict(zip(l,[1,2,3]))
    print(toy_function(l,1))
    toy_obj = ToyClass("toy_name", l,d)
    for s in toy_obj.get_from_l([1,2]):
        print(s)
    print(toy_obj.get_from_d(["a","b"]))


if __name__=="__main__":
    run()