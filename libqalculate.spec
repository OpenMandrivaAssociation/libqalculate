%define sname qalc
%define bname qalculate
%define major 23
%define libname %mklibname %{bname}
%define devname %mklibname %{bname} -d
# For obsoletion
%define lib19name %mklibname %{bname} 19
%define lib20name %mklibname %{bname} 20
%define lib21name %mklibname %{bname} 21
%define lib22name %mklibname %{bname} 22

Summary:	The library for Qalculate!
Name:	 	libqalculate
Version:	5.1.1
Release:	2
License:	GPLv2+
Group:		System/Libraries
Url:		https://qalculate.github.io/
Source0:	https://github.com/Qalculate/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.gz
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
Requires:	%{libname} = %{EVRD}

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
Requires:	%{name}-data >= %{EVRD}
Obsoletes:	%{lib19name} < %{EVRD}
Obsoletes:	%{lib20name} < %{EVRD}
Obsoletes:	%{lib21name} < %{EVRD}
Obsoletes:	%{lib22name} < %{EVRD}
Obsoletes:	%{mklibname qalculate 8} < %{EVRD}
Obsoletes:	%{mklibname qalculate 9} < %{EVRD}
Obsoletes:	%{mklibname qalculate 10} < %{EVRD}

%description -n %{libname}
Shared library for Qalculate!.

%files -n %{libname}
%{_libdir}/libqalculate.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/Other
Requires:	%{libname} = %{EVRD}
Requires:	gmp-devel
Requires:	pkgconfig(mpfr)
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
BuildArch:	noarch

%description data
Data files for %{name}.

%files data -f %{name}.lang
%{_datadir}/qalculate/*.xml
%{_datadir}/qalculate/rates.json
%{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%autosetup -p1
NOCONFIGURE=1 ./autogen.sh
autoheader

%build
# docs
cd docs/reference
doxygen
cd -

# binaries
%configure
%make_build

%install
%make_install

# locales
%find_lang %{name}
