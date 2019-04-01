Name:           LimeSuite
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Driver and GUI for LMS7002M-based SDR platforms
License:        Apache 2.0
Group:          Development/Libraries/C and C++
Url:            https://myriadrf.org/projects/software/lime-suite/
Source:         %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake
BuildRequires:	libusbx-devel
BuildRequires:	octave-devel
BuildRequires:	gnuplot
BuildRequires:	wxGTK3-devel
BuildRequires:	fltk-devel

%description
The Lime Suite application software provides drivers and SDR application support for the LMS7002M RFIC, and hardware like the LimeSDR, NovenaRF7, and others.

%package devel
Summary:    Development headers and library for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}

%description devel
This package contains the development headers and library for %{name}.

%prep
%setup -n %{name}-%{version}

%build
mkdir builddir
pushd builddir
cmake3 -DCMAKE_INSTALL_PREFIX:PATH=/usr -DLIB_SUFFIX=64 ../
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
pushd builddir
make install DESTDIR=%{buildroot}
popd

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README.md
%{_bindir}/Lime*
%{_libdir}/lib%{name}.so.*
%{_libdir}/octave/*
%{_libdir}/SoapySDR/*
%{_datadir}/Lime/*
%{_datadir}/octave/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/lime
%{_libdir}/lib%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/cmake/%{name}/*.cmake

%changelog
