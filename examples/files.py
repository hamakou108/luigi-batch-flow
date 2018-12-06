from luigi_batch_flow.file import File


class File1(File):
    """
    File1 is an example.
    """

    def __init__(self):
        super().__init__()
        self.name_template = "file1_{{ date|datetimeformat(%Y%m%d) }}.csv"
        self.destination = "./tmp"
        self.item_dict['first_name'] = "Peter"
        self.item_dict['last_name'] = "Parker"
        self.item_dict['age'] = 28


class File2(File):
    """
    File2 is an example.
    """

    def __init__(self):
        super().__init__()
        self.name_template = "file2_{{ date|datetimeformat(%Y%m%d) }}.csv"
        self.destination = "./tmp"
        self.item_dict['name'] = "omurice"
        self.item_dict['price'] = 980


class File3(File):
    """
    File3 is an example.
    """

    def __init__(self):
        super().__init__()
        self.name_template = "file3_{{ date|datetimeformat(%Y%m%d) }}.csv"
        self.destination = "./tmp"
        self.item_dict['country'] = "Japan"
        self.item_dict['prefecture'] = "Tokyo"

