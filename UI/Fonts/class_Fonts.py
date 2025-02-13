from pygame.font import SysFont
from dataclasses import dataclass

@dataclass(frozen=True)
class Fonts:
    arial: object = SysFont('Arial', 36)
    roboto: object = SysFont('Roboto', 55)