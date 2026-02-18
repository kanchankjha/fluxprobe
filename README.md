# FluxProbe YUM Repository

This branch contains the YUM/DNF repository for installing FluxProbe on RHEL/CentOS/Fedora systems.

## Quick Installation

curl -fsSL https://raw.githubusercontent.com/kanchankjha/fluxprobe/yum-repo/install.sh | sudo bash

## Manual Setup

sudo tee /etc/yum.repos.d/fluxprobe.repo << EOF
[fluxprobe]
name=FluxProbe Repository
baseurl=https://kanchankjha.github.io/fluxprobe/packages
enabled=1
gpgcheck=0
EOF

sudo dnf install fluxprobe
# or on older systems: sudo yum install fluxprobe
