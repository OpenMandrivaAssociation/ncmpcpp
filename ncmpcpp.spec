%define name            ncmpcpp
%define version         0.5.1
%define release         %mkrel 1

Summary:                An ncurses mpd client inspired by ncmpc
Name:                   %name
Version:                %version
Release:                %release
License:                GPLv2+
Group:                  Sound
URL:                    http://unkart.ovh.org/ncmpcpp
Source:                 http://unkart.ovh.org/ncmpcpp/%{name}-%{version}.tar.bz2
BuildRoot:              %{_tmppath}/%{name}-%{version}-buildroot
BuildRequires:  ncurses-devel
BuildRequires:  ncursesw-devel
BuildRequires:  pkgconfig
BuildRequires:  libmpdclient-devel
BuildRequires:  curl-devel
BuildRequires:  taglib-devel
BuildRequires:  fftw-devel

%description
Ncmpcpp has UI very similar to ncmpc's one, but it provides new useful features
such as support for regular expressions in search engine, extended song format,
items filtering, last.fm support, ability to sort playlist, local filesystem
browser and other minor functions.

%prep
%setup -q

%build
%configure
%make

%install
rm -rf %buildroot
%makeinstall

%find_lang %name

%clean
rm -rf %buildroot

%files -f %name.lang
%defattr(-,root,root)
%doc AUTHORS NEWS COPYING
%_bindir/%{name}
%_mandir/man1/%{name}.*
