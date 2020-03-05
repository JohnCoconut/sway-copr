Name:		wofi
Version:	1.1
Release:	1%{?dist}
Summary:	Wofi is a launcher/menu program for wlroots based wayland compositors

Group:		User Interface/X
License:	MIT
URL:		https://hg.sr.ht/~scoopta/wofi
Source0:	%{url}/archive/v%{version}.tar.gz

BuildRequires:	gcc
BuildRequires:	meson
BuildRequires:  hg
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(wayland-client)


%description
%{summary}

%prep
%autosetup -n %{name}-v%{version}

%build
%meson
%meson_build

%install
%meson_install

%files
%doc README.md
%{_bindir}/wofi
%exclude %{_exec_prefix}/lib/debug/usr/bin/*.debug

%changelog
* Fri Mar 06 2020 John Zhang <johannkokos@example.com> 1.1-1
- Bump to version 1.1

* Fri Jan 31 2020 João Pinto <jpinto@barcodeu.com> 1.0-1
- Initial RPM release
