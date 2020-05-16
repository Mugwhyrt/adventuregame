# adventuregame

## Introduction
A text-based adventure game based on a tutorial by Phillip Johnson. I first encountered Phillip Johnson's tutorial prior to returning to school for Computer Science, and I've revisited it towards the end of my school career. Partly as a birthday gift for a friend and partly as coding project that seemed poetically appropriate for the end of school. Phillip Johnson's original source code comprises the core functionality of the game: A basic adventure game where a player navigates a cave with enemies to fight and items to pick up. 

Links to Phillip Johnson's original work:
* [Original Tutorial](https://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/)
* [Original Source Code](https://github.com/phillipjohnson/text-adventure-tut)

## Dependencies
adventuregame requires the following libraries:
* [colorama](https://pypi.org/project/colorama/)

## Development Stage Overiew
### Stage 0

This iteration comprises changes to the game made as part of a birthday gift. It includes (but is not necessarily limited to): 
* new room types (locked doors and shops)
* new room functionality (alternative text based on whether an enemy is alive or items remain)
* new enemy tiles
* new player abilities (healing, search for items)
* bug fixes (left in as additional challenge by Phillip Johnson)
* colored font
* changes to aid in compilation via pyinstaller
* a new map

The new map is based on a [One Page Dungeon](https://www.sageadvice.eu/2016/03/22/need-an-adventure-one-page-dungeon/) submission by Redrobes titled [Three Witches and A Hermit](https://campaignwiki.org/1pdc/2010/ ).

### Stage 1

This is the current iteration. The goal of this iteration is to implement deeper changes to the UI and mechanics such as ability to display a map showing a player the rooms they've visited, and a natural language based UI (as in, user types "go north" to move to the northern tile).

### Stage 2

The goal of this iteration is to improve standard RPG mechanics. First by introducing a more in-depth statistical system including attributes such as strength, intelligence, and luck.
