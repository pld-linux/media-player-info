Summary:	Media player info files
Summary(pl.UTF-8):	Pliki media player info
Name:		media-player-info
Version:	24
Release:	1
License:	BSD-like
Group:		Applications
Source0:	https://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
# Source0-md5:	1ccbfe93a671dffd5cd67d7965ccd7b3
URL:		https://www.freedesktop.org/wiki/Software/media-player-info/
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3
BuildRequires:	rpmbuild(macros) >= 1.691
BuildRequires:	udev-devel >= 1:196
Requires(post,postun):	udev-core >= 1:196
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
media-player-info is a repository of data files describing media
player (mostly USB Mass Storage ones) capabilities. These files
contain information about the directory layout to use to add music to
these devices, about the supported file formats, etc.

%description -l pl.UTF-8
media-player-info to repozytorium plikowe opisujące właściwości
odtwarzaczy muzyki (większość to pamięci masowe USB). Pliki zawierają
informację o strukturze katalogów aby dodawać muzykę do tych urządzeń,
o wspieranych formatach dzwiękowych, itd.

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

%post
%udev_hwdb_update

%postun
%udev_hwdb_update

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog NEWS
%{_datadir}/media-player-info
/lib/udev/hwdb.d/20-usb-media-players.hwdb
/lib/udev/rules.d/40-usb-media-players.rules
