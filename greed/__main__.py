import os
import random

from greed.casting.actor import Actor
from greed.casting.artifact import Artifact
from greed.casting.cast import Cast

from greed.directing.director import Director

from greed.services.keyboard_service import KeyboardService
from greed.services.video_service import VideoService

from greed.shared.color import Color
from greed.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40

star = ""
rock = ""

def main():
    """Application entry point
    """

    # create the cast
    cast = Cast()

    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    pass

if __name__ == "__main__":
    main()