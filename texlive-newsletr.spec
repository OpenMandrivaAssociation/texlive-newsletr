Name:		texlive-newsletr
Version:	15878
Release:	2
Summary:	Macros for making newsletters with Plain TeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/plain/contrib/newsletr
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newsletr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/newsletr.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
