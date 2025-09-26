from context import Context
from vectors import Vec2, VecRange

# ======== Configuration ========

start = Vec2(100, 100)
end = Vec2(104, 104)

# ===============================

if __name__ == "__main__":
    context = Context(
        tile_range = VecRange(start, end))
    context.fetch_all_tiles()
    context.save_all_tiles(with_timestamp=True, format="png")