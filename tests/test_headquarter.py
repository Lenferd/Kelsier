from unittest import TestCase
from core.command_home.headquarter import Headquarter
from core.execution_unit.unit_status import UnitStatus


class TestHeadquarters(TestCase):
  def test_can_execute_create_todo_command(self):
    head = "create todo:"
    tail = "test todo from headquarters"
    exec_unit = Headquarter.process(head + tail)

    self.assertEqual(exec_unit.getStatus(), UnitStatus.OK)

  def test_can_initiate_interactive_process(self):
    initiate = "fill form:"
    exec_unit = Headquarter.process(initiate)
    self.assertEqual(exec_unit.getStatus(), UnitStatus.READY_TO_WORK)

  def test_can_get_question_for_user(self):
    initiate = "fill form"
    expected_question = "Question 1"
    exec_unit = Headquarter.process(initiate)
    question = exec_unit.getQuestion()
    self.assertEqual(expected_question, question)

  def test_can_get_sequence_of_questions(self):
    initiate = "fill form"
    expected_question = "Question 2"
    exec_unit = Headquarter.process(initiate)
    question1 = exec_unit.getQuestion()
    exec_unit.execute("Answer")
    question2 = exec_unit.getQuestion()
    self.assertEqual(expected_question, question2)

