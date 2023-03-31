Name:		texlive-rutitlepage
Version:	62143
Release:	2
Summary:	Radboud University Titlepage Package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/rutitlepage
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rutitlepage.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rutitlepage.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/rutitlepage.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an unofficial LaTeX package to generate titlepages for
the Radboud University, Nijmegen. It uses official vector logos
from the university. This package requires the following other
LaTeX packages: geometry, graphicx, ifpdf, keyval, iflang, and,
optionnaly, babel-dutch.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/rutitlepage
%{_texmfdistdir}/tex/latex/rutitlepage
%doc %{_texmfdistdir}/doc/latex/rutitlepage

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
