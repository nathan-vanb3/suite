%define __spec_install_pre /bin/true

Name: boundless-server-gs-printng
Version: REPLACE_VERSION
Release: REPLACE_RELEASE
Summary: Boundless Server PrintNG Plugin
Group: Applications/Engineering
License: GPLv2
URL: http://geoserver.org
BuildRoot: %{_WORKSPACE}/boundless-server-gs-printng/BUILDROOT
Requires(post): bash
Requires(preun): bash
Requires:  unzip, boundless-server-geoserver >= CURRENT_VER, boundless-server-geoserver < NEXT_VER
Obsoletes: suite-gs-printng
Conflicts: suite-gs-printng
AutoReqProv: no

%define _rpmdir archive/el/7/
%define _rpmfilename %%{NAME}-%%{VERSION}-%%{RELEASE}.%%{ARCH}.rpm
%define _unpackaged_files_terminate_build 0
# Don't waste time re-packing jars (http://makewhatis.com/2011/12/remove-unwanted-commpression-in-during-rpmbuild-for-jar-files)
%define __os_install_post %{nil}


%description
PrintNG plugin for Boundless Server.

%prep

%install
mkdir -p  %{buildroot}/opt/boundless/server/geoserver/WEB-INF/lib
cp %{_WORKSPACE}/SRC/BoundlessServer-ext/printng/*.jar %{buildroot}/opt/boundless/server/geoserver/WEB-INF/lib

%pre

%post

%preun

%postun

%files
%defattr(-,root,root,-)
/opt/boundless/server/geoserver/WEB-INF/lib/*
