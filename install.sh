#!/bin/bash

# Sud0NetScanner Installation Script
# This script sets up Sud0NetScanner for easy system-wide usage
# Developed by Sud0-x

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root for system-wide installation
check_permissions() {
    if [[ $EUID -eq 0 ]]; then
        INSTALL_DIR="/usr/local/bin"
        print_status "Installing system-wide (requires root)"
    else
        INSTALL_DIR="$HOME/.local/bin"
        print_status "Installing for current user"
        mkdir -p "$INSTALL_DIR"
    fi
}

# Main installation function
install_netscanner() {
    print_status "Starting NetScanner installation..."
    
    # Check Python3 availability
    if ! command -v python3 &> /dev/null; then
        print_error "Python3 is not installed. Please install Python3 first."
        exit 1
    fi
    
    print_success "Python3 found: $(python3 --version)"
    
    # Get script directory
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
    
    # Check if netscanner.py exists
    if [[ ! -f "$SCRIPT_DIR/netscanner.py" ]]; then
        print_error "netscanner.py not found in $SCRIPT_DIR"
        exit 1
    fi
    
    # Check permissions and set install directory
    check_permissions
    
    # Copy the script
    print_status "Copying netscanner.py to $INSTALL_DIR"
    cp "$SCRIPT_DIR/netscanner.py" "$INSTALL_DIR/netscanner"
    chmod +x "$INSTALL_DIR/netscanner"
    
    # Check if install directory is in PATH
    if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
        print_warning "$INSTALL_DIR is not in your PATH"
        print_status "Add this line to your ~/.bashrc or ~/.zshrc:"
        echo "export PATH=\"$INSTALL_DIR:\$PATH\""
        
        # Offer to add to PATH automatically
        read -p "Add to PATH automatically? [y/N]: " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Yy]$ ]]; then
            if [[ -f "$HOME/.bashrc" ]]; then
                echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.bashrc"
                print_success "Added to ~/.bashrc"
            fi
            if [[ -f "$HOME/.zshrc" ]]; then
                echo "export PATH=\"$INSTALL_DIR:\$PATH\"" >> "$HOME/.zshrc"
                print_success "Added to ~/.zshrc"
            fi
        fi
    fi
    
    # Create desktop entry (if desktop environment detected)
    if [[ -n "$XDG_CURRENT_DESKTOP" ]] && [[ $EUID -ne 0 ]]; then
        create_desktop_entry
    fi
    
    print_success "NetScanner installation completed!"
    print_status "You can now run: netscanner -h"
    print_status "Or use full path: $INSTALL_DIR/netscanner -h"
}

# Create desktop entry for GUI environments
create_desktop_entry() {
    DESKTOP_DIR="$HOME/.local/share/applications"
    mkdir -p "$DESKTOP_DIR"
    
    cat > "$DESKTOP_DIR/netscanner.desktop" << EOF
[Desktop Entry]
Name=NetScanner
Comment=Advanced Network Port Scanner
Exec=gnome-terminal -- netscanner -h
Icon=network-scanner
Terminal=true
Type=Application
Categories=Network;Security;
Keywords=network;scanner;port;security;
EOF
    
    print_success "Desktop entry created"
}

# Uninstall function
uninstall_netscanner() {
    print_status "Uninstalling NetScanner..."
    
    # Remove from common installation directories
    for dir in "/usr/local/bin" "$HOME/.local/bin"; do
        if [[ -f "$dir/netscanner" ]]; then
            rm -f "$dir/netscanner"
            print_success "Removed $dir/netscanner"
        fi
    done
    
    # Remove desktop entry
    if [[ -f "$HOME/.local/share/applications/netscanner.desktop" ]]; then
        rm -f "$HOME/.local/share/applications/netscanner.desktop"
        print_success "Removed desktop entry"
    fi
    
    print_success "NetScanner uninstalled successfully"
}

# Main script logic
case "${1:-install}" in
    "install")
        install_netscanner
        ;;
    "uninstall")
        uninstall_netscanner
        ;;
    "help"|"-h"|"--help")
        echo "NetScanner Installation Script"
        echo ""
        echo "Usage: $0 [install|uninstall|help]"
        echo ""
        echo "Commands:"
        echo "  install     Install NetScanner (default)"
        echo "  uninstall   Remove NetScanner"
        echo "  help        Show this help message"
        ;;
    *)
        print_error "Unknown command: $1"
        echo "Use '$0 help' for usage information"
        exit 1
        ;;
esac
