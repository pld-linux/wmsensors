Summary: 	wmsensors draws graphs of data using CPU sensors
Summary(pl):	wmsensors przedstawia graficznie dane z czujników CPU
Name: 		wmsensors
Version: 	1.0.3
Release: 	2
Copyright: 	GPL
Group: 		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0: 	http://users.ox.ac.uk/~kebl0850/wmlm78/%{name}-%{version}.tar.gz
Source1:	wmsensors.desktop
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	lm_sensors-devel >= 2.0
BuildRoot: 	/var/tmp/%{name}-%{version}-root

%define 	_prefix 	/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
This application docks into the Window Maker dock and draws graphs of data
obtained from the sensors kernel module via a userspace library.

%description -l pl
Aplikacja przeznaczona dla Doku WindowMakera, przedtstawia w postaci
graficznej dane uzyskane z czujników procesora przez modu³ kernela.

%prep
%setup -q -n %{name}

%build
xmkmf
make CDEBUGFLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

make install \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/man1 \
	BINDIR=%{_bindir}

install wmsensors.1x $RPM_BUILD_ROOT/usr/X11R6/man/man1
install %{SOURCE1} $RPM_BUILD_ROOT/usr/X11R6/share/applnk/DockApplets

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	FAQ TODO *README Changes

%files
%defattr(644,root,root,755)
%doc {FAQ,TODO,*README,Changes}.gz
%attr(755,root,root) %{_bindir}/wmsensors
%{_mandir}/man1/wmsensors.1x.gz

/usr/X11R6/share/applnk/DockApplets/wmsensors.desktop

%clean
rm -rf $RPM_BUILD_ROOT
