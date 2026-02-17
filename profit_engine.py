def calculate_fuel_cost(fuel_price_per_gallon, gallons_used):
    return fuel_price_per_gallon * gallons_used


def calculate_maintenance_reserve(engine_hours, reserve_per_hour):
    return engine_hours * reserve_per_hour


def calculate_total_trip_cost(fuel_cost, maintenance_cost, bait_cost, fixed_overhead):
    return fuel_cost + maintenance_cost + bait_cost + fixed_overhead


def calculate_profit(trip_price, total_cost):
    return trip_price - total_cost


def calculate_profit_margin(trip_price, profit):
    if trip_price == 0:
        return 0
    return (profit / trip_price) * 100


def break_even_price(total_cost):
    return total_cost
