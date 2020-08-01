from timeit import default_timer as timer


def exec_time(func):
    def wrapper(*args):
        start = timer()
        func(*args)
        end = timer()
        result = end = start
        return result
    return wrapper



# да се качи без долното в джъдж

@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
