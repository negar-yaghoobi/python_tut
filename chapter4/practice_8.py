month = input('enter the month: ')
if month in ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand']:
    if month in ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar']:
        print(31)
    elif month in ['mehr', 'aban', 'azar', 'dey', 'bahman']:
        print(30)
    else:
        print(f'{29} or {30}')
else:
    print('your choice is false')