from typing import List
from Corrida import Corrida

class Motorista:

    def __init__(self, nota: int, corridas: List[Corrida]):
        self.nota = nota
        self.corridas = corridas