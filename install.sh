#!/bin/bash
set -e
echo "Setting up FluxProbe YUM repository..."
sudo tee /etc/yum.repos.d/fluxprobe.repo << EOF
[fluxprobe]
name=FluxProbe Repository
baseurl=https://kanchankjha.github.io/fluxprobe/packages
enabled=1
gpgcheck=0
EOF

# Use dnf if available, otherwise yum
if command -v dnf &> /dev/null; then
    sudo dnf install -y fluxprobe
else
    sudo yum install -y fluxprobe
fi
echo "FluxProbe installed successfully!"
echo "Run 'fluxprobe --help' to get started."
