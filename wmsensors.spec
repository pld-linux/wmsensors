Summary:	wmsensors draws graphs of data using CPU sensors
Summary(pl):	wmsensors przedstawia graficznie dane z czujników CPU
Name:		wmsensors
Version:	1.0.3
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://users.ox.ac.uk/~kebl0850/wmlm78/%{name}-%{version}.tar.gz
# Source0-md5:	7e9805f46151db0ea6adb2abd6e3ae8f
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRequires:	lm_sensors-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This application docks into the Window Maker dock and draws graphs of
data obtained from the sensors kernel module via a userspace library.

%description -l pl
Aplikacja przeznaczona dla Doku WindowMakera, przedstawia w postaci
graficznej dane uzyskane przez modu³ kernela z czujników procesora.

%prep
%setup -q -n %{name}

%build
mv wmsensors.1x wmsensors.man
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
%{__make} DESTDIR=$RPM_BUILD_ROOT install.man

#install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/DockApplets

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc FAQ TODO *README Changes
%attr(755,root,root) %{_bindir}/wmsensors
%{_mandir}/man1/wmsensors.1x*
#%%{_applnkdir}/DockApplets/wmsensors.desktop
