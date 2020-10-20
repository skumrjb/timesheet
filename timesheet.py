"""
Goal of the timesheet is to ensure I have reached 4 hours of focussed productive work workflow:

Aim - Open the terminal and run the script to note the start of the clock

2 - User types in the prompt - 'in' to start the clock details of the day and time are stored in the .csv

3 - User types in the prompt - 'end' end the app records the timeout

this action will also record the total time of the session in a separate column

4 - if the clock is started later in the day - the timesheet should be able to do steps 2 and 3

5 - at the end of the week (Sunday) a graph is plotted against day of the week and number of hours spent - incomplete

the results are saved in the directory as a jpg and sent as an attachment to my email id - incomplete
"""

import datetime
import csv
import os.path

Username = input('Please enter the username: ')
print('Please enter the timesheet code to begin')
action = input('Punch (in/out): ')

if action == 'in':

    clock = datetime.datetime.now()
    timesheet_log = []


    def punch_action(user_name, user_action):
        time_of_punch = datetime.datetime.now()
        print(f'{user_name}, your punch was recorded at {time_of_punch.hour}:{time_of_punch.minute} \n'
              f'Timesheet status is: {user_action}')


    def punch_out(time):
        clock_time = time.now()
        total = clock_time - startTime
        print(f'Total time of your session is {total}')
        timesheet_log.append(
            {'Username': Username,
             'Date': str(startTime.date()),
             'Start Time': str(startTime.hour) + ':' + str(startTime.minute) + ':' + str(startTime.second),
             'End Time': str(clock_time.hour) + ':' + str(clock_time.minute) + ':' + str(clock_time.second),
             'Total Time': str(total.seconds)})


    """
    Displaying program's instructions and collecting the username and action
    """

    punch_action(Username, action)

    try:
        startTime = clock
        action2 = input('Punch (in/out): ')

        if action2 == 'out':
            punch_action(Username, action2)
            punch_out(clock)
            print(timesheet_log)

            # Creating a custom csv file to add with timesheet punches
            file_name = 'timesheet_log' + '.csv'

            # Exporting the data dict into the custom datecsv file

            with open(file_name, 'a+', newline='') as into_csv:
                writer = csv.DictWriter(into_csv, timesheet_log[0])
                file_is_empty = os.stat('timesheet_log.csv').st_size == 0  # to check if file is empty

                if file_is_empty:
                    writer.writeheader()  # writes the row header, since the file is empty

                for rows in timesheet_log:
                    writer.writerow(rows)

        elif action2 == action:
            print('You cannot have duplicate punch-ins')
            punch_out(clock)

        else:
            print('Your punch-out code is incorrect')
            punch_out(clock)

    except KeyboardInterrupt:
        punch_out(clock)

else:
    raise Exception('Please enter a valid response to begin the timesheet')