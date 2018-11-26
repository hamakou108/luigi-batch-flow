import subprocess
import sys
from luigi_batch_flow.file import FileGenerator


class Batch:
    """
    Batch prepares and executes a batch script.
    """

    def __init__(self):
        self.input_files = []
        self.script_path = ""

    def prepare(self):
        """
        Run some tasks for preparation before execution of a batch script.
        """

        # create input files
        fg = FileGenerator()
        for f in self.input_files:
            fg.generate(f)

    def execute(self):
        """
        Execute batch script.
        """
        subprocess.run("sh {script}".format(script=self.script_path), shell=True, check=True)

    def run(self):
        """
        Run batch.
        """

        self.prepare()
        self.execute()
        return True

