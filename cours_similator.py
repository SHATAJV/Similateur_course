#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Course Simulator:
A program to simulate a trotting race.
"""

import random

total_distance = 2400
min_number_horses = 12
max_number_horses = 20


def start_dice():
    """
    Simulate rolling a six-sided die.

    Returns:
        int: A random integer between 1 and 6 inclusive.
    """
    return random.randint(1, 6)


def Speed(current_speed, DQ):
    """
    Update the speed of a horse based on its current speed and the dice roll.

    Args:
        current_speed (int): The current speed of the horse.
        DQ (bool): The disqualification status of the horse.

    Returns:
        tuple: Updated speed and disqualification status.
    """
    if DQ:
        return current_speed, DQ

    dice = start_dice()

    if current_speed == 0:
        if dice in [1, 2]:
            DQ = True
        elif dice in [3, 4, 5]:
            current_speed += 1
        elif dice in [6]:
            current_speed += 2
    elif current_speed == 1:
        if dice in [1]:
            pass
        elif dice in [2, 3, 4, 5]:
            current_speed += 1
        elif dice in [6]:
            current_speed += 2
    elif current_speed == 2:
        if dice in [1, 2]:
            pass
        elif dice in [3, 4, 5]:
            current_speed += 1
        elif dice in [6]:
            current_speed += 2
    elif current_speed == 3:
        if dice in [1]:
            current_speed -= 1
        elif dice in [2, 3]:
            pass
        elif dice in [4, 5]:
            current_speed += 1
        elif dice in [6]:
            current_speed += 1
    elif current_speed == 4:
        if dice in [1]:
            current_speed -= 1
        elif dice in [2, 3, 4]:
            pass
        elif dice in [5, 6]:
            current_speed += 1
    elif current_speed == 5:
        if dice in [1, 2]:
            current_speed -= 1
        elif dice in [3, 4, 5]:
            pass
        elif dice in [6]:
            current_speed += 1
    elif current_speed == 6:
        if dice in [1, 2]:
            current_speed -= 1
        elif dice in [3, 4, 5]:
            pass
        elif dice in [6]:
            DQ = True

    if current_speed < 0:
        current_speed = 0

    return current_speed, DQ


def position_horse(position, speed, DQ, time_elapsed):
    """
    Display the current positions, speeds, and disqualification statuses of all horses.

    Args:
        position (list): A list of positions for each horse.
        speed (list): A list of speeds for each horse.
        DQ (list): A list of disqualification statuses for each horse.
        time_elapsed (int): The time elapsed in the race in seconds.
    """
    print(f"\nTime elapsed: {time_elapsed} seconds")
    for i, pos in enumerate(position):
        status = "DQ" if DQ[i] else f"Position: {pos} m, Speed: {speed[i]} m/s"
        print(f"Horse {i + 1} - {status}")

        # Visual progression
        progress = int((pos / total_distance) * 50)  # Scale the progress bar to 50 characters
        print(f"[{'=' * progress}>{'.' * (50 - progress)}]")


def winner(positions):
    """
    Check if any horse has reached or exceeded the total distance.

    Args:
        positions (list): A list of positions for each horse.

    Returns:
        int or None: The index of the winning horse if there is a winner, otherwise None.
    """
    for i, pos in enumerate(positions):
        if pos >= total_distance:
            return i
    return None


def main():
    """
    The main function to run the trotting race simulator.
    """
    print("Welcome to the trotting race simulator!")

    while True:
        try:
            num_horses = int(input(f"Enter the number of horses ({min_number_horses} to {max_number_horses}): "))
            if min_number_horses <= num_horses <= max_number_horses:
                break
            else:
                print(f"Please enter a number between {min_number_horses} and {max_number_horses}.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            race_type = int(input("Enter the type of race (3 for Tiercé, 4 for Quarté, 5 for Quinté): "))
            if race_type in [3, 4, 5]:
                break
            else:
                print("Please enter a valid race type (3, 4, or 5).")
        except ValueError:
            print("Please enter a valid number.")

    # Initialize horses
    positions = [0] * num_horses
    speeds = [0] * num_horses
    DQ = [False] * num_horses
    time_elapsed = 0

    while True:
        input("Press Enter to advance the race by one turn...")
        time_elapsed += 10

        for i in range(num_horses):
            if not DQ[i]:
                speeds[i], DQ[i] = Speed(speeds[i], DQ[i])
                positions[i] += speeds[i] * 10  # Distance covered in 10 seconds

        position_horse(positions, speeds, DQ, time_elapsed)

        if all(DQ):
            print("All horses are disqualified. No winner.")
            break

        winning_horse = winner(positions)
        if winning_horse is not None:
            print(f"Horse {winning_horse + 1} has won the race!")
            break

    # Display the top N horses based on race type
    results = sorted([(pos, i) for i, pos in enumerate(positions)], reverse=True)[:race_type]
    print(f"\nTop {race_type} horses:")
    for pos, i in results:
        print(f"Horse {i + 1} - Position: {pos} m")


if __name__ == "__main__":
    main()

