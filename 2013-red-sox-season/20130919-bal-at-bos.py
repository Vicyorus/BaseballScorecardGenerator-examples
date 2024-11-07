import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2013-09-19
# https://www.baseball-reference.com/boxes/BOS/BOS201309190.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2013/09/19/349022/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-19 19:11-21:29",
        "at": "Fenway Park, Boston, MA",
        "att": "36,436",
        "temp": "69F, Clear",
        "wind": "2mph, In From CF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 30,
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
                30: "Chris Tillman",
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
                40: "Troy Patton",
                66: "T.J. McFarland",
                34: "Scott Feldman",
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
            "bullpen": [50, 40, 66, 34, 60, 57, 29, 39, 56, 25, 39, 17, 43, 52, 16],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                15: "Dustin Pedroia",
                29: "Daniel Nava",
                34: "David Ortiz",
                12: "Mike Napoli",
                37: "Mike Carp",
                39: "Jarrod Saltalamacchia",
                16: "Will Middlebrooks",
                7: "Stephen Drew",
                25: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                26: "Brock Holt",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                35: "Steven Wright",
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
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [15, "4"],
                [29, "9"],
                [34, "0"],
                [12, "3"],
                [37, "7"],
                [39, "2"],
                [16, "5"],
                [7, "6"],
                [25, "8"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [18, "CF"],
                [26, "2B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 67, 56, 60, 32, 66, 44, 31, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Mark Wegner",
            "1B": "Tim Timmons",
            "2B": "Mike Winters",
            "3B": "Laz Diaz",
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
# Pitching: BOS #41 John Lackey
t1 = game.new_inning()

# 1. BAL #9  Nate McLouth (X - X - X)
t1.new_ab()
t1.out("G4-3")

# 2. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("c c b")
t1.out("G6-3")

# 3. BAL #19 Chris Davis (X - X - X)
t1.new_ab()
t1.pitch_list("c s b b f f s")
t1.out("K")


# Bot 1st
# Pitching: BAL #30 Chris Tillman
b1 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f f")
b1.hit(2)
b1.advance(3, "29 G1-6-3")

# 2. BOS #29 Daniel Nava (X - 15 - X)
b1.new_ab(is_risp=True)
b1.out("G1-6-3")

# 3. BOS #34 David Ortiz (15 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b f f f b f b")
b1.reach("BB")

# 4. BOS #12 Mike Napoli (15 - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b c s f f s")
b1.out("K")

# 5. BOS #37 Mike Carp (15 - X - 34)
b1.new_ab(is_risp=True)
b1.pitch_list("b c b f")
b1.out("L7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t2.new_ab()
t2.pitch_list("f f f t")
t2.out("KT")

# 5. BAL #21 Nick Markakis (X - X - X)
t2.new_ab()
t2.pitch_list("c c b f f s")
t2.out("K")

# 6. BAL #35 Danny Valencia (X - X - X)
t2.new_ab()
t2.pitch_list("c s")
t2.out("F9")


# Bot 2nd
# Pitching: BAL #30 Chris Tillman
b2 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(2)
b2.advance(4, "7 HR")

# 7. BOS #16 Will Middlebrooks (X - 39 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c t c")
b2.out("!K")

# 8. BOS #7  Stephen Drew (X - 39 - X)
b2.new_ab(is_risp=True)
b2.hit(4, rbis=2)

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(2)
b2.advance(4, "15 1B")

# 1. BOS #15 Dustin Pedroia (X - 25 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b b")
b2.hit(1, rbis=1)
b2.advance(2, "T")

# 2. BOS #29 Daniel Nava (X - 15 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b b b b")
b2.reach("BB")

# 3. BOS #34 David Ortiz (X - 15 - 29)
b2.new_ab(is_risp=True)
b2.pitch_list("c b s t")
b2.out("KT")

# 4. BOS #12 Mike Napoli (X - 15 - 29)
b2.new_ab(is_risp=True)
b2.pitch_list("c c b b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 7. BAL #32 Matt Wieters (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b f c")
t3.out("!K")

# 8. BAL #2  J.J. Hardy (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F7")

# 9. BAL #1  Brian Roberts (X - X - X)
t3.new_ab()
t3.pitch_list("b c c b b b")
t3.reach("BB")

# 1. BAL #9  Nate McLouth (X - X - 1)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BAL #30 Chris Tillman
b3 = game.new_inning()

# 5. BOS #37 Mike Carp (X - X - X)
b3.new_ab()
b3.pitch_list("b f b f f b")
b3.out("L9")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b3.new_ab()
b3.pitch_list("b c s s")
b3.out("K")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
t4.new_ab()
t4.pitch_list("s")
t4.out("G6-3")

# 3. BAL #19 Chris Davis (X - X - X)
t4.new_ab()
t4.out("G4-3")

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("b s f")
t4.out("F9")


# Bot 4th
# Pitching: BAL #30 Chris Tillman
b4 = game.new_inning()

# 8. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f c")
b4.out("!K")

# 9. BOS #25 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("c c")
b4.hit(1)

# 1. BOS #15 Dustin Pedroia (X - X - 25)
b4.new_ab()
b4.pitch_list("1 c f f")
b4.out("F8")

# 2. BOS #29 Daniel Nava (X - X - 25)
b4.new_ab()
b4.pitch_list("c b 1 s")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 5. BAL #21 Nick Markakis (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("F8")

# 6. BAL #35 Danny Valencia (X - X - X)
t5.new_ab()
t5.pitch_list("s f b b b s")
t5.out("K")

# 7. BAL #32 Matt Wieters (X - X - X)
t5.new_ab()
t5.pitch_list("f b f f")
t5.out("G1-3")


# Bot 5th
# Pitching: BAL #30 Chris Tillman
b5 = game.new_inning()

# 3. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("b b b")
b5.out("F8")

# 4. BOS #12 Mike Napoli (X - X - X)
b5.new_ab()
b5.pitch_list("s c")
b5.out("F9")

# 5. BOS #37 Mike Carp (X - X - X)
b5.new_ab()
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 8. BAL #2  J.J. Hardy (X - X - X)
t6.new_ab()
t6.pitch_list("f f s")
t6.out("K")

# 9. BAL #1  Brian Roberts (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G3")

# 1. BAL #9  Nate McLouth (X - X - X)
t6.new_ab()
t6.pitch_list("c b b b b")
t6.reach("BB")

# 2. BAL #13 Manny Machado (X - X - 9)
t6.new_ab()
t6.pitch_list("f b")
t6.out("F9")


# Bot 6th
# Pitching: BAL #30 Chris Tillman
b6 = game.new_inning()

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("L6")

# 8. BOS #7  Stephen Drew (X - X - X)
b6.new_ab()
b6.hit(3)

# 9. BOS #25 Jackie Bradley Jr. (7 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c s f f b t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 3. BAL #19 Chris Davis (X - X - X)
t7.new_ab()
t7.pitch_list("f b c")
t7.out("G5-3")

# 4. BAL #10 Adam Jones (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.hit(4)

# 5. BAL #21 Nick Markakis (X - X - X)
t7.new_ab()
t7.pitch_list("b c s s")
t7.out("K")

# 6. BAL #35 Danny Valencia (X - X - X)
t7.new_ab()
t7.pitch_list("c f b")
t7.out("G6-3")


# Bot 7th
# Pitching: BAL #30 Chris Tillman
b7 = game.new_inning()

# 1. BOS #15 Dustin Pedroia (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G5-3")

# 2. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b b c s")
b7.out("K")

# 3. BOS #34 David Ortiz (X - X - X)
b7.new_ab()
b7.out("L5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #41 John Lackey
t8 = game.new_inning()

# 7. BAL #32 Matt Wieters (X - X - X)
t8.new_ab()
t8.out("F9")

# 8. BAL #2  J.J. Hardy (X - X - X)
t8.new_ab()
t8.pitch_list("b c s")
t8.hit(1)

# 9. BAL #1  Brian Roberts (X - X - 2)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")

# 1. BAL #9  Nate McLouth (X - X - 2)
t8.new_ab()
t8.pitch_list("c")
t8.out("G4-3")


# Bot 8th
# Pitching: BAL #56 Darren O'Day
b8 = game.new_inning()

# Pitching change (BAL): #56 Darren O'Day replaces #30 Chris Tillman
b8.pitching_substitution(56)

# 4. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.out("G5-3")

# Pitching change (BAL): #17 Brian Matusz replaces #56 Darren O'Day
b8.pitching_substitution(17)

# Offensive change (BOS): Pinch-hitter #5 Jonny Gomes replaces #37 Mike Carp, batting 5th
b8.offensive_substitution(5, 5, "PH")

# 5. BOS #5  Jonny Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("b s c s")
b8.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
b8.new_ab()
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #41 John Lackey
t9 = game.new_inning()

# Defensive switch (BOS): #5 Jonny Gomes moves to LF
t9.defensive_switch(5, "7")

# 2. BAL #13 Manny Machado (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("(F)P3")

# 3. BAL #19 Chris Davis (X - X - X)
t9.new_ab()
t9.pitch_list("f f b f f s")
t9.out("K")

# 4. BAL #10 Adam Jones (X - X - X)
t9.new_ab()
t9.pitch_list("f b s b")
t9.out("F9")

# Winning team: BOS
# WP: BOS #41 John Lackey
game.winning_pitcher(41)

# Loser team: BAL
# LP: BAL #30 Chris Tillman
game.losing_pitcher(30, is_away_team=True)

# print(game)
game.generate_scorecard()
