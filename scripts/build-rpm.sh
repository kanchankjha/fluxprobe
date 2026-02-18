#!/bin/bash
# Build RPM package locally
set -e

echo "Building FluxProbe RPM package..."

# Check for required tools
if ! command -v rpmbuild &> /dev/null; then
    echo "Installing build dependencies..."
    if command -v dnf &> /dev/null; then
        sudo dnf install -y rpm-build rpmdevtools python3-devel python3-setuptools python3-pip
    elif command -v yum &> /dev/null; then
        sudo yum install -y rpm-build rpmdevtools python3-devel python3-setuptools python3-pip
    else
        echo "Error: Neither dnf nor yum found. Please install rpm-build manually."
        exit 1
    fi
fi

# Setup RPM build environment
rpmdev-setuptree || true

# Get version from pyproject.toml
VERSION=$(grep -E '^version\s*=' pyproject.toml | sed 's/.*"\(.*\)".*/\1/')
echo "Building version: $VERSION"

# Create tarball
TARBALL_DIR="fluxprobe-$VERSION"
mkdir -p "$TARBALL_DIR"
cp -r fluxprobe examples LICENSE README.md pyproject.toml requirements.txt "$TARBALL_DIR/"
tar czf ~/rpmbuild/SOURCES/fluxprobe-$VERSION.tar.gz "$TARBALL_DIR"
rm -rf "$TARBALL_DIR"

# Copy spec file
cp rpm/fluxprobe.spec ~/rpmbuild/SPECS/

# Update version in spec file
sed -i "s/^Version:.*/Version:        $VERSION/" ~/rpmbuild/SPECS/fluxprobe.spec

# Build RPM
rpmbuild -ba ~/rpmbuild/SPECS/fluxprobe.spec

# Move packages to dist directory
mkdir -p dist
cp ~/rpmbuild/RPMS/noarch/fluxprobe-*.rpm dist/ 2>/dev/null || true
cp ~/rpmbuild/SRPMS/fluxprobe-*.rpm dist/ 2>/dev/null || true

echo ""
echo "Build complete! Package(s) in dist/:"
ls -la dist/*.rpm

echo ""
echo "To install: sudo dnf install dist/fluxprobe-*.noarch.rpm"
