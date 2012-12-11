
%define plugin	filebrowser
%define name	vdr-plugin-%plugin
%define version	0.2.0
%define rel	5

Summary:	VDR plugin: Browse through files and execute actions on them
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPLv3+
URL:		http://vdr.nasenbaeren.net/filebrowser/
Source:		http://vdr.nasenbaeren.net/filebrowser/vdr-%plugin-%version.tgz
Patch0:		filebrowser-format-string.patch
Patch1:		filebrowser-type-fixes.patch
# workaround for http://sourceware.org/bugzilla/show_bug.cgi?id=9759
# for pre-2.10 glibc
Patch2:		filebrowser-dirent.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0-7
Requires:	vdr-abi = %vdr_abi

%description
This plugin is a filebrowser with user-defined commands to execute
on files.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%if %{mdkversion} < 201000
# patch2
VDR_PLUGIN_EXTRA_FLAGS="-DGLIBC_SCANDIR_BUG"
%endif
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY examples




%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-5mdv2010.0
+ Revision: 404583
- split dirent fix from type-fixes.patch to dirent.patch
- add a workaround for upstream glibc bug #9759 on 2009.1 and earlier

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-4mdv2010.0
+ Revision: 401088
- rebuild for new VDR
- fix type issues (type-fixes.patch, fixes build and a call that would
  abort at runtime)

* Sat Mar 21 2009 Anssi Hannula <anssi@mandriva.org> 0.2.0-3mdv2009.1
+ Revision: 359707
- fix format strings (format-string.patch)
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.2.0-2mdv2009.0
+ Revision: 197932
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.2.0-1mdv2009.0
+ Revision: 197670
- new version
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- apply new license policy

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.6b-6mdv2008.1
+ Revision: 145098
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6b-5mdv2008.1
+ Revision: 103106
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6b-4mdv2008.0
+ Revision: 50003
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6b-3mdv2008.0
+ Revision: 42089
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6b-2mdv2008.0
+ Revision: 22679
- rebuild for new vdr

* Fri Apr 20 2007 Anssi Hannula <anssi@mandriva.org> 0.0.6b-1mdv2008.0
+ Revision: 16313
- 0.0.6b


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-5mdv2007.0
+ Revision: 90926
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-4mdv2007.1
+ Revision: 74017
- rebuild for new vdr
- Import vdr-plugin-filebrowser

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-3mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-2mdv2007.0
- stricter abi requires

* Tue Aug 08 2006 Anssi Hannula <anssi@mandriva.org> 0.0.6-1mdv2007.0
- 0.0.6

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-2mdv2007.0
- rebuild for new vdr

* Thu Jul 13 2006 Anssi Hannula <anssi@mandriva.org> 0.0.5-1mdv2007.0
- initial Mandriva release

