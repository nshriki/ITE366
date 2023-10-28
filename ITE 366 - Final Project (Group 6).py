import calendar
from colorama import Fore, Style
import datetime as dt

now = dt.datetime.now()
print(f"{Fore.GREEN}""Current Date and Time:",
      f"{Fore.BLUE}", now.strftime("\n%B %d, %Y - %A\n%X %p"),
      f"{Style.RESET_ALL}")

def display_calendar(year, month, highlighted_days):
    cal = calendar.monthcalendar(year, month)
    print("  ", calendar.month_name[month], year)
    print("Mo Tu We Th Fr Sa Su")

    for week in cal:
        for day in week:
            if day == 0:
                print("  ", end=" ")
            elif day in highlighted_days:
                print(f"{Fore.RED}{day:2}{Style.RESET_ALL}", end=" ")
            else:
                print(f"{day:2}", end=" ")
        print()

# For highlighting the days in the calendar

# highlighting the sched of ITE 366 every monday of the month (September only)
highlight_ite366 = [4, 11, 18, 25]

# highlighting the sched of NST 021 every monday (SSP) & thursday (NSTP) of the month (September only)
highlight_nst021 = [4, 7, 11, 14, 18, 21, 25, 28]

# highlighting the sched of ITE 260 every tuesday & friday of the month (September only)
highlight_ite260 = [5, 8, 12, 15, 19, 22, 26, 29]

# highlighting the sched of GEN 002 every wednesday & saturday of the month (September only)
highlight_gen002 = [6, 9, 13, 16, 20, 23, 27, 30]

# highlighting the sched of PED 030 every saturday of the month (September only)
highlight_ped030 = [2, 9, 16, 23, 30]

year = 2023
month = 9

while True:
    project = input("\nEnter subject code: ")
    match project:
        case "ITE 366" | "ite 366" | "ITE366" | "ite366":
            print("Subject Description: " f"{Fore.LIGHTMAGENTA_EX}" "Introduction to Computing (including IT Fundamentals)" f"{Style.RESET_ALL}"
                  "\nSchedule: " f"{Fore.LIGHTMAGENTA_EX}" "Monday (9:00 AM - 4:00 PM)" f"{Style.RESET_ALL}"
                  "\nTeacher: " f"{Fore.LIGHTMAGENTA_EX}" "Engr. Jerry P. Tabon" f"{Style.RESET_ALL}"
                  "\n")
            display_calendar(year, month, highlight_ite366)

        case "NST 021" | "nst 021" | "NST021" | "nst021":
            print("Subject Description: " f"{Fore.LIGHTMAGENTA_EX}" "National Service Training Program 1" f"{Style.RESET_ALL}"
                  "\nSchedule: " f"{Fore.LIGHTMAGENTA_EX}" "SSP: Monday (4:00 PM - 5:30 PM) | NSTP: Thursday (4:00 PM - 5:30 PM)" f"{Style.RESET_ALL}"
                  "\nTeacher: " f"{Fore.LIGHTMAGENTA_EX}" "SSP - Mr. Roland N. Bolso & NSTP - Mr. Michael Franks M. Arcamo" f"{Style.RESET_ALL}"
                  "\n")
            display_calendar(year, month, highlight_nst021)

        case "ITE 260" | "ite 260" | "ITE260" | "ite260":
            print("Subject Description: " f"{Fore.LIGHTMAGENTA_EX}" "Computer Programming 1" f"{Style.RESET_ALL}"
                  "\nSchedule: " f"{Fore.LIGHTMAGENTA_EX}" "Tuesday (8:00 AM - 4:00 PM) | Friday (8:00 AM - 4:00 PM)" f"{Style.RESET_ALL}"
                  "\nTeacher: " f"{Fore.LIGHTMAGENTA_EX}" "Mr. Jimuel L. Destura" f"{Style.RESET_ALL}"
                  "\n")
            display_calendar(year, month, highlight_ite260)

        case "GEN 002" | "gen 002" | "GEN002" | "gen002":
            print("Subject Description: " f"{Fore.LIGHTMAGENTA_EX}" "Understanding the Self" f"{Style.RESET_ALL}"
                  "\nSchedule: " f"{Fore.LIGHTMAGENTA_EX}" "Wednesday (9:00 AM - 4:OO PM) | Saturday (9:00 AM - 4:00 PM)" f"{Style.RESET_ALL}"
                  "\nTeacher: " f"{Fore.LIGHTMAGENTA_EX}" "Ms. Joy Tiffany T. Degamo" f"{Style.RESET_ALL}"
                  "\n")
            display_calendar(year, month, highlight_gen002)

        case "PED 030" | "ped 030" | "PED030" | "ped030":
            print("Subject Description: " f"{Fore.LIGHTMAGENTA_EX}" "Physical Activities Toward Health and Fitness (PATHFit 1): Movement Competency Training" f"{Style.RESET_ALL}"
                  "\nSchedule: " f"{Fore.LIGHTMAGENTA_EX}" "Saturday (7:00 AM - 9:00 AM)" f"{Style.RESET_ALL}"
                  "\nTeacher: " f"{Fore.LIGHTMAGENTA_EX}" "Mr. Marino A. Garcia" f"{Style.RESET_ALL}"
                  "\n")
            display_calendar(year, month, highlight_ped030)

        case _:
            print(f"{Fore.RED}" "Invalid Input" f"{Style.RESET_ALL}")


    result = input("\nDo you want to enter another subject code? (Yes/No): ")
    if result == "No" or result == "no" or result == "NO":
        quit("Thank you for using our program! :)")
    elif result == "Yes" or result == "yes" or result == "YES":
        print()
    else:
        print(f"{Fore.RED}" "Invalid Input" f"{Style.RESET_ALL}")


# Updated Code :)
# GROUP 6 Members:

# 1. Atillo, Harold Andrei L.
# 2. Bernardo, Jilbert
# 3. Lariosa, Antonette
# 4. Pacifico, Melpame Melfe J.
# 5. Sohon, Bren D.
