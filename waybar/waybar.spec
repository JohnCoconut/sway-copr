%define debug_package %{nil}
%define waybar_dir Waybar-%{version}

Name:       waybar
Version:    0.9.0
Release:    1%{?dist}
Summary:    Highly customizable Wayland bar for Sway and Wlroots based compositors.
License:    MIT
Group:      System/GUI/Other
URL:        https://github.com/Alexays/Waybar
Source0:    https://github.com/Alexays/Waybar/archive/%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	meson
BuildRequires:	gcc-c++
BuildRequires:	pkgconfig(threads)
BuildRequires:	pkgconfig(libinput)
BuildRequires:	pkgconfig(gtkmm30) >= 3.22.0
BuildRequires:	pkgconfig(jsoncpp)
BuildRequires:	libappindicator-gtk3-devel
BuildRequires:	pkgconfig(dbusmenu-gtk3-0.4)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-cursor)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:	sway >= 1.0
BuildRequires:  wlroots-devel < 0.9
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(libnl-3.0)
BuildRequires:	pkgconfig(libnl-genl-3.0)
BuildRequires:	pkgconfig(libudev)
BuildRequires:	pkgconfig(fmt) >= 5.3.0
BuildRequires:	pkgconfig(libmpdclient)
BuildRequires:	git
BuildRequires:	pkgconfig(spdlog) >= 1.3.1
BuildRequires:	pkgconfig(gtk-layer-shell-0)
BuildRequires:	gtk3-devel
BuildRequires:	gobject-introspection
BuildRequires:  pkgconfig(systemd)
BuildRequires:  scdoc >= 1.9.2
Requires:	    fmt >= 5.3.0
Recommends:     sway
Recommends:     fontawesome-fonts

%description
Highly customizable Wayland bar for Sway and Wlroots based compositors.

%prep
%autosetup -n %{waybar_dir}

%build
%meson
%meson_build

%install
%meson_install

%files
%license LICENSE
%doc README.md
%{_sysconfdir}/xdg/waybar/
%{_bindir}/waybar


%changelog
* Thu Jan 30 2020 João Pinto <jpinto@barcodeu.com> 0.9.0-1
- Initial RPM release