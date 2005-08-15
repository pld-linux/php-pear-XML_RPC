%include	/usr/lib/rpm/macros.php
%define		_class		XML
%define		_subclass	RPC
%define		_status		stable
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - implementation of the XML-RPC protocol
Summary(pl):	%{_pearname} - implementacja protoko³u XML-RPC
Name:		php-pear-%{_pearname}
Version:	1.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	01202c4bcc2c03e7bb1bff5570d98367
URL:		http://pear.php.net/package/XML_RPC/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEAR-ified version of Useful inc's XML-RPC for PHP. It has
support for HTTP transport, proxies and authentication.

In PEAR status of this package is: %{_status}.

%description -l pl
Jest to zPEARowana wersja u¿ytecznego include-a dla PHP. Posiada
wsparcie dla transportu HTTP, proxy oraz autentyfikacji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/RPC.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/Server.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
