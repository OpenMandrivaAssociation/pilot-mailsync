%define name pilot-mailsync
%define version 0.9.2
%define release %mkrel 2


Summary:	Email synchronization program to/from the Palm OS
Name:		pilot-mailsync
Version:	0.9.2
Release:	%{mkrel 2}
License:	MPLv1.0
Source0:	http://www.garcke.de/PMS/%{name}-%{version}.tar.bz2
Patch0:		pilot-mailsync-0.9.2-configh.patch
URL:		http://www.garcke.de/PMS/
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	sendmail-command
Requires:	gnome-pilot
BuildRequires:	pilot-link-devel
BuildRequires:	openssl-devel
BuildRequires:	gnome-pilot-devel
BuildRequires:	pam-devel
BuildRequires:	bison

%description
Pilot-Mailsync is an application to transfer outgoing mail from and deliver
incoming mail to a Palm OS device. pilot-mailsync relies on the libraries
installed by pilot-link.

%prep
%setup -q
%patch0 -p1 -b .configh

%build
sed -i -e 's,-DHAVE_CONFIG_H,,g' configure
%configure2_5x --enable-gpilot
make

%install
rm -rf %{buildroot}

# Create installation root folders
mkdir -p %{buildroot}%{_libdir}/gnome-pilot/conduits/
mkdir -p %{buildroot}%{_datadir}/gnome-pilot/conduits/

make prefix=%{buildroot}%{_prefix} \
	GNOMEPILOTCONDUITDIR=%{buildroot}%{_libdir}/gnome-pilot/conduits/ gplugin_install

install -m 644 mailsync.conduit %{buildroot}%{_datadir}/gnome-pilot/conduits/

%files
%defattr(-,root,root)
%{_datadir}/gnome-pilot/conduits/mailsync.conduit
%{_libdir}/gnome-pilot/conduits/libgnome_mailsync_conduit.so
%defattr(644,root,root,755)
%doc README INSTALL docs/*

%clean
rm -rf %{buildroot}

