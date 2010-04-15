Summary:	Email synchronization program to/from the Palm OS
Name:		pilot-mailsync
Version:	0.9.2
Release:	%{mkrel 4}
License:	MPLv1.0
Source0:	http://www.garcke.de/PMS/%{name}-%{version}.tar.bz2
# Work around a build problem caused by some includes issues
# - AdamW 2008/09
Patch0:		pilot-mailsync-0.9.2-configh.patch
# Look for libs in /usr/lib64 as well as /usr/lib - AdamW 2008/09
Patch1:		pilot-mailsync-0.9.2-lib64.patch
Patch2:		pilot-mailsync-0.9.2-gnome2.patch
Patch3:		pilot-mailsync-0.9.2-link.patch
URL:		http://www.garcke.de/PMS/
Group:		Communications
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	sendmail-command
Requires:	gnome-pilot
BuildRequires:	gnome-pilot-devel
BuildRequires:	pam-devel
BuildRequires:	bison
BuildRequires:	libtool

%description
Pilot-Mailsync is an application to transfer outgoing mail from and deliver
incoming mail to a Palm OS device. pilot-mailsync relies on the libraries
installed by pilot-link.

%prep
%setup -q
%patch0 -p1 -b .configh
%patch1 -p1 -b .lib64
%patch2 -p0 -b .gnome2
%patch3 -p0 -b .link

%build
autoconf
sed -i -e 's,-DHAVE_CONFIG_H,,g' configure
export CFLAGS="$CFLAGS -fPIC"
export CPPFLAGS="$CPPFLAGS -fPIC"
%configure2_5x --enable-gpilot=yes \
	--enable-jpilot=no
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

