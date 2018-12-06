from luigi_batch_flow.batch import Batch
from examples import files as f


class FirstBatch(Batch):
    """
    FirstBatch is an example.
    """

    def __init__(self):
        self.input_files = [
            f.File1(),
            f.File2()
        ]
        self.script_path = "./examples/script/first_batch.sh"


class SecondBatch(Batch):
    """
    SecondBatch is an example.
    """

    def __init__(self):
        self.input_files = [
            f.File3()
        ]
        self.script_path = "./examples/script/second_batch.sh"

