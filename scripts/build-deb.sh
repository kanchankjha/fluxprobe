#!/bin/bash
# Build Debian package locally
set -e

echo "Building FluxProbe Debian package..."

# Check for required tools
if ! command -v dpkg-buildpackage &> /dev/null; then
    echo "Installing build dependencies..."
    sudo apt-get update
    sudo apt-get install -y build-essential devscripts debhelper dh-python python3-all python3-setuptools python3-yaml dpkg-dev fakeroot
fi

# Build package
dpkg-buildpackage -us -uc -b

# Move packages to dist directory
mkdir -p dist
mv ../fluxprobe_*.deb dist/ 2>/dev/null || true
mv ../fluxprobe_*.changes dist/ 2>/dev/null || true
mv ../fluxprobe_*.buildinfo dist/ 2>/dev/null || true

echo ""
echo "Build complete! Package(s) in dist/:"
ls -la dist/

echo ""
echo "To install: sudo dpkg -i dist/fluxprobe_*.deb"
