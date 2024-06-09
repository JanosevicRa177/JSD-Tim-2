from abc import ABC, abstractmethod


class Command(ABC):

    @abstractmethod
    def run_command(self) -> bool:
        pass

    @abstractmethod
    def is_regular_move(self) -> bool:
        pass
