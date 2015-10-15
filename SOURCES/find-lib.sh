#! /bin/sh
BUILDROOT=$1
BUILDDIR=$2
shift 2

while [ "$1" != "" ]; do
  the_lib_name=lib`echo $1 | grep '[0-9]$' > /dev/null && echo ${1}_$2 || echo $1$2`
  echo "%defattr(-,root,root,-)" > $BUILDDIR/$the_lib_name.list
  find $BUILDROOT/{lib,lib64,/usr/lib,/usr/lib64} 2>/dev/null \
    | sed -e"s,^$BUILDROOT,," \
    | grep -v /usr/lib/debug/ \
    | grep /lib$1.so.$2 >> $BUILDDIR/$the_lib_name.list
  if ! grep /lib$1.so.$2 $BUILDDIR/$the_lib_name.list; then
    echo "$0: error: No /lib$1.so.$2 found in build!"
  fi
  shift 2
done

exit 0
