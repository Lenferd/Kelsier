from unittest import TestCase
from modules.ms.one_note.one_note import OneNote

class TestOneNote(TestCase):
  def setUp(self) -> None:
    self.one_note = OneNote()
    self.notebook = "TestNotebook"
    self.section = "TestSection"
    self.pageName = "TestPage"
    self.validationText = "Text for validation"

  def test_can_get_page(self):
    page = self.one_note.get_page(self.notebook, self.section, self.pageName)
    self.assertIsNotNone(page)

  def test_can_get_content_of_page(self):
    page = self.one_note.get_page(self.notebook, self.section, self.pageName)
    content = page.getContent()
    self.assertNotEqual(content.find(self.validationText), -1)
