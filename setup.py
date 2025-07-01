#!/usr/bin/env python3
"""
Sud0NetScanner Setup Script
Developed by Sud0-x
"""

from setuptools import setup, find_packages
import os

# Read the README file
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sud0netscanner",
    version="2.0.0",
    author="Sud0-x",
    author_email="contact@sud0-x.dev",
    description="Advanced Network Port Scanner - A sophisticated network reconnaissance tool",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/Sud0-x/Sud0NetScanner",
    project_urls={
        "Bug Reports": "https://github.com/Sud0-x/Sud0NetScanner/issues",
        "Source": "https://github.com/Sud0-x/Sud0NetScanner",
        "Documentation": "https://github.com/Sud0-x/Sud0NetScanner#readme",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Intended Audience :: Information Technology",
        "Topic :: System :: Networking",
        "Topic :: Security",
        "Topic :: System :: Systems Administration",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Unix",
        "Operating System :: MacOS",
        "Environment :: Console",
    ],
    python_requires=">=3.6",
    install_requires=[],  # No external dependencies - uses standard library only
    extras_require={
        "dev": [
            "pytest>=6.0",
            "black>=21.0",
            "flake8>=3.8",
            "mypy>=0.800",
        ],
        "enhanced": [
            "python-nmap>=0.7.1",
            "scapy>=2.4.5",
        ],
    },
    entry_points={
        "console_scripts": [
            "sud0netscanner=netscanner.scanner:main",
            "netscanner=netscanner.scanner:main",
        ],
    },
    keywords=[
        "network", "scanner", "port", "security", "penetration-testing", 
        "cybersecurity", "reconnaissance", "nmap", "networking", "pentesting"
    ],
    include_package_data=True,
    zip_safe=False,
    platforms=["Linux", "Unix", "MacOS"],
)
