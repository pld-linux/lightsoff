Summary:	Lights Off
Summary(pl.UTF-8):	Gra Lights Off dla GNOME
Name:		lightsoff
Version:	3.12.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://ftp.gnome.org/pub/GNOME/sources/lightsoff/3.12/%{name}-%{version}.tar.xz
# Source0-md5:	40a100d7db0f2badf63024d1c8d4e69e
URL:		https://wiki.gnome.org/Apps/Lightsoff
BuildRequires:	appdata-tools
BuildRequires:	autoconf >= 2.63
BuildRequires:	automake >= 1:1.11
BuildRequires:	clutter-devel >= 1.14.0
BuildRequires:	clutter-gtk-devel >= 1.4.0
BuildRequires:	gnome-common
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	intltool >= 0.50.0
BuildRequires:	pkgconfig
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	clutter >= 1.14.0
Requires:	clutter-gtk >= 1.4.0
Requires:	gtk+3 >= 3.10.0
Requires:	hicolor-icon-theme
Provides:	gnome-games-lightsoff = 1:%{version}-%{release}
Obsoletes:	gnome-games-lightsoff < 1:3.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lights Off is a puzzle game, where the objective is to turn off all of
the tiles on the board. Each click toggles the state of the clicked
tile and its non-diagonal neighbors.

%description -l pl.UTF-8
Lights Off to układanka, której celem jest zgaszenie wszystkich pól na
planszy. Każde kliknięcie zmienia stan klikniętego pola oraz jego
najbliższych sąsiadów (nie po przekątnej).

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-silent-rules

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache HighContrast
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lightsoff
%{_datadir}/appdata/lightsoff.appdata.xml
%{_datadir}/glib-2.0/schemas/org.gnome.lightsoff.gschema.xml
%{_datadir}/lightsoff
%{_desktopdir}/lightsoff.desktop
%{_iconsdir}/HighContrast/*/*/*.png
%{_iconsdir}/hicolor/*/*/*.svg