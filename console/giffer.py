#!/usr/bin/env python3
"""
Standalone GIF Generator Tool - Console Interface
Converts multiple PNG and BMP files into an animated GIF

Usage:
    python giffer.py file1.png file2.bmp file3.png
    or drag PNG/BMP files onto the batch file wrapper
"""

import sys
import os
import argparse

# Add parent directory to path to import core library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core import create_gif_from_images


def main():
    parser = argparse.ArgumentParser(description='Convert PNG and BMP files to animated GIF')
    parser.add_argument('files', nargs='+', help='PNG and BMP files to convert')
    parser.add_argument('-o', '--output', help='Output GIF file path')
    parser.add_argument('-f', '--fps', type=float, default=10.0, help='Frames per second (default: 10.0)')
    parser.add_argument('--no-transparency', action='store_true', help='Disable transparency handling')
    parser.add_argument('--no-magic-pink', action='store_true', help='Disable magic pink replacement')
    parser.add_argument('-b', '--background', default='#f8f9fa', help='Background color for transparency (default: #f8f9fa)')
    parser.add_argument('-d', '--disposal', type=int, default=2, choices=[0, 1, 2, 3], 
                        help='Frame disposal method: 0=no disposal, 1=restore to background, 2=restore to previous (default: 2)')
    parser.add_argument('--pause', action='store_true', help='Pause for user input before exiting (useful for console mode)')
    
    args = parser.parse_args()
    
    # Convert arguments to function parameters
    show_transparency = not args.no_transparency
    replace_magic_pink_flag = not args.no_magic_pink
    
    success = create_gif_from_images(
        args.files,
        output_path=args.output,
        fps=args.fps,
        show_transparency=show_transparency,
        replace_magic_pink_flag=replace_magic_pink_flag,
        custom_background_color=args.background,
        disposal_method=args.disposal
    )
    
    if success:
        print("GIF creation completed successfully!")
        if args.pause:
            input("\nPress Enter to exit...")
        return 0
    else:
        print("GIF creation failed!")
        if args.pause:
            input("\nPress Enter to exit...")
        return 1


if __name__ == '__main__':
    sys.exit(main())

