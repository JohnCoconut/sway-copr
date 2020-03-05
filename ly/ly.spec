Name:       ly
Version:    0.5.0
Release:    1%{?dist}
Summary:    TUI (ncurses-like) display manager 
License:    MIT
URL:        https://github.com/cylgom/ly
Source0:	%{url}/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  git
BuildRequires:  pam-devel
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(xorg-server)
BuildRequires:  xorg-x11-xauth 
BuildRequires:  util-linux
BuildRequires:  pkgconfig(ncurses)

%description
%{summary}

%prep
%autosetup

%build
make github
make
make install

%files

%changelog
* Fri Mar 06 2020 John Zhang <johannkokos@example.com> 0.5.0-1
- Fix build

* Wed Feb 5 2020 João Pinto <jpinto@barcodeu.com> 0.5.0-1
- Bump version to 0.5.0
- Fixed build flow

* Fri Jan 31 2020 João Pinto <jpinto@barcodeu.com> 0.4.0-1
- Initial RPM release
