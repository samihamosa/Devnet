from math import pi
def area_of_circle(r):
    if r<0:
        raise ValueError(' negative radius value error')
    return pi*(r**2)
