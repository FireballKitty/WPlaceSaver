from vectors import Vec2
import requests
from io import BytesIO

class WPlace:
    WPLACE_BACKEND_URL: str = "https://backend.wplace.live/"
    
    def __init__(self, backend_url: str = "") -> None:
        if backend_url == "":
            self.backend_url = self.WPLACE_BACKEND_URL
        else:
            self.backend_url = backend_url
    
    def get_tile_url(self, coords: Vec2):
        return f"{self.backend_url}files/s0/tiles/{coords.x}/{coords.y}.png"
    
    def fetch_file_from_url(self, url: str) -> BytesIO | int:
        response = requests.get(url)
        if response.status_code == 200:
            image = BytesIO(response.content)
            return image
        else:
            return response.status_code
        
    def fetch_file_from_coord(self, coords: Vec2) -> BytesIO | int:
        return self.fetch_file_from_url(self.get_tile_url(coords))