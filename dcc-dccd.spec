Summary:	Distributed Checksum Clearinghouse, anti-spam tool
Summary(pl):	Narzêdzie anty-spamowe bazuj±ce na sumach kontrolnych (DCC)
Name:		dcc-dccd
Version:	1.2.50
Release:	1
License:	BSD-like
Group:		Networking
Source0:	http://www.dcc-servers.net/dcc/source/%{name}-%{version}.tar.Z
# Source0-md5:	676b17dca43a3dabe22c057a6cfdde77
URL:		http://www.dcc-servers.net/
BuildRequires:	fhs-compliance
BuildRequires:	using-special-registered-not-regular-user
BuildRequires:	rpmbuild(macros) >= 1.202
Requires(pre):	/usr/sbin/useradd
Requires(postun):	/usr/sbin/userdel
Requires(post,preun):	/sbin/chkconfig
Provides:	user(dcc)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dccdir	/var/lib/dcc
%define		cgidir	/srv/httpd/cgi-bin

%description
Distributed Checksum Clearinghouse or DCC is a cooperative,
distributed system intended to detect "bulk" mail or mail sent to many
people. It allows individuals receiving a single mail message to
determine that many other people have been sent essentially identical
copies of the message and so reject the message. It can identify some
unsolicited bulk mail using "spam traps" and other detectors, but that
is not its focus.

The DCC can be viewed as a tool for end users to enforce their right
to "opt-in" to streams of bulk mail by refusing all bulk mail except
from sources in a "white list." White lists are generally the
responsibility of DCC clients, since only they know which bulk mail
they solicited.

%description -l pl
DCC (Distributed Checksum Clearinghouse) jest kooperatywnym,
rozproszonym systemem maj±cym na celu wykrywanie masowej poczty lub
poczty wys³anej do wielu ludzi. Pozwala jednostkom otrzymuj±cym
pojedynczy list okre¶liæ, jak wielu innych otrzyma³o dok³adnie
identyczne kopie tej wiadomo¶ci i na tej podstawie odrzuciæ j±. Mo¿e
zidentyfikowaæ niechcian± masow± pocztê przy u¿yciu "pu³apek
antyspamowych" i innych wykrywaczy, ale to nie jest podstawowym celem.

DCC mo¿na odbieraæ jako narzêdzie dla u¿ytkowników koñcowych,
zapewniaj±ce im prawo do przeciwstawienia siê zalewowi masowej poczty
przez odrzucenie wszystkich ¶mieci oprócz ¼róde³ z "bia³ej listy".
Za bia³e listy odpowiadaj± klienci DCC, jako ¿e tylko oni wiedz±,
jak± masow± pocztê zamawiali.

%package client
Summary:	Tools to access a DCC server
Summary(pl):	Narzêdzia dostêpowe dla serwera DCC
Group:		Networking
Requires:	%{name} = %{version}-%{release}

%description client
Distributed Checksum Clearinghouse or DCC is a cooperative,
distributed system intended to detect "bulk" mail or mail sent to many
people. It allows individuals receiving a single mail message to
determine that many other people have been sent essentially identical
copies of the message and so reject the message. It can identify some
unsolicited bulk mail using "spam traps" and other detectors, but that
is not its focus.

The DCC can be viewed as a tool for end users to enforce their right
to "opt-in" to streams of bulk mail by refusing all bulk mail except
from sources in a "white list." White lists are generally the
responsibility of DCC clients, since only they know which bulk mail
they solicited.

%description client -l pl
DCC (Distributed Checksum Clearinghouse) jest kooperatywnym,
rozproszonym systemem maj±cym na celu wykrywanie masowej poczty lub
poczty wys³anej do wielu ludzi. Pozwala jednostkom otrzymuj±cym
pojedynczy list okre¶liæ, jak wielu innych otrzyma³o dok³adnie
identyczne kopie tej wiadomo¶ci i na tej podstawie odrzuciæ j±. Mo¿e
zidentyfikowaæ niechcian± masow± pocztê przy u¿yciu "pu³apek
antyspamowych" i innych wykrywaczy, ale to nie jest podstawowym celem.

DCC mo¿na odbieraæ jako narzêdzie dla u¿ytkowników koñcowych,
zapewniaj±ce im prawo do przeciwstawienia siê zalewowi masowej poczty
przez odrzucenie wszystkich ¶mieci oprócz ¼róde³ z "bia³ej listy".
Za bia³e listy odpowiadaj± klienci DCC, jako ¿e tylko oni wiedz±,
jak± masow± pocztê zamawiali.

%package server
Summary:	DCC Server
Summary(pl):	Serwer DCC
Group:		Networking
Requires:	%{name} = %{version}-%{release}

%description server
Distributed Checksum Clearinghouse or DCC is a cooperative,
distributed system intended to detect "bulk" mail or mail sent to many
people. It allows individuals receiving a single mail message to
determine that many other people have been sent essentially identical
copies of the message and so reject the message. It can identify some
unsolicited bulk mail using "spam traps" and other detectors, but that
is not its focus.

The DCC can be viewed as a tool for end users to enforce their right
to "opt-in" to streams of bulk mail by refusing all bulk mail except
from sources in a "white list." White lists are generally the
responsibility of DCC clients, since only they know which bulk mail
they solicited.

%description server -l pl
DCC (Distributed Checksum Clearinghouse) jest kooperatywnym,
rozproszonym systemem maj±cym na celu wykrywanie masowej poczty lub
poczty wys³anej do wielu ludzi. Pozwala jednostkom otrzymuj±cym
pojedynczy list okre¶liæ, jak wielu innych otrzyma³o dok³adnie
identyczne kopie tej wiadomo¶ci i na tej podstawie odrzuciæ j±. Mo¿e
zidentyfikowaæ niechcian± masow± pocztê przy u¿yciu "pu³apek
antyspamowych" i innych wykrywaczy, ale to nie jest podstawowym celem.

DCC mo¿na odbieraæ jako narzêdzie dla u¿ytkowników koñcowych,
zapewniaj±ce im prawo do przeciwstawienia siê zalewowi masowej poczty
przez odrzucenie wszystkich ¶mieci oprócz ¼róde³ z "bia³ej listy".
Za bia³e listy odpowiadaj± klienci DCC, jako ¿e tylko oni wiedz±,
jak± masow± pocztê zamawiali.

%package cgi
Summary:	CGI scripts for managing mail delivery on a DCC enabled server
Summary(pl):	Skrypty CGI do obs³ugi dostarczania poczty na serwerze DCC
Group:		Networking
Requires:	%{name} = %{version}-%{release}

%description cgi
Example set of CGI scripts to allow users to point-and-click manage
their own DCC whitelists and thus what is delivered to them. Allows
overriding of site level lists. The scripts give controlled access to
the whitelists which are otherwise in protected directory space (owned
by dcc).

NB these scripts need configured after installation.

%description cgi -l pl
Przyk³adowy zestaw skryptów CGI pozwalaj±cych u¿ytkownikom na klikane
zarz±dzenie ich bia³ymi listami DCC, a wiêc i tym, co dostaj±. Pozwala
przykrywaæ listy dotycz±ce serwera. Skrypty daj± dostêp do bia³ych
list, które normalnie s± w zabezpieczonym katalogu (którego
w³a¶cicielem jest DCC).

Te skrypty wymagaj± konfiguracji po zainstalowaniu.

%prep
%setup -q

%build
CFLAGS="%{rpmcflags}"; export CFLAGS
LDFLAGS="%{rpmldflags}"; export LDFLAGS
./configure \
	--bindir=%{_bindir} \
	--libexecdir=%{_libexecdir} \
	--mandir=%{_mandir} \
	--homedir=%{dccdir} \
	--with-uid=99 \
	--with-cgibin=%{cgidir} \
	--with-rundir=%{_var}/run \
	--with-db-memory=32

%{__make}
%{__make} -C dccifd/dccif-test

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_initrddir}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{cron.daily,httpd}
install -d $RPM_BUILD_ROOT/var/run/dcc
install -d $RPM_BUILD_ROOT%{dccdir}/{log,userdirs/{local,esmtp,cyrus,procmail}}
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sbindir},%{_mandir},%{_libdir}}
install -d $RPM_BUILD_ROOT%{_includedir}/dcc

INST_UID="$( id -u )" INST_GID="$( id -g )"; export INST_UID INST_GID

%{makeinstall} \
	MANOWN=$INST_UID \
	MANGRP=$INST_GID \
	DCC_SUID=$INST_UID \
	DCC_OWN=$INST_UID \
	DCC_GRP=$INST_GID \
	BINOWN=$INST_UID \
	GRP=$INST_GID \
	INSTALL="install -C" \
	INST_BINDIR=$RPM_BUILD_ROOT%{cgidir} \
	DCC_HOMEDIR=$RPM_BUILD_ROOT%{dccdir} \
	DCC_CGIBINDIR=$RPM_BUILD_ROOT%{cgidir} \
	DCC_LIBEXECDIR=$RPM_BUILD_ROOT%{_sbindir} \
	DCC_BINDIR=$RPM_BUILD_ROOT%{_sbindir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man

install misc/cron-dccd $RPM_BUILD_ROOT%{_sysconfdir}/cron.daily/dccd
install misc/rcDCC $RPM_BUILD_ROOT%{_initrddir}/dccd
install homedir/flod $RPM_BUILD_ROOT%{dccdir}/flod

# move some binaries in place, wierd stuff...
for i in dbclean dblist dccd dccifd dccsight wlist; do
	mv -f $RPM_BUILD_ROOT%{_bindir}/$i $RPM_BUILD_ROOT%{_sbindir}
done

# install extras
install dccifd/dccif-test/dccif-test $RPM_BUILD_ROOT%{_sbindir}
install dccifd/dccif-test/dccif-test.pl $RPM_BUILD_ROOT%{_sbindir}
install dccifd/dccif.pl $RPM_BUILD_ROOT%{_sbindir}

# Set some initial logging, but no rejections
perl -p -i -e "s/BRAND=\$/BRAND=%{version}-%{release}/ ; s/DCCM_LOG_AT=\$/\$&10/ ; " \
	$RPM_BUILD_ROOT%{dccdir}/dcc_conf

# prepare for docs inclusion
cp misc/README README.misc
cp homedir/README README.homedir
cp cgi-bin/README README.cgi-bin

# install devel files
install dccd/*.h $RPM_BUILD_ROOT%{_includedir}/dcc
install dcclib/*.h $RPM_BUILD_ROOT%{_includedir}/dcc
install include/*.h $RPM_BUILD_ROOT%{_includedir}/dcc
install srvrlib/*.h $RPM_BUILD_ROOT%{_includedir}/dcc
install dcclib/libdcc.a $RPM_BUILD_ROOT%{_libdir}
install srvrlib/libsrvr.a $RPM_BUILD_ROOT%{_libdir}
install thrlib/libthr.a $RPM_BUILD_ROOT%{_libdir}

# house cleaning
rm -f $RPM_BUILD_ROOT/var/www/dcc-bin/README
rm -f $RPM_BUILD_ROOT%{_sbindir}/rcDCC
rm -f $RPM_BUILD_ROOT%{_sbindir}/cron-dccd
rm -f $RPM_BUILD_ROOT%{_sbindir}/logger
rm -f $RPM_BUILD_ROOT%{_sbindir}/updatedcc

%clean
rm -rf $RPM_BUILD_ROOT

%pre
# TODO register userid in uid_gid.db.txt
%useradd -u XXX -d %{dccdir} -r dcc

%postun
if [ $1 = 0 ]; then
	%userremove dcc
fi

%post
/sbin/chkconfig --add dccd
umask 022
/usr/bin/cdcc info > %{dccdir}/map.txt

%post cgi
echo The scripts need configured and added into your web configuration.
echo see %{dccdir}/cgi-bin/README

%preun
if [ $1 = 0 ]; then
	/sbin/chkconfig --del dccd || :
	/etc/rc.d/init.d/dccd stop || :
fi

%files
%defattr(644,root,root,755)
%doc CHANGES FAQ.html FAQ.txt INSTALL.html INSTALL.txt LICENSE cdcc.html
%doc dbclean.html dblist.html dccd.html dcc.html dccproc.html
%doc dccsight.html homedir/flod homedir/ids homedir/map.txt homedir/README
%doc misc/dcc.m4 misc/dccdnsbl.m4 misc/hackmc
#%doc dccm.html 
%dir %{dccdir}
%dir %{dccdir}/log
%dir %{dccdir}/userdirs/local
%dir %{dccdir}/userdirs/cyrus
%dir %{dccdir}/userdirs/procmail
%dir %{dccdir}/userdirs/esmtp
%dir /var/run/dcc
%config(noreplace) %verify(not size mtime md5) %{dccdir}/dcc_conf
%config(noreplace) %verify(not size mtime md5) %{dccdir}/whiteclnt
%config(noreplace) %verify(not size mtime md5) %{dccdir}/whitecommon
%config(noreplace) %verify(not size mtime md5) %{dccdir}/whitelist
%config(noreplace) %verify(not size mtime md5) %{dccdir}/ids
%config(noreplace) %verify(not size mtime md5) %{dccdir}/flod
%attr(600,root,root) %config(noreplace) %verify(not size mtime md5) %{dccdir}/map
#%config(noreplace) %verify(not size mtime md5) %{dccdir}/dcc_db
#%config(noreplace) %verify(not size mtime md5) %{dccdir}/dcc_db.hash
%{dccdir}/map.txt
%{dccdir}/grey_flod
%{dccdir}/grey_whitelist

%files client
%defattr(644,root,root,755)
%attr(4755,root,root) %{_bindir}/cdcc
%attr(4755,root,root) %{_bindir}/dccproc
%{_mandir}/man8/cdcc.8*
%{_mandir}/man8/dccproc.8*

%files server
%defattr(644,root,root,755)
%attr(754,root,root) /etc/rc.d/init.d/dccd
%attr(750,root,root) /etc/cron.daily/dccd
%attr(4755,root,root) %{_sbindir}/dccsight
%attr(755,root,root) %{_sbindir}/dbclean
%attr(755,root,root) %{_sbindir}/dblist
%attr(755,root,root) %{_sbindir}/dcc-stats-collect
%attr(755,root,root) %{_sbindir}/dcc-stats-graph
%attr(755,root,root) %{_sbindir}/dcc-stats-init
%attr(755,root,root) %{_sbindir}/dccd
%attr(755,root,root) %{_sbindir}/dccif-test
%attr(755,root,root) %{_sbindir}/dccif-test.pl
%attr(755,root,root) %{_sbindir}/dccif.pl
%attr(755,root,root) %{_sbindir}/dccifd
%attr(755,root,root) %{_sbindir}/fetch-testmsg-whitelist
%attr(755,root,root) %{_sbindir}/hackmc
%attr(755,root,root) %{_sbindir}/newwebuser
%attr(755,root,root) %{_sbindir}/wlist
# sendmail stuff
#%attr(755,root,root) %{_sbindir}/dccm
#%{_datadir}/sendmail-cf/feature/dcc.m4
#%{_datadir}/sendmail-cf/feature/dccdnsbl.m4
%attr(755,root,root) %{_sbindir}/start-dccd
%attr(755,root,root) %{_sbindir}/start-dccifd
%attr(755,root,root) %{_sbindir}/start-dccm
%attr(755,root,root) %{_sbindir}/start-grey
%attr(755,root,root) %{_sbindir}/stats-get
%attr(755,root,root) %{_sbindir}/stop-dccd
%{_mandir}/man8/dbclean.8*
%{_mandir}/man8/dblist.8*
%{_mandir}/man8/dcc.8*
%{_mandir}/man8/dccd.8*
%{_mandir}/man8/dccifd.8*
%{_mandir}/man8/dccm.8*
%{_mandir}/man8/dccsight.8*

%files cgi
%defattr(644,root,root,755)
%{cgidir}/chgpasswd
%{cgidir}/common
%{cgidir}/edit-whiteclnt
%{cgidir}/http2https
%{cgidir}/list-log
%{cgidir}/list-msg
%{cgidir}/README
%{cgidir}/webuser-notify
