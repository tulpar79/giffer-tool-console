"""
Core GIF creation functionality
"""

import os
import time
from PIL import Image
from .image_processor import process_image_for_gif, analyze_image_dimensions


def create_gif_from_images(image_files, output_path=None, fps=10.0, show_transparency=True, 
                        replace_magic_pink_flag=True, custom_background_color='#f8f9fa', 
                        disposal_method=2):
    """Create GIF from list of PNG and BMP files
    
    Args:
        disposal_method: Frame disposal method for GIF animation
            0 = No disposal (next frame draws over current)
            1 = Restore to background color
            2 = Restore to previous frame (recommended for most cases)
            3 = Restore to previous frame (alternative implementation)
    """
    
    if not image_files:
        print("No image files provided")
        return False
    
    # Filter for supported files only
    from .utils import get_supported_extensions, validate_image_files
    supported_extensions = get_supported_extensions()
    image_files = [f for f in image_files if f.lower().endswith(supported_extensions)]
    
    if not image_files:
        print(f"No supported image files found. Supported formats: {', '.join(supported_extensions)}")
        return False
    
    print(f"Processing {len(image_files)} image files...")
    
    # Analyze dimensions of all images to find maximum canvas size
    print("Analyzing image dimensions...")
    max_width, max_height, dimensions_info = analyze_image_dimensions(image_files)
    
    if max_width == 0 or max_height == 0:
        print("Error: Could not determine canvas dimensions")
        return False
    
    # Check for dimension inconsistencies and warn user
    unique_dimensions = set((info['width'], info['height']) for info in dimensions_info)
    if len(unique_dimensions) > 1:
        print(f"\n⚠️  WARNING: Canvas size inconsistencies detected!")
        print(f"   Found {len(unique_dimensions)} different canvas sizes:")
        for width, height in sorted(unique_dimensions):
            files_with_size = [info['file'] for info in dimensions_info if info['width'] == width and info['height'] == height]
            print(f"   - {width}x{height}: {len(files_with_size)} file(s)")
        print(f"   Using maximum canvas size: {max_width}x{max_height}")
        print(f"   Smaller sprites will be centered on this canvas.\n")
    else:
        print(f"✓ All images have consistent canvas size: {max_width}x{max_height}")
    
    # Process all images with target canvas size
    images = []
    for image_file in image_files:
        if not os.path.exists(image_file):
            print(f"Warning: File not found: {image_file}")
            continue
            
        print(f"Processing: {os.path.basename(image_file)}")
        img = process_image_for_gif(image_file, show_transparency, replace_magic_pink_flag, 
                                   custom_background_color, target_size=(max_width, max_height))
        if img:
            images.append(img)
    
    if not images:
        print("No valid images could be processed")
        return False
    
    # Generate output filename if not provided
    if not output_path:
        # Use the directory of the first image file
        first_image_dir = os.path.dirname(os.path.abspath(image_files[0]))
        timestamp = int(time.time())
        output_path = os.path.join(first_image_dir, f'animation_{timestamp}.gif')
    
    # Calculate frame duration from FPS
    if fps <= 0:
        print("Error: FPS must be greater than 0")
        return False
    
    frame_duration = int(1000 / fps)
    
    # Create GIF
    try:
        print(f"Creating GIF with {len(images)} frames at {fps} FPS...")
        images[0].save(
            output_path,
            format='GIF',
            save_all=True,
            append_images=images[1:],
            duration=frame_duration,
            loop=0,  # Infinite loop
            optimize=False,  # No optimization for maximum compatibility
            disposal=disposal_method  # Frame disposal method
        )
        
        print(f"GIF created successfully: {output_path}")
        return True
        
    except Exception as e:
        print(f"Error creating GIF: {e}")
        return False

