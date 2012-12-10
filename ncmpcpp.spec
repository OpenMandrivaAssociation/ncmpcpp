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


%changelog
* Tue Apr 03 2012 Andrey Bondrov <abondrov@mandriva.org> 0.5.10-1mdv2012.0
+ Revision: 788954
- New version 0.5.10

* Thu Mar 22 2012 Andrey Bondrov <abondrov@mandriva.org> 0.5.9-1
+ Revision: 786078
- New version 0.5.9

* Fri Dec 23 2011 Andrey Bondrov <abondrov@mandriva.org> 0.5.8-2
+ Revision: 744800
- Remove find_lang as there are no translations yet

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update to 0.5.8

* Wed Jun 15 2011 Sandro Cazzaniga <kharec@mandriva.org> 0.5.7-1
+ Revision: 685351
- new version 0.5.7

* Sun Jan 09 2011 Rémy Clouard <shikamaru@mandriva.org> 0.5.6-1
+ Revision: 630831
- New version 0.5.6

* Wed Sep 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.5-1mdv2011.0
+ Revision: 576859
- bump release

* Sun Aug 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.4-2mdv2011.0
+ Revision: 567658
- rebuild for new libmpdclient

* Tue Jul 13 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.4-1mdv2011.0
+ Revision: 552823
- bump release, many bugfixes and improvements

* Thu Apr 08 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.3-1mdv2010.1
+ Revision: 533119
- bump release

* Mon Mar 15 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.2-1mdv2010.1
+ Revision: 520351
- bump release

* Sun Feb 21 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.1-1mdv2010.1
+ Revision: 508965
- bump release

* Sun Jan 10 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5-1mdv2010.1
+ Revision: 488763
- update to new release (0.5)
- add taglib support

* Sat Nov 07 2009 Rémy Clouard <shikamaru@mandriva.org> 0.4.1-1mdv2010.1
+ Revision: 462100
- import ncmpcpp

