Summary:	wmsensors draws graphs of data using CPU sensors
Summary(pl):	wmsensors przedstawia graficznie dane z czujników CPU
Name:		wmsensors
Version:	1.0.3
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://users.ox.ac.uk/~kebl0850/wmlm78/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRequires:	lm_sensors-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix 	/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
This application docks into the Window Maker dock and draws graphs of
data obtained from the sensors kernel module via a userspace library.

%description -l pl
Aplikacja przeznaczona dla Doku WindowMakera, przedstawia w postaci
graficznej dane uzyskane przez modu³ kernela z czujników procesora.

%prep
%setup -q -n %{name}

%build
xmkmf
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install wmsensors.1x $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf FAQ TODO *README Changes

%files
%defattr(644,root,root,755)
%doc {FAQ,TODO,*README,Changes}.gz
%attr(755,root,root) %{_bindir}/wmsensors
%{_mandir}/man1/wmsensors.1x*

%{_applnkdir}/DockApplets/wmsensors.desktop

%clean
rm -rf $RPM_BUILD_ROOT
