Name:           setgittag
Version:        0.1.0
Release:        %autorelease
Summary:        Sets a git tag to the current folder

License:        MIT
URL:            https://github.com/grillo-delmal/setgittag
Source0:        https://github.com/grillo-delmal/setgittag/archive/%{version}/%{name}-%{version}.tar.gz

Requires:       bash

BuildArch:      noarch

%description
Creates a repository in the current folder, creates an empty commit
and sets the described tag for it.
The purpose of this is to have a method to set what the 'git describe' 
command shows without needing to import a project's git history.

%prep
%setup -q
sed -i "s/VERSION=\"UNTAGGED\"/VERSION=\"%{version}\"/" setgittag

%build

%install

mkdir -p %{buildroot}/%{_bindir}

install -m 0755 %{name} %{buildroot}/%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
