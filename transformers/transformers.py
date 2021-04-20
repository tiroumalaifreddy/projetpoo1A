from abc import ABC, abstractmethod

class Transformers(ABC):
    def __init__(self) -> None:
        pass

    def transform(self):
        print("Je suis un transformer")