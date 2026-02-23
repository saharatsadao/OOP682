import csv
from .ILogSource import ILogSource


class CsvLogSource(ILogSource):

    def __init__(self, file_path: str):
        self.file_path = file_path

    def read_logs(self):
        logs = []

        with open(self.file_path, 'r', newline='', encoding="utf-8") as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # skip header

            for row in reader:
                if row:
                    log_entry = " ".join(row)
                    logs.append(log_entry)

        return logs