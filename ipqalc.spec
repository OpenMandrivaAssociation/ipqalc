%define		oname	ipQalc

Name:		ipqalc
Version:	1.2
Release:	%mkrel 1
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
%__rm -rf %{buildroot}

# install binary
%__mkdir_p %{buildroot}%{_bindir}
%__cp %{oname} %{buildroot}%{_bindir}/%{name}

# install locales
%__mkdir_p %{buildroot}%{_datadir}/%{name}
%__cp *.qm %{buildroot}%{_datadir}/%{name}/

# XDG menu entry
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Type=Application
Name=%{oname}
Comment=IP address calculator
Icon=networking_www_section
Exec=%{name}
Terminal=false
Categories=Utility;
EOF

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop

