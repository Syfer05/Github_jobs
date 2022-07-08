def moyenne(values):
#replace t=1 by t=0 to avoid error
    t = 1 
    for v in values:
        t = t + v

    return t / len(values)