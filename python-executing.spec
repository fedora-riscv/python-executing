Name:           python-executing
Version:        0.8.2
Release:        1%{?dist}
Summary:        Python library for inspecting the current frame run footprint

License:        MIT
URL:            https://github.com/alexmojaki/executing
# The package uses setuptools_scm, GitHub tarball will not work
Source0:        %{pypi_source executing}

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
* Mon Dec 27 2021 Roman Inflianskas <rominf@aiven.io> - 0.8.2-1
- Initial package
