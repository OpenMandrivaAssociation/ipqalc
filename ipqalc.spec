Name:		ipqalc
Version:	1.5.2
Release:	1
Summary:	Small utility for IP address calculations
Group:		Networking/Other
License:	GPL
URL:		https://bitbucket.org/admsasha/ipqalc/
Source0:	https://bitbucket.org/admsasha/ipqalc/downloads/%{name}-%{version}.tar.gz

BuildRequires:	qt5-linguist-tools
BuildRequires:  qt5-macros
BuildRequires:  qmake5
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets) 

%description
Small utility for IP address calculations including broadcast
and network addresses as well as Cisco wildcard mask.

%prep
%setup -q

%build
%qmake_qt5
%make

%install
%make_install INSTALL_ROOT=%{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png 

