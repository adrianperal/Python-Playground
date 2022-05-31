def generate_report(main_tank, external_tank, hydrogen_tank):
    print(f"""
    Report:
    Main Tank: {main_tank}
    External Tank: {external_tank}
    Hydrogen Tank: {hydrogen_tank}
    """)
    return (main_tank+external_tank+hydrogen_tank)/3

average_fuel = generate_report(545, 1542, 325)
print(f"Average fuel: {average_fuel}")

def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60:.2f} hours"

print(sequence_time(5,15,30))
print(sequence_time(15,25,40))