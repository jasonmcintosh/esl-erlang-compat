# esl-erlang Shim Package

Compat RPM to get esl-erlang RPMs to provide `erlang` to the RPM Database as well as `esl-erlang`.

## Binary Builds

See [GitHub releases](https://github.com/jasonmcintosh/esl-erlang-compat/releases) for binary builds.

## Building new RPMs
Command (with the right tools installed) to build:
```
docker run -e "VERSION=1.2.3" -v $(pwd):/srv -v $(pwd):/home/builder rpmbuild/centos7
```
