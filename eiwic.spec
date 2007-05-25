# TODO
# - initscript
Summary:	IRC-bot written in pure C
Name:		eiwic
Version:	1.0.14
Release:	0.1
License:	GPL
Group:		Applications/Communications
Source0:	http://lordi.styleliga.org/eiwic/%{name}-%{version}.tar.gz
# Source0-md5:	61e8ca179a35608ba9674fabf3bb8563
URL:		http://lordi.styleliga.org/eiwic/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eiwic is an IRC bot which can be easily extended by modules that can
be loaded at runtime. It has a module API which is designed to make
the creation of your own modules as easy as possible, including
"output routing", a TCP/IP socket interface, and timer functions.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/eiwic
%dir %{_libdir}/eiwic
%attr(755,root,root) %{_libdir}/eiwic/bc.so
%attr(755,root,root) %{_libdir}/eiwic/conv.so
%attr(755,root,root) %{_libdir}/eiwic/ctcp.so
%attr(755,root,root) %{_libdir}/eiwic/cyborg.so
%attr(755,root,root) %{_libdir}/eiwic/dict.so
%attr(755,root,root) %{_libdir}/eiwic/getop.so
%attr(755,root,root) %{_libdir}/eiwic/google.so
%attr(755,root,root) %{_libdir}/eiwic/heise.so
%attr(755,root,root) %{_libdir}/eiwic/info.so
%attr(755,root,root) %{_libdir}/eiwic/lol.so
%attr(755,root,root) %{_libdir}/eiwic/modadmin.so
%attr(755,root,root) %{_libdir}/eiwic/remind.so
%attr(755,root,root) %{_libdir}/eiwic/rot13.so
%attr(755,root,root) %{_libdir}/eiwic/rssfeed.so
%attr(755,root,root) %{_libdir}/eiwic/spiegel.so
%attr(755,root,root) %{_libdir}/eiwic/stats.so
%attr(755,root,root) %{_libdir}/eiwic/stream.so
%attr(755,root,root) %{_libdir}/eiwic/template.so
%attr(755,root,root) %{_libdir}/eiwic/translate.so
%attr(755,root,root) %{_libdir}/eiwic/wikipedia.so
