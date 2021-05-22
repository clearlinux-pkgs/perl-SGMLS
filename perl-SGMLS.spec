#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-SGMLS
Version  : 1.1
Release  : 9
URL      : https://cpan.metacpan.org/authors/id/R/RA/RAAB/SGMLSpm-1.1.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/R/RA/RAAB/SGMLSpm-1.1.tar.gz
Summary  : "a perl5 class library for parsing the output from James Clark's SGMLS and NSGMLS parsers."
Group    : Development/Tools
License  : GPL-2.0
Requires: perl-SGMLS-bin = %{version}-%{release}
Requires: perl-SGMLS-license = %{version}-%{release}
Requires: perl-SGMLS-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
SGMLS.PM: A PERL5 CLASS LIBRARY FOR USE WITH THE
SGMLS AND NSGMLS PARSERS
Version 1.03ii

%package bin
Summary: bin components for the perl-SGMLS package.
Group: Binaries
Requires: perl-SGMLS-license = %{version}-%{release}

%description bin
bin components for the perl-SGMLS package.


%package dev
Summary: dev components for the perl-SGMLS package.
Group: Development
Requires: perl-SGMLS-bin = %{version}-%{release}
Provides: perl-SGMLS-devel = %{version}-%{release}
Requires: perl-SGMLS = %{version}-%{release}

%description dev
dev components for the perl-SGMLS package.


%package license
Summary: license components for the perl-SGMLS package.
Group: Default

%description license
license components for the perl-SGMLS package.


%package perl
Summary: perl components for the perl-SGMLS package.
Group: Default
Requires: perl-SGMLS = %{version}-%{release}

%description perl
perl components for the perl-SGMLS package.


%prep
%setup -q -n SGMLSpm-1.1
cd %{_builddir}/SGMLSpm-1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-SGMLS
cp %{_builddir}/SGMLSpm-1.1/COPYING %{buildroot}/usr/share/package-licenses/perl-SGMLS/17e3b0eea99abffe6ac71e65627413236e0b117a
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sgmlspl.pl

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/SGMLS.3
/usr/share/man/man3/SGMLS::Output.3
/usr/share/man/man3/SGMLS::Refs.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-SGMLS/17e3b0eea99abffe6ac71e65627413236e0b117a

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/SGMLS.pm
/usr/lib/perl5/vendor_perl/5.34.0/SGMLS/Output.pm
/usr/lib/perl5/vendor_perl/5.34.0/SGMLS/Refs.pm
/usr/lib/perl5/vendor_perl/5.34.0/sgmlspl-specs/skel.pl
