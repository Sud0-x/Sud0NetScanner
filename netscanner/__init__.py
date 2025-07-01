"""
Sud0NetScanner - Advanced Network Port Scanner Package

A sophisticated and powerful network reconnaissance tool built by Sud0-x.

This package provides advanced network scanning capabilities including:
- High-speed multi-threaded scanning
- Service detection and banner grabbing  
- OS fingerprinting capabilities
- Stealth mode scanning
- Multiple output formats
- Real-time progress tracking

Author: Sud0-x
GitHub: https://github.com/Sud0-x/Sud0NetScanner
Version: 2.0.0
"""

__version__ = "2.0.0"
__author__ = "Sud0-x"
__email__ = "contact@sud0-x.dev"
__description__ = "Advanced Network Port Scanner"
__url__ = "https://github.com/Sud0-x/Sud0NetScanner"

from .scanner import NetScanner, Colors

__all__ = ["NetScanner", "Colors"]
