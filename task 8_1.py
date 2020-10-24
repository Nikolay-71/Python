class Data:
    def __init__(self, day_month_year):
        self.day_month_year = str(day_month_year)

    @classmethod
    def extract(cls, day_month_year):
        my_date = []

        for i in day_month_year.split():
            if i != '-':
                my_date.append(i)

        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                return f'OK'
            else:
                return f'Wrong data'
        else:
            return f'Wrong data'

    def __str__(self):
        return f'Date {Data.extract(self.day_month_year)}'


date = Data('13 - 1 - 2001')
print(date)
print(date.valid(11, 14, 2001))
print(Data.valid(41, 11, 2001))
