def super_can_access_sibiling():
    class Root:
        def f(self):
            print("Root called")
    class A(Root):
        def f(self):
            print("A called")
            super().f()
    class B(Root):
        def f(self):
            print("B called")
            super().f()
    class C(A, B):
        def f(self):
            print("C called")
            super().f()

    c = C()
    c.f()
super_can_access_sibiling()

# super === next in line. super doesn't depends on parent. it depends on MRO (method resolution order)