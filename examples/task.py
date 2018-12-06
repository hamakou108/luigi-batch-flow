from luigi.mock import MockTarget

from examples import batch as b
from luigi_batch_flow.task import Task


class FirstTask(Task):
    """
    FirstTask is an example.
    """

    batch = b.FirstBatch()
    target = MockTarget("first_task.txt")


class SecondTask(Task):
    """
    SecondTask is an example.
    """

    required_task = FirstTask()
    batch = b.SecondBatch()
    target = MockTarget("second_task.txt")

