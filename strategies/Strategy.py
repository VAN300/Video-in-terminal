import sys
from abc import ABC, abstractmethod


class Strategy(ABC):
    SYMS = ' \'.,:^";*!²¤/r(?+¿cLª7t1fJCÝy¢zF3±$S2kñ5AZXG$À0Ãm&Q8%RÔßÊNBåMÆØ@'
    out = sys.stdout

    @abstractmethod
    def execute(Aimage) -> None:
        pass
