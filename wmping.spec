Summary:	Network hosts status monitor
Summary(pl):	Monitor stanu komputerów w sieci
Name:		wmping
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://cad.ntu-kpi.kiev.ua/~serg/projects/wm/%{name}-%{version}.tgz
# Source0-md5:	e4bb437531460be9f101e05da3b5cb64
Source1:	%{name}.desktop
URL:		http://freshmeat.net/projects/wmping/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Wmping is a dockapp which checks the status of hosts in a network. It
show "up" status for a host that is available and "down" status for a
host that cannot be pinged.

%description -l pl
Wmping jest apletem, który sprawdza stan komputerów w sieci. Pokazuje
stan "w³±czony" dla komputerów, które s± osi±galne i "wy³±czony" dla
tych, które nie odpowiadaj± na pingi.

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
install -d $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_applnkdir}/DockApplets/*
%{_mandir}/man1/*
