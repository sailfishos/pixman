# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
# 
# >> macros
# << macros

Name:       pixman
Summary:    Pixel manipulation library
Version:    0.22.0
Release:    1
Group:      System/Libraries
License:    MIT
URL:        http://www.x.org/
Source0:    http://xorg.freedesktop.org/archive/individual/lib/%{name}-%{version}.tar.bz2
Source100:  pixman.yaml
Patch0:     0.22.0-fixes.patch
%ifarch %{arm}
Patch1:     pixman-0.22.0-arm-revert-Do-CPU-features-detection-from-constructor-function.patch
%endif
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig


%description
pixman is a library that provides low-level pixel manipulation
features such as image compositing and trapezoid rasterization.



%package devel
Summary:    Development components for the pixman library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
pixman Development Library 



%prep
%setup -q -n %{name}-%{version}

# 0.22.0-fixes.patch
%patch0 -p1
%ifarch %{arm}
# pixman-0.22.0-arm-revert-Do-CPU-features-detection-from-constructor-function.patch
%patch1 -p1
%endif
# >> setup
# << setup

%build
# >> build pre
autoreconf --force --install
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
# << install post



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig





%files
%defattr(-,root,root,-)
# >> files
%{_libdir}/libpixman-1*.so.*
# << files


%files devel
%defattr(-,root,root,-)
# >> files devel
%dir %{_includedir}/pixman-1
%{_includedir}/pixman-1/pixman.h
%{_includedir}/pixman-1/pixman-version.h
%{_libdir}/libpixman-1*.so
%{_libdir}/pkgconfig/pixman-1.pc
# << files devel
