from settings import MEMORY_FILE
    
def load():
    with open(MEMORY_FILE, "r") as f:
        data = f.read()
    return data

def save(w):
    data = load()

    with open(MEMORY_FILE, "w") as f:

        f.write(data + f"{w} \n")

def delete():
    with open(MEMORY_FILE,  "w"):
        pass

delete()



