Summary:	Create an APNG from multiple PNG files
Name:		apngasm
Version:	2.6
Release:	2
License:	zlib
Group:		Graphics
URL:		http://sourceforge.net/projects/apngasm
Source0:	http://downloads.sourceforge.net/project/apngasm/%{version}/%{name}-%{version}-src.zip
Buildrequires:	zlib-devel
BuildRequires:	libpng-devel
BuildRequires:	pkgconfig

%description
create an APNG from multiple PNG files

%prep

%setup -q -c apnopt

%build
%make

%install
mkdir -p %{buildroot}%{_bindir}/%{name}
mkdir -p %{buildroot}%{_docdir}/%{name}

install -m 0755 %{name} %{buildroot}%{_bindir}/%{name}
install -m 0644 readme.txt %{buildroot}%{_docdir}/%{name}/readme.txt


%files 
%doc readme.txt 
%{_bindir}/%{name}


%changelog
* Fri Feb 24 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.6-1
+ Revision: 780114
- version update 2.6

* Thu Jan 12 2012 Alexander Khrukin <akhrukin@mandriva.org> 2.5-1
+ Revision: 760335
- imported package apngasm

