Name:		texlive-zztex
Version:	55862
Release:	1
Summary:	A full-featured TeX macro package for producing books, journals, and manuals
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/zztex
License:	mit
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zztex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zztex.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The ZzTeX macro package is a full-featured TeX macro package
specially designed for producing books, journals, and manuals.
Development of the package began in 1989. Since then, about 500
textbooks and journals have been produced with it for a variety
of publishers. Numerous authors have used the package to
produce subsequent editions of their books. ZzTeX runs under
Plain TeX. The only documentation available for the package is
contained in the zz*.dat files that accompany the TeX files.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/zztex
%doc %{_texmfdistdir}/doc/plain/zztex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
