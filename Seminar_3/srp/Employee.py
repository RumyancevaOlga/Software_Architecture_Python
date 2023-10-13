import datetime


class Employee:

    def __init__(self, name: str, dob: datetime.date, post: str):
        self.__name = name
        self.__dob = dob
        self.__post = post

    def __str__(self):
        return f'name={self.__name}, dob={self.__dob}, post={self.__post}'
