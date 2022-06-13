Name:           python-executing
Version:        0.8.2
Release:        3%{?dist}
Summary:        Python library for inspecting the current frame run footprint

License:        MIT
URL:            https://github.com/alexmojaki/executing
# The package uses setuptools_scm, GitHub tarball will not work
Source0:        %{pypi_source executing}
Patch1:         0001-Disable-failing-test-on-Python-3.11.patch
# patch needed for compatibility with Python 3.11
# https://github.com/alexmojaki/executing/pull/31
Patch31:        31.patch

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Get information about what a Python frame is currently doing, particularly the
AST node being executed}

%description %_description

%package -n python3-executing
Summary:        %{summary}

%description -n python3-executing %_description


%prep
%autosetup -p1 -n executing-%{version}


%generate_buildrequires
%pyproject_buildrequires -t


%build
%pyproject_wheel


%install
%pyproject_install
%pyproject_save_files executing


%check
%tox


%files -n python3-executing -f %{pyproject_files}
%doc README.md
%license LICENSE.txt


%changelog
* Mon Jun 13 2022 Python Maint <python-maint@redhat.com> - 0.8.2-3
- Rebuilt for Python 3.11

* Fri Jan 21 2022 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Mon Dec 27 2021 Roman Inflianskas <rominf@aiven.io> - 0.8.2-1
- Initial package
