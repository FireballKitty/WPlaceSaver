from typing import List

class Vec2:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"{self.x}.{self.y}"
        
class VecRange:
    def get_range(self) -> List[Vec2]:
        output: List[Vec2] = []

        for y_idx in range(self.start.y, self.end.y+1):
            for x_idx in range(self.start.x, self.end.x+1):
                output.append(Vec2(x_idx, y_idx))
                    
        return output
    
    def __init__(self, start: Vec2, end: Vec2) -> None:
        self.start = start
        self.end = end
        self.range: List[Vec2] = self.get_range()