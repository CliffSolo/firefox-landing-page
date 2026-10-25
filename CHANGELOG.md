
# Changelog

## 2026-10-25
- First prototype: left pane of link buttons (Banks: SoFi, Fidelity, Bank of America, DCU, USAA, Venmo; Expenses and Loans: Navient Loans), centered 12-hour digital clock with date, month calendar (Sunday start, pink, glowing border on today, prev/next/Today), right half with two empty cyan-outlined boxes (Bills Due This Month, ASAP).
- All-dark theme based on the first screenshot in `ScrapYard/04 - Dev/Homepage/Theme Examples.md`; cyan + pink accents from the Omarchy/Tokyo Night examples.
- Replaced the earlier draft (search box, editable bookmarks, backup/restore).
- Moved from `~/Homepage` to `~/Projects/Homepage`; Firefox startup page updated in `user.js`.
- Link buttons now open in a new tab.
- Added "Misc Sites" favorites section (5 slots: 1–4 empty, 5 = GitHub).
- Added "Last Visited" section: last 5 buttons clicked on the homepage, newest first (saved in Firefox local storage).
- Added a daily inspirational quote and a psychology/behavior tip between the clock and the calendar (20 of each, built in; changes each day).
- Made the right pane (Bills Due This Month, ASAP) much thinner, the same width as the left pane, so the clock, quote and calendar sit in the center of the page.
- Bank buttons now have a blue (`#7aa2f7`) glowing outline, styled like today's date on the calendar.
- All link buttons (Expenses and Loans, Misc Sites, Last Visited too) now get the same blue glowing outline.
- Larger quote and tip text (quote 16→21px, author 13→15px, tip 14→18px, label 11→13px); text area widened to 580px.
- More space above the clock (top padding 4vh→7vh) and one extra blank line between the date and the quote.
- Click any calendar date to open an "Add to Google Calendar" dialog (Event or Task, title, all day or start/end time, notes). It opens Google Calendar's new-event page in a new tab, pre-filled; you press Save there. Tasks are added as all-day events titled "Task: …".
- Calendar dates can no longer be text-selected (clicking/double-clicking a date was highlighting the number).
- Added `firefox/` folder: `autoconfig.js` + `mozilla.cfg` + `install-newtab.sh` to make every new tab open the Homepage (Firefox autoconfig; needs sudo to install into /usr/lib/firefox, `--remove` to undo).
- More horizontal space: gap between the panes 20→56px, page side padding 20→36px.
- Even more: gap between the panes 56→96px, page side padding 36→60px.
- Added bank buttons: Credit One (creditonebank.com, sign-in on home page) and Target Circle Card (target.com/mycirclecard).
- Added weather under the date (Open-Meteo, no account/key): icon, temp, conditions, feels-like, high/low, rain chance. Refreshes every 30 min; shows the last reading marked "offline" when there's no internet. Location set in `WEATHER` at the top of the weather code.
- Added bank button: Concora Credit (Milestone) → mymilestonecard.com.
- Fit everything on one screen again: calendar day cells 40px tall (were square), top padding 7vh→6vh; left pane scrollbar thin and dark instead of white.
