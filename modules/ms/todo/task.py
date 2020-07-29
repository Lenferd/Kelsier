import json

class Task:
  def __init__(self, title: str):
    self._title = title
    self._importance = 'normal'
    self._isReminderOn = 'false'  # reminders for looser
    self._status = 'notStarted'

  def get_json(self):
    return json.dumps(self.get_dict())

  def get_dict(self):
    return {
      'title': self._title,
      'importance': self._importance,
      'isReminderOn': self._isReminderOn,
      'status': self._status
    }
