"""
GIF Creator Core Library
Shared functionality for console and web interfaces
"""

from .image_processor import (
    replace_magic_pink,
    process_image_for_gif,
    analyze_image_dimensions
)
from .gif_creator import create_gif_from_images
from .utils import get_supported_extensions, validate_image_files

__version__ = "1.0.0"
__all__ = [
    'replace_magic_pink',
    'process_image_for_gif', 
    'analyze_image_dimensions',
    'create_gif_from_images',
    'get_supported_extensions',
    'validate_image_files'
]

