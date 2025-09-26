Save anything you want from [wplace.live](https://wplace.live)!

# Installation
1. Install the newest version of [Python](https://www.python.org/downloads/).
2. Download this repository by clicking on the green `<> Code` button, then `Download ZIP`.
3. Unzip the download to somewhere on your computer.

# Usage
1. Inside the `main.py` file, replace the tile coordinates in `start` and `end` with the ones you want to save.
2. Run `main.py` with Python.

All the images will be saved to a folder named `storage` in the same place where the project is stored. 
This can be changed by adding `store_dir = "C:\Your\Path\To\Whatever\You\Want"` inside of Context.

The program has a few other features which can be customized, though that shouldn't be necessary.

**NOTE**: If the rate limit is set to anything lower than 5 seconds, you may or may not be temporarily blocked from wplace.live! This should ideally disappear after some time, although that hasn't been tested.

# How to get Tile Coordinates
1. Open your browser of choice, go to [wplace.live](https://wplace.live), and press `{Ctrl}+{Shift}+I`.
2. In the new window, click on the `Network` tab.
3. In the search bar that says `Filter`, type in `png` and refresh the page.

The coordinates to the tiles are in the column called `Path`, where the two numbers after `/files/s0/tiles/`, those being the `x` and `y` coordinates of amy given tile.

It's recommended to zoom in as far as you can on the map in one corner to only see one tile at a time.

**NOTE**: If there is no `Path` column, right-click on the row with all the labels, then click `Path` in the menu.
