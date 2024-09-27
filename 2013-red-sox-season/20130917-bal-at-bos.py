import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-09-17
# https://www.baseball-reference.com/boxes/BOS/BOS201309170.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/09/17/348994/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-17 19:12-22:20",
        "at": "Fenway Park, Boston, MA",
        "att": "35,030",
        "temp": "59F, Partly Cloudy",
        "wind": "5mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 34,
            "roster": {
                # Lineup
                9: "Nate McLouth",
                13: "Manny Machado",
                19: "Chris Davis",
                10: "Adam Jones",
                21: "Nick Markakis",
                35: "Danny Valencia",
                32: "Matt Wieters",
                2: "J.J. Hardy",
                1: "Brian Roberts",
                # Starting pitcher
                34: "Scott Feldman",
                # Bench
                28: "Steve Pearce",
                3: "Ryan Flaherty",
                36: "Chris Dickerson",
                6: "Jonathan Schoop",
                48: "Chris Snyder",
                38: "Michael Morse",
                51: "Henry Urrutia",
                45: "Steve Clevenger",
                55: "Dan Johnson",
                12: "Alexi Casilla",
                # Bullpen
                50: "Miguel González",
                30: "Chris Tillman",
                40: "Troy Patton",
                66: "T.J. McFarland",
                60: "Josh Stinson",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                39: "Kevin Gausman",
                56: "Darren O'Day",
                25: "Bud Norris",
                39: "Jason Hammel",
                17: "Brian Matusz",
                43: "Jim Johnson",
                52: "Steve Johnson",
                16: "Wei-Yin Chen",
            },
            "lefties": [40, 66, 17, 16],
            "lineup": [
                [9, "7"],
                [13, "5"],
                [19, "3"],
                [10, "8"],
                [21, "9"],
                [35, "0"],
                [32, "2"],
                [2, "6"],
                [1, "4"],
            ],
            "bench": [
                [28, "1B"],
                [3, "2B"],
                [36, "LF"],
                [6, "2B"],
                [48, "C"],
                [38, "LF"],
                [51, "OF"],
                [45, "C"],
                [55, "1B"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 60, 57, 29, 39, 56, 25, 39, 17, 43, 52, 16],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                18: "Shane Victorino",
                34: "David Ortiz",
                12: "Mike Napoli",
                29: "Daniel Nava",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                72: "Xander Bogaerts",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                16: "Will Middlebrooks",
                26: "Brock Holt",
                5: "Jonny Gomes",
                3: "David Ross",
                25: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [15, "4"],
                [18, "8"],
                [34, "0"],
                [12, "3"],
                [29, "9"],
                [37, "7"],
                [39, "2"],
                [7, "6"],
                [72, "5"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [16, "3B"],
                [26, "2B"],
                [5, "LF"],
                [3, "C"],
                [25, "CF"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 31, 36, 11, 64, 19, 38, 62, 22],
        },
        "umpires": {
            "HP": "Mike Winters",
            "1B": "Laz Diaz",
            "2B": "Mark Wegner",
            "3B": "Tim Timmons",
        },
    },
)

##########################################################
# PLAY BALL!
##########################################################


##########################################################
# 1st Inning
##########################################################
# Top 1st
# Pitching: BOS #46 Ryan Dempster
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)

# 3. BAL #19 Chris Davis (X - X - 13)
t1.new_ab()
t1.pitch_list("c d s f s")
t1.out("K")

# 4. BAL #10 Adam Jones (X - X - 13)
t1.new_ab()
t1.pitch_list("1 f b s 1 t")
t1.out("KT")


# Bot 1st
# Pitching: BAL #34 Scott Feldman
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b")
b1.hit(4)

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b f f b")
b1.reach("BB")
b1.thrown_out(2, "34 DP4-6-3", 1, 34)

# 3. BOS #34 David Ortiz (X - X - 18)
b1.new_ab()
b1.pitch_list("f 1 1 b")
b1.out("DP4-6-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. BAL #21 Nick Markakis (X - X - X)
t2.new_ab()
t2.pitch_list("c b c f f f b c")
t2.out("!K")

# 6. BAL #35 Danny Valencia (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b b f b b")
t2.reach("BB")
t2.advance(2, "32 G4-3")

# 7. BAL #32 Matt Wieters (X - X - 35)
t2.new_ab()
t2.pitch_list("f b b s")
t2.out("G4-3")

# 8. BAL #2  J.J. Hardy (X - 35 - X)
t2.new_ab()
t2.out("G6-3")


# Bot 2nd
# Pitching: BAL #34 Scott Feldman
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b c c b c")
b2.out("!K")

# 6. BOS #37 Mike Carp (X - X - X)
b2.new_ab()
b2.hit(2)
b2.advance(3, "39 G3-1")

# 7. BOS #39 Jarrod Saltalamacchia (X - 37 - X)
b2.new_ab()
b2.pitch_list("b c")
b2.out("G3-1")

# 8. BOS #7  Stephen Drew (37 - X - X)
b2.new_ab()
b2.pitch_list("b b b c c b")
b2.reach("BB")
b2.advance(2, "72 SB")

# 9. BOS #72 Xander Bogaerts (37 - X - 7)
b2.new_ab()
b2.pitch_list("b b c b 3 c f b")
b2.reach("BB")

# 1. BOS #15 Dustin Pedroia (37 - 7 - 72)
b2.new_ab()
b2.pitch_list("c")
b2.out("L4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 9. BAL #1  Brian Roberts (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f f")
t3.out("F8")

# 1. BAL #9  Nate McLouth (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("F9")

# 2. BAL #13 Manny Machado (X - X - X)
t3.new_ab()
t3.out("P6")


# Bot 3rd
# Pitching: BAL #34 Scott Feldman
b3 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b f c")
b3.out("!K")

# 3. BOS #34 David Ortiz (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G5-3")

# 4. BOS #12 Mike Napoli (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f d f b b")
b3.reach("BB")

# 5. BOS #29 Daniel Nava (X - X - 12)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("f b f s")
t4.out("K")

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("b f s b b s")
t4.out("K")

# 5. BAL #21 Nick Markakis (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G4-3")


# Bot 4th
# Pitching: BAL #34 Scott Feldman
b4 = game.new_inning()

# 6. BOS #37 Mike Carp (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F8")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b4.new_ab()
b4.pitch_list("b f b b")
b4.error(5)
b4.reach("E5")
b4.advance(2, "7 BB")
b4.advance(3, "72 SB")
b4.advance("U", "72 SF7")

# 8. BOS #7  Stephen Drew (X - X - 39)
b4.new_ab()
b4.pitch_list("b b b c f b")
b4.reach("BB")
b4.advance(2, "72 SB")
b4.advance(3, "72 SF7")

# 9. BOS #72 Xander Bogaerts (X - 39 - 7)
b4.new_ab()
b4.pitch_list("s f f")
b4.error(7)
b4.reach("SF7", rbis=1)
b4.thrown_out(2, "15 DP5-4-3", 2, 34)

# 1. BOS #15 Dustin Pedroia (7 - X - 72)
b4.new_ab()
b4.pitch_list("1 d f b f f f 1")
b4.out("DP5-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 6. BAL #35 Danny Valencia (X - X - X)
t5.new_ab()
t5.pitch_list("b c b b f b")
t5.reach("BB")
t5.advance(3, "2 2B")
t5.advance(4, "1 G5-3")

# 7. BAL #32 Matt Wieters (X - X - 35)
t5.new_ab()
t5.pitch_list("s")
t5.out("L4")

# 8. BAL #2  J.J. Hardy (X - X - 35)
t5.new_ab()
t5.pitch_list("b c c")
t5.hit(2)

# 9. BAL #1  Brian Roberts (35 - 2 - X)
t5.new_ab()
t5.pitch_list("c c f")
t5.out("G5-3", rbis=1)

# 1. BAL #9  Nate McLouth (X - 2 - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")

# 2. BAL #13 Manny Machado (X - 2 - 9)
t5.new_ab()
t5.pitch_list("b")
t5.out("P6")


# Bot 5th
# Pitching: BAL #34 Scott Feldman
b5 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.out("G5-3")

# 3. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("f b b f c")
b5.out("!K")

# 4. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b b b")
b5.reach("BB")

# 5. BOS #29 Daniel Nava (X - X - 12)
b5.new_ab()
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("s b b")
t6.hit(4)

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("b s b t b f f b")
t6.reach("BB")
t6.thrown_out(2, "35 DP6-4-3", 2, 46)

# 5. BAL #21 Nick Markakis (X - X - 10)
t6.new_ab()
t6.pitch_list("b f b")
t6.out("L8")

# 6. BAL #35 Danny Valencia (X - X - 10)
t6.new_ab()
t6.pitch_list("c b c 1")
t6.out("DP6-4-3")


# Bot 6th
# Pitching: BAL #66 T.J. McFarland
b6 = game.new_inning()

# Pitching change (BAL): #66 T.J. McFarland replaces #34 Scott Feldman
b6.pitching_substitution(66)

# 6. BOS #37 Mike Carp (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.out("G4-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f s")
b6.out("K")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.pitch_list("c c b b d f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #67 Brandon Workman
t7 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #46 Ryan Dempster
t7.pitching_substitution(67)

# 7. BAL #32 Matt Wieters (X - X - X)
t7.new_ab()
t7.pitch_list("c c f b f b f b f s")
t7.out("K")

# 8. BAL #2  J.J. Hardy (X - X - X)
t7.new_ab()
t7.pitch_list("b b b")
t7.out("F9")

# 9. BAL #1  Brian Roberts (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b")
t7.out("G6-3")


# Bot 7th
# Pitching: BAL #39 Kevin Gausman
b7 = game.new_inning()

# Pitching change (BAL): #39 Kevin Gausman replaces #66 T.J. McFarland
b7.pitching_substitution(39)

# 9. BOS #72 Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G1-3")

# 1. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c c f b")
b7.error(5)
b7.reach("E5")
b7.thrown_out(2, "18 DP5-4-3", 2, 39)

# 2. BOS #18 Shane Victorino (X - X - 15)
b7.new_ab()
b7.pitch_list("b 1 f")
b7.out("DP5-4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #67 Brandon Workman
t8 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b")
t8.hit(1)
t8.advance(3, "13 2B")

# 2. BAL #13 Manny Machado (X - X - 9)
t8.new_ab()
t8.pitch_list("1")
t8.hit(2)

# Pitching change (BOS): #32 Craig Breslow replaces #67 Brandon Workman
t8.pitching_substitution(32)

# 3. BAL #19 Chris Davis (9 - 13 - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")

# 4. BAL #10 Adam Jones (9 - 13 - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")

# 5. BAL #21 Nick Markakis (9 - 13 - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F7")


# Bot 8th
# Pitching: BAL #17 Brian Matusz
b8 = game.new_inning()

# Pitching change (BAL): #17 Brian Matusz replaces #39 Kevin Gausman
b8.pitching_substitution(17)

# 3. BOS #34 David Ortiz (X - X - X)
b8.new_ab()
b8.pitch_list("s b b c b f s")
b8.out("K")

# Pitching change (BAL): #29 Tommy Hunter replaces #17 Brian Matusz
b8.pitching_substitution(29)

# 4. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b s s f f b f")
b8.out("G6-3")

# 5. BOS #29 Daniel Nava (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #19 Koji Uehara
t9 = game.new_inning()

# Pitching change (BOS): #19 Koji Uehara replaces #32 Craig Breslow
t9.pitching_substitution(19)

# 6. BAL #35 Danny Valencia (X - X - X)
t9.new_ab()
t9.pitch_list("f f")
t9.hit(3)
# Offensive change (BAL): Pinch-runner #12 Alexi Casilla replaces #35 Danny Valencia
t9.offensive_substitution(6, 12, "PR")
t9.atbase("PR")
t9.advance(4, "32 SF9")

# 7. BAL #32 Matt Wieters (35 - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("SF9", rbis=1)

# 8. BAL #2  J.J. Hardy (X - X - X)
t9.new_ab()
t9.pitch_list("b c c")
t9.out("G6-3")

# 9. BAL #1  Brian Roberts (X - X - X)
t9.new_ab()
t9.pitch_list("f s s")
t9.out("K")


# Bot 9th
# Pitching: BAL #43 Jim Johnson
b9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #29 Tommy Hunter
b9.pitching_substitution(43)

# Defensive switch (BAL): #12 Alexi Casilla moves to DH
b9.defensive_switch(12, "0")

# 6. BOS #37 Mike Carp (X - X - X)
b9.new_ab()
b9.pitch_list("c b s")
b9.out("G5-3")

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b9.new_ab()
b9.pitch_list("f b")
b9.hit(1)
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #39 Jarrod Saltalamacchia
b9.offensive_substitution(7, 50, "PR")
b9.atbase("PR")
b9.advance(2, "7 G1-3")

# 8. BOS #7  Stephen Drew (X - X - 39)
b9.new_ab()
b9.pitch_list("f b b b")
b9.out("G1-3")

# 9. BOS #72 Xander Bogaerts (X - 50 - X)
b9.new_ab()
b9.pitch_list("b c s s")
b9.out("K")

# Winning team: BAL
# WP: BAL #29 Tommy Hunter
game.winning_pitcher(29, is_away_team=True)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43, is_away_team=True)

# Loser team: BOS
# LP: BOS #19 Koji Uehara
game.losing_pitcher(19)

# print(game)
game.generate_scorecard()
