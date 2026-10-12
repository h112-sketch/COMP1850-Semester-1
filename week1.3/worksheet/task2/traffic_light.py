"""
Portfolio Task - Week 1.3
By submitting this code you are declaring that all work in this file, other than any provided template code, was written and developed by you independently.
Name: Haris Mehmood
"""

states = { "red":4, "red_amber":3, "green":5, "amber":3 }

systime = 0
maxtime = int(input("How many steps to simulate?"))  # read an integer number of steps (>0)

state = "red"
stepsOnState = 0

for steps in range(1, maxtime + 1):
    if state == "red" and stepsOnState == states["red"]:
        stepsOnState = 0
        state = "red_amber"
    elif state == "red_amber" and stepsOnState == states["red_amber"]:
        state = "green"
        stepsOnState = 0
    elif state == "green" and stepsOnState == states["green"]:
        state = "amber"
        stepsOnState = 0
    elif state == "amber" and stepsOnState == states["amber"]:
        state = "red"
        stepsOnState = 0


    print(f"Time {systime:03} State {state}")
    systime += 1
    stepsOnState += 1



# Simulate the traffic light system up to time=maxtime in 1-second steps

# At the end of each step you should output the time and state using the statement on line 14