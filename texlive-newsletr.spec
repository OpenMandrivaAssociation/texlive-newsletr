Name:		texlive-newsletr
Version:	20061222
Release:	1
Summary:	Macros for making newsletters with Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/newsletr
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newsletr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newsletr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive newsletr package.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/plain/newsletr/newsletr.tex
%doc %{_texmfdistdir}/doc/plain/newsletr/italic.tex
%doc %{_texmfdistdir}/doc/plain/newsletr/lodriver.tex
%doc %{_texmfdistdir}/doc/plain/newsletr/losample.tex
%doc %{_texmfdistdir}/doc/plain/newsletr/newsletr.txt
%doc %{_texmfdistdir}/doc/plain/newsletr/newssamp.pdf
%doc %{_texmfdistdir}/doc/plain/newsletr/newssamp.tex
%doc %{_texmfdistdir}/doc/plain/newsletr/quote.tex
%doc %{_texmfdistdir}/doc/plain/newsletr/read.me
%doc %{_texmfdistdir}/doc/plain/newsletr/sample.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
