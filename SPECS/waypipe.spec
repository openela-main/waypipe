Name:		waypipe
Version:	0.8.2
Release:	1%{?dist}
Summary:	Wayland forwarding proxy

License:	MIT
URL:		https://gitlab.freedesktop.org/mstoeckl/%{name}
Source0:	https://gitlab.freedesktop.org/mstoeckl/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz
Source1:	waypipe.1

BuildRequires:	gcc
BuildRequires:	meson
%if !0%{?rhel}
BuildRequires:	scdoc
%endif
BuildRequires:	pkgconfig(gbm)
BuildRequires:	pkgconfig(libdrm)
BuildRequires:	pkgconfig(liblz4)
BuildRequires:	pkgconfig(libzstd)
BuildRequires:	pkgconfig(libva)
BuildRequires:	pkgconfig(wayland-protocols)
BuildRequires:	pkgconfig(wayland-client)
BuildRequires:	pkgconfig(wayland-server)

%description
Waypipe is a proxy for Wayland clients. It forwards Wayland messages and
serializes changes to shared memory buffers over a single socket. This makes
application forwarding similar to "ssh -X" feasible.


%prep
%setup -q -n %{name}-v%{version}


%build
%meson -Dwith_video=disabled -Dwerror=false %{?rhel:-Dman-pages=disabled}
%meson_build


%install
%meson_install
%if 0%{?rhel}
mkdir -p %{buildroot}%{_mandir}/man1/
install -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/
%endif


%check
%meson_test


%files
%{_bindir}/waypipe
%{_mandir}/man1/waypipe.1*
%doc CONTRIBUTING.md README.md
%license COPYING


%changelog
* Tue May 17 2022 Olivier Fourdan <ofourdan@redhat.com> - 0.8.2-1
- Update to 0.8.2 (#2071907)

* Tue Aug 10 2021 Mohan Boddu <mboddu@redhat.com> - 0.8.0-2
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Tue Jun 22 2021 Olivier Fourdan <ofourdan@redhat.com> - 0.8.0-1
- Update to 0.8.0
- Provide a pre-built man page on RHEL to avoid pulling scdoc

* Wed Jan 27 2021 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Fri Nov 06 2020 Dominique Martinet <asmadeus@codewreck.org> - 0.7.1-1
- Update to 0.7.1

* Tue Nov 03 2020 Dominique Martinet <asmadeus@codewreck.org> - 0.7.0-1
- Update to version 0.7.0

* Mon Sep 28 2020 Jeff Law <law@redhat.com> - 0.6.1-7
- Re-enable LTO as upstream GCC target/96939 has been fixed

* Mon Aug 10 2020 Jeff Law <law@redhat.com> - 0.6.1-6
- Disable LTO for now.

* Sat Aug 01 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-5
- Second attempt - Rebuilt for
  https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon May 11 2020 Dominique Martinet <asmadeus@codewreck.org> - 0.6.1-3
- Fix FTBS (test failure)

* Fri Jan 31 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 28 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.6.1-1
- Update to version 0.6.1

* Thu Aug 22 2019 Lubomir Rintel <lkundrak@v3.sk> - 0.6.0-1
- Initial packaging
