def print_args(arg1,kwarg1=None,kwarg2=None):
    print arg1,kwarg1,kwarg2


if __name__=="__main__":
    import pdb
    pdb.set_trace()

    print_args("arg1","arg2","arg3")
    print_args("arg1",kwarg1="arg2")
    print_args("arg1",kwarg2="arg3")
    print_args("arg1",{'kwarg1':"arg2",'kwarg2':"arg3"})
    print_args("arg1",**{'kwarg1':"arg2",'kwarg2':"arg3"})

