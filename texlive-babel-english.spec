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
Requires(pre):	texlive-tlpkg
Requires:	texlive(hyphen-english)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides the language definition file for support of English
in babel. Care is taken to select british hyphenation patterns for
British English and Australian text, and default ('american') patterns
for Canadian and USA text.

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/generic
%dir %{_datadir}/texmf-dist/source/generic
%dir %{_datadir}/texmf-dist/tex/generic
%dir %{_datadir}/texmf-dist/doc/generic/babel-english
%dir %{_datadir}/texmf-dist/source/generic/babel-english
%dir %{_datadir}/texmf-dist/tex/generic/babel-english
%doc %{_datadir}/texmf-dist/doc/generic/babel-english/README
%doc %{_datadir}/texmf-dist/doc/generic/babel-english/english.pdf
%doc %{_datadir}/texmf-dist/source/generic/babel-english/english.dtx
%doc %{_datadir}/texmf-dist/source/generic/babel-english/english.ins
%{_datadir}/texmf-dist/tex/generic/babel-english/UKenglish.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/USenglish.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/american.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/australian.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/british.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/canadian.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/english.ldf
%{_datadir}/texmf-dist/tex/generic/babel-english/newzealand.ldf
