from dataclasses import dataclass, field

@dataclass
class TextGroup:
    group: list = field(default_factory = list)
    
    def update(self):
        for obj in self.group:
            obj.update()