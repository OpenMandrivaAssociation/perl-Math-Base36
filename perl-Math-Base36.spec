%define upstream_name    Math-Base36
%define upstream_version 0.09

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Encoding and decoding of base36 strings
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Math::BigInt)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This module converts to and from Base36 numbers (0..9 - A..Z)

It was created because of an article/challenge in "The Perl Review"

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2mdv2011.0
+ Revision: 657788
- rebuild for updated spec-helper

* Wed Dec 08 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1mdv2011.0
+ Revision: 616215
- update to new version 0.09

* Fri Jul 16 2010 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2011.0
+ Revision: 554286
- import perl-Math-Base36


* Fri Jul 16 2010 cpan2dist 0.07-1mdv
- initial mdv release, generated with cpan2dist
