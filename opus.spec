Name:          opus
Version:       1.0.2
Release:       4%{?dist}
Summary:       An audio codec for use in low-delay speech and audio communication

Group:         System Environment/Libraries
License:       BSD
URL:           http://www.opus-codec.org/
Source0:       http://downloads.xiph.org/releases/%{name}/%{name}-%{version}.tar.gz
# This is the final IETF Working Group RFC
Source1:       http://tools.ietf.org/rfc/rfc6716.txt 

Patch0: 0001-Fix-several-memory-errors-in-the-SILK-resampler.patch
Patch1: 0001-Fixes-an-assertion-failure-in-SILK.patch

%description
The Opus codec is designed for interactive speech and audio transmission over 
the Internet. It is designed by the IETF Codec Working Group and incorporates 
technology from Skype's SILK codec and Xiph.Org's CELT codec.

%package devel
Summary: Development package for opus
Group: Development/Libraries
Requires: libogg-devel
Requires: opus = %{version}-%{release}

%description devel
Files for development with opus.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
cp %{SOURCE1} .

%build
%configure --enable-custom-modes

make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

# Remove libtool archives and static libs
find %{buildroot} -name '*.la' -exec rm -f {} ';'
find %{buildroot} -name '*.a' -exec rm -f {} ';'

%check
make check

%clean
rm -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYING README rfc6716.txt
%{_libdir}/libopus.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/opus
%{_libdir}/libopus.so
%{_libdir}/pkgconfig/opus.pc
%{_datadir}/aclocal/opus.m4

%changelog
* Tue Nov  5 2013 Matthias Clasen <mclasen@redhat.com> - 1.0.2-4
- Apply two crash fixes from upstream
- Resolves: #1017240

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.2-2
- Enable extra custom modes API

* Thu Dec  6 2012 Peter Robinson <pbrobinson@fedoraproject.org> 1.0.2-1
- Official 1.0.2 release

* Wed Sep 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.1-1
- Official 1.0.1 release now rfc6716 is stable

* Tue Sep  4 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.1rc3-0.1
- Update to 1.0.1rc3

* Thu Aug  9 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 1.0.0rc1-0.1
- Update to 1.0.0rc1

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.14-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun May 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.14-1
- Update to 0.9.14

* Sat May 12 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.10-2
- Add make check - fixes RHBZ # 821128

* Fri Apr 27 2012 Peter Robinson <pbrobinson@fedoraproject.org> - 0.9.10-1
- Update to 0.9.10

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.9.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Nov  8 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.8-1
- Update to 0.9.8

* Mon Oct 10 2011 Peter Robinson <pbrobinson@fedoraproject.org> 0.9.6-1
- Initial packaging
