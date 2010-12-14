%define oname rumai

Name:       rubygem-%{oname}
Version:    3.3.1
Release:    %mkrel 1
Summary:    Ruby interface to the wmii window manager
Group:      Development/Ruby
License:    ISC License
URL:        http://snk.tuxfamily.org/lib/rumai/
Source0:    http://rubygems.org/gems/%{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
Requires:   wmii >= 3.9
Suggests:   rubygem(inochi) >= 5.0.2
Suggests:   rubygem(detest) >= 3.1.0
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Rumai is a pure [Ruby] interface to the [wmii] window manager. Its name is a
portmanteau of "Ruby" and "wmii", which I pronounce as "vim eye".


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

# Move manpages to mandir
mkdir -p %{buildroot}/%{_mandir}
mv %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man/* %{buildroot}/%{_mandir}
rmdir %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/man

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/rumai
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/CREDITS
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/LICENSE
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec
%{_mandir}/man1/%{oname}.1.*
