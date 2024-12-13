def exp_calculator(total_exp, exp_per_min):
    if exp_per_min <= 0:
        return "EXP per minute must be greater than 0."

    total_time_minutes = total_exp / exp_per_min
    hours = int(total_time_minutes // 60)
    minutes = int(total_time_minutes % 60)
    return f"Time required: {hours} hours {minutes} minutes."
    
print("")
total_exp = float(input("Enter the total EXP needed: "))
exp_per_min = float(input("Enter the EXP per minute: "))

result = exp_calculator(total_exp, exp_per_min)
print(result)
