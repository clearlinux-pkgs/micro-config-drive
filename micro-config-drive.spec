#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : micro-config-drive
Version  : 27
Release  : 3
URL      : https://github.com/clearlinux/micro-config-drive/releases/download/v27/micro-config-drive-27.tar.xz
Source0  : https://github.com/clearlinux/micro-config-drive/releases/download/v27/micro-config-drive-27.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0
Requires: micro-config-drive-bin
Requires: micro-config-drive-autostart
Requires: micro-config-drive-config
Requires: micro-config-drive-doc
BuildRequires : e2fsprogs-bin
BuildRequires : pkgconfig(blkid)
BuildRequires : pkgconfig(check)
BuildRequires : pkgconfig(glib-2.0)
BuildRequires : pkgconfig(json-glib-1.0)
BuildRequires : pkgconfig(libparted)
BuildRequires : pkgconfig(systemd)
BuildRequires : pkgconfig(yaml-0.1)

%description
A config-drive handler.
====
Contents:
1) Description of this project
2) Compiling, prerequisites
3) Bugs and feedback?

%package autostart
Summary: autostart components for the micro-config-drive package.
Group: Default

%description autostart
autostart components for the micro-config-drive package.


%package bin
Summary: bin components for the micro-config-drive package.
Group: Binaries
Requires: micro-config-drive-config

%description bin
bin components for the micro-config-drive package.


%package config
Summary: config components for the micro-config-drive package.
Group: Default

%description config
config components for the micro-config-drive package.


%package doc
Summary: doc components for the micro-config-drive package.
Group: Documentation

%description doc
doc components for the micro-config-drive package.


%prep
%setup -q -n micro-config-drive-27

%build
export LANG=C
export SOURCE_DATE_EPOCH=1493417585
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1493417585
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files autostart
%defattr(-,root,root,-)
/usr/lib/systemd/system/multi-user.target.wants/ucd.service

%files bin
%defattr(-,root,root,-)
/usr/bin/ucd
/usr/bin/ucd-aws

%files config
%defattr(-,root,root,-)
%exclude /usr/lib/systemd/system/multi-user.target.wants/ucd.service
/usr/lib/systemd/system/ucd-aws.service
/usr/lib/systemd/system/ucd.service

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man5/*
