Name:		jools
Summary:	Graphical puzzle game
Version: 0.20
Release: %mkrel 5
Url:		http://www.eecs.umich.edu/~pelzlpj/jools/
Source0:	%{name}-%{version}.tar.bz2
Patch0:	%{name}-%{version}-sys.patch
Patch1:	%{name}-%{version}-sharegames.patch
#Source2:	%{name}-48.png
#Source3:	%{name}-32.png
#Source4:	%{name}-16.png
Group:		Games/Puzzles
License:	GPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  python-devel
Requires:	pygame
BuildArch:      noarch

%description
Jools is a graphical puzzle game in the tradition of Tetris.
In a nutshell, the goal is to swap adjacent jools (jewels) within a grid,
in order to create rows of three or more of a kind.
These jools will then disappear, and more will fall to fill their places.
Jools features nifty 3D rendered graphics.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
python setup.py install --root=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_datadir}/doc
find $RPM_BUILD_ROOT%{_gamesdatadir}/%{name} -name '.arch-ids' -o -name '.placeholder' | xargs rm -rf

install -d -m 755 $RPM_BUILD_ROOT%{_gamesbindir}
mv $RPM_BUILD_ROOT%{_bindir}/%{name} $RPM_BUILD_ROOT%{_gamesbindir}
rmdir $RPM_BUILD_ROOT%{_bindir}

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat > $RPM_BUILD_ROOT%{_menudir}/%{name} << EOF
?package(%{name}): command="%{_gamesbindir}/%{name}" icon="%{name}.png" section="More Applications/Games/Puzzles" title="Jools" longtitle="Graphical puzzle game" needs="x11"
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_menus

%postun
%clean_menus

%files
%defattr(-,root,root,755)
%doc COPYING ChangeLog README doc/manual.html doc/manual.tex doc/detonate.txt doc/POINTS doc/TODO
%{_gamesbindir}/%{name}
%{py_puresitedir}/%{name}*
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_menudir}/%{name}
#%{_liconsdir}/%{name}.png
#%{_iconsdir}/%{name}.png
#%{_miconsdir}/%{name}.png
