#! /bin/sh
BUILDROOT=$1

exec >> $2/develfiles.list

TMPFILE=`mktemp /tmp/find-devel.XXXXXX` || exit 1
TMPFILE2=`mktemp /tmp/find-devel.XXXXXX` || exit 1

find_files_in() {
    findargs="$1"
    shift
    for dir in "$@"; do
	if [ -d $BUILDROOT$dir ]; then
	    for file in `find $BUILDROOT$dir $findargs \! -type d | sed -e"s,$BUILDROOT,,"`; do
		if echo $file | grep '\.so$' > /dev/null; then
		    if ls -l $BUILDROOT$file | grep '\.so\.[0-9.]*$' > /dev/null; then
			echo $file >> $TMPFILE
		    fi
		else
		    echo $file >> $TMPFILE
		fi
	    done 
	    for xdir in `sed -e's,/[^/]*$,,' < $TMPFILE | sort -u`; do
		while [ "$xdir" != "$dir" ]; do
		    echo $xdir >> $TMPFILE2
		    xdir=`echo $xdir | sed -e's,/[^/]*$,,'`
		done
	    done
	    sort -u < $TMPFILE2 | sed -e's,^,%dir ,'
	    sort $TMPFILE
	    : > $TMPFILE2
	    : > $TMPFILE
	fi
    done
}

set -f
find_files_in '' /usr/include
find_files_in '-name *.a -or -name *.la -or ( -name *.so -type l )' /usr/lib /usr/lib64 | sed -e's,^\(.*\.l?a\)$,%exclude \1,'
find_files_in '' /usr/share/aclocal /usr/lib/pkgconfig /usr/lib64/pkgconfig /usr/share/gtk-doc
find_files_in '' /usr/share/man/man3 | sed -e's,$,*,'

rm -f $TMPFILE $TMPFILE2
exit 0
