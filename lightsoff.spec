Summary:	GNOME Lights Off game
Summary(pl.UTF-8):	Gra Lights Off dla GNOME
Name:		lightsoff
Version:	46.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	https://download.gnome.org/sources/lightsoff/46/%{name}-%{version}.tar.xz
# Source0-md5:	6d5984a6a665d451d19689e05f82eda2
URL:		https://wiki.gnome.org/Apps/Lightsoff
BuildRequires:	appstream-glib
BuildRequires:	gettext-tools >= 0.19.8
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gtk+3-devel >= 3.24
BuildRequires:	librsvg-devel >= 1:2.32.0
BuildRequires:	meson >= 0.56.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	tar >= 1:1.22
BuildRequires:	vala >= 2:0.22.0
BuildRequires:	vala-librsvg >= 1:2.32.0
BuildRequires:	xz
BuildRequires:	yelp-tools
Requires(post,postun):	gtk-update-icon-cache
Requires(post,postun):	glib2 >= 1:2.38.0
Requires:	glib2 >= 1:2.38.0
Requires:	gtk+3 >= 3.24
Requires:	hicolor-icon-theme
Requires:	librsvg >= 1:2.32.0
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
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas
%update_icon_cache hicolor

%postun
%glib_compile_schemas
%update_icon_cache hicolor

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc NEWS
%attr(755,root,root) %{_bindir}/lightsoff
%{_datadir}/dbus-1/services/org.gnome.LightsOff.service
%{_datadir}/glib-2.0/schemas/org.gnome.LightsOff.gschema.xml
%{_datadir}/lightsoff
%{_datadir}/metainfo/org.gnome.LightsOff.appdata.xml
%{_desktopdir}/org.gnome.LightsOff.desktop
%{_iconsdir}/hicolor/scalable/apps/org.gnome.LightsOff.svg
%{_iconsdir}/hicolor/scalable/apps/org.gnome.LightsOff.Devel.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.LightsOff-symbolic.svg
%{_mandir}/man6/lightsoff.6*
