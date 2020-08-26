from unittest import TestCase
from core.command_home.headquarter import Headquarter
from core.execution_unit.unit_status import UnitStatus


class TestHeadquarters(TestCase):
  def setUp(self) -> None:
    initiate = "fill page"
    text_to_set_1 = "Question 1: { Question 1 reply } "
    text_to_set_2 = "Question 2: { Question 2 reply } "
    exec_unit_set = Headquarter.process(initiate)
    exec_unit_set.execute(text_to_set_1)
    exec_unit_set.execute(text_to_set_2)

  def test_can_execute_create_todo_command(self):
    head = "create todo:"
    tail = "test todo from headquarters"
    exec_unit = Headquarter.process(head + tail)

    self.assertEqual(exec_unit.getStatus(), UnitStatus.OK)

  def test_can_initiate_interactive_process(self):
    initiate = "fill form:"
    exec_unit = Headquarter.process(initiate)
    self.assertEqual(exec_unit.getStatus(), UnitStatus.HAVE_QUESTION)

  def test_can_get_question_for_user(self):
    initiate = "fill form"
    expected_question = "Question 1"
    exec_unit = Headquarter.process(initiate)
    question = exec_unit.getQuestion()
    self.assertEqual(expected_question, question)

  def test_can_get_sequence_of_questions(self):
    initiate = "fill form"
    exec_unit = Headquarter.process(initiate)
    question1 = exec_unit.getQuestion()

    exec_unit.execute("Answer")

    question2 = exec_unit.getQuestion()
    expected_question = "Question 2"
    self.assertEqual(expected_question, question2)

  def test_can_can_read_oneNote(self):
    initiate = "read note"
    exec_unit = Headquarter.process(initiate)
    text = exec_unit.execute("get first")

    expected_text = "Question 1: { Question 1 reply }"
    self.assertEqual(expected_text.strip(), text.strip())

  def test_can_reply_for_question(self):
    initiate = "fill form"
    answer = "Answer"
    exec_unit = Headquarter.process(initiate)
    question1 = exec_unit.getQuestion()
    exec_unit.execute(answer)

    initiate = "read note"
    exec_unit = Headquarter.process(initiate)
    text = exec_unit.execute("get first")

    expected_answer = "Question 1: " + answer
    self.assertEqual(expected_answer, text)

  def test_can_set_line(self):
    initiate = "fill page"
    text_to_set = "KEK"
    exec_unit_set = Headquarter.process(initiate)
    exec_unit_set.execute(text_to_set)

    initiate = "read note"
    exec_unit_get = Headquarter.process(initiate)
    result_text = exec_unit_get.execute("get first")
    self.assertEqual(text_to_set, result_text)

  # TODO For now test with my faith
  def test_can_set_two_lines(self):
    pass

