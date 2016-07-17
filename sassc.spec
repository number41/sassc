%{?scl:%scl_package sassc}
%{!?scl:%global pkg_name %{name}}

Name:       %{?scl_prefix}sassc
Version:    3.3.6
Release:    1%{?dist}
Summary:    CLI wrapper around libsass

Group:      Tools
License:    Custom
URL:        https://github.com/sass/sassc
Source0:    https://github.com/sass/%{pkg_name}/archive/%{version}.tar.gz

BuildRequires:  %{?scl_prefix}libsass-devel
Requires:       %{?scl_prefix}libsass

%description
CLI wrapper around libsass

%prep
%setup -q -n %{pkg_name}-%{version}


%build
%{?scl:scl enable %{scl} - << \EOF}
%configure
make %{?_smp_mflags}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%make_install
%{?scl:EOF}

%files
%doc



%changelog

