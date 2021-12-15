class MyClass (object):
    pass

inst1 = MyClass()
inst2 = MyClass()
inst3 = MyClass()
MyClass.class_attribute = 27
inst1.class_attribute = 72
print(inst1.class_attribute)
print(inst2.class_attribute)
print(inst3.class_attribute)
MyClass.class_attribute = 999
print(inst1.class_attribute)
print(inst2.class_attribute)
print(inst3.class_attribute)