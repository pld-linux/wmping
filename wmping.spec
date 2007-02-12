Summary:	Network hosts status monitor
Summary(pl.UTF-8):   Monitor stanu komputerów w sieci
Name:		wmping
Version:	0.2.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://cad.ntu-kpi.kiev.ua/~serg/projects/wm/%{name}-%{version}.tar.gz
# Source0-md5:	c8f3f501bc39389385558022f2a36f66
Source1:	%{name}.desktop
URL:		http://freshmeat.net/projects/wmping/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
Requires:	iputils-ping
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmping is a dockapp which checks the status of hosts in a network. It
show "up" status for a host that is available and "down" status for a
host that cannot be pinged.

%description -l pl.UTF-8
Wmping jest apletem, który sprawdza stan komputerów w sieci. Pokazuje
stan "włączony" dla komputerów, które są osiągalne i "wyłączony" dla
tych, które nie odpowiadają na pingi.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
install -d $RPM_BUILD_ROOT%{_desktopdir}/docklets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/docklets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/docklets/*
%{_mandir}/man1/*
