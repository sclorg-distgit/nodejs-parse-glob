%{?scl:%scl_package nodejs-%{npm_name}}
%{!?scl:%global pkg_name %{name}}

%{?nodejs_find_provides_and_requires}
%global npm_name parse-glob

Summary:       Parse a glob pattern into an object of tokens
Name:          %{?scl_prefix}nodejs-%{npm_name}
Version:       3.0.4
Release:       4%{?dist}
License:       MIT
URL:           https://github.com/jonschlinkert/parse-glob
Source0:       http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}runtime
ExclusiveArch: %{nodejs_arches} noarch
BuildArch:     noarch
Provides:      %{?scl_prefix}nodejs-%{npm_name} = %{version}

%description
Parse a glob pattern into an object of tokens.

%prep
%setup -q -n package

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}

%nodejs_symlink_deps

%files
%{!?_licensedir:%global license %doc}
%doc README.md
%license LICENSE
%{nodejs_sitelib}/%{npm_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.4-4
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 3.0.4-3
- Rebuilt with updated metapackage

* Mon Jan 11 2016 Tomas Hrcka <thrcka@redhat.com> - 3.0.4-2
- Enable scl macros

* Wed Dec 16 2015 Troy Dawson <tdawson@redhat.com> - 3.0.4-1
- Initial package