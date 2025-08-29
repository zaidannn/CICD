def add(a, b):
    return a + b

def divide(a, b):
    return a / b  # akan error kalau b = 0

if __name__ == "__main__":
    print("Add:", add(5, 3))
    print("Divide:", divide(5, 0))  # sengaja error
