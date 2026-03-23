'''
### Travel Weather Planner – Notes

This program determines whether commuting is possible based on distance, weather conditions, and available transportation.

* If the distance is falsy (e.g., 0), commuting is not possible.
* For distances ≤ 1 mile, commuting is only possible if it is not raining (walking).
* For distances between 1 and 6 miles, commuting is only possible if the user has a bike and it is not raining.
* For distances > 6 miles, commuting is possible if the user has a car or access to a ride-share app.

The logic uses conditional statements (`if`, `elif`, `else`) to evaluate each scenario in order and outputs a boolean (`True` or `False`).

'''


distance_mi = 0
is_raining = False
has_bike = False
has_car = False
has_ride_share_app = False


#NOTES
#1 less than or equal to 1m and not raining = True else false
#2 greater than or equal to 1m and less than or equal to 6 miles = True only if person has a bike and != raining else false
#3 greater than = True only if the person has a car or has a ride-share app else false


if distance_mi == 0:
    print(False)
elif distance_mi <=1 and not is_raining:
    print(True)
elif distance_mi >1 and distance_mi <= 6 and has_bike and not is_raining:
    print(True)
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True)
else:
    print(False)