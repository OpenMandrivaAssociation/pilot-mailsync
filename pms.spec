%define name pilot-mailsync
%define version 0.9.2
%define release %mkrel 1


Summary: Email synchronization program to/from the Palm OS
Name: %{name}
Version: %{version}
Release: %{release}
License: MPL
Source: %{name}-%{version}.tar.bz2
URL: http://wissrech.iam.uni-bonn.de/people/garcke/pms/
Group: Communications
Requires: sendmail gnome-pilot
BuildRequires: pilot-link-devel openssl-devel gnome-pilot-devel pam-devel
BuildRequires:	bison

%description
Pilot-Mailsync is an application to transfer outgoing mail from and deliver
incoming mail to a Palm OS device. pilot-mailsync relies on the libraries
installed by pilot-link.

%prep

%setup

%build

./configure --enable-gpilot

make

%install

# Create installation root folders
rm -rf $RPM_BUILD_ROOT
RPM_DOC_ROOT=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm -rf $RPM_DOC_ROOT
mkdir -p $RPM_DOC_ROOT

mkdir -p $RPM_BUILD_ROOT%_libdir/gnome-pilot/conduits/
mkdir -p $RPM_BUILD_ROOT%_datadir/gnome-pilot/conduits/

make prefix=$RPM_BUILD_ROOT%{_prefix} \
	GNOMEPILOTCONDUITDIR=$RPM_BUILD_ROOT%_libdir/gnome-pilot/conduits/ gplugin_install

install -m 644 mailsync.conduit $RPM_BUILD_ROOT%_datadir/gnome-pilot/conduits/

%files
%defattr(-,root,root)
%{_datadir}/gnome-pilot/conduits/mailsync.conduit
%{_libdir}/gnome-pilot/conduits/libgnome_mailsync_conduit.so
%defattr(644,root,root,755)
%doc README INSTALL docs/*

%clean
rm -rf $RPM_BUILD_ROOT

