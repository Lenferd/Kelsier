from unittest import TestCase
from modules.ms.one_note.one_note import OneNote

class TestOneNote(TestCase):
  def setUp(self) -> None:
    self.oneNote = OneNote()
    self.notebook = "TestNotebook"
    self.section = "TestSection"
    self.nameForRead = "TestPage"
    self.nameForModification = "ModificationPage"

  def test_can_get_page(self):
    page = self.oneNote.getPage(self.notebook, self.section, self.nameForRead)
    self.assertIsNotNone(page)

  def test_can_get_content_of_page(self):
    validation_text = "Text for validation"
    page = self.oneNote.getPage(self.notebook, self.section, self.nameForRead)
    text = page.getText()
    self.assertNotEqual(text.find(validation_text), -1)

  def test_can_modify_content_of_page(self):
    page = self.oneNote.getPage(self.notebook, self.section,
                                self.nameForModification)
    modification_text = "TextForModification"
    text = page.getText()
    self.assertNotEqual(text.find(modification_text), -1)

    paragraphs = page.getParagraphs()
    updated_paragraph = paragraphs[0]
    updated_paragraph['text'] = "New text"
    page.updateContent(updated_paragraph)
