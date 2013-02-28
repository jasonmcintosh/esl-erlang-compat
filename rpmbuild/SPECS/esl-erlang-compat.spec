%define release R14B
%define name esl-erlang-compat

Name: %{name}
Version: R14B
Release: 1%{?dist}
Summary: A compat file to get esl-erlang to provide erlang

License: MPLv1.1 and MIT and ASL 2.0 and BSD
Source0: %{name}-%{version}.tar.gz
BuildArch: noarch
Requires: esl-erlang >= R14B
Provides: erlang
#BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
A compat file to allow esl-erlang to provide erlang dependencies

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sysconfdir}/esl-erlang-compat/
cp -p version.txt $RPM_BUILD_ROOT%{_sysconfdir}/esl-erlang-compat/

%files
%defattr(-,root,root,-)
/etc/esl-erlang-compat/version.txt

%clean
rm -rf $RPM_BUILD_ROOT
