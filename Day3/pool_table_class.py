class PoolTable:
    def __init__(self, table_number):
        self.table_number = table_number
        self.is_occupied = False
        self.start_time = None
        self.end_time = None

    def check_out(self):
        self.is_occupied = True
        self.end_time = datetime.datetime.now()

    def check_in(self):
        self.is_occupied = False
        self.start_time = now

    def total_time_played(self):
        self.start_time = start_time
        self.end_time = end_time
        return end_time - start_time
