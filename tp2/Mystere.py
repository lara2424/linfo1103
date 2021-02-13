def mystere(n):
    """
    pre: `n` > 0
    post: ???
    """
    rep = 0
    for i in range(n+1):
        rep = rep + ((i + 1) * i)
    return rep


print(mystere(1))
