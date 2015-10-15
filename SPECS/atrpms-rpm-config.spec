Summary: Additional rpm configuration files
Name: atrpms-rpm-config
Version: 204
Release: 1%{?dist}
License: GPL
Group: Development/System
Source1: rpmrc
Source20: macros.atrpms
Source21: macros.xperl
Source22: macros.kmdl
Source23: macros.libs
Source24: macros.bcond
Source3: find-devel.sh
Source4: find-lib.sh
Source5: python_burninversion.sh
Source6: find-debuginfo.sh
Source7: find-unamer.sh
Patch0: redhat-rpm-config-8.0.45-strip-kmdls.patch
Patch1: redhat-rpm-config-8.0.31-nodocdependencies.patch
BuildArch: noarch
BuildRequires: redhat-rpm-config
#BuildRequires: /usr/lib/rpm/find-debuginfo.sh
#Requires: rpmbuild(VendorConfig) <= 4.1
#Requires: mktemp
#Requires: redhat-release = %{distversion}
BuildRoot: %{_tmppath}/%{name}-root

%description
These rpm configuration files contain support for various rpm build
features used by atrpms. These include easying the task of packaging
certain software categories like tex, perl, sgml etc.

%prep
%setup -q -T -c %{name}-%{version}
install -m 0755 -p %{SOURCE6} .
cp -a /usr/lib/rpm/redhat/* .
%patch0 -p1 -b .kmdls
%patch1 -p1 -b .nodocautodeps
cd ..

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/lib/rpm/atrpms
#mkdir -p %{buildroot}/usr/sbin
mkdir -p %{buildroot}%{_sysconfdir}/rpm

install -m 0755 -p %{SOURCE1} %{SOURCE3} %{SOURCE4} %{SOURCE5} %{SOURCE7} %{buildroot}/usr/lib/rpm/atrpms/
install -m 0644 -p %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} %{buildroot}%{_sysconfdir}/rpm/
cat %{SOURCE20} %{SOURCE21} %{SOURCE22} %{SOURCE23} %{SOURCE24} > %{buildroot}/usr/lib/rpm/atrpms/macros
for file in \
  find-requires find-provides find-debuginfo.sh \
  brp-compress brp-strip brp-strip-static-archive brp-strip-comment-note; do
  install -p $file %{buildroot}/usr/lib/rpm/atrpms/
done

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/lib/rpm/atrpms
%{_sysconfdir}/rpm/*

%changelog
* Mon Mar 17 2014 Axel Thimm <Axel.Thimm@ATrpms.net> - 204-1
- Add pkgdocdir.

* Tue Oct  6 2009 Axel Thimm <Axel.Thimm@ATrpms.net>
- Rename macros.perl to macros.xperl to avoid conflict with perl-devel.

* Sun Aug 22 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Honor PERL5LIB if set in specfile.

* Fri Aug 20 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Add find-requires which does not scan docdir.

* Sat Jul 31 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Add fc2.90 support.

* Thu May 13 2004 Axel Thimm <Axel.Thimm@ATrpms.net>
- Add fc2 support.

* Mon Sep 29 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Unify different macrofiles into one conditional.

* Sun Jun 15 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Add /sbin/mkkerneldoth.atrpms.

* Sun Apr  6 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Updated for Red Hat 9.

* Sun Mar 30 2003 Axel Thimm <Axel.Thimm@ATrpms.net>
- Initial package.
