Name:           fluxprobe
Version:        0.1.0
Release:        1%{?dist}
Summary:        Schema-driven protocol fuzzer

License:        MIT
URL:            https://github.com/kanchankjha/fluxprobe
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pip
BuildRequires:  python3-wheel

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
python3 setup.py build

%install
python3 setup.py install --root=%{buildroot} --optimize=1

%files
%license LICENSE
%doc README.md
%{python3_sitelib}/%{name}/
%{python3_sitelib}/%{name}-%{version}*
%{_bindir}/fluxprobe

%changelog
* Thu Feb 12 2026 Kanchan Kumar Jha <kanchankjha@gmail.com> - 0.1.0-1
- Initial RPM release
- Schema-driven protocol fuzzing with YAML/JSON support
- Built-in profiles: echo, http, dns, mqtt, modbus, coap, tcp, udp, ip, snmp, ssh
- TCP and UDP transport support
- Multiple mutation strategies
