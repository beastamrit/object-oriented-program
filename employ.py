class employ:
    def __init__(self):
        print("employe created")
    def __del__(self):
        print("destructer call")
def create_object():
    obj=employ()
    print("Function end")
    return obj
obj= create_object()