from datetime import date, timedelta
from dateutil.relativedelta import relativedelta
import random

choices: list[str] = [
    'add 4 years',
    'subtract 4 years',
    'subtract 5 days',
    'add 2 weeks',
]

timedeltamoments: list[str] = [
    'microseconds',
    'milliseconds',
    'seconds',
    'minutes',
    'hours',
    'days',
    'weeks',
]
moments: dict[str, str] = {
    'seconds': 'seconds',
    'second': 'seconds',
    'minute': 'minutes',
    'minutes': 'minutes',
    'hour': 'hours',
    'hours': 'hours',
    'day': 'days',
    'days': 'days',
    'week': 'weeks',
    'weeks': 'weeks',
    'month': 'months',
    'months': 'months',
    'year': 'years',
    'years': 'years',
}

def main():
    print("--- Welcome to Calendary ---\n")

    # Know your user
    name = input("May I know your name? ")
    print(f"\nHi, {name.title()} 👋")
    print("Let's get started...\n")

    # Display options for the entry date
    print("""Pick a starting date (choose between 1-3):
        1: Today
        2: Yesterday
        3: Enter a date..."""
    )
    try:
        entry_date_input = int(input())
        print("---")
    except ValueError:
        entry_date_input = 3

    # Set the entry date
    if entry_date_input == 1:
        entry_date = date.today()
    elif entry_date_input == 2:
        entry_date = date.today() - timedelta(days=1)
    else:
        try:
            entry_date_input = input(f"Enter a date (Y-m-d, e.g. {date.today()}): ")
            entry_date = date.fromisoformat(entry_date_input)
        except ValueError:
            print(f"Invalid Format: {entry_date_input}. Supported format: {date.today()}")
            exit(1)

    # Collect the command trail
    [symbol, number, moment] = askCommandTrail(f"What do you want to calculate? E.g. {random.choice(choices)}: ")
    realmoment = moments.get(moment)

    # Final calculation
    if realmoment not in timedeltamoments:
        if realmoment == 'months':
            answer = relativedelta(months=number)
        elif realmoment == 'years':
            answer = relativedelta(years=number)
    else:
        param = {
            realmoment: number
        }
        answer = timedelta(**param)


    if symbol == "add":
        print(f"{symbol.title()}ing {number} {moment} to {entry_date} is {entry_date + answer}")
    else:
        print(f"{symbol.title()}ing {number} {moment} to {entry_date} is {entry_date - answer}")


def askCommandTrail(question: str) -> list[str|int]:
    command_input = input(question)
    command = command_input.split(" ")

    symbol = None
    number = None
    moment = None

    try:
        # Validate the command
        if len(command) != 3:
            raise Exception("Incomplete")

        # Validate the symbol
        if command[0] not in ['add', 'subtract']:
            raise ValueError("Invalid command")
        symbol = command[0]

        # Validate the number
        number = int(command[1])

        # Validate the moment
        if command[2] not in moments.keys():
            raise ValueError("Invalid moment")
        moment = command[2]
    except Exception as err:
        askCommandTrail(f"{err}: Try '{random.choice(choices)}': ")

    return [symbol, number, moment]

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('\nGoodbye!')