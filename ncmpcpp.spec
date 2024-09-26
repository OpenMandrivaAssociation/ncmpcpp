Summary:	An ncurses mpd client inspired by ncmpc
Name:		ncmpcpp
Version:	0.10
Release:	1
License:	GPLv2+
Group:		Sound
Url:		http://rybczak.net/ncmpcpp/
Source0:	https://github.com/ncmpcpp/ncmpcpp/archive/%{version}/%{name}-%{version}.tar.gz
BuildRequires:	boost-devel >= 1.60.0
BuildRequires:	readline-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(libmpdclient) >= 2.9
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(ncursesw)
BuildRequires:	pkgconfig(taglib)
BuildRequires:  pkgconfig(zlib)

%description
Ncmpcpp has UI very similar to ncmpc's one, but it provides new useful
features such as support for regular expressions in search engine, extended
song format, items filtering, last.fm support, ability to sort playlist, local
filesystem browser and other minor functions.

%files
%doc doc/config doc/bindings AUTHORS COPYING CHANGELOG.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install
