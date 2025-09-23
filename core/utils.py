"""
Utility functions for the GIF creator
"""

def get_supported_extensions():
    """Get list of supported file extensions"""
    return ('.png', '.bmp')


def validate_image_files(files):
    """Validate that files are supported image types"""
    supported_extensions = get_supported_extensions()
    valid_files = []
    
    for file in files:
        if file.lower().endswith(supported_extensions):
            valid_files.append(file)
    
    return valid_files


def format_file_size(bytes):
    """Format file size in human readable format"""
    if bytes == 0:
        return '0 Bytes'
    k = 1024
    sizes = ['Bytes', 'KB', 'MB', 'GB']
    i = int(__import__('math').floor(__import__('math').log(bytes) / __import__('math').log(k)))
    return f"{round(bytes / (k ** i), 2)} {sizes[i]}"


def get_default_settings():
    """Get default settings for GIF creation"""
    return {
        'fps': 10.0,
        'show_transparency': True,
        'replace_magic_pink': True,
        'background_color': '#f8f9fa',
        'disposal_method': 2
    }

