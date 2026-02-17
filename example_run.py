from profit_engine import (
    calculate_fuel_cost,
    calculate_maintenance_reserve,
    calculate_total_trip_cost,
    calculate_profit,
    calculate_profit_margin,
    break_even_price
)

from database import create_table, save_trip

# Ensure table exists
create_table()


# Example trip data
trip_price = 900
fuel_price = 3.75
gallons_used = 45
engine_hours = 6
reserve_per_hour = 25
bait_cost = 120
fixed_overhead = 150

fuel = calculate_fuel_cost(fuel_price, gallons_used)
maintenance = calculate_maintenance_reserve(engine_hours, reserve_per_hour)
total_cost = calculate_total_trip_cost(fuel, maintenance, bait_cost, fixed_overhead)

profit = calculate_profit(trip_price, total_cost)
margin = calculate_profit_margin(trip_price, profit)
breakeven = break_even_price(total_cost)

print("Total Cost:", total_cost)
print("Profit:", profit)
print("Profit Margin (%):", margin)
print("Break Even Price:", breakeven)


# Save trip to database
save_trip(
    trip_price,
    fuel,
    maintenance,
    bait_cost,
    fixed_overhead,
    total_cost,
    profit,
    margin
)

print("Trip successfully saved to database.")

