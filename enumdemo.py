from enum import Enum
from collections import namedtuple


StatusAttrs = namedtuple("StatusAttrs", ["name", "desc"])

class Status(Enum):
    PENDING = 1
    APPROVED = 2
    REJECTED = 3
    __attributes = [
        None,
        StatusAttrs("Pending","The request is pending approval."),
        StatusAttrs("Approved", "The request has been approved."),
        StatusAttrs("Rejected", "The request was rejected.")
    ]
    @property
    def name(self):
        return self.__attributes[self.value].name.lower()
    @property
    def Name(self):
        return self.__attributes[self.value].name
    @property
    def NAME(self):
        return self.__attributes[self.value].name.upper()
    @property
    def description(self):
        return self.__attributes[self.value].desc


x = Status.APPROVED
print(x)
print(x.value)
print(Status.APPROVED)
print(Status.APPROVED.value)
print(Status.APPROVED.name)
print(Status.APPROVED.Name)
print(Status.APPROVED.NAME)
print(Status.APPROVED.description)
