Name:		ytop
Version:	0.4.1
Release:	1%{?dist}
Summary:	TUI based system monitor in Rust

Group: 		Applications/System
License:	MIT
URL:		https://github.com/cjbassi/ytop
Source0:	%{url}/archive/%{version}.tar.gz


BuildRequires:  cargo

%description
%{summary}

%prep
%autosetup

%build
cargo build --release --locked --all-features

%files

%changelog
* Fri Feb 7 2020 João Pinto <jpinto@barcodeu.com> 0.4.1-1
- Initial RPM release
