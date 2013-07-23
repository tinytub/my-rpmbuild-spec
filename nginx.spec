Summary: Apache for CentOS5.* compiled from CentOS5.4
Name: httpd
Version: 2.4.4
Release: 1
Source0: %{name}-%{version}.tar.gz
Source1: apr-1.4.8.tar.gz
Source2: apr-util-1.5.2.tar.gz
License: MIT
Group: Applications/Internet
Buildroot: %{_tmppath}/%{name}-%{version}-root
Requires: pcre,pcre-devel
%description
The Apache HTTP Server Project is a collaborative software development effort aimed at creating a robust, commercial-grade, featureful, and freely-available source code implementation of an HTTP (Web) server. The project is jointly managed by a group of volunteers located around the world, using the Internet and the Web to communicate, plan, and develop the server and its related documentation. This project is part of the Apache Software Foundation. In addition, hundreds of users have contributed ideas, code, and documentation to the project. This file is intended to briefly describe the history of the Apache HTTP Server and recognize the many contributors.
%prep
%setup -c
#%setup -T -b 0
#%setup -b 1 -c -n %{_topdir}/BUILD/
#%setup -b 2 -c -n %{_topdir}/BUILD/
%setup -b 1
%setup -b 2
mv  %{_topdir}/BUILD/apr-1.4.8  %{_topdir}/BUILD/%{name}-%{version}/srclib/apr
mv  %{_topdir}/BUILD/apr-util-1.5.2  %{_topdir}/BUILD/%{name}-%{version}/srclib/apr-util

%build
#cd %{_topdir}/BUILD/%{name}-%{version}
./configure --prefix=/usr/local/apache2 --enable-deflate --enable-rewrite --enable-so --enable-mods-shared=all --with-included-apr
#./configure --prefix=/usr/local/apache2 --with-pcre=/usr/local/pcre --enable-deflate --enable-rewrite --enable-so --enable-mods-shared=all --with-included-apr
make
%install
rm -rf $RPM_BUILD_ROOT/usr/local/apache2
#rm -rf $RPM_BUILD_ROOT/usr/local/apache2
make DESTDIR=$RPM_BUILD_ROOT install

%post
%preun
#if [ $1 == 0 ];then
#/usr/sbin/userdel -r apache 2> /dev/null


%clean
rm -rf $RPM_BUILD_ROOT
%files
%defattr(-,root,root)
%{_prefix}
