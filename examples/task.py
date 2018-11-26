import luigi
from luigi.mock import MockTarget
from luigi_batch_flow.batch import Batch
from examples.batch import FirstBatch


class BaseTask(luigi.Task):
    """
    Parent class of all concrete batch tasks.
    """

    task_namespace = 'batch'
    batch = None

    def run(self):
        """
        Execute a task.
        """

        self.batch.run()
        with self.output().open('w') as output:
            output.write("{task} says: Hello world!".format(task=self.__class__.__name__))

    def output(self):
        """
        Generate an output file.
        """

        return MockTarget("first_task.txt")


class FirstTask(BaseTask):
    """
    FirstTask is an example.
    """

    task_namespace = 'batch'
    batch = FirstBatch()


#if __name__ == '__main__':
#    luigi.run(['batch.FirstTask', '--workers', '1', '--local-scheduler'])

