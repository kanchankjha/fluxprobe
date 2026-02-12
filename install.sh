#!/bin/bash
set -e
echo "Setting up FluxProbe APT repository..."
echo "deb [trusted=yes] https://kanchankjha.github.io/fluxprobe stable main" | sudo tee /etc/apt/sources.list.d/fluxprobe.list
sudo apt-get update
sudo apt-get install -y fluxprobe
echo "FluxProbe installed successfully!"
echo "Run 'fluxprobe --help' to get started."
