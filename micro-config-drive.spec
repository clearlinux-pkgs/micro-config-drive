#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : micro-config-drive
Version  : 47
Release  : 34
URL      : https://github.com/clearlinux/micro-config-drive/releases/download/v47/micro-config-drive-47.tar.xz
Source0  : https://github.com/clearlinux/micro-config-drive/releases/download/v47/micro-config-drive-47.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: micro-config-drive-autostart = %{version}-%{release}
Requires: micro-config-drive-bin = %{version}-%{release}
Requires: micro-config-drive-license = %{version}-%{release}
Requires: micro-config-drive-man = %{version}-%{release}
Requires: micro-config-drive-services = %{version}-%{release}
Requires: e2fsprogs-bin
BuildRequires : e2fsprogs-bin
BuildRequires : glib-dev
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libparted)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(yaml-0.1)

%description
## A config-drive handler.
### Contents:
- Description of this project
- Compiling, prerequisites
- Security considerations
- Bugs and feedback?

%package autostart
Summary: autostart components for the micro-config-drive package.
Group: Default

%description autostart
autostart components for the micro-config-drive package.


%package bin
Summary: bin components for the micro-config-drive package.
Group: Binaries
Requires: micro-config-drive-license = %{version}-%{release}
Requires: micro-config-drive-services = %{version}-%{release}

%description bin
bin components for the micro-config-drive package.


%package license
Summary: license components for the micro-config-drive package.
Group: Default

%description license
license components for the micro-config-drive package.


%package man
Summary: man components for the micro-config-drive package.
Group: Default

%description man
man components for the micro-config-drive package.


%package services
Summary: services components for the micro-config-drive package.
Group: Systemd services

%description services
services components for the micro-config-drive package.


%prep
%setup -q -n micro-config-drive-47
cd %{_builddir}/micro-config-drive-47

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1667587183
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1667587183
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/micro-config-drive
cp %{_builddir}/micro-config-drive-%{version}/COPYING %{buildroot}/usr/share/package-licenses/micro-config-drive/8624bcdae55baeef00cd11d5dfcfa60f68710a02
cp %{_builddir}/micro-config-drive-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/micro-config-drive/b5e5f8134b8651d53d5804bb982b9eb4217611c4
%make_install

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/ucd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/ucd
/usr/bin/ucd-data-fetch

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/micro-config-drive/8624bcdae55baeef00cd11d5dfcfa60f68710a02
/usr/share/package-licenses/micro-config-drive/b5e5f8134b8651d53d5804bb982b9eb4217611c4

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/ucd-data-fetch.1
/usr/share/man/man1/ucd.1
/usr/share/man/man5/cloud-config.5

%files services
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/ucd.service
/usr/lib/systemd/system/ucd.service
/usr/lib/systemd/system/ucd@.service
