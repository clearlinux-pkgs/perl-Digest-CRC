#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-CRC
Version  : 0.24
Release  : 44
URL      : https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-0.24.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/O/OL/OLIMAUL/Digest-CRC-0.24.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: perl-Digest-CRC-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Digest::CRC version 0.24
========================
NAME
Digest::CRC - Generic CRC functions

%package dev
Summary: dev components for the perl-Digest-CRC package.
Group: Development
Provides: perl-Digest-CRC-devel = %{version}-%{release}
Requires: perl-Digest-CRC = %{version}-%{release}

%description dev
dev components for the perl-Digest-CRC package.


%package perl
Summary: perl components for the perl-Digest-CRC package.
Group: Default
Requires: perl-Digest-CRC = %{version}-%{release}

%description perl
perl components for the perl-Digest-CRC package.


%prep
%setup -q -n Digest-CRC-0.24
cd %{_builddir}/Digest-CRC-0.24

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

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Digest::CRC.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
