# Question 5: Taxi Fare Calculator

trips = [
    {"distance": 1.5, "hour": 14},
    {"distance": 5.0, "hour": 22},
    {"distance": 12.0, "hour": 3},
    {"distance": 8.5, "hour": 10},
    {"distance": 2.0, "hour": 23},
]

for trip_number, trip in enumerate(trips, start=1):
    distance = trip["distance"]
    hour = trip["hour"]

    if distance <= 2:
        fare = 150
    elif distance <= 10:
        fare = 150 + ((distance - 2) * 35)
    else:
        fare = 150 + (8 * 35) + ((distance - 10) * 28)

    night_trip = hour >= 22 or hour < 5

    if night_trip:
        fare = fare + (fare * 0.10)

    print(f"Trip {trip_number}")
    print(f"Distance: {distance} km")
    print(f"Travel hour: {hour}:00")

    if night_trip:
        print("Night surcharge applied: 10%")
    else:
        print("Night surcharge applied: No")

    print(f"Total taxi fare: NPR {fare:.2f}")
    print("-" * 30)
