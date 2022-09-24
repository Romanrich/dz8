from datetime import datetime, date
import calendar

for _ in range(20):
    print()


users = [
    {"name": "Alex", "birthday": datetime(year=1999, month=3, day=20)},
    {"name": "Miron", "birthday": datetime(year=1989, month=5, day=22)},
    {"name": "Sisyastaya", "birthday": datetime(year=2002, month=9, day=23)},
    {"name": "Zhopastaya", "birthday": datetime(year=2006, month=8, day=21)},
    {"name": "Serhiy", "birthday": datetime(year=1996, month=2, day=22)},
    {"name": "Leonid", "birthday": datetime(year=1996, month=4, day=20)},
    {"name": "Davalka", "birthday": datetime(year=1996, month=6, day=22)},
    {"name": "Roma", "birthday": datetime(year=1996, month=10, day=23)}
]




print("\n{:=^50}\n".format("-Birthday-"))





def get_birthday_per_week(users):
    current_month = date.today().month

    result = {}

    for person in users:

        month, day = person['birthday'].month, person['birthday'].day
        cur_year = date.today().year
        cur_day = date.today().day
        birthday = date(cur_year, month, day)
        if month != current_month:
            print("***")
            continue

        print(f'My name is {person["name"]} and my birthday {month}-{day}')

        print(f"Date of celebration - {birthday}")
        print(f"{birthday.strftime('%A %d-%m-%y')}")
        week_day = birthday.strftime('%A')
        weeks = calendar.monthcalendar(cur_year, month)

        print()
        for week in weeks:
            if cur_day in week:
                cur_week = week
                ind = weeks.index(week)
                pre_week = weeks[ind-1]
                working_week = pre_week[-2:]+cur_week[:-2]

                if day not in working_week:
                    print("Not this time")
                    continue

                print(f"Сurrent week - {cur_week}")
                print(f"Previos week - {pre_week}")
                print(f"Working week - {working_week}")

                if day in working_week[:2]:
                    if 'Monday' in result:
                        result['Monday'].append(person['name'])
                    else:
                        result['Monday'] = []
                        result['Monday'].append(person['name'])
                else:
                    if birthday.strftime('%A') in result:
                        result[week_day].append(person['name'])
                    else:
                        result[week_day] = []
                        result[week_day].append(person['name'])

                print(f"result is - {result}")
                break
            else:
                continue
        print("*"*10)
        for day in result:
            print(f"{day}: {', '.join(result[day])}")

        return "S DR!"


print(get_birthday_per_week(users))


