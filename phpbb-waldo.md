---
title: phpBB Where's Waldo MOD
layout: mod
topic-url: http://www.phpbb.com/community/viewtopic.php?f=70&t=2092309
repo-name: phpBB-waldo
demo-url: http://phpbb.dellsystem.me/waldo/
versions:
- {number: 0.0.1, status: ALPHA, notes: First release}
- {number: 0.0.2, status: ALPHA, notes: "Fixing up code to better adhere to standards, some new config settings"}
- {number: 0.0.3, status: ALPHA, notes: "Some small bug fixes (maintenance release)"}
- {number: 0.0.4, status: ALPHA, notes: "More bugfixes from last release, fixed UTF problem in mouseover text"}
- {number: 0.0.5, status: ALPHA, notes: "Another maintenance release - removed reference to unnecessary variable"}
abandoned: false
screenshots:
- https://github.com/dellsystem/phpBB-waldo/raw/0.1.0-dev/contrib/screenshot-index.png
- https://github.com/dellsystem/phpBB-waldo/raw/0.1.0-dev/contrib/screenshot-profile.png
- https://github.com/dellsystem/phpBB-waldo/raw/0.1.0-dev/contrib/screenshot-ucp.png
requests-open: true
---

A small image of Waldo \[US\] / Wally \[UK\] may appear somewhere on every page as you browse the board. Inspired by Xore's 2.x MOD CamelMOD.

**Features:**

*   The probability of finding Waldo on any page is adjustable through the ACP
*   If you have the Ultimate Points MOD installed, you can set the number of points that will be awarded to a user that finds Waldo
*   You can set it so that clicking on the image of Waldo will lead you to another page (either within your domain or off-site)
*	Mouseover text and the URL to the image of Waldo are both adjustable through the ACP
*	Waldo can appear anywhere in the visible part of the window

**Planned features:**

*	The ability to select specific pages only where Waldo will appear (in conjunction with the random feature)\
*	ACP permissions
*	Enable/disable for guests (or groups)
*	Users can be choose between having points awarded upon seeing Waldo and have them awarded upon clicking him and being directed to a specific page (with user-configurable text)
*	Ability to upload the new Waldo image via the ACP
*	Ability to set a cap on the maximum amount of points a user can earn in a specific time period
