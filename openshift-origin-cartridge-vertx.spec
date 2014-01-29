%global cartridgedir %{_libexecdir}/openshift/cartridges/vertx
%define vertx_name vert.x
%define vertx_version 2.1M4

Summary:       Provides Vertx.x support
Name:          openshift-origin-cartridge-vertx
Version: 0.1.2
Release:       1%{?dist}
Group:         Development/Languages
License:       ASL 2.0
URL:           http://www.openshift.com
Source0:       http://mirror.openshift.com/pub/openshift-origin/source/%{name}/%{name}-%{version}.tar.gz
Source1:       http://dl.bintray.com/nscavell/vertx/%{vertx_name}-%{vertx_version}.tar.gz

Requires:      rubygem(openshift-origin-node)
Requires:      openshift-origin-node-util
Requires:      java-1.7.0-openjdk
Requires:      java-1.7.0-openjdk-devel

BuildArch:     noarch

%description
Provides Vertx.x support to OpenShift. (Cartridge Format V2)

%prep
%setup -q
%setup -a 1

%build
%__rm %{name}.spec
# Remove docs
%__rm -rf %{vertx_name}-%{vertx_version}/api-docs
# Copy runtime to usr dir of cartridge
%__mv %{vertx_name}-%{vertx_version} usr/

%install
%__mkdir -p %{buildroot}%{cartridgedir}
%__cp -r * %{buildroot}%{cartridgedir}

%files
%dir %{cartridgedir}
%attr(0755,-,-) %{cartridgedir}/bin/
%{cartridgedir}
%doc %{cartridgedir}/README.md
%doc %{cartridgedir}/COPYRIGHT
%doc %{cartridgedir}/LICENSE

%changelog
* Fri Jan 24 2014 Nick Scavelli <nscavell@redhat.com> 0.1.2-1
- Change vertx logging to point to OPENSHIFT_VERTX_LOG_DIR instead of tmp dir

* Tue Jan 21 2014 Nick Scavelli <nscavell@redhat.com> 0.1.1-1
- Add usr directory to store vert.x runtime so it can be symlinked

* Mon Jan 6 2014 Nick Scavelli <nscavell@redhat.com> 0.1.0-1
- Initial RPM spec
