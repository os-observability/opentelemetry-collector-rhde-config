Name: opentelemetry-collector-rhde-config
Version: 1.0
Release: 1%{?dist}
Summary: RHDE Observability Agent
BuildArch: noarch

License: Apache-2.0
Source1: config.yaml
Source2: opentelemetry-collector-rhde-config.service

# Necessary to access the systemd macros
BuildRequires: systemd
Requires: opentelemetry-collector

Requires(pre): /usr/sbin/useradd, /usr/bin/getent
Requires(postun): /usr/sbin/userdel

%description
RHDE observability agent configuration.

%install
# create expected directory layout
mkdir -p %{buildroot}%{_sysconfdir}/opentelemetry-collector-rhde-config
mkdir -p %{buildroot}%{_unitdir}

# install files
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/opentelemetry-collector-rhde-config/config.yaml
install -p -m 0644 -D %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

# TODO give access to microshift logs
# TODO give access to proc for metrics
%pre
/usr/bin/getent group rhde-observability > /dev/null || /usr/sbin/groupadd -r rhde-observability
/usr/bin/getent passwd rhde-observability > /dev/null || /usr/sbin/useradd -r -M -s /sbin/nologin -g rhde-observability -G systemd-journal rhde-observability

%postun
/usr/sbin/userdel rhde-observability

%post
/bin/systemctl --system daemon-reload 2>&1

%preun
if [ $1 -eq 0 ]; then
    /bin/systemctl --quiet stop %{name}.service
    /bin/systemctl --quiet disable %{name}.service
fi

%posttrans
/bin/systemctl is-enabled %{name}.service >/dev/null 2>&1
if [  $? -eq 0 ]; then
    /bin/systemctl restart %{name}.service >/dev/null
fi

%files
%{_unitdir}/%{name}.service
%{_sysconfdir}/opentelemetry-collector-rhde-config/config.yaml

%changelog
* Fri Jan 26 2024 Benedikt Bongartz <bongartz@redhat.com> - 1.0-1
- initialize package
