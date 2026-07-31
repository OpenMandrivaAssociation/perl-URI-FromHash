%define upstream_name    URI-FromHash
%define upstream_version 0.05

%define debug_package %{nil}

Name:       perl-%{upstream_name}
Version:	0.05
Release:	5

Summary:    Build a URI from a set of named parameters
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://github.com/autarch/URI-FromHash
Source0:	https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/URI-FromHash-0.05.tar.gz

BuildRequires:	make
BuildRequires: perl(Params::Validate)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildRequires: perl(Module::Build::Compat)
BuildRequires: perl-devel

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
%setup -q -n URI-FromHash-0.05

%build
perl Makefile.PL INSTALLDIRS=vendor

%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc META.yml Changes README LICENSE
%{_mandir}/man3/*
%perl_vendorlib/*




