Summary:	Distributed Checksum Clearinghouse, anti-spam tool
Summary(pl):	Narzêdzie anty-spamowe bazuj±ce na sumach kontrolnych (DCC)
Name:		dcc-dccd
Version:	1.1.13
Release:	1
License:	BSD-like
Group:		Networking
Source0:	http://www.dcc-servers.net/dcc/source/%{name}-%{version}.tar.Z
URL:		http://www.dcc-servers.net/
Prereq:		/sbin/chkconfig
Prereq:		/usr/sbin/useradd
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

NB to use DCC to reject SPAM you need to configure /var/dcc/dcc_conf
and either use procmail or sendmail to feed the messages to DCC

%package cgi
Summary:	cgi-scripts for managing mail delivery on a DCC enabled server
Group:		Networking/Mail
######		Unknown group!
Requires:	%{name} >= 1.1.2

%description cgi
Example set of cgi-scripts to allow users to point-and-click manage
their own DCC whitelists and thus what is delivered to them. Allows
overriding of site level lists. The scripts give controlled access to
the whitelists which are otherwise in protected directory space (owned
by dcc).

NB these scripts need configured after installation

%prep
%setup -q

%build
%configure2_13 \
	--with-uid=99 \
	--with-cgibin=/home/httpd/html/cgi-bin \
	--with-rundir=%{_var}/run \
	--with-db-memory=32
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{makeinstall} \
	MANOWN=$(id -u) \
	MANGRP=$(id -g) \
	BINOWN=$(id -u) \
	BINGRP=$(id -u) \
	MANDIR=$RPM_BUILD_ROOT%{_mandir} \
	BINDIR=$RPM_BUILD_ROOT%{_bindir}


	DCC_PROTO_HOMEDIR=$RPM_BUILD%{_var}/lib/dcc
	DCC_CGIBINDIR=$RPM_BUILD_ROOT/var/dcc/cgi-bin export DCC_CGIBINDIR
DCC_SUID=$BINOWN DCC_OWN=$BINOWN DCC_GRP=$BINGRP export DCC_SUID DCC_OWN DCC_GRP
install -d $RPM_BUILD_ROOT%{_datadir}/sendmail-cf/feature $DCC_CGIBINDIR
install -d $RPM_BUILD_ROOT%{_sysconfdir}/{init.d,cron.daily} $RPM_BUILD_ROOT/{var/{run/dcc,dcc/{log,userdirs/{local,esmtp,cyrus,procmail}}},usr/bin}
%makeinstall
cp misc/dcc.m4 misc/dccdnsbl.m4 $RPM_BUILD_ROOT/usr/share/sendmail-cf/feature
mv $RPM_BUILD_ROOT/usr/sbin/cron-dccd $RPM_BUILD_ROOT/etc/cron.daily/dccd

# There already is a logger program which takes the required arguments on Linux

rm -f $RPM_BUILD_ROOT/usr/sbin/logger

# We are putting these in the docs directory
rm -f $RPM_BUILD_ROOT/usr/sbin/hackmc
rm -f $RPM_BUILD_ROOT/usr/sbin/na-spam
rm -f $RPM_BUILD_ROOT/usr/sbin/ng-spam

mv $RPM_BUILD_ROOT/usr/sbin/rcDCC $RPM_BUILD_ROOT/etc/init.d/dccd
chmod 755 $RPM_BUILD_ROOT/etc/init.d/dccd

# Set some initial logging, but no rejections
perl -p -i -e "s/BRAND=\$/BRAND=RPMDEFAULT/ ; s/DCCM_LOG_AT=\$/\$&10/ ; " \
	$RPM_BUILD_ROOT/var/dcc/dcc_conf

umask 077
cat > $RPM_BUILD_ROOT/var/dcc/flod <<EOF
# hostname,port     rem-id [passwd-id] [out-opts] [in-opts]

# this will not work
# nonesuch.example.com,-	32767 100
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%pre
/usr/sbin/useradd -d /var/dcc -r dcc >/dev/null 2>&1 || :

%postun
if [ $1 = 0 ]; then
        /usr/sbin/userdel -r dcc > /dev/null 2>&1 || :
fi

%post
/sbin/chkconfig --add dccd || :
/sbin/chkconfig --level 016 dccd off || :
/usr/bin/cdcc info > /var/lib/dcc/map.txt || :

%post cgi
echo The scripts need configured and added into your web configuration.
echo see /var/dcc/cgi-bin/README


%preun
if [ $1 = 0 ]; then
	#
	# This is remove rather than update
	#
	/sbin/chkconfig --del dccd || :
	/etc/init.d/dccd stop || :
fi

%files
%defattr(644,root,root,755)

%dir	/var/dcc
%dir	/var/dcc/log
%dir	/var/dcc/userdirs/local
%dir	/var/dcc/userdirs/cyrus
%dir	/var/dcc/userdirs/procmail
%dir	/var/dcc/userdirs/esmtp
%dir	/var/run/dcc
%doc CHANGES FAQ.html FAQ.txt INSTALL.html INSTALL.txt LICENSE cdcc.html dbclean.html dblist.html dccd.html dcc.html dccm.html dccproc.html dccsight.html homedir/flod homedir/ids homedir/map.txt homedir/README misc/dcc.m4 misc/dccdnsbl.m4 misc/hackmc misc/na-spam misc/ng-spam
%config(noreplace)	/var/dcc/dcc_conf
%config(noreplace)	/var/dcc/whiteclnt
%config(noreplace)	/var/dcc/whitecommon
%config(noreplace)	/var/dcc/whitelist
%config(noreplace)	/var/dcc/ids
%config(noreplace)	/var/dcc/flod
%config(noreplace)	/var/dcc/dcc_db
%config(noreplace)	/var/dcc/dcc_db.hash
%config(noreplace)	/var/dcc/map
/var/dcc/map.txt
%{_sysconfdir}/init.d/dccd
/etc/cron.daily/dccd
%attr(755,root,root) %{_bindir}/cdcc
%attr(755,root,root) %{_bindir}/dccproc
%attr(755,root,root) %{_sbindir}/dbclean
%attr(755,root,root) %{_sbindir}/dblist
%attr(755,root,root) %{_sbindir}/dccd
%attr(755,root,root) %{_sbindir}/dccm
%attr(755,root,root) %{_sbindir}/dccsight
%attr(755,root,root) %{_sbindir}/refeed
%attr(755,root,root) %{_sbindir}/start-dccd
%attr(755,root,root) %{_sbindir}/start-dccm
%attr(755,root,root) %{_sbindir}/stop-dccd
%attr(755,root,root) %{_sbindir}/wlist
%{_datadir}/sendmail-cf/feature/dcc.m4
%{_datadir}/sendmail-cf/feature/dccdnsbl.m4

%{_mandir}/man8/*

%files cgi
%defattr(644,root,root,755)
%dir	/var/dcc/cgi-bin
/var/dcc/cgi-bin/chgpasswd
/var/dcc/cgi-bin/common
/var/dcc/cgi-bin/edit-whiteclnt
/var/dcc/cgi-bin/http2https
/var/dcc/cgi-bin/list-log
/var/dcc/cgi-bin/list-msg
/var/dcc/cgi-bin/README
/var/dcc/cgi-bin/webuser-notify
