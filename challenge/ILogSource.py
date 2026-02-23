from abc import ABC, abstractmethod

class ILogSource(ABC):

    @abstractmethod
    def read_logs(self):
        pass