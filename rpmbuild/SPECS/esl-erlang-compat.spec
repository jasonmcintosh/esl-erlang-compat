Name: esl-erlang-compat
Version: 19.3.6
Release: 1
Summary: A compat file to get esl-erlang to provide erlang
URL:  https://github.com/jasonmcintosh/esl-erlang-compat
License: MPLv1.1 and MIT and ASL 2.0 and BSD
BuildArch: noarch
Requires: esl-erlang >= 19.3.6
Provides: erlang
BuildRoot: %{_tmppath}/%{name}-root

%description
A shim (compatibility) package to allow esl-erlang to provide an erlang package dependency.

%prep

%build

%install

%files

%changelog
* Tue Feb 20 2018 Michael Klishin <michael@clojurewerkz.org>
- Updated to use 19.3.6 as minimum version

* Wed Aug 17 2016 Gabriele Santomaggio <g.santomaggio@gmail.com>
- Updated to use 19.0 as minimum version

* Wed Jul 08 2015 Jason McIntosh <mcintoshj@gmail.com>
- Updated to use 18.1 as minimum version

%clean
rm -rf $RPM_BUILD_ROOT
