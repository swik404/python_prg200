# ============================================================
#   NEA Electricity Unit Cost
# ============================================================

print("=" * 50)
print("   ⚡  NEA Electricity Bill Calculator  ⚡")
print("=" * 50)

# --- Inputs ---
previous_reading = float(input("Enter previous meter reading (kWh) : "))
current_reading  = float(input("Enter current meter reading  (kWh) : "))
rate_per_unit    = float(input("Enter per-unit rate          (NPR)  : "))
service_charge   = float(input("Enter fixed monthly service charge  : "))

# --- Calculations ---
units_consumed = current_reading - previous_reading
energy_charge  = units_consumed * rate_per_unit
total_bill     = energy_charge + service_charge

# --- Output ---
print()
print("=" * 50)
print("           📄  Electricity Bill")
print("=" * 50)
print(f"  Previous Reading         : {previous_reading:.2f} kWh")
print(f"  Current Reading          : {current_reading:.2f} kWh")
print(f"  Units Consumed           : {units_consumed:.2f} kWh")
print(f"  Energy Charge            : NPR {energy_charge:.2f}")
print(f"  Monthly Service Charge   : NPR {service_charge:.2f}")
print(f"  ─────────────────────────────────────")
print(f"  Total Bill               : NPR {total_bill:.2f}")
print("=" * 50)