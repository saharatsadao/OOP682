from file_log_source import FileLogSource
from csv_log_source import CsvLogSource

def get_log_source(filepath):
    if filepath.lower().endswith(".csv"):
        return CsvLogSource(filepath)
    return FileLogSource(filepath)