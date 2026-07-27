# Question 3 - Date Converter for Nepal Bank System

bs_months = [
    "Baisakh", "Jestha", "Ashadh", "Shrawan",
    "Bhadra", "Ashwin", "Kartik", "Mangsir",
    "Poush", "Magh", "Falgun", "Chaitra"
]

customers = [
    {
        "name": "Ramesh Thapa",
        "date": "1985-06-24",
        "cal": "AD",
        "need": "BS",
        "style": "full"
    },
    {
        "name": "Sunita Karki",
        "date": "2055-09-10",
        "cal": "BS",
        "need": "AD",
        "style": "iso"
    },
    {
        "name": "Bikash Rai",
        "date": "1998-11-30",
        "cal": "AD",
        "need": "BS",
        "style": "nepali"
    },
    {
        "name": "Anjali Gurung",
        "date": "2040-01-05",
        "cal": "BS",
        "need": "AD",
        "style": "full"
    }
]


def convert_date(date_str, from_cal, to_cal):
    year, month, day = date_str.split("-")
    year = int(year)

    if from_cal == to_cal:
        new_year = year
    elif from_cal == "AD" and to_cal == "BS":
        new_year = year + 56
    elif from_cal == "BS" and to_cal == "AD":
        new_year = year - 56
    else:
        return "Invalid calendar type"

    return f"{new_year:04d}-{month}-{day}"


def day_with_suffix(day):
    day = int(day)

    if 10 <= day % 100 <= 20:
        suffix = "th"
    elif day % 10 == 1:
        suffix = "st"
    elif day % 10 == 2:
        suffix = "nd"
    elif day % 10 == 3:
        suffix = "rd"
    else:
        suffix = "th"

    return f"{day}{suffix}"


def format_date(date_str, calendar, style):
    year, month, day = date_str.split("-")
    month_number = int(month)

    if style == "iso":
        return f"{date_str} {calendar}"

    if calendar == "BS":
        month_name = bs_months[month_number - 1]

        if style == "full":
            return f"{day_with_suffix(day)} {month_name}, {year} {calendar}"

        if style == "nepali":
            return f"{int(day)} {month_name} {year} {calendar}"

    return f"{date_str} {calendar}"


for customer in customers:
    converted_date = convert_date(
        customer["date"],
        customer["cal"],
        customer["need"]
    )

    final_date = format_date(
        converted_date,
        customer["need"],
        customer["style"]
    )

    print(
        f"{customer['name']} | "
        f"Original: {customer['date']} {customer['cal']} | "
        f"Converted: {final_date}"
    )
