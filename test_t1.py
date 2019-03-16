import datetime
from dateutil.relativedelta import relativedelta



def test_check_old(app):
    open('results.txt', 'w').close() # Чистим содержимое файла
    app.open_home_page()
    d = datetime.date(1992, 1, 1)
    last_date = datetime.date(2020, 3, 1)

    while d < last_date:
        now = datetime.date.today()
        #d += datetime.timedelta(days=1) # +1 день
        d += relativedelta(months=+1) # +1 месяц
        #d += relativedelta(years=+1) # +1 год

        date_for_site = fill_date_for_site(d)

        app.fill_date(date_for_site)
        app.click_button()
        age = app.get_value_age()
        age_only = age.split(' ')[0] # Берём то, что до пробела
        correct_age = relativedelta(now, d)

        f = open('results.txt', 'a', encoding='utf-8')

        if age.split(' ')[1][0] in 'лг':
            if int(age_only) == correct_age.years:
                f.write(date_for_site + '  ----  ' + age + '  ----  УСПЕХ  ----  ' + str(correct_age) + '\n')
            else:
                f.write(date_for_site + '  ----  ' + age + '  ----  БАГ  ----  ' + str(correct_age) + '\n')
        elif age.split(' ')[1][0] == 'м':
            if int(age_only) == correct_age.months:
                f.write(date_for_site + '  ----  ' + age + '  ----  УСПЕХ  ----  ' + str(correct_age) + '\n')
            else:
                f.write(date_for_site + '  ----  ' + age + '  ----  БАГ  ----  ' + str(correct_age) + '\n')
        elif age.split(' ')[1][0] == 'д':
            if int(age_only) == correct_age.days:
                f.write(date_for_site + '  ----  ' + age + '  ----  УСПЕХ  ----  ' + str(correct_age) + '\n')
            else:
                f.write(date_for_site + '  ----  ' + age + '  ----  БАГ  ----  ' + str(correct_age) + '\n')

        f.close()


def fill_date_for_site(d):
    if d.day < 10:
        date_for_site = '0%s.' % d.day
    else:
        date_for_site = '%s.' % d.day
    if d.month < 10:
        date_for_site += '0%s.' % d.month
    else:
        date_for_site += '%s.' % d.month
    date_for_site += '%s' % d.year
    return date_for_site







