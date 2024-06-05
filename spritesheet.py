import pygame
from typing import List, Tuple, Optional

class Spritesheet:
    """
    Class to handle sprite sheets.
    
    This class was adapted from https://www.pygame.org/wiki/Spritesheet
    """

    def __init__(self, filename: str) -> None:
        """
        Initialize the spritesheet object by loading the image file.

        Args:
            filename (str): The path to the sprite sheet image file.

        Raises:
            SystemExit: If the sprite sheet image file cannot be loaded.
        """
        try:
            self.sheet = pygame.image.load(filename).convert()
        except pygame.error as message:
            print(f'Unable to load spritesheet image: {filename}')
            raise SystemExit(message)

    def image_at(self, rectangle: Tuple[int, int, int, int], colorkey: Optional[Tuple[int, int, int]] = None, scale: Optional[Tuple[int, int]] = None) -> pygame.Surface:
        """
        Load a specific image from a specific rectangle.

        Args:
            rectangle (Tuple[int, int, int, int]): A tuple defining the area of the sprite sheet to load.
            colorkey (Optional[Tuple[int, int, int]]): A color to be treated as transparent.
                                                       If set to -1, the top-left pixel color is used as the transparent color. Default is None.
            scale Optional[Tuple[int, int]]: Width and height to which the image will be scaled. Default is None.

        Returns:
            pygame.Surface: The loaded image.
        """
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        if scale:
            image = pygame.transform.scale(image, scale)            
        return image

    def images_at(self, rects: List[Tuple[int, int, int, int]], colorkey: Optional[Tuple[int, int, int]] = None, scale: Optional[Tuple[int, int]] = None) -> List[pygame.Surface]:
        """
        Load multiple images from a list of rectangles.

        Args:
            rects (List[Tuple[int, int, int, int]]): A list of tuples, each defining a rectangle on the sprite sheet.
            colorkey (Optional[Tuple[int, int, int]]): A color to be treated as transparent.
                                                       If set to -1, the top-left pixel color is used as the transparent color. Default is None.
            scale Optional[Tuple[int, int]]: Width and height to which the image will be scaled. Default is None.

        Returns:
            List[pygame.Surface]: A list of loaded images.
        """
        return [self.image_at(rect, colorkey, scale) for rect in rects]

    def load_strip(self, rect: Tuple[int, int, int, int], image_count: int, colorkey: Optional[Tuple[int, int, int]] = None, scale: Optional[Tuple[int, int]] = None) -> List[pygame.Surface]:
        """
        Load a strip of images from the sprite sheet.

        Args:
            rect (Tuple[int, int, int, int]): A tuple defining the first image in the strip.
            image_count (int): The number of images in the strip.
            colorkey (Optional[Tuple[int, int, int]]): A color to be treated as transparent.
                                                       If set to -1, the top-left pixel color is used as the transparent color. Default is None.
            scale Optional[Tuple[int, int]]: Width and height to which the image will be scaled. Default is None.
                                                       
        Returns:
            List[pygame.Surface]: A list of loaded images from the strip.
        """
        tups = [(rect[0] + rect[2] * x, rect[1], rect[2], rect[3]) for x in range(image_count)]
        return self.images_at(tups, colorkey, scale)
