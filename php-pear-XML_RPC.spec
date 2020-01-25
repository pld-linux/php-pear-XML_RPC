%define		_status		stable
%define		_pearname	XML_RPC
Summary:	%{_pearname} - implementation of the XML-RPC protocol
Summary(pl.UTF-8):	%{_pearname} - implementacja protokołu XML-RPC
Name:		php-pear-%{_pearname}
Version:	1.5.5
Release:	2
Epoch:		0
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	02f9b1a27636527ddf6661e545799d45
URL:		http://pear.php.net/package/XML_RPC/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(xml)
Requires:	php-pear
Obsoletes:	php-pear-XML_RPC-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEAR-ified version of Useful inc's XML-RPC for PHP. It has
support for HTTP transport, proxies and authentication.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Jest to zPEARowana wersja użytecznego include-a dla PHP. Posiada
wsparcie dla transportu HTTP, proxy oraz autentyfikacji.

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
%{php_pear_dir}/XML/*.php
%{php_pear_dir}/XML/RPC
