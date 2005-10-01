%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RPC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - implementation of the XML-RPC protocol
Summary(pl):	%{_pearname} - implementacja protokołu XML-RPC
Name:		php-pear-%{_pearname}
Version:	1.4.3
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	83138a445e424102db17b3b9588dbfef
URL:		http://pear.php.net/package/XML_RPC/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEAR-ified version of Useful inc's XML-RPC for PHP. It has
support for HTTP transport, proxies and authentication.

In PEAR status of this package is: %{_status}.

%description -l pl
Jest to zPEARowana wersja użytecznego include-a dla PHP. Posiada
wsparcie dla transportu HTTP, proxy oraz autentyfikacji.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl):	Testy dla PEAR::%{_pearname}
Group:		Development
Requires:	%{name} = %{epoch}:%{version}-%{release}
AutoReq:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl
Testy dla PEAR::%{_pearname}.

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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/*
