def calculate_outcome(pass_credits, defer_credits, fail_credits):
    total_credits = pass_credits + defer_credits + fail_credits

    
    if total_credits != 120:
        return "Total incorrect."

    
    if pass_credits == 120:
        return "Progress"
    elif pass_credits == 100:
        return "Progress (module trailer)"
    elif pass_credits <= 80 and (fail_credits<80 or defer_credits>=40):
        return "Do not progress-module retriever"
       
    elif fail_credits>=80 or defer_credits<40:
        return "Exclude"

    
    return "Out of range."


def validate_input(credit_value):
    try:
        credit_value = int(credit_value)
        if credit_value not in [0, 20, 40, 60, 80, 100, 120]:
            return "Out of range"
        else:
            return credit_value
    except ValueError:
        return "Integer required"


progress_count = 0
trailer_count = 0
retriever_count = 0
exclude_count = 0
progress_data = []
trailer_data = []
retriever_data = []
exclude_data = []


while True:
    pass_credits = input("Enter your total PASS credits (press q to quit): ")
    if pass_credits == 'q':
        break
    defer_credits = input("Enter your total DEFER credits: ")
    fail_credits = input("Enter your total FAIL credits: ")

    
    pass_credits = validate_input(pass_credits)
    defer_credits = validate_input(defer_credits)
    fail_credits = validate_input(fail_credits)

    
    if pass_credits == "Integer required" or defer_credits == "Integer required" or fail_credits == "Integer required":
        print("Integer required.")
        continue
    elif pass_credits == "Out of range" or defer_credits == "Out of range" or fail_credits == "Out of range":
        print("Out of range.")
        continue
    elif pass_credits == 0 and defer_credits == 0 and fail_credits == 0:
        break
    elif pass_credits == "Total incorrect.":
        print("Total incorrect.")
        continue

    # calculate the progression outcome
    outcome = calculate_outcome(pass_credits, defer_credits, fail_credits)

    
    print(outcome)

    # list data
    if outcome == "Progress":
        progress_count += 1
        progress_data.append([pass_credits, defer_credits, fail_credits])
    elif outcome == "Progress (module trailer)":
        trailer_count += 1
        trailer_data.append([pass_credits, defer_credits, fail_credits])
    elif outcome == "Do not progress – module retriever":
        retriever_count += 1
        retriever_data.append([pass_credits, defer_credits, fail_credits])
    elif outcome == "Exclude":
        exclude_count += 1
        exclude_data.append([pass_credits, defer_credits, fail_credits])

for data, outcome in [(progress_data, "Progress"), (trailer_data, "Progress (module trailer)"), (retriever_data, "Do not progress – module retriever"), (exclude_data, "Exclude")]:
    for credits in data:
        print(outcome, "-", credits[0], ",", credits[1], ",", credits[2])
       
