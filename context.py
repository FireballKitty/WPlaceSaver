from typing import Dict
from pathlib import Path
from vectors import *
from wplace import *
import datetime
import time
import random

class Context:
    DEFAULT_STORE_DIR: Path = Path("storage").resolve()
    
    def __init__(self, 
                 tile_range: VecRange, 
                 rate_limit_seconds: int = 5, 
                 rate_limit_jitter: float = float(1), 
                 wplace_instance: WPlace = WPlace(),
                 store_dir: Path = DEFAULT_STORE_DIR) -> None:
        
        self.tiles: Dict[str, BytesIO] = {}
        self.tile_range: VecRange = tile_range
        self.rate_limit: int = rate_limit_seconds
        self.jitter: float = rate_limit_jitter
        self.wplace: WPlace = wplace_instance
        self.store_dir: Path = store_dir

    def __get_delay(self) -> float:
        return random.uniform(-(self.jitter/2), self.jitter/2) + self.rate_limit

    def fetch_tile(self, coord: Vec2) -> None:
        file = self.wplace.fetch_file_from_coord(coord)
        
        if type(file) != BytesIO:
            print(f"Couldn't fetch tile {coord.x}, {coord.y}:\n\tGot response {file}")
        else:
            print(f"Fetched: {coord.x}, {coord.y}")
            self.tiles[str(coord)] = file
        
    def fetch_all_tiles(self):        
        for tile_coord in self.tile_range.range:
            time.sleep(self.__get_delay())
            self.fetch_tile(tile_coord)
    
    def save_all_tiles(self, with_timestamp: bool = False, format: str = "png"):
        self.store_dir.mkdir(parents=True, exist_ok=True)

        for coord_str, image in self.tiles.items():
            if with_timestamp:
                filename = f"{coord_str}_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.{format}"
            else:
                filename = f"{coord_str}.{format}"
            filepath = Path.joinpath(self.store_dir, filename)
            
            with open(filepath, "wb") as file:
                file.write(image.read())
        print(f"Saved {len(self.tiles)} tiles to {self.store_dir}")
