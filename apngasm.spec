%define libname %mklibname apngasm
%define devname %mklibname -d apngasm

Summary:	Create an APNG from multiple PNG files
Name:		apngasm
Version:	3.1.9
Release:	1
License:	zlib
Group:		Graphics
URL:		https://github.com/apngasm/apngasm
Source0:	https://github.com/apngasm/apngasm/archive/master/%{name}-%{version}.tar.gz
Buildrequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(libpng16)
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig

%description
create an APNG from multiple PNG files

%package -n %{libname}
Summary:	Library for assembling APNG files from PNG files

%description -n %{libname}
Library for assembling APNG files from PNG files

%package -n %{devname}
Summary:	Headers for the library for assembling APNG files from PNG files
Requires:	%{libname} = %{EVRD}

%description -n %{devname}
Headers for the library for assembling APNG files from PNG files

%prep
%autosetup -p1 -n %{name}-master
%cmake -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build
mkdir -p %{buildroot}%{_datadir}
mv %{buildroot}%{_prefix}/man %{buildroot}%{_datadir}/

%files 
%{_bindir}/%{name}
%{_mandir}/man1/apngasm.1*

%files -n %{libname}
%{_libdir}/libapngasm.so

%files -n %{devname}
%{_includedir}/*.h
%{_libdir}/pkgconfig/libapngasm.pc
