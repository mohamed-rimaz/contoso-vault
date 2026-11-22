DAYS_IN_WEEK : int = 7

days = int(input("days : "))


days_to_wait :int = int(input("days to wait :"))
delivery_day = days + days_to_wait

if delivery_day > DAYS_IN_WEEK:
   delivery_day = delivery_day - DAYS_IN_WEEK 

print("Delivery day:",delivery_day)

assert delivery_day < 1 and < DAYS_IN_WEEK