# -----------------------------------------------------------------------------
# Author: Jasmine Oliveira
# Date:   10/2016
# -----------------------------------------------------------------------------
# virtual_calendar.py
# -----------------------------------------------------------------------------
# Module designed to represent a virtual calendar. Functions allow you to iterate
# through dates in a year, and get the corresponding string or integer values.
#
#       Public Functions:
#           * get_next_date(self)
#           * get_year(self)
#           * get_month_abbr
#           * get_weekday_abbr
#           * get_day(self)
#
#       Private Functions:
#           * __adjust_iterator__(self, day, year)
#
import calendar


class VirtualCalendar:

    def __init__(self, day, month, year):
        """
        Initialize a Virtual Calendar object with
        the start day, month and year.
        :param day:
        :param month:
        :param year:
        """

        ''' Set Calendar Object '''
        self.calendar_obj = calendar.Calendar()

        ''' Current date '''
        self.date = None

        ''' Initialize Calendar Iterator '''
        self.month_iterator = self.calendar_obj.itermonthdates(year, month)
        self.__adjust_iterator__(day, year)

    def __adjust_iterator__(self, day, year):
        """
        Private method that adjusts the current
        calendar date in the month iterator, so it begins on the
        given day and year of the given month.
        :param day: Day for the iterator to move to
        :param year: Year for the iterator to move to
        """

        for date in self.month_iterator:
            if (date.day == day) and (date.year == year):
                self.date = date
                break

    def get_next_date(self):
        """
        Gets the next date, after the current date.
        :return: Next date object
        """

        try:
            self.date = self.month_iterator.next()
        except:
            day = self.date.day
            month = self.date.month
            year = self.date.year
            self.month_iterator = self.calendar_obj.itermonthdates(year, month)
            self.date = self.month_iterator.next()
            self.__adjust_iterator__(day, year)

        return self.date

    def get_day(self):
        """
        :return: Integer value of the current year
        """
        return self.date.day

    def get_year(self):
        """
        :return: Integer value of the current year
        """
        return self.date.year

    def get_weekday_abbr(self):
        """
        :return: Abbreviated string of the current weekday
        """
        return calendar.day_abbr[self.date.weekday()]

    def get_month_abbr(self):
        """
        :return: Abbreviated string of the current weekday
        """
        return calendar.month_abbr[self.date.month]


def main():
    '''
    Example of virtual calendar
    '''

    # Initialize calendar
    virtual_calendar = VirtualCalendar(30, 11, 2016)

    # Display current day, month, and weekday
    print virtual_calendar.get_day()
    print virtual_calendar.get_month_abbr()
    print virtual_calendar.get_weekday_abbr()

    i=0
    # Display the next 60 Dates
    while i< 60:
        virtual_calendar.get_next_date()
        i += 1
        print virtual_calendar.date

if __name__ == '__main__':
    main()

