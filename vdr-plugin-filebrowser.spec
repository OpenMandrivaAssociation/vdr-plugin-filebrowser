
%define plugin	filebrowser
%define name	vdr-plugin-%plugin
%define version	0.2.0
%define rel	3

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
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This plugin is a filebrowser with user-defined commands to execute
on files.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
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


