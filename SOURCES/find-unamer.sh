#! /bin/sh

if test ! -d "$1"; then
    echo 0.0.0
    exit
else
    # $(KERNELVERSION) is not defined on all systems
cat > /tmp/Makefile.unamer.$$ << 'EOF'
include Makefile
release:
	echo $(KERNELRELEASE)
version:
	echo $(KERNELVERSION)
EOF
    make -f /tmp/Makefile.unamer.$$ -sC "$1" release version \
      | grep -v '^$' | head -n 1
    rm -f /tmp/Makefile.unamer.$$
fi