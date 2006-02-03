Summary:	Input protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Input i pomocnicze
Name:		xorg-proto-inputproto
Version:	1.3.2
Release:	1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0/src/proto/inputproto-X11R7.0-%{version}.tar.bz2
# Source0-md5:	0da271f396bede5b8d09a61f6d1c4484
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Input protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Input i pomocnicze.

%package devel
Summary:	Input protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Input i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Input protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Input i pomocnicze.

%prep
%setup -q -n inputproto-X11R7.0-%{version}

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
