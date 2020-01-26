from functools import partial
from square import GridSquare

def validate(functions, square: GridSquare):
	for f in functions:
		if not f(square):
			return False
	return True

def max_wind_speed(limit: float, square: GridSquare):
	return square.speed < limit

take_off = [partial(max_wind_speed, 6)]
landing = [partial(max_wind_speed, 6)]
flight = [partial(max_wind_speed, 10)]

validate_take_off = partial(validate, take_off)
validate_landing = partial(validate, landing)
validate_flight = partial(validate, flight)