Summary:	Media player info files
Name:		media-player-info
Version:	6
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://hal.freedesktop.org/releases/%{name}-%{version}.tar.gz
# Source0-md5:	ac345d186ae8112f4854c1535ede51e8
BuildRequires:	pkgconfig
BuildRequires:	udev-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
media-player-info is a repository of data files describing media player (mostly
USB Mass Storage ones) capabilities. These files contain information about the
directory layout to use to add music to these devices, about the supported file
formats, etc.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING
%{_datadir}/media-player-info
/lib/udev/rules.d/40-usb-media-players.rules
