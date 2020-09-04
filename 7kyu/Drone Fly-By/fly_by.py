def fly_by(lamps, drone):
    return ''.join(['o' if len(drone) > i else 'x' for i in range(len(lamps))])
