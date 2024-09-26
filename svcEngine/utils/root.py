def dir():
    file = __file__
    split = file.split('\\')
    split.pop()
    path = [i for i in split if i != split[len(split) - 1]]
    path.pop()
    path = '/'.join(i for i in path)
    return path

print(f"root directory found at {dir()}")