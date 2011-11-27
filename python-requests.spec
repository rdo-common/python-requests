Name:           python-requests
Version:        0.8.2
Release:        1%{?dist}
Summary:        HTTP library, written in Python, for human beings

License:        ISC
URL:            http://pypi.python.org/pypi/requests
Source0:        http://pypi.python.org/packages/source/r/requests/requests-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python-devel

%description
Most existing Python modules for sending HTTP requests are extremely verbose and 
cumbersome. Python’s built-in urllib2 module provides most of the HTTP 
capabilities you should need, but the API is thoroughly broken. This library is 
designed to make HTTP requests easy for developers.


%prep
%setup -q -n requests-%{version}


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

 
%files
%doc LICENSE README.rst HISTORY.rst
%{python_sitelib}/*.egg-info
%dir %{python_sitelib}/requests
%dir %{python_sitelib}/requests/packages
%dir %{python_sitelib}/requests/packages/oreos
%dir %{python_sitelib}/requests/packages/urllib3
%{python_sitelib}/requests/packages/*.py*
%{python_sitelib}/requests/packages/oreos/*.py*
%{python_sitelib}/requests/packages/urllib3/*.py*
%{python_sitelib}/requests/*.py*



%changelog
* Sun Nov 27 2011 Arun SAG <sagarun@gmail.com> - 0.8.2-1
- New upstream version
- keep alive support
- complete removal of cookiejar and urllib2

* Thu Nov 10 2011 Arun SAG <sagarun@gmail.com> - 0.7.6-1
- Updated to new upstream release 0.7.6

* Thu Oct 20 2011 Arun SAG <sagarun@gmail.com> - 0.6.6-1
- Updated to version 0.6.6

* Fri Aug 26 2011 Arun SAG <sagarun@gmail.com> - 0.6.1-1
- Updated to version 0.6.1

* Sat Aug 20 2011 Arun SAG <sagarun@gmail.com> - 0.6.0-1
- Updated to latest version 0.6.0

* Mon Aug 15 2011 Arun SAG <sagarun@gmail.com> - 0.5.1-2
- Remove OPT_FLAGS from build section since it is a noarch package
- Fix use of mixed tabs and space
- Remove extra space around the word cumbersome in description

* Sun Aug 14 2011 Arun SAG <sagarun@gmail.com> - 0.5.1-1
- Initial package
