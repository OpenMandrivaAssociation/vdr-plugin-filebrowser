
%define plugin	filebrowser
%define name	vdr-plugin-%plugin
%define version	0.0.6b
%define rel	5

Summary:	VDR plugin: Browse through files and execute actions on them
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://www.stud.uni-karlsruhe.de/~uqg8/vdr/filebrowser/
Source:		http://www.stud.uni-karlsruhe.de/~uqg8/vdr/filebrowser/vdr-%plugin-%version.tar.bz2
BuildRequires:	vdr-devel >= 1.4.1-6
Requires:	vdr-abi = %vdr_abi

%description
This plugin is a filebrowser with user-defined commands to execute
on files.

%prep
%setup -q -n %plugin-%version

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


