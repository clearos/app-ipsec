
Name: app-ipsec
Epoch: 1
Version: 2.0.1
Release: 1%{dist}
Summary: IPsec - Core
License: LGPLv3
Group: ClearOS/Libraries
Source: app-ipsec-%{version}.tar.gz
Buildarch: noarch

%description
The IPsec app provides core system functions for IPsec VPNs

%package core
Summary: IPsec - Core
Requires: app-base-core
Requires: /usr/sbin/ipsec

%description core
The IPsec app provides core system functions for IPsec VPNs

This package provides the core API and libraries.

%prep
%setup -q
%build

%install
mkdir -p -m 755 %{buildroot}/usr/clearos/apps/ipsec
cp -r * %{buildroot}/usr/clearos/apps/ipsec/

install -D -m 0644 packaging/ipsec.php %{buildroot}/var/clearos/base/daemon/ipsec.php

%post core
logger -p local6.notice -t installer 'app-ipsec-core - installing'

if [ $1 -eq 1 ]; then
    [ -x /usr/clearos/apps/ipsec/deploy/install ] && /usr/clearos/apps/ipsec/deploy/install
fi

[ -x /usr/clearos/apps/ipsec/deploy/upgrade ] && /usr/clearos/apps/ipsec/deploy/upgrade

exit 0

%preun core
if [ $1 -eq 0 ]; then
    logger -p local6.notice -t installer 'app-ipsec-core - uninstalling'
    [ -x /usr/clearos/apps/ipsec/deploy/uninstall ] && /usr/clearos/apps/ipsec/deploy/uninstall
fi

exit 0

%files core
%defattr(-,root,root)
%exclude /usr/clearos/apps/ipsec/packaging
%dir /usr/clearos/apps/ipsec
/usr/clearos/apps/ipsec/deploy
/usr/clearos/apps/ipsec/language
/var/clearos/base/daemon/ipsec.php
