Summary:	Pastemage - easily join images forming a panorama
Summary(pl):	Pastemage - ³atwe ³±czenie zdjêæ w panowamê
Name:		pastemage
Version:	20041108
Release:	1
License:	GPL
Group:		X11/Applications/Graphics
Source0:	http://dl.sourceforge.net/pastemage/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	5194a7af27180c7f70792c83bde8f388
URL:		http://pastemage.sourceforge.net/
# gtk-sharp and glade-sharp
BuildRequires:	dotnet-gtk-sharp-devel >= 1.0
BuildRequires:	mono-csharp >= 1.0
BuildRequires:	sed >= 4.0
Requires:	dotnet-gtk-sharp >= 1.0
ExclusiveArch:	%{ix86} amd64 arm hppa ppc s390 sparc sparcv9 sparc64
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pastemage is an easy to use program to join two or more images from a
digital camera or other sources to form one big panorama image. It
allows the user to interactively move the images with the mouse,
adjusting all the joining parameters.
 
%description -l pl
Pastemage to ³atwy w u¿yciu program do ³±czenia dwóch lub wiêkszej
liczby zdjêæ z aparatu cyfrowego lub innych ¼róde³ w celu stworzenia
du¿ej panoramy. Pozwala u¿ytkownikowi interaktywnie przesuwaæ zdjêcia
myszk±, reguluj±c parametry ³±czenia.

%prep
%setup -q -n %{name}-alpha-%{version}

sed -i -e 's,pastemage\.glade,%{_datadir}/%{name}/&,' ImageWindow.cs Preferences.cs
sed -i -e 's,libgtk-win32-2\.0-0\.dll,libgtk-x11-2.0.so.0,g' CompatFileChooser.cs

rm -f *.exe*

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}}

install pastemage.exe $RPM_BUILD_ROOT%{_bindir}
install pastemage.glade $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS TODO
%attr(755,root,root) %{_bindir}/pastemage.exe
%{_datadir}/%{name}
