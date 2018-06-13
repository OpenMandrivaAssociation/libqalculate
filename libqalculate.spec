%define sname	qalc
%define bname	qalculate
%define major	18
%define libname	%mklibname %{bname} %{major}
%define devname	%mklibname %{bname} -d

Summary:	The library for Qalculate!
Name:	 	libqalculate
Version:	2.6.0b
Release:	1
License:	GPLv2+
Group:		System/Libraries
Url:		https://qalculate.github.io/
Source0:	https://github.com/Qalculate/libqalculate/archive/v2.6.0b.tar.gz
BuildRequires:	doxygen
BuildRequires:	gmp-devel
BuildRequires:	readline-devel
BuildRequires:	intltool
BuildRequires:	perl(XML::Parser)
BuildRequires:	pkgconfig(cln)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(icu-uc)
BuildRequires:	pkgconfig(libcurl)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	pkgconfig(mpfr)
BuildRequires:	pkgconfig(ncurses)

%description
Libraries needed by Qalculate!.

#----------------------------------------------------------------------------

%package -n %{sname}
Group:		System/Libraries
Summary:	CLI frontend for Qalculate!
Requires:	%{libname} = %{version}-%{release}

%description -n %{sname}
Qalculate! is a multi-purpose desktop calculator for GNU/Linux. It is small
and simple to use but with much power and versatility underneath

Features include customizable functions, units, arbitrary precision,
plotting, and a user-friendly interface (GTK+ and CLI).

This package provides the CLI frontend.

%files -n %{sname}
%{_bindir}/%{sname}

#----------------------------------------------------------------------------

%package -n %{libname}
Group:		System/Libraries
Summary:	The library for qalculate
Requires:	%{name}-data = %{version}-%{release}

%description -n %{libname}
Shared library for Qalculate!.

%files -n %{libname}
%{_libdir}/libqalculate.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{bname}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{devname}
Headers and development files for Qalculate!.

%files -n %{devname}
%doc AUTHORS ChangeLog NEWS README* TODO
%doc %dir %{_datadir}/%{bname}
%doc %{_docdir}/%{name}
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc

#----------------------------------------------------------------------------

%package data
Summary:	Data files for %{name}
Group:		System/Libraries
Requires:	%{libname} = %{version}-%{release}
BuildArch:	noarch
Obsoletes:	%mklibname qalculate 8
Obsoletes:	%mklibname qalculate 9
Obsoletes:	%mklibname qalculate 10

%description data
Data files for %{name}.

%files data -f %{name}.lang
%{_datadir}/qalculate/*.xml
%{_datadir}/qalculate/*.json

#----------------------------------------------------------------------------

%prep
%setup -q
NOCONFIGURE=1 ./autogen.sh
autoheader

%build
# docs
pushd docs/reference
doxygen
popd

# binaries
%configure
%make_build

%install
%makeinstall_std

# locales
%find_lang %{name}

