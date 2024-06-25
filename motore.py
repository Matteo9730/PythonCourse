from Auto import Auto
from abc import ABC

class Motore(Auto,ABC):
    def __init__(self, targa, marca, modello):
        super().__init__(targa, marca, modello)
    