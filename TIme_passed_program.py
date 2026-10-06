import datetime

def parse_target_date(date_str):
    result= datetime.datetime.strptime(date_str, "%Y-%m-%d")
    return result

def get_days_remaining(target_date):
    current_time=datetime.datetime.now()
    difference= target_date-current_time
    return difference.days

def format_milestone(date_obj):
    date_obj=datetime.datetime.strftime(date_obj, "%B %d, %Y")
    return date_obj

if __name__ == "__main__":

    user_input=input("Enter target date (YYYY-MM-DD): ")
    
    try:
        target=parse_target_date(user_input)
        days_left=get_days_remaining(target)
        formatted_date=format_milestone(target)

        if days_left<0:
            print("That date has already passed!")
        else:
            print(f"There are {days_left} days left until {formatted_date}.")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")