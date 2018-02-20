# esl-erlang Shim Package

Compat RPM to get esl-erlang RPMs to provide `erlang` to the RPM Database as well as `esl-erlang`.

## Binary Builds

See [GitHub releases](https://github.com/jasonmcintosh/esl-erlang-compat/releases) for binary builds.

## Building new RPMs
Command (with the right tools installed) to build:
```
cd rpmbuilds 
rpmbuild -ba SPECS/esl-erlang-compat.spec 
mv ~/rpmbuilds/RPMS/noarch/esl-erlang-compat-19.3.6-1.noarch.rpm ./RPMS/noarch
```
