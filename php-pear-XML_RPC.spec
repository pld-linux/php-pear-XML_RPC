%include	/usr/lib/rpm/macros.php
%define         _class          XML
%define         _subclass       RPC
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - implementation of the XML-RPC protocol
Summary(pl):	%{_pearname} - implementacja protoko�u XML-RPC
Name:		php-pear-%{_pearname}
Version:	1.0.4
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
Patch0:		%{name}-cosmetic.patch
URL:		http://pear.php.net/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a PEAR-ified version of Useful inc's XML-RPC for PHP. It has
support for HTTP transport, proxies and authentication.

%description -l pl
Jest to zPEARowana wersja u�ytecznego include-a dla PHP. Posiada
wsparcie dla transportu HTTP, proxy oraz autentyfikacji.

%prep
%setup -q -c
cd %{_pearname}-%{version}
%patch0 -p1

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
%{php_pear_dir}/%{_class}/%{_subclass}/*.php