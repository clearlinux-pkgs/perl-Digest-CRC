#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Digest-CRC
Version  : 0.22.2
Release  : 10
URL      : http://search.cpan.org/CPAN/authors/id/O/OL/OLIMAUL/Digest-CRC-0.22.2.tar.gz
Source0  : http://search.cpan.org/CPAN/authors/id/O/OL/OLIMAUL/Digest-CRC-0.22.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Public-Domain
Requires: perl-Digest-CRC-lib
Requires: perl-Digest-CRC-doc

%description
Digest::CRC version 0.22
========================
NAME
Digest::CRC - Generic CRC functions

%package doc
Summary: doc components for the perl-Digest-CRC package.
Group: Documentation

%description doc
doc components for the perl-Digest-CRC package.


%package lib
Summary: lib components for the perl-Digest-CRC package.
Group: Libraries

%description lib
lib components for the perl-Digest-CRC package.


%prep
%setup -q -n Digest-CRC-0.22

%build
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make V=1  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot}
else
./Build install --installdirs=site --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/Digest/CRC.pm

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib/perl5/site_perl/5.24.0/x86_64-linux/auto/Digest/CRC/CRC.so
