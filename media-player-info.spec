Summary:	Media player info files
Summary(pl.UTF-8):	Pliki media player info	
Name:		media-player-info
Version:	16
Release:	1
License:	BSD-like
Group:		Applications
Source0:	http://www.freedesktop.org/software/media-player-info/%{name}-%{version}.tar.gz
# Source0-md5:	11a01496a94522583431cc6c12b2c678
URL:		http://www.freedesktop.org/wiki/Software/media-player-info/
BuildRequires:	pkgconfig
BuildRequires:	udev-devel
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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README COPYING
%{_datadir}/media-player-info
/lib/udev/rules.d/40-usb-media-players.rules
