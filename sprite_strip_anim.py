import pygame
import spritesheet
from typing import Optional, Tuple

class SpriteStripAnim:
    """
    Sprite strip animator.

    This class provides an iterator (iter() and next() methods), and a
    __add__() method for joining strips which comes in handy when a
    strip wraps to the next row.

    Ref: https://www.pygame.org/wiki/Spritesheet
    """
    
    def __init__(self, filename: str, rect: Tuple[int, int, int, int], count: int, colorkey: Optional[Tuple[int, int, int]] = None, loop: bool = False, frames: int = 1, scale: Optional[Tuple[int, int]] = None) -> None:
        """
        Construct a SpriteStripAnim.

        Args:
            filename (str): The path to the sprite sheet image file.
            rect (Tuple[int, int, int, int]): A tuple defining the first image in the strip.
            count (int): The number of images in the strip.
            colorkey (Optional[Tuple[int, int, int]]): A color to be treated as transparent.
                                                       If set to -1, the top-left pixel color is used as the transparent color. Default is None.
            loop (bool): A boolean that, when True, causes the next() method to loop. If False, the terminal case raises StopIteration.
            frames (int): The number of ticks to return the same image before the iterator advances to the next image.
            scale Optional[Tuple[int, int]]: Width and height to which the image will be scaled. Default is None.
        """
        self.filename = filename
        ss = spritesheet.Spritesheet(filename)
        self.images = ss.load_strip(rect, count, colorkey, scale)
        self.i = 0
        self.loop = loop
        self.frames = frames
        self.f = frames

    def iter(self) -> 'SpriteStripAnim':
        """
        Initialize the iterator.

        Returns:
            SpriteStripAnim: The initialized iterator.
        """
        self.i = 0
        self.f = self.frames
        return self

    def next(self) -> pygame.Surface:
        """
        Advance to the next image in the strip.

        Returns:
            pygame.Surface: The next image in the strip.

        Raises:
            StopIteration: If the end of the strip is reached and loop is False.
        """
        if self.i >= len(self.images):
            if not self.loop:
                raise StopIteration
            else:
                self.i = 0
        image = self.images[self.i]
        self.f -= 1
        if self.f == 0:
            self.i += 1
            self.f = self.frames
        return image

    def __add__(self, ss: 'SpriteStripAnim') -> 'SpriteStripAnim':
        """
        Add another SpriteStripAnim's images to this one.

        Args:
            ss (SpriteStripAnim): Another SpriteStripAnim instance.

        Returns:
            SpriteStripAnim: The combined SpriteStripAnim instance.
        """
        self.images.extend(ss.images)
        return self
