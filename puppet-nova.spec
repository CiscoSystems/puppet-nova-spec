Name:		puppet-nova	
Version:	0.1
Release:	1cisco%{?dist}
Summary:	Puppet module to configure nova, the compute service of openstack

Group:		System Environment/Base
License: 	Apache License 2.0	
URL:		https://github.com/CiscoSystems/puppet-nova.git
Source0: 	%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

%description
This module can be used to flexibly configure nova, the compute service of openstack. It has been tested with a combination of other modules, and has primarily been developed as a subcomponent of the openstack module. The examples that come with this module are out of date. It is recommended to use the openstack module as a starting place.

%prep
%setup -q


%build

%install
rm -rf %{buildroot}
install -d %{buildroot}/%{_usr}/share/puppet/modules/%{name}/
cp -R * %{buildroot}/%{_usr}/share/puppet/modules/%{name}/

%files
%dir %{_usr}/share/puppet/modules/%{name}/
%{_usr}/share/puppet/modules/%{name}/*


%defattr(-,root,root,-)
%doc CHANGELOG LICENSE examples/

%clean
rm -rf %{buildroot}

%changelog
* Tue Apr 23 2013 Pradeep Kilambi <pkilambi@cisco.com> - 0.1-1cisco
- Initial package.

