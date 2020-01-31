Name:       ly
Version:    0.4.0
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
make github

%build
make
make install

%files

%changelog
* Fri Jan 31 2020 João Pinto <jpinto@barcodeu.com> 0.4.0-1
- Initial RPM release