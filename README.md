# GIF Creator Tool

A console tool to convert multiple PNG and BMP files into animated GIFs.

> **Modular Structure**: This repository uses a modular architecture with a shared core library. See [README-STRUCTURE.md](README-STRUCTURE.md) for details on the organization.

## Features

- **Drag & Drop**: Simply drag PNG and BMP files onto the batch file
- **Transparency Handling**: Automatically handles transparent backgrounds
- **Magic Pink Replacement**: Replaces magic pink (#FF00FF) with custom background color
- **Customizable**: Adjustable FPS, background color, and other options
- **Standalone**: No dependencies on the main sprite browser application

## Quick Start

1. **Install Python** (if not already installed)
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Drag PNG and BMP files** onto `console/create_gif.bat`
4. **GIF will be created** in the same folder as your first image file

## Usage

### Console Tool Usage

#### Drag & Drop (Easiest)
- Drag multiple PNG and BMP files onto `console/create_gif.bat`
- The GIF will be created automatically with default settings

#### Command Line
```bash
python console/giffer.py file1.png file2.bmp file3.png
```

#### Advanced Options
```bash
python console/giffer.py file1.png file2.bmp file3.png -o output.gif -f 10 --background "#ffffff"
```


## Command Line Options

- `-o, --output`: Output GIF file path (default: auto-generated)
- `-f, --fps`: Frames per second (default: 7.0)
- `--no-transparency`: Disable transparency handling
- `--no-magic-pink`: Disable magic pink replacement
- `-b, --background`: Background color for transparency (default: #f8f9fa)
- `-d, --disposal`: Frame disposal method (0-3, default: 2)

### Frame Disposal Methods
The disposal method controls how the canvas is refreshed between frames, preventing tearing artifacts:

- **0 (No Disposal)**: Next frame draws over current frame (may cause artifacts)
- **1 (Restore to Background)**: Clears frame area to background color
- **2 (Restore to Previous)**: Restores canvas to state before current frame (recommended)
- **3 (Restore to Previous Alt)**: Alternative implementation of method 2

**Default (2)** works best for most animations and prevents tearing artifacts.

## Examples

### Basic Usage
```bash
python giffer.py sprite1.png sprite2.bmp sprite3.png
```

### Custom FPS and Background
```bash
python giffer.py *.png -f 12 -b "#000000"
```

### No Transparency Handling
```bash
python giffer.py *.png --no-transparency
```

### Fix Tearing Artifacts
```bash
python giffer.py *.png -d 2
```

## File Processing

The tool processes images in the following way:

1. **Transparency**: Converts RGBA/LA images to RGB with background color
2. **Magic Pink**: Replaces magic pink (#FF00FF) and pink-purple (#F800F8) pixels
3. **Color Optimization**: Converts to palette mode for optimal GIF size
4. **Frame Timing**: Uses specified FPS for smooth animation
5. **Frame Disposal**: Controls how frames are cleared between animations (prevents tearing artifacts)

## Requirements

- Python 3.6+
- Pillow (PIL) library

## Installation

1. Clone or download this repository
2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Ready to use!

## Troubleshooting

### "Python not found"
- Install Python from [python.org](https://python.org)
- Make sure Python is added to your system PATH

### "Pillow not found"
- Run: `pip install Pillow`

### "No PNG or BMP files found"
- Make sure you're dragging actual PNG or BMP files
- Check that file extensions are `.png` or `.bmp` (case-insensitive)

### GIF too large
- Try reducing the number of frames
- Use `--no-transparency` to disable transparency processing
- Consider resizing your PNG or BMP files before processing

## Future Format Support

This tool currently supports PNG and BMP files, with plans to expand support for additional image formats commonly used in game development and pixel art:

### Planned Support (Priority Order)
- **GIF** - Static GIF frames (common for sprite animations)
- **TGA** - Gaming industry standard with strong alpha channel support
- **WebP** - Modern web format with efficient compression
- **ICO** - Windows icon format for game icons
- **JPEG** - General purpose format (with quality considerations for pixel art)
- **TIFF** - Professional format for high-quality exports

### Aseprite Compatibility
These planned formats align with Aseprite's export capabilities, making the tool more useful for pixel artists and game developers who use Aseprite for sprite creation.

*Note: Vector formats (SVG) and proprietary formats (.ase, .aseprite) are not planned for support as they don't align with the tool's raster image focus.*

## License

This tool is extracted from the nm-sprite-browser project and follows the same license terms.
