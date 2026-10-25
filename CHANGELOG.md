
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
