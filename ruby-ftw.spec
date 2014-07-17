#
# Conditional build:
%bcond_with	tests		# build without tests

%define	pkgname	ftw
Summary:	Ruby FTW - For The Web. Experimentation in web clients and servers
Name:		ruby-%{pkgname}
Version:	0.0.34
Release:	2
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	1ad00afe5009fdb887c70e3a107891e2
URL:		http://github.com/jordansissel/ruby-ftw
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
%if %{with tests}
BuildRequires:	ruby-minitest
%endif
Requires:	ruby-addressable
Requires:	ruby-backports >= 2.6.2
Requires:	ruby-cabin
Requires:	ruby-http_parser.rb = 0.5.3
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
For The Web. Trying to build a solid and sane API for client and
server web stuff. Client and Server operations for HTTP, WebSockets,
SPDY, etc.

%prep
%setup -q -n %{pkgname}-%{version}

%build
%__gem_helper spec

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec

# ruby-rack subpackage?
%dir %{ruby_vendorlibdir}/rack
%dir %{ruby_vendorlibdir}/rack/handler
%{ruby_vendorlibdir}/rack/handler/ftw.rb
