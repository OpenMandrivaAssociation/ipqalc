%define		oname	ipQalc

Name:		ipqalc
Version:	1.2
Release:	2
Summary:	Small utility for IP address calculations
Group:		Networking/Other
License:	GPL
URL:		http://qt-apps.org/content/show.php/ipQalc?content=107286
Source0:	%{oname}-%{version}.tar.gz
Patch0:		ipqalc-1.2-localepath.patch
BuildRequires:	qt4-devel

%description
Small utility for IP address calculations including broadcast
and network addresses as well as Cisco wildcard mask.

%prep
%setup -q -n %{oname}
%patch0 -p1

%build
%qmake_qt4 %{oname}.pro
%make

%install
# install binary
mkdir -p %{buildroot}%{_bindir}
cp %{oname} %{buildroot}%{_bindir}/%{name}

# install locales
mkdir -p %{buildroot}%{_datadir}/%{name}
cp *.qm %{buildroot}%{_datadir}/%{name}/

# XDG menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{oname}
Comment=IP address calculator
Icon=networking_www_section
Exec=%{name}
Terminal=false
Categories=Utility;
EOF

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop


%changelog
* Fri Mar 30 2012 Andrey Bondrov <abondrov@mandriva.org> 1.2-1mdv2011.0
+ Revision: 788283
- imported package ipqalc

