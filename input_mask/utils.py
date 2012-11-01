def chunks(l, n, j):
    """
    Divide string l in n chunks and join with j
    """
    final = []
    for i in range(0, len(l), n):
        final.append(l[i:i+n])
    return j.join(final)
