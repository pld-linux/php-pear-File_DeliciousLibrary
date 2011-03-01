%include	/usr/lib/rpm/macros.php
%define		_class		File
%define		_subclass	DeliciousLibrary
%define		_status		alpha
%define		_pearname	File_DeliciousLibrary
Summary:	%{_pearname} - Parser for the library database of the Delicious Library software
Summary(pl.UTF-8):	%{_pearname} - parser baz danych oprogramowania Delicious Library
Name:		php-pear-%{_pearname}
Version:	0.1.1
Release:	2
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	815562a17e2b698d57413d20f91db3bc
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/File_DeliciousLibrary/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-pear
Obsoletes:	php-pear-File_DeliciousLibrary-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a convenient interface to extract information
out of the XML based library database being used by Delicious Library.
This makes it possible to e.g. export the items from the library to a
website.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Pakiet ten dostarcza wygodnego w użyciu interfejsu do wydobywania
informacji z opartych na XML baz danych wykorzystywanych w projekcie
Delicious Library. Pozwala to na np. eksport informacji z biblioteki
na stronę internetową.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/File/DeliciousLibrary
%{php_pear_dir}/File/DeliciousLibrary.php
