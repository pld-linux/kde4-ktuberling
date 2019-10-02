%define		_state		stable
%define		orgname		ktuberling
%define		qtver		4.8.0

Summary:	KDE game for small children
Summary(pl.UTF-8):	Gra dla małych dzieci
Summary(pt_BR.UTF-8):	Jogo de desenho do 'Homem-batata' para crianças
Name:		kde4-%{orgname}
Version:	4.14.3
Release:	3
License:	GPL
Group:		X11/Applications/Games
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	c65a101c5c5958db7a3fc651b0919a08
BuildRequires:	automoc4 >= 0.9.88
BuildRequires:	cmake >= 2.8.0
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-libkdegames-devel >= %{version}
BuildRequires:	qt4-build >= %{qtver}
BuildRequires:	qt4-qmake >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.600
Obsoletes:	kde4-kdegames-%{orgname}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
It is a potato editor. That means that you can drag and drop eyes,
mouths, moustache, and other parts of face and goodies onto a
potato-like guy.

There is no winer. The only purpose is to make the funniest faces you
can.

%description -l pl.UTF-8
KTuberling to edytor ziemniaków. Oznacza to, że można układać oczy,
usta, wąsy oraz inne części twarzy na postać podobną do ziemniaka.

W grze nie ma zwycięzcy. Jedynym celem gry jest stworzenie
najzabawniejszej twarzy, jaką się da ułożyć.

%description -l pt_BR.UTF-8
Jogo de desenho do 'Homem-batata' para crianças.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT/var/games
# remove locolor icons
rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

%find_lang %{orgname}	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktuberling
%{_desktopdir}/kde4/ktuberling.desktop
%{_datadir}/apps/ktuberling
%{_iconsdir}/*/*/apps/ktuberling.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-tuberling.png
