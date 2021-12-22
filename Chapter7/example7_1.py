class MyClass (object):
    pass
my_instance = MyClass()
MyClass.class_attribute = 'hello'
my_instance.instance_attribute = 'world'
dir(my_instance)
print (my_instance.__class__)
type(my_instance)
print (my_instance.instance_attribute)
print(my_instance.class_attribute)
# print(MyClass.instance_attribute)