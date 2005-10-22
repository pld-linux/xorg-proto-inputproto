Summary:	Input protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Input i pomocnicze
Name:		xorg-proto-inputproto
Version:	1.3.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/inputproto-%{version}.tar.bz2
# Source0-md5:	6710bb1961bcceb099a1635c1f101016
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Input protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u Input i pomocnicze.

%package devel
Summary:	Input protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Input i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Input protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u Input i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/inputproto.pc
