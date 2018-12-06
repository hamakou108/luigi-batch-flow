import luigi
from luigi.mock import MockTarget
from luigi_batch_flow.batch import Batch


class Task(luigi.Task):
    """
    Parent class of all concrete batch tasks.
    """

    task_namespace = 'batch'

    required_task = None
    batch = Batch
    target = MockTarget("task.txt")

    def requires(self):
        """
        Returns:
            `luigi.Task` object assigned to `required_task`.
        """
        return self.required_task

    def run(self):
        """
        This method executes a batch script.
        """

        self.batch.run()
        with self.output().open('w') as output:
            output.write("{task} says: Hello world!".format(task=self.__class__.__name__))

    def output(self):
        """
        Returns:
            `luigi.Target` object assigned to `target`
        """

        return self.target

