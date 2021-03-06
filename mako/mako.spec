Name:       mako
Version:	1.4.1
Release:	1%{?dist}
Summary:	A lightweight notification daemon for Wayland.

License:     MIT
URL:        https://github.com/emersion/mako
Source0:    %{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson >= 0.47.0
BuildRequires:  pkgconfig(libsystemd)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-protocols) >= 1.14
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(pangocairo)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gobject-2.0)
#To fix issue 213
BuildRequires:	scdoc >= 1.9.7
BuildRequires:  pkgconfig(gdk-pixbuf-2.0)

%description
%{summary}

%prep
%setup -q


%build
%meson
%meson_build


%install
%meson_install


%files
%license LICENSE
%doc README*.md
%{_bindir}/mako
%{_bindir}/makoctl
%{_mandir}/man1/mako*.1*
%{_mandir}/man5/mako*.5*
%{_mandir}/man1/makoctl*.1*
%{_datadir}/dbus-1/services/fr.emersion.mako.service

%changelog
* Thu Jan 30 2020 João Pinto <jpinto@barcodeu.com> 1.4.1-1
- Initial RPM release
