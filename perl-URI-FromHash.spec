%define upstream_name    URI-FromHash
%define upstream_version 0.03

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Build a URI from a set of named parameters
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/URI/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(Module::Build::Compat)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides a simple one-subroutine "named parameters" style
interface for creating URIs. Underneath the hood it uses 'URI.pm', though
because of the simplified interface it may not support all possible options
for all types of URIs.

It was created for the common case where you simply want to have a simple
interface for creating syntactically correct URIs from known components
(like a path and query string). Doing this using the native 'URI.pm'
interface is rather tedious, requiring a number of method calls, which is
particularly ugly when done inside a templating system such as Mason or
TT2.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc META.yml Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*

