class Time:
    """Represents and manipulates hours and minutes"""
    def __init__(self, hour=12, minute=0):
        valid_hour, valid_minute = Time.make_valid(hour, minute)
        self.__hour = valid_hour
        self.__minute = valid_minute

    def __str__(self):
        return "{0}:{1:02}".format(self.__hour, self.__minute)

    def __add__(self, other):
        return Time.add_minute(Time.add_hour(self, other.__hour),
                               other.__minute)

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def is_valid_time(self):
        return Time.is_valid_hour(self.__hour) and Time.is_valid_minute(self.__minute)

    def add(self, other):
        result_time = self + other
        self.__hour = result_time.__hour
        self.__minute = result_time.__minute

    @staticmethod
    def add_hour(other, hour):
        """
        :rtype: Time
        """
        return Time(other.__hour + hour, other.__minute)

    @staticmethod
    def add_minute(other, minute):
        return Time(other.__hour, other.__minute + minute)

    @staticmethod
    def is_valid_hour(hour):
        return 1 <= hour <= 12

    @staticmethod
    def is_valid_minute(minute):
        return 0 <= minute < 60

    @staticmethod
    def make_valid(hour, minute):
        valid_minute, carryover_hour = Time.make_valid_minute(minute)
        valid_hour = Time.make_valid_hour(hour)
        return valid_hour + carryover_hour, valid_minute

    @staticmethod
    def make_valid_hour(hour):
        if not Time.is_valid_hour(hour):
            valid_hour = hour % 12
        else:
            valid_hour = hour
        return valid_hour

    @staticmethod
    def make_valid_minute(minute):
        """
        :param minute:
        :return:
        """
        if not Time.is_valid_minute(minute):
            valid_minute = minute % 60
            carryover_hour = minute // 60
        else:
            valid_minute = minute
            carryover_hour = 0
        return valid_minute, carryover_hour

    @staticmethod
    def from_string(time_str):
        """
        Semi-constructor from string
        :param time_str: String representing time (ex: 5:09)
        :return: Time object represented by time_str
        """
        hour, minute = map(int, time_str.strip().split(":"))
        return Time(hour, minute)


def get_time_from_user(time_kind):
    """
    Prompts for "time_kind time" and returns inputted time
    :rtype: Time
    """
    try:
        entered_time = (input("Enter " + time_kind + " time (HH:MM): "))
        return Time.from_string(entered_time)
    except ValueError:
        print("Must enter a time (ex: 5:09)")
        return get_time_from_user(time_kind)
    except ImportError:
        print("Entered time not valid (1-12)")
        return get_time_from_user(time_kind)

startTime = get_time_from_user("start")
timerTime = get_time_from_user("timer")
endTime = startTime + timerTime
print("End time: " + str(endTime))
