# GIF Creator Tool - Modular Structure

This repository uses a modular architecture that separates core functionality from the console interface, making it easy to maintain and extend.

## 🏗️ Repository Structure

```
giffer-tool-console/
├── core/                          # 🔧 Shared core library
│   ├── __init__.py               # Core library exports
│   ├── image_processor.py        # Image processing functions
│   ├── gif_creator.py           # GIF creation logic
│   └── utils.py                 # Utility functions
├── console/                       # 💻 Console/CLI interface
│   ├── giffer.py                # CLI application
│   ├── create_gif.bat           # Windows drag-and-drop wrapper
│   └── requirements.txt         # Console-specific dependencies
├── requirements.txt              # 📦 Shared dependencies
└── README.md                    # 📖 Documentation
```

## 🎯 Benefits of This Structure

### ✅ **Clean Separation**
- **Core library**: Pure business logic, no UI dependencies
- **Console tool**: Simple CLI interface using core library
- **Easy maintenance**: Changes to core logic automatically benefit the interface

### ✅ **Easy Extension**
- Add new file formats in `core/utils.py` → automatically available
- Add new processing features in `core/image_processor.py` → interface gets them
- Create new interfaces (GUI, API, etc.) by importing the core library

### ✅ **Independent Development**
- Console tool remains simple and lightweight
- Core library can evolve independently
- Each component has its own dependencies and requirements

## 🚀 Quick Start

### Console Tool (Original Functionality)
```bash
# Install dependencies
pip install -r console/requirements.txt

# Use the tool
python console/giffer.py file1.png file2.bmp

# Or drag files onto console/create_gif.bat (Windows)
```


## 🔧 Development Workflow

### Adding New File Format Support

1. **Update core library** (`core/utils.py`):
   ```python
   def get_supported_extensions():
       return ('.png', '.bmp', '.gif', '.tga')  # Add new formats here
   ```

2. **Test console tool**:
   ```bash
   python console/giffer.py newformat.tga
   ```

3. **Console tool automatically supports it** - no changes needed!

### Adding New Processing Features

1. **Add to core library** (`core/image_processor.py`):
   ```python
   def new_processing_feature(img, options):
       # Your new processing logic
       return processed_img
   ```

2. **Update console tool** (if needed):
   ```python
   # Add command line argument
   parser.add_argument('--new-feature', action='store_true')
   ```


### Creating New Interfaces

1. **Create new directory** (e.g., `gui/`, `api/`, `desktop/`)
2. **Import core library**:
   ```python
   import sys
   import os
   sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
   from core import create_gif_from_images
   ```
3. **Build your interface** using the core functions

## 📦 Dependencies

### Core Library
- `Pillow>=9.0.0` - Image processing

### Console Tool
- Uses core library dependencies only
- No additional dependencies needed


## 🔄 Migration from Old Structure

The old `giffer.py` has been refactored into:

- **Core functions** → `core/image_processor.py` and `core/gif_creator.py`
- **CLI interface** → `console/giffer.py`
- **Batch wrapper** → `console/create_gif.bat`

**All functionality is preserved** - the console tool works exactly the same as before!

## 🎨 Console Tool Features

| Feature | Description |
|---------|-------------|
| **File Input** | Drag & drop (Windows) / CLI args |
| **Processing** | Server-side (Python) |
| **Dependencies** | Minimal (Pillow only) |
| **Deployment** | Local only |
| **Privacy** | Files stay local |

## 🛠️ Core Library API

### Main Functions
```python
from core import create_gif_from_images, get_supported_extensions

# Create GIF from image files
success = create_gif_from_images(
    image_files=['file1.png', 'file2.bmp'],
    output_path='output.gif',
    fps=10.0,
    show_transparency=True,
    replace_magic_pink_flag=True,
    custom_background_color='#f8f9fa',
    disposal_method=2
)

# Get supported file extensions
extensions = get_supported_extensions()  # ('.png', '.bmp')
```

### Image Processing
```python
from core import process_image_for_gif, replace_magic_pink

# Process single image
processed_img = process_image_for_gif(
    image_path='sprite.png',
    show_transparency=True,
    replace_magic_pink_flag=True,
    custom_background_color='#ffffff',
    target_size=(100, 100)
)

# Replace magic pink pixels
new_img = replace_magic_pink(img, '#ffffff')
```

## 🚀 Future Extensions

This structure makes it easy to add:

- **GUI Interface** (tkinter, PyQt, etc.)
- **REST API** (FastAPI, Django REST)
- **Desktop App** (Electron, PyInstaller)
- **Mobile App** (React Native, Flutter)
- **Command Line Tools** (different argument styles)
- **Batch Processing** (multiple GIFs at once)
- **Cloud Functions** (AWS Lambda, Google Cloud Functions)

## 📝 Development Tips

1. **Always test core changes** with the console interface
2. **Keep core library pure** - no UI dependencies
3. **Use type hints** in core functions for better IDE support
4. **Write tests** for core functions (consider adding `tests/` directory)
5. **Document new features** in the interface

## 🔍 Troubleshooting

### Import Errors
```bash
# Make sure you're in the right directory
cd console

# Check Python path
python -c "import sys; print(sys.path)"
```

### Missing Dependencies
```bash
# Install core dependencies
pip install -r requirements.txt

# Install interface-specific dependencies
pip install -r console/requirements.txt
```

This modular structure gives you a simple, clean console tool with easy code sharing and future extensibility!

