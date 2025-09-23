"""
Core image processing functions
"""

import os
from PIL import Image


def replace_magic_pink(img, replacement_color):
    """Replace magic pink and pink-purple pixels with the specified color"""
    # Convert to RGB if not already
    if img.mode != 'RGB':
        img = img.convert('RGB')
    
    # Convert replacement color from hex to RGB
    if replacement_color.startswith('#'):
        replacement_color = replacement_color[1:]
    r = int(replacement_color[0:2], 16)
    g = int(replacement_color[2:4], 16)
    b = int(replacement_color[4:6], 16)
    
    # Get image data as a list of pixels
    pixels = list(img.getdata())
    width, height = img.size
    
    # Count pixels to replace
    pixel_count = 0
    
    # Process each pixel
    for i, pixel in enumerate(pixels):
        if len(pixel) >= 3:  # Ensure we have RGB values
            pr, pg, pb = pixel[:3]
            
            # Check for magic pink variations
            is_magic_pink = (
                # Classic magic pink (RGB 255,0,255)
                (pr == 255 and pg == 0 and pb == 255) or
                # Pink-purple (RGB 248,0,248)
                (pr == 248 and pg == 0 and pb == 248) or
                # Near-magic pink (within 1 RGB value)
                (pr >= 254 and pr <= 255 and pg >= 0 and pg <= 1 and pb >= 254 and pb <= 255) or
                # Near-pink-purple (within 1 RGB value)
                (pr >= 247 and pr <= 249 and pg >= 0 and pg <= 1 and pb >= 247 and pb <= 249)
            )
            
            if is_magic_pink:
                pixels[i] = (r, g, b)
                pixel_count += 1
    
    if pixel_count > 0:
        print(f"Replacing {pixel_count} magic pink/pink-purple pixels with RGB({r},{g},{b})")
    
    # Create new image with modified pixels
    new_img = Image.new('RGB', (width, height))
    new_img.putdata(pixels)
    return new_img


def analyze_image_dimensions(image_files):
    """Analyze all input images to find maximum width and height"""
    max_width = 0
    max_height = 0
    dimensions_info = []
    
    for image_file in image_files:
        if not os.path.exists(image_file):
            continue
            
        try:
            with Image.open(image_file) as img:
                width, height = img.size
                max_width = max(max_width, width)
                max_height = max(max_height, height)
                dimensions_info.append({
                    'file': os.path.basename(image_file),
                    'width': width,
                    'height': height
                })
        except Exception as e:
            print(f"Warning: Could not analyze dimensions of {image_file}: {e}")
    
    return max_width, max_height, dimensions_info


def process_image_for_gif(image_path, show_transparency=True, replace_magic_pink_flag=True, 
                         custom_background_color='#f8f9fa', target_size=None):
    """Process a single image for GIF creation"""
    try:
        img = Image.open(image_path)
        original_size = img.size
        
        # Handle transparency
        if show_transparency and img.mode in ('RGBA', 'LA'):
            # Create a background
            if img.mode == 'RGBA':
                background = Image.new('RGB', img.size, custom_background_color)
                background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                img = background
            elif img.mode == 'LA':
                background = Image.new('L', img.size, 200)  # Light gray for grayscale
                background.paste(img, mask=img.split()[-1])  # Use alpha channel as mask
                img = background.convert('RGB')
        elif img.mode == 'P':
            # Palette mode with transparency
            if 'transparency' in img.info:
                img = img.convert('RGBA')
                if show_transparency:
                    background = Image.new('RGB', img.size, custom_background_color)
                    background.paste(img, mask=img.split()[-1])
                    img = background
                else:
                    img = img.convert('RGB')
            else:
                img = img.convert('RGB')
        elif img.mode == 'L':
            # Grayscale, convert to RGB
            img = img.convert('RGB')
        elif img.mode == 'RGB':
            # Already RGB, no transparency to remove
            pass
        else:
            # For any other mode, convert to RGB
            img = img.convert('RGB')
        
        # Replace magic pink if background color is specified
        if replace_magic_pink_flag and custom_background_color:
            img = replace_magic_pink(img, custom_background_color)
        
        # Center the image on target canvas if target_size is specified
        if target_size and target_size != original_size:
            target_width, target_height = target_size
            # Create a new canvas with the target size and background color
            canvas = Image.new('RGB', target_size, custom_background_color)
            
            # Calculate position to center the image
            x_offset = (target_width - original_size[0]) // 2
            y_offset = (target_height - original_size[1]) // 2
            
            # Paste the image centered on the canvas
            canvas.paste(img, (x_offset, y_offset))
            img = canvas
        
        # Convert to palette mode for GIF (safest approach)
        img = img.convert('P', palette=Image.ADAPTIVE, colors=256)
        return img
        
    except Exception as e:
        print(f"Error processing {image_path}: {e}")
        return None

