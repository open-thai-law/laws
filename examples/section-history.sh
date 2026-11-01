#!/bin/sh
# Every change to one section (มาตรา) of one law, newest first.
#   examples/section-history.sh "acts/พ.ร.บ.ว่าด้วยการกระทำความผิดเกี่ยวกับคอมพิวเตอร์ พ.ศ. ๒๕๕๐.md" ๑๔
set -eu
file=$1
section=$2

# The section runs from its heading to the next heading of any level.
exec git -c core.quotepath=false log --date=short --format='%n== %ad  %an%n   %s' \
  -L "/^### มาตรา ${section}\$/,/^#/:${file}"
