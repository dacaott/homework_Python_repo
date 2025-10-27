def curry(func, n):
    assert isinstance(n, int), "Error: n should be a natural number"
    assert n >= 0, "Error: n can't be negative"

    if n == 0:
        return func

    def step(args):
        if len(args) == n:
            return func(*args)

        def next_func(arg):
            # создаём новый список, чтобы не изменить существующий
            return step(args + [arg])

        return next_func

    return step([])


def uncurry(curried_func, n):
    assert isinstance(n, int), "Error: n should be a natural number"
    assert n >= 0, "Error: n can't be negative"

    if n == 0:
        return curried_func

    def uncurried(*args):
        assert len(args) == n, f"Error: {n} arguments expected, {len(args)} given"
        result = curried_func
        for arg in args:
            result = result(arg)
        return result

    return uncurried
