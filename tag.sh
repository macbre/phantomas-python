#!/bin/sh
VERSION=`grep -r '__version__' phantomas/__init__.py | awk -F\' '{ print $2 }'`

echo "Tagging v${VERSION}..."

git tag -a v${VERSION} -m "v${VERSION}"
git push origin v${VERSION}

echo "Done"
