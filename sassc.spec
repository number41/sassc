%{?scl:%scl_package sassc}
%{!?scl:%global pkg_name %{name}}

Name:       %{?scl_prefix}sassc
Version:    3.4.5
Release:    1%{?dist}
Summary:    CLI wrapper around libsass

Group:      Tools
License:    Custom
URL:        https://github.com/sass/sassc
Source0:    https://github.com/sass/%{pkg_name}/archive/%{version}.tar.gz

BuildRequires:  %{?scl_prefix}libsass-devel
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  libtool
Requires:       %{?scl_prefix}libsass

%description
CLI wrapper around libsass

%prep
%setup -q -n %{pkg_name}-%{version}
autoreconf --force --install


%build
%{?scl:scl enable %{scl} - << \EOF}
export SASSC_VERSION="%{version}"
%configure
make %{?_smp_mflags}
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - << \EOF}
%make_install
%{?scl:EOF}

%files
%doc Readme.md LICENSE
%{_bindir}/%{name}



%changelog

