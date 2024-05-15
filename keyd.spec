Name:     keyd
Version:  {{{ git_dir_version }}}
Release:  1%{?dist}
Summary:  A powerful key remapper for the Linux desktop
License:  MIT
URL:      https://github.com/ignic/%{name}

Source:   %{url}/archive/refs/heads/master.tar.gz

BuildRequires: gcc-c++
BuildRequires: kernel-headers

%description
%{summary}

%prep
%autosetup

%build
make

%install
install -dm755 "%{buildroot}/usr/lib/systemd/system"
install -dm755 "%{buildroot}/usr/share/libinput"
make DESTDIR=%{buildroot} install
echo 'g keyd' | install -Dm644 /dev/stdin "%{buildroot}/usr/lib/sysusers.d/%{name}.conf"

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-application-mapper
%{_docdir}/%{name}
%{_datadir}/%{name}

%{_prefix}/lib/systemd/system/%{name}.service
%{_prefix}/lib/sysusers.d/%{name}.conf

%{_mandir}/man1/%{name}.1.gz
%{_mandir}/man1/%{name}-application-mapper.1.gz
%license LICENSE

%changelog
{{{ git_dir_changelog }}}

