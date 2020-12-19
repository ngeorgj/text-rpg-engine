name = 'city name'
description = ''

places = []

cost_of_travel = 1000

@property
def has_port():
    if PORT in places:
        return True
    return False