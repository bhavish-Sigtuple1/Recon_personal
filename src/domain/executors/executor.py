from abc import ABC, abstractmethod
from garuda_algorithm.reader.reader_factory import Readers_Factory

class Executor(ABC):
    """
    Abstract base class for all executors.
    """

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def execute(self, reader: Readers_Factory = None):
        pass