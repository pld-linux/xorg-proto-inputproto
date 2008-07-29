Summary:	Input extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Input
Name:		xorg-proto-inputproto
Version:	1.4.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
#Source0:	http://xorg.freedesktop.org/releases/individual/proto/inputproto-%{version}.tar.bz2
Source0:	inputproto-20080702.tar.bz2
# Source0-md5:	408e23bd5ab98494d7146cc240e0639e
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Input extension headers.

%description -l pl.UTF-8
Nagłówki rozszerzenia Input.

%package devel
Summary:	Input extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Input
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Input extension headers.

%description devel -l pl.UTF-8
Nagłówki rozszerzenia Input.

%prep
%setup -q -n inputproto

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/inputproto.pc
