
%define plugin	filebrowser

Summary:	VDR plugin: Browse through files and execute actions on them
Name:		vdr-plugin-%plugin
Version:	0.2.0
Release:	7
Group:		Video
License:	GPLv3+
URL:		http://vdr.nasenbaeren.net/filebrowser/
Source:		http://vdr.nasenbaeren.net/filebrowser/vdr-%plugin-%{version}.tgz
Patch0:		filebrowser-format-string.patch
Patch1:		filebrowser-type-fixes.patch
# workaround for http://sourceware.org/bugzilla/show_bug.cgi?id=9759
# for pre-2.10 glibc
Patch2:		filebrowser-dirent.patch
BuildRequires:	vdr-devel >= 1.6.0-7
Requires:	vdr-abi = %vdr_abi

%description
This plugin is a filebrowser with user-defined commands to execute
on files.

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY examples




