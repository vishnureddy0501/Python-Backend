def super_does_not_access_parent():
    class Root:
        def f(self):
            print("root called")
    class A(Root):
        pass
    class B(A):
        def f(self):
            print("B called")
            super().f() # here ideally it should call A's f. but f is not there in A. so it goes to A's parent and look for f there
    
    b = B()
    b.f()
super_does_not_access_parent()