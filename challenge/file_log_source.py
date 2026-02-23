from .ILogSource import ILogSource


class FileLogSource(ILogSource):

    def __init__(self, filepath):
        self.filepath = filepath

    def read_logs(self):
        logs = []
        with open(self.filepath, encoding="utf-8") as f:
            for line in f:
                logs.append(line.strip())
        return logs