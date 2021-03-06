# revision 15878
# category Package
# catalog-ctan /macros/plain/contrib/newsletr
# catalog-date 2006-12-22 19:14:47 +0100
# catalog-license other-free
# catalog-version undef
Name:		texlive-newsletr
Version:	20190228
Release:	1
Summary:	Macros for making newsletters with Plain TeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/plain/contrib/newsletr
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newsletr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newsletr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive newsletr package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20061222-2
+ Revision: 754337
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20061222-1
+ Revision: 719112
- texlive-newsletr
- texlive-newsletr
- texlive-newsletr
- texlive-newsletr

