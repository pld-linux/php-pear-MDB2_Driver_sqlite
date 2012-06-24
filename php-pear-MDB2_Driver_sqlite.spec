%include	/usr/lib/rpm/macros.php
%define		_class		MDB2
%define		_subclass	Driver_sqlite
%define		_status		beta
%define		_pearname	MDB2_Driver_sqlite

Summary:	%{_pearname} - sqlite MDB2 driver
Summary(pl):	%{_pearname} - sterownik sqlite dla MDB2
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	566e3b4dcfc4d2cec5787a30b069c98d
URL:		http://pear.php.net/package/MDB2_Driver_sqlite/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-common >= 3:4.2.0
Requires:	php-pear-PEAR >= 1:1.0b1
Requires:	php-pear-MDB2 >= 2.0.0beta5
Requires:	php-sqlite
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the SQLite MDB2 driver.

In PEAR status of this package is: %{_status}.

%description -l pl
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
%{php_pear_dir}/MDB2/Driver/sqlite.php
