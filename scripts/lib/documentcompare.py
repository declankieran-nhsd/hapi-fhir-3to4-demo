from abc import ABC, abstractmethod


class DocumentCompare(ABC):

    @abstractmethod
    def generate_comparison(self, input_file, transformed_file) -> dict:
        pass

