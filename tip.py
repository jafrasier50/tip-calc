
import math
bill_total = str(input("Please enter Your bill Total: "))
tip_percentage = str(input("Please enter your desired tip percentage: "))

total = (float(bill_total) * float(tip_percentage))
# line below formats tip to round only two decimal places
tip_amount = ("{:.2f}".format(total))
print(f"Your added tip: {tip_amount}")
