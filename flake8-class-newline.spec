#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : flake8-class-newline
Version  : 1.6.0
Release  : 1
URL      : https://files.pythonhosted.org/packages/17/f3/d93a95971801e0bd28539e7727e90553217ea76d48098ea02d10832f609f/flake8-class-newline-1.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/f3/d93a95971801e0bd28539e7727e90553217ea76d48098ea02d10832f609f/flake8-class-newline-1.6.0.tar.gz
Summary  : Flake8 lint for newline after class definitions.
Group    : Development/Tools
License  : MIT
Requires: flake8-class-newline-python3
Requires: flake8-class-newline-python
Requires: flake8
BuildRequires : buildreq-distutils3
BuildRequires : flake8

%description
===========================================

%package python
Summary: python components for the flake8-class-newline package.
Group: Default
Requires: flake8-class-newline-python3

%description python
python components for the flake8-class-newline package.


%package python3
Summary: python3 components for the flake8-class-newline package.
Group: Default
Requires: python3-core

%description python3
python3 components for the flake8-class-newline package.


%prep
%setup -q -n flake8-class-newline-1.6.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532979057
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
