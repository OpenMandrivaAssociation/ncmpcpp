Summary:	An ncurses mpd client inspired by ncmpc
Name:		ncmpcpp
Version:	0.5.10
Release:	%mkrel 1
License:	GPLv2+
Group:		Sound
URL:		http://unkart.ovh.org/ncmpcpp
Source:		http://unkart.ovh.org/ncmpcpp/%{name}-%{version}.tar.bz2
BuildRequires:	ncurses-devel
BuildRequires:	ncursesw-devel
BuildRequires:	libmpdclient-devel
BuildRequires:	curl-devel
BuildRequires:	taglib-devel
BuildRequires:	fftw-devel

%description
Ncmpcpp has UI very similar to ncmpc's one, but it provides new useful features
such as support for regular expressions in search engine, extended song format,
items filtering, last.fm support, ability to sort playlist, local filesystem
browser and other minor functions.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall

%clean
%__rm -rf %{buildroot}

%files
%doc AUTHORS NEWS COPYING
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.*
