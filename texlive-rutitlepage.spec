%global tl_name rutitlepage
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.0
Release:	%{tl_revision}.1
Summary:	Radboud University Titlepage Package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/rutitlepage
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rutitlepage.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rutitlepage.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/rutitlepage.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an unofficial LaTeX package to generate titlepages for the
Radboud University, Nijmegen. It uses official vector logos from the
university. This package requires the following other LaTeX packages:
geometry, graphicx, ifpdf, keyval, iflang, and, optionally, babel-dutch.

