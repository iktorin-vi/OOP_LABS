from abc import ABC, abstractmethod

class Person():
    def __init__(self, firstname, lastname):
        self.first_name = firstname
        self.last_name = lastname

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
