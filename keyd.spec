%if 0%{?fedora}
%global debug_package %{nil}
%endif

Name:     keyd
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  A powerful key remapper for the Linux desktop
License:  MIT
URL:      https://github.com/ignic/keyd

VCS:      {{{ git_dir_vcs }}}
Source:   {{{ git_dir_pack }}}

BuildRequires: gcc-c++
BuildRequires: systemd-rpm-macros

%description
%{summary}

%prep
{{{ git_dir_setup_macro }}}

%build
make

%install
make DESTDIR=%{buildroot} PREFIX=/usr install

%files
%{_sysconfdir}/%{name}
%{_bindir}/%{name}
%{_unitdir}/%{name}.service
%{_docdir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.gz
%license LICENSE

%post
%systemd_post %{name}.service

%preun
%systemd_preun %{name}.service

%postun
%systemd_postun_with_restart %{name}.service

%changelog
* Wed May 15 2024 ignic <ignic@mail.org> - 1
- First package
