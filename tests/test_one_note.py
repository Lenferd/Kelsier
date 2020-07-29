from unittest import TestCase
from modules.ms.one_note.one_note import OneNote

class TestOneNote(TestCase):
  def setUp(self) -> None:
    self.one_note = OneNote()

  def test_can_get_content_of_page(self):
    notebook = "TestNotebook"
    section = "TestSection"
    pageName = "TestPage"
    page = self.one_note.get_page(notebook, section, pageName)
    self.assertIsNotNone(page)
