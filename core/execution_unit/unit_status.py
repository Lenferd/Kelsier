from enum import Enum


class UnitStatus(Enum):
  ERROR = -1
  OK = 0

  READY_TO_WORK = 10
  HAVE_QUESTION = 11