from profit_engine import (
    calculate_fuel_cost,
    calculate_maintenance_reserve,
    calculate_total_trip_cost,
    calculate_profit,
    calculate_profit_margin,
    break_even_price
)

from database import create_table, save_trip, get_profit_summary

# Ensure database table exists
create_table()

print("\n=== Charter Profit Entry ===\n")

trip_price = float(input("Trip price charged: "))
fuel_price = float(input("Fuel price per gallon: "))
gallons_used = float(input("Gallons used: "))
engine_hours = float(input("Engine hours run: "))
reserve_per_hour = float(input("Maintenance reserve per hour: "))
bait_cost = float(input("Bait cost: "))
fixed_overhead = float(input("Fixed overhead allocation: "))

fuel = calculate_fuel_cost(fuel_price, gallons_used)
maintenance = calculate_maintenance_reserve(engine_hours, reserve_per_hour)
total_cost = calculate_total_trip_cost(fuel, maintenance, bait_cost, fixed_overhead)

profit = calculate_profit(trip_price, total_cost)
margin = calculate_profit_margin(trip_price, profit)
breakeven = break_even_price(total_cost)

print("\n=== Trip Results ===")
print("Total Cost:", round(total_cost, 2))
print("Profit:", round(profit, 2))
print("Profit Margin (%):", round(margin, 2))
print("Break Even Price:", round(breakeven, 2))

# Save trip
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

print("\nTrip saved successfully.")

# Display summary
summary = get_profit_summary()

if summary:
    total_profit, avg_margin = summary
    print("\n=== Overall Performance ===")
    print("Total Historical Profit:", round(total_profit, 2))
    print("Average Profit Margin (%):", round(avg_margin, 2))
