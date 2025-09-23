#!/usr/bin/env python3
"""
Web Interface for GIF Creator Tool
Serves a web application that allows users to create GIFs client-side
"""

import os
import sys
from flask import Flask, render_template, jsonify

# Add parent directory to path to import core library
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from core import get_supported_extensions

app = Flask(__name__)

@app.route('/')
def index():
    """Serve the main web interface"""
    return render_template('index.html')

@app.route('/api/supported-formats')
def supported_formats():
    """API endpoint to get supported file formats"""
    extensions = get_supported_extensions()
    return jsonify({
        'extensions': extensions,
        'formats': [ext[1:].upper() for ext in extensions]  # Remove dot and uppercase
    })

@app.route('/health')
def health():
    """Health check endpoint for Railway"""
    return jsonify({"status": "healthy", "service": "giffer-web"})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

