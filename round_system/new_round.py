def round_system(func: callable, time: 1):
    if time <= 0:
        time ==1
        
    def inner(*args, **kwargs):
        for x in range(time):
            func(args, kwargs)
        return inner
