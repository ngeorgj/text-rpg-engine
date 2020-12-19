from game.utils.cmd_line_functions import cls

def clear_and_text(argument):
    cls()
    print(argument)

def text(content):
    print(f" {content}")

def game_says(content):
    print((len(content) + 3) * '-')
    print(" Game Says ")
    print((len(content) + 3) * '-')
    print(f'  {content}')
    print((len(content) + 3) * '-')
    print()

def get_month(integer):
    months = {
        'January'   :  1,
        'February'  :  2,
        'March'     :  3,
        'April'     :  4,
        'May'       :  5,
        'June'      :  6,
        'July'      :  7,
        'August'    :  8,
        'September' :  9,
        'October'   : 10,
        'November'  : 11,
        'December'  : 12
    }
    for month in months.items():
        if integer == month[1]:
            return month[0]
    else:
        return 'Error on utils/functions/get_month'
