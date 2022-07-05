
listOfTemp = [100, 80, 90, 70]
thresHold = 20

# printer(elements)
# - Accepts a list
# - Prints every element of the list


def printer(elements):
    # Your code here
    for element in elements:
        print(element)


# to_celsius(temperatures)
# - Accepts a list of temperatures
#   in degrees Fahrenheit
# - Returns a list of temperatures
#   in degrees Celsius
# The conversion is:
#   C = (F - 32) * (5/9)
def to_celsius(temperatures):
    # Your code here

    listInC = []
    for tempreture in temperatures:
        tempretureInCelsius = (tempreture-32)*(5/9)
        listInC.append(tempretureInCelsius)

    return listInC


# hottest_days(temperatures, threshold)
# - Accepts a list of temperatures
# - Accepts a threshold temperature
# - Returns a list of temperatures
#   that exceed the threshold
def hottest_days(temperatures, threshold):
    # Your code here
    listOfHot = []
    for hotTempreture in temperatures:
        if hotTempreture > threshold:
            listOfHot.append(hotTempreture)
        else:
            None
    return listOfHot


# log_hottest_days(temperatures, threshhold)
# - Accepts a list of temperatures
#   IN DEGREES FAHRENHEIT
# - Accepts a threshold temperature
#   IN DEGREES FAHRENHEIT
# - Prints temperatures that exceed the
#   threshold IN DEGREES CELSIUS
# hint: you can combine
#       all previous functions
def print_hottest_days(temperatures, threshhold):
    # Your code here
    listOfCel = to_celsius(temperatures=listOfTemp)
    hottestList = hottest_days(temperatures=listOfCel, threshold=thresHold)
    print(hottestList)


printer(listOfTemp)
print_hottest_days(temperatures=listOfTemp, threshhold=thresHold)
