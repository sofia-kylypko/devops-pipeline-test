def hello():
    return "Hello, CI World!"

def add(a, b):
    return a + b

if __name__ == "__main__":
    print(hello())
    print(f"1 + 2 = {add(1, 2)}")