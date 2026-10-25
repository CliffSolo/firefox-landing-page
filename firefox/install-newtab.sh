#!/usr/bin/env bash
# Makes Firefox open the Homepage in every new tab.
# Run with: sudo ~/Projects/Homepage/firefox/install-newtab.sh
# Undo with: sudo ~/Projects/Homepage/firefox/install-newtab.sh --remove
set -e
here="$(cd "$(dirname "$0")" && pwd)"
ff=/usr/lib/firefox
green=$'\e[32m'; yellow=$'\e[33m'; reset=$'\e[0m'

if [[ "$1" == "--remove" ]]; then
  rm -f "$ff/defaults/pref/autoconfig.js" "$ff/mozilla.cfg"
  echo "${green}Removed. New tabs go back to Firefox's normal page after a restart.${reset}"
  exit 0
fi

install -m 644 "$here/autoconfig.js" "$ff/defaults/pref/autoconfig.js"
install -m 644 "$here/mozilla.cfg" "$ff/mozilla.cfg"
echo "${green}Installed. Fully close Firefox and reopen it.${reset}"
echo "${yellow}If a Firefox update ever undoes it, run this script again.${reset}"
