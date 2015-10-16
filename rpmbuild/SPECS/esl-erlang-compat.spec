Name: esl-erlang-compat
Version: 18.1
Release: 1
Summary: A compat file to get esl-erlang to provide erlang
URL:  https://github.com/jasonmcintosh/esl-erlang-compat
License: MPLv1.1 and MIT and ASL 2.0 and BSD
BuildArch: noarch
Requires: esl-erlang >= 18.1
Provides: erlang
BuildRoot: %{_tmppath}/%{name}-root

%description
A compat file to allow esl-erlang to provide erlang dependencies.  Updated to 18.1 for rabbitmq 3.6.0

%prep

%build

%install

%files

%changelog
* Wed Jul 5 2015 Jason McIntosh <mcintoshj@gmail.com>
- Updated to use 18.1 as minimum version

%clean
rm -rf $RPM_BUILD_ROOT
