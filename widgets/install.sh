#!/bin/bash
# Installs the handler behind the Landing Page's "Start desktop widgets" button (no sudo needed):
# the script goes in ~/.local/bin and desktopwidgets:// links are set to open it.
set -e
here="$(cd "$(dirname "$0")" && pwd)"
install -Dm755 "$here/start-desktop-widgets" "$HOME/.local/bin/start-desktop-widgets"
install -Dm644 "$here/start-desktop-widgets.desktop" "$HOME/.local/share/applications/start-desktop-widgets.desktop"
update-desktop-database "$HOME/.local/share/applications" 2>/dev/null || true
xdg-mime default start-desktop-widgets.desktop x-scheme-handler/desktopwidgets
echo "Installed. desktopwidgets:// now opens: $(xdg-mime query default x-scheme-handler/desktopwidgets)"
