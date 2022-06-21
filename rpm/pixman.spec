Name:       pixman

Summary:    Pixel manipulation library
Version:    0.40.0
Release:    1
License:    MIT
URL:        https://github.com/sailfishos/pixman
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

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
%autogen --disable-static \
%ifarch %{arm}
    --disable-arm-iwmmxt \
%endif
%ifarch mipsel
    --disable-loongson-mmi
%endif

%make_build

%install
rm -rf %{buildroot}
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license COPYING
%{_libdir}/libpixman-1*.so.*

%files devel
%defattr(-,root,root,-)
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc
