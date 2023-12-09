def convert_to_24_hour(hour, minute, period):
    if period.lower() == "pm" and hour != 12:
        hour += 12
    elif period.lower() == "am" and hour == 12:
        hour = 0

    return f"{hour:02d}{minute:02d}"

# Example usage:
result = convert_to_24_hour(8, 30, "am")
print(result)  # Output: "0830"

result = convert_to_24_hour(8, 30, "pm")
print(result)  # Output: "2030"
