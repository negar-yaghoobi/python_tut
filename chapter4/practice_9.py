month = input('enter the month: ')
if month in ['farvardin', 'ordibehesht', 'khordad', 'tir', 'mordad', 'shahrivar', 'mehr', 'aban', 'azar', 'dey', 'bahman', 'esfand']:
    if month in ['farvardin', 'ordibehesht', 'khordad']:
        print('bahar')
    elif month in ['tir', 'mordad', 'shahrivar']:
        print('tabestan')
    elif month in ['mehr', 'aban', 'azar']:
        print('paeez')
    else:
        print('zemestan')
else:
    print('your word is false')
