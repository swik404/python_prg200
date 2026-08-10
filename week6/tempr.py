import math

station_name = "Kathmandu Weather Station"
temperatures = [18.4, 22.1, 15.7, 29.3, 11.8, 25.6, 19.2]

def get_average(temps):
    return sum(temps) / len(temps)

def get_deviation(temps):
    mean = get_average(temps)  # local variable
    variance = sum((temp - mean) ** 2 for temp in temps) / len(temps)
    return math.sqrt(variance)

def get_summary(temps):
    print("Station:", station_name)
    print("Minimum Temperature:", min(temps))
    print("Maximum Temperature:", max(temps))
    print("Average Temperature:", round(get_average(temps), 2))
    print("Standard Deviation:", round(get_deviation(temps), 2))

get_summary(temperatures)

# print(mean)
# This would cause NameError because 'mean' is local to get_deviation().
