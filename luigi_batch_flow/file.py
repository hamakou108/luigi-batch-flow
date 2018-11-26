from collections import OrderedDict


class File:
    """
    The subclass of File has fields correspond to items of the data file.
    Each field must have a default value.
    """

    def __init__(self):
        self.item_dict = OrderedDict()


class FileGenerator:
    """
    FileGenerator creates input files of a batch.
    """

    def render_path(self):
        """
        Render path based on template string.
        """

        pass

    def generate(self, f):
        """
        Create input files based on file information.
        """

        self.render_path()

        print(f.name_template)
        print(f.destination)
        for k, v in f.item_dict.items():
            print("{key}: {val}".format(key=k, val=v))
        print()

