Summary:	Input protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Input i pomocnicze
Name:		xorg-proto-inputproto
Version:	1.4
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/inputproto-%{version}.tar.bz2
# Source0-md5:	0208a5cf8ab43f10d87145f1535f7101
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Input protocol and ancillary headers.

%description -l pl.UTF-8
Nagłówki protokołu Input i pomocnicze.

%package devel
Summary:	Input protocol and ancillary headers
Summary(pl.UTF-8):	Nagłówki protokołu Input i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Input protocol and ancillary headers.

%description devel -l pl.UTF-8
Nagłówki protokołu Input i pomocnicze.

%prep
%setup -q -n inputproto-%{version}

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
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/inputproto.pc
