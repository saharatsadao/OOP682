from .file_log_source import FileLogSource
from .csv_log_source import CsvLogSource


class LogSourceFactory:

    @staticmethod
    def create_log_source(source_type: str, **kwargs):

        if source_type == "file":
            return FileLogSource(kwargs.get("file_path"))

        elif source_type == "csv":
            return CsvLogSource(kwargs.get("file_path"))

        else:
            raise ValueError(f"Unknown source type: {source_type}")