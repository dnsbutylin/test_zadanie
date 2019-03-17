import datetime
from dateutil.relativedelta import relativedelta


def test_check_old(app):
    app.open_home_page()
    startdate = datetime.date(1, 1, 1)  # (Год, месяц, день)
    last_date = datetime.date(10, 1, 1)

    open('%s - %s.txt' % (startdate, last_date), 'w').close()  # Чистим содержимое файла

    d = startdate

    while d < last_date:
        now = datetime.date.today()

        #flag = 0
        #if 1 <= d.year <= now.year - 2000:
        #    d += relativedelta(years=+2000)
        #    flag = 1
        #if now.year - 2000 <= d.year <= 99:
        #    d += relativedelta(years=+1900)
        #    flag = 2

        d += datetime.timedelta(days=1)  # +1 день
        # d += relativedelta(months=+1) # +1 месяц
        # d += relativedelta(years=+1) # +1 год

        date_for_site = fill_date_for_site(d)

        app.fill_date(date_for_site)
        app.click_button()
        age = app.get_value_age()
        age_only = age.split(' ')[0]  # Берём то, что до пробела

        if 1 <= d.year <= now.year - 2000:
            correct_age = relativedelta(now, d) + relativedelta(years=-2000)
        elif now.year - 2000 <= d.year <= 99:
            correct_age = relativedelta(now, d) + relativedelta(years=-1900)
        else:
            correct_age = relativedelta(now, d)


        f = open('%s - %s.txt' % (startdate, last_date), 'a', encoding='utf-8')

        if age.split(' ')[1][0] in 'лг':
            if age_only == str(correct_age.years):
                f.write(date_for_site + '  ----  ' + age + '  ----  УСПЕХ  ----  ' + str(correct_age) + '\n')
            else:
                f.write(date_for_site + '  ----  ' + age + '  ----  БАГ  ----  ' + str(correct_age) + '\n')


        elif age.split(' ')[1][0] == 'м' and str(correct_age.years) == '0':
            if age_only == str(correct_age.months):
                f.write(date_for_site + '  ----  ' + age + '  ----  УСПЕХ  ----  ' + str(correct_age) + '\n')
            else:
                f.write(date_for_site + '  ----  ' + age + '  ----  БАГ  ----  ' + str(correct_age) + '\n')


        elif age.split(' ')[1][0] == 'д' and str(correct_age.years) == '0' and str(correct_age.months) == '0':

            if age_only == str(correct_age.days):
                f.write(date_for_site + '  ----  ' + age + '  ----  УСПЕХ  ----  ' + str(correct_age) + '\n')
            else:
                f.write(date_for_site + '  ----  ' + age + '  ----  БАГ  ----  ' + str(correct_age) + '\n')


        else:
            f.write(date_for_site + '  ----  ' + age + '  ----  СУПЕР БАГ  ----  ' + str(
                correct_age) + '\n')

        f.close()

        #if flag == 1:
        #    d += relativedelta(years=-2000)
        #if flag == 2:
        #    d += relativedelta(years=-1900)

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







