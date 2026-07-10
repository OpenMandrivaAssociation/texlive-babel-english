%global tl_name babel-english
%global tl_revision 77682

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.3r
Release:	%{tl_revision}.1
Summary:	Babel support for English
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/babel-contrib/english
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-english.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-english.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/babel-english.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Requires:	texlive(hyphen-english)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of English
in babel. Care is taken to select british hyphenation patterns for
British English and Australian text, and default ('american') patterns
for Canadian and USA text.

