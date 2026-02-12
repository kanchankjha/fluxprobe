# FluxProbe APT Repository

This branch contains the APT repository for installing FluxProbe via apt-get.

## Quick Installation

curl -fsSL https://raw.githubusercontent.com/kanchankjha/fluxprobe/apt-repo/install.sh | sudo bash

## Manual Setup

echo "deb [trusted=yes] https://kanchankjha.github.io/fluxprobe stable main" | sudo tee /etc/apt/sources.list.d/fluxprobe.list
sudo apt-get update
sudo apt-get install fluxprobe
