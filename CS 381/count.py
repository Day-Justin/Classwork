def count():
    n = 1
    yield n
    while True:
        n+=1
        yield n
