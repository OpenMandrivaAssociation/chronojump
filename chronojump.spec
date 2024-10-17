%define url_ver %(echo %{version}|cut -d. -f1,2)
%define	gstapi	1.0

Summary:	A measurement, management and statistics sport testing tool
Name:		chronojump
Version:	2.1.2
Release:	1
Group:		Sciences/Mathematics
License:	GPLv2+
Url:		https://chronojump.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/chronojump/%{url_ver}/%{name}-%{version}.tar.xz

BuildRequires:	pkgconfig(glade-sharp-2.0)
BuildRequires:	pkgconfig(glib-sharp-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(gtk-sharp-2.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-app-%{gstapi})
#BuildRequires:	pkgconfig(mono)

%description
ChronoJump is an open hardware, free software, multiplatform complete system
for measurement, management and statistics of sport short-time tests.

Chronojump uses a contact platform and/or photocells, 
and also a chronometer printed circuit designed ad hoc in
order to obtain precise and trustworthy measurements.

Chronojump is used by trainers, teachers and students.

%prep
%setup -q
#TMP=`mktemp`
#sed -e "s/share\/doc\/chronojump/share\/doc\/chronojump-%{version}/g" src/util.cs > $TMP
#mv $TMP src/util.cs

%build
%configure \
	--disable-static

%make_build

#cat > src/chronojump <<EOF
#!/bin/sh

#exec mono "%{_libdir}/chronojump/Chronojump.exe" "\$@"
#EOF

%install
%make_install

# this file should be in the standard dir
#rm %{buildroot}/%{_datadir}/doc/chronojump/chronojump_manual_es.pdf
#rm %{buildroot}/%{_datadir}/doc/chronojump/chronojump_manual_en.pdf

%find_lang %{name}

%files -f %{name}.lang
%doc README COPYING AUTHORS ChangeLog
%doc manual/chronojump_manual_es.pdf
%doc manual/chronojump_manual_en.pdf
%{_bindir}/chronojump
%{_bindir}/chronojump_mini
%{_bindir}/chronojump-test-accuracy
%{_bindir}/chronojump-test-jumps
%{_bindir}/chronojump-test-stream
%{_bindir}/chronopic-firmwarecord
%dir %{_libdir}/chronojump
%{_libdir}/chronojump/*
%dir %{_datadir}/chronojump
%{_datadir}/chronojump/*
%{_datadir}/applications/chronojump.desktop
%{_iconsdir}/hicolor/48x48/apps/chronojump.png

