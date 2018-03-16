# NOTE: now maintained in xorg-proto-xorgproto.spec
Summary:	Input extension headers
Summary(pl.UTF-8):	Nagłówki rozszerzenia Input
Name:		xorg-proto-inputproto
Version:	2.3.2
Release:	1.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	https://xorg.freedesktop.org/releases/individual/proto/inputproto-%{version}.tar.bz2
# Source0-md5:	b290a463af7def483e6e190de460f31a
URL:		https://xorg.freedesktop.org/
BuildRequires:	asciidoc >= 8.4.5
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros >= 1.10
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
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog README specs/{XIproto.txt,XI2proto.txt}
%{_includedir}/X11/extensions/XI.h
%{_includedir}/X11/extensions/XIproto.h
%{_includedir}/X11/extensions/XI2.h
%{_includedir}/X11/extensions/XI2proto.h
%{_pkgconfigdir}/inputproto.pc
