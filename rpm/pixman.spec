Name:       pixman

Summary:    Pixel manipulation library
Version:    0.44.2
Release:    1
License:    MIT
URL:        https://github.com/sailfishos/pixman
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires: meson

%description
pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.

%package devel
Summary:    Development components for the pixman library
Requires:   %{name} = %{version}-%{release}

%description devel
pixman Development Library

%prep
%autosetup -n %{name}-%{version}/upstream

%build
%meson --auto-features=auto
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc
