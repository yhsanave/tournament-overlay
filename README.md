# Tourney Overlay

A simple PyQT6 Based UI for managing stream overlays for tournaments. 

Supports player tags and social links, sponsor tags, set count, round title and games, and commentator tags.

---

## Setup

First, download TourneyOverlay [here](https://github.com/yhsanave/tourney-overlay/releases) or clone the repository (if you don't know what that means, choose the first option).

Save the executable in wherever you want the files to be and run it. It will create a folder called `TourneyOverlay` in the same directory. 

Create a text element in your streaming software for each value you want to use and set it to read from the corresponding file (see below).

---

## Files

All paths are relative to the `TourneyOverlay` folder in the same directory as the executable. Player sponsors and tags are combined for convenience.

| Value | Example | File |
| ----- | ------- | ---- |
| Round | Grand Finals | `/Set/round.txt` |
| Games | Best of 5 | `/Set/games.txt` |
| Commentator 1 | @Yhsanave | `/Commentators/1.txt` |
| Commentator 2 | @Yhsanave | `/Commentators/2.txt` |
| Player 1 Tag | Smoosh \| Yhsanave | `/Player 1/tag.txt` |
| Player 1 Social | @Yhsanave | `/Player 1/social.txt` |
| Player 1 Score | 0 | `/Player 1/score.txt` |
| Player 2 Tag | Smoosh \| Yhsanave | `/Player 2/tag.txt` |
| Player 2 Social | @Yhsanave | `/Player 2/social.txt` |
| Player 2 Score | 0 | `/Player 2/score.txt` |

---

Found an issue or have a suggestion? 

DM me on discord @Yhsanave#2301, on twitter [@Yhsanave](https://twitter.com/Yhsanave), or send me an email at [yhsanave@puff.rest](mailto:yhsanave@puff.rest)
