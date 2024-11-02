class employee:
    def __init__(self):
        print('Employee created')
    def __del__(self):
        print('Destructor called')
def CreateObj():
    print('Making Object...')
    obj=employee()
    print('Function end...')
    return obj
print('Calling CreateObj() function')
obj=CreateObj()
print('Program End...')