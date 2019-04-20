#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-CRC
Version  : 0.22.2
Release  : 27
URL      : https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-0.22.2.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-0.22.2.tar.gz
Summary  : Generic interface to CRC algorithms
Group    : Development/Tools
License  : Public-Domain
Requires: perl-Digest-CRC-lib = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Digest::CRC version 0.22
========================
NAME
Digest::CRC - Generic CRC functions

%package dev
Summary: dev components for the perl-Digest-CRC package.
Group: Development
Requires: perl-Digest-CRC-lib = %{version}-%{release}
Provides: perl-Digest-CRC-devel = %{version}-%{release}
Requires: perl-Digest-CRC = %{version}-%{release}

%description dev
dev components for the perl-Digest-CRC package.


%package lib
Summary: lib components for the perl-Digest-CRC package.
Group: Libraries

%description lib
lib components for the perl-Digest-CRC package.


%prep
%setup -q -n Digest-CRC-0.22

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/Digest/CRC.pm

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Digest::CRC.3

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.2/x86_64-linux-thread-multi/auto/Digest/CRC/CRC.so
