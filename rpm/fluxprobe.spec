Name:           fluxprobe
Version:        0.1.0
Release:        1%{?dist}
Summary:        Schema-driven protocol fuzzer

License:        MIT
URL:            https://github.com/kanchankjha/fluxprobe
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python3
Requires:       python3-pyyaml >= 6.0

%description
FluxProbe is a lightweight, schema-driven protocol fuzzer that generates
a mix of valid and intentionally corrupted frames for testing network
protocols against devices under test.

Features include:
* Declarative protocol schemas (YAML/JSON)
* Structure-aware and byte-level mutation strategies
* Multiple built-in protocol profiles (HTTP, DNS, MQTT, Modbus, etc.)
* TCP and UDP transport support
* Comprehensive test suite

%prep
%autosetup -n %{name}-%{version}

%build
# Nothing to build

%install
# Install using pip to a target directory
pip3 install --no-deps --target=%{buildroot}/usr/lib/python3/dist-packages .
# Remove the bin directory created by pip (we create our own wrapper)
rm -rf %{buildroot}/usr/lib/python3/dist-packages/bin
# Remove __pycache__ to avoid issues
find %{buildroot} -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
# Create bin directory and wrapper script
mkdir -p %{buildroot}/usr/bin
cat > %{buildroot}/usr/bin/fluxprobe << 'EOF'
#!/usr/bin/env python3
from fluxprobe.cli import main
if __name__ == "__main__":
    main()
EOF
chmod +x %{buildroot}/usr/bin/fluxprobe
# Debug: List installed files
echo "=== Installed files ==="
find %{buildroot} -type f | sort

%files
%license LICENSE
%doc README.md
%dir /usr/lib/python3/dist-packages/%{name}/
/usr/lib/python3/dist-packages/%{name}/*
/usr/lib/python3/dist-packages/%{name}-*.dist-info
/usr/bin/fluxprobe

%changelog
* Thu Feb 12 2026 Kanchan Kumar Jha <kanchankjha@gmail.com> - 0.1.0-1
- Initial RPM release
- Schema-driven protocol fuzzing with YAML/JSON support
- Built-in profiles: echo, http, dns, mqtt, modbus, coap, tcp, udp, ip, snmp, ssh
- TCP and UDP transport support
- Multiple mutation strategies
