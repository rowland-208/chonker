from dataclasses import dataclass
from typing import Iterable


@dataclass
class Chonk:
    size: int
    rawindex: int = 0

    @property
    def is_start_of(self):
        return self.subindex == 0

    @property
    def is_end_of(self):
        return self.subindex == self.size - 1

    @property
    def index(self):
        return self.rawindex // self.size

    @property
    def subindex(self):
        return self.rawindex % self.size


def chonkify(iterable: Iterable, size=0):
    chonk = Chonk(size)
    for rawindex, x in enumerate(iterable):
        chonk.rawindex = rawindex
        yield chonk, x
