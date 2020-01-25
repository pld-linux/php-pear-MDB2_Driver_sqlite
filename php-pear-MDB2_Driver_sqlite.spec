%define		_status		beta
%define		_pearname	MDB2_Driver_sqlite
%define		subver	b4
%define		rel		1
Summary:	%{_pearname} - sqlite MDB2 driver
Summary(pl.UTF-8):	%{_pearname} - sterownik sqlite dla MDB2
Name:		php-pear-%{_pearname}
Version:	1.5.0
Release:	0.%{subver}.%{rel}
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}%{subver}.tgz
# Source0-md5:	266234565071b41646d0dfe0290004a9
URL:		http://pear.php.net/package/MDB2_Driver_sqlite/
BuildRequires:	php-pear-PEAR >= 1:1.9.1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php(sqlite)
Requires:	php-pear
Requires:	php-pear-MDB2 >= 1:2.5.0-0.b4
Obsoletes:	php-pear-MDB2_Driver_sqlite-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the SQLite MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Sterownik SQLite dla MDB2.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

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
%{php_pear_dir}/MDB2/Driver/Datatype/sqlite.php
%{php_pear_dir}/MDB2/Driver/Manager/sqlite.php
%{php_pear_dir}/MDB2/Driver/Native/sqlite.php
%{php_pear_dir}/MDB2/Driver/Reverse/sqlite.php
%{php_pear_dir}/MDB2/Driver/Function/sqlite.php
%{php_pear_dir}/MDB2/Driver/sqlite.php
%{php_pear_dir}/data/MDB2_Driver_sqlite
