
# Homepage

Offline Firefox start page. Single file (`index.html`), no internet needed to load.

## Layout
- **Left pane:** link buttons by group (Banks, Expenses and Loans). Edit the `LINKS` list at the top of the script in `index.html`.
- **Center:** large 12-hour digital clock, date, and a month calendar (pink, today glows; ◀ ▶ and Today buttons).
- **Right half:** two cyan-outlined boxes, "Bills Due This Month" and "ASAP" (empty for now; later filled from Obsidian lists).

## Theme
All dark. Base `#15171a`, panels `#1e2125`, borders `#2c3036`, text `#e7e9ec`. Accents: cyan `#2de2e6`, calendar pink `#ff3caa`. All colours are at the top of the `<style>` block.

## Firefox
Opens at startup and on the Home button via two lines in `~/.config/mozilla/firefox/e1fxaqv2.default-release/user.js`. Delete them to undo.

New tabs: `sudo firefox/install-newtab.sh` copies `autoconfig.js` and `mozilla.cfg` into `/usr/lib/firefox` (Firefox autoconfig sets the new-tab URL). Undo with `sudo firefox/install-newtab.sh --remove`. Re-run if a Firefox update ever removes it.
