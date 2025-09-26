from context import Context
from vectors import Vec2, VecRange

if __name__ == "__main__":
    context = Context(
        tile_range = VecRange(Vec2(100,100), Vec2(104,104)))
    context.fetch_all_tiles()
    context.save_all_tiles(with_timestamp=True, format="png")