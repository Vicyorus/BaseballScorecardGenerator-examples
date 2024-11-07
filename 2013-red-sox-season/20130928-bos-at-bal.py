import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2013-09-28
# https://www.baseball-reference.com/boxes/BAL/BAL201309280.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2013/09/28/349145/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-28 19:06-22:27",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "36,556",
        "temp": "70F, Partly Cloudy",
        "wind": "4mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                7: "Stephen Drew",
                15: "Dustin Pedroia",
                12: "Mike Napoli",
                5: "Jonny Gomes",
                29: "Daniel Nava",
                23: "Brandon Snyder",
                3: "David Ross",
                16: "Will Middlebrooks",
                # Starting pitcher
                31: "Jon Lester",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                34: "David Ortiz",
                26: "Brock Holt",
                72: "Xander Bogaerts",
                25: "Jackie Bradley Jr.",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                # Bullpen
                35: "Steven Wright",
                41: "John Lackey",
                67: "Brandon Workman",
                56: "Franklin Morales",
                60: "Brayan Villarreal",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                64: "Allen Webster",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [31, 56, 32, 66, 38, 22],
            "lineup": [
                [18, "8"],
                [7, "6"],
                [15, "4"],
                [12, "0"],
                [5, "7"],
                [29, "9"],
                [23, "3"],
                [3, "2"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [39, "C"],
                [37, "1B"],
                [34, "DH"],
                [26, "2B"],
                [72, "2B"],
                [25, "CF"],
                [20, "C"],
                [10, "SS"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 44, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 16,
            "roster": {
                # Lineup
                1: "Brian Roberts",
                2: "J.J. Hardy",
                19: "Chris Davis",
                10: "Adam Jones",
                32: "Matt Wieters",
                35: "Danny Valencia",
                21: "Nick Markakis",
                28: "Steve Pearce",
                24: "Jason Pridie",
                # Starting pitcher
                16: "Wei-Yin Chen",
                # Bench
                3: "Ryan Flaherty",
                36: "Chris Dickerson",
                6: "Jonathan Schoop",
                9: "Nate McLouth",
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
                34: "Scott Feldman",
                60: "Josh Stinson",
                57: "Francisco Rodríguez",
                29: "Tommy Hunter",
                39: "Kevin Gausman",
                56: "Darren O'Day",
                25: "Bud Norris",
                53: "Zack Britton",
                39: "Jason Hammel",
                17: "Brian Matusz",
                43: "Jim Johnson",
                52: "Steve Johnson",
                65: "Mike Belfiore",
            },
            "lefties": [16, 40, 66, 53, 17, 65],
            "lineup": [
                [1, "4"],
                [2, "6"],
                [19, "3"],
                [10, "8"],
                [32, "2"],
                [35, "5"],
                [21, "9"],
                [28, "0"],
                [24, "7"],
            ],
            "bench": [
                [3, "2B"],
                [36, "LF"],
                [6, "2B"],
                [9, "CF"],
                [48, "C"],
                [38, "LF"],
                [51, "OF"],
                [45, "C"],
                [55, "1B"],
                [12, "2B"],
            ],
            "bullpen": [50, 30, 40, 66, 34, 60, 57, 29, 39, 56, 25, 53, 39, 17, 43, 52, 65],
        },
        "umpires": {
            "HP": "Bill Welke",
            "1B": "Brian O'Nora",
            "2B": "Fieldin Culbreth",
            "3B": "Adrian Johnson",
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
# Pitching: BAL #16 Wei-Yin Chen
t1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b s b c s")
t1.out("K")

# 2. BOS #7  Stephen Drew (X - X - X)
t1.new_ab()
t1.pitch_list("b s f b")
t1.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t1.new_ab()
t1.pitch_list("b b f")
t1.hit(1)
t1.advance(2, "12 BB")

# 4. BOS #12 Mike Napoli (X - X - 15)
t1.new_ab()
t1.pitch_list("b f s f d f d f b")
t1.reach("BB")

# 5. BOS #5  Jonny Gomes (X - 15 - 12)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.out("P4")


# Bot 1st
# Pitching: BOS #31 Jon Lester
b1 = game.new_inning()

# 1. BAL #1  Brian Roberts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b f")
b1.out("P3")

# 2. BAL #2  J.J. Hardy (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b b b f f")
b1.hit(1)

# 3. BAL #19 Chris Davis (X - X - 2)
b1.new_ab()
b1.out("P6")

# 4. BAL #10 Adam Jones (X - X - 2)
b1.new_ab()
b1.pitch_list("s f f f b b b f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #16 Wei-Yin Chen
t2 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)

# 7. BOS #23 Brandon Snyder (X - X - 29)
t2.new_ab()
t2.pitch_list("b b")
t2.out("F9")

# 8. BOS #3  David Ross (X - X - 29)
t2.new_ab()
t2.pitch_list("f 1 f s")
t2.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - 29)
t2.new_ab()
t2.pitch_list("c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #31 Jon Lester
b2 = game.new_inning()

# 5. BAL #32 Matt Wieters (X - X - X)
b2.new_ab()
b2.out("G5-3")

# 6. BAL #35 Danny Valencia (X - X - X)
b2.new_ab()
b2.pitch_list("c b c s")
b2.out("K")

# 7. BAL #21 Nick Markakis (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(4, "28 2B")

# 8. BAL #28 Steve Pearce (X - X - 21)
b2.new_ab()
b2.pitch_list("f")
b2.hit(2, rbis=1)
b2.advance(3, "24 PB")

# 9. BAL #24 Jason Pridie (X - 28 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c s f s")
b2.pb()
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #16 Wei-Yin Chen
t3 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("P4")

# 2. BOS #7  Stephen Drew (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c")
t3.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("b f f")
t3.out("P4")


# Bot 3rd
# Pitching: BOS #31 Jon Lester
b3 = game.new_inning()

# 1. BAL #1  Brian Roberts (X - X - X)
b3.new_ab()
b3.hit(4)

# 2. BAL #2  J.J. Hardy (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("L7")

# 3. BAL #19 Chris Davis (X - X - X)
b3.new_ab()
b3.pitch_list("c t f b b b b")
b3.reach("BB")
b3.thrown_out(2, "10 FC5-4", 2, 31)

# 4. BAL #10 Adam Jones (X - X - 19)
b3.new_ab()
b3.reach("FC5-4")
b3.advance(2, "32 BB")

# 5. BAL #32 Matt Wieters (X - X - 10)
b3.new_ab()
b3.pitch_list("b b b c c b")
b3.reach("BB")

# 6. BAL #35 Danny Valencia (X - 10 - 32)
b3.new_ab(is_risp=True)
b3.pitch_list("s b s b b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #16 Wei-Yin Chen
t4 = game.new_inning()

# 4. BOS #12 Mike Napoli (X - X - X)
t4.new_ab()
t4.pitch_list("c b s b f")
t4.out("G3")

# 5. BOS #5  Jonny Gomes (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "29 1B")
t4.advance(4, "3 1B")

# 6. BOS #29 Daniel Nava (X - X - 5)
t4.new_ab()
t4.pitch_list("c c b f d f")
t4.hit(1)
t4.advance(3, "3 1B")

# 7. BOS #23 Brandon Snyder (X - 5 - 29)
t4.new_ab(is_risp=True)
t4.pitch_list("c s s")
t4.out("K")

# 8. BOS #3  David Ross (X - 5 - 29)
t4.new_ab(is_risp=True)
t4.pitch_list("t s f d")
t4.hit(1, rbis=1)

# 9. BOS #16 Will Middlebrooks (29 - X - 3)
t4.new_ab(is_risp=True)
t4.out("F8")


# Bot 4th
# Pitching: BOS #31 Jon Lester
b4 = game.new_inning()

# 7. BAL #21 Nick Markakis (X - X - X)
b4.new_ab()
b4.pitch_list("b f b")
b4.hit(1)
b4.thrown_out(2, "1 FC6-4", 3, 31)

# 8. BAL #28 Steve Pearce (X - X - 21)
b4.new_ab()
b4.pitch_list("d f c")
b4.out("F7")

# 9. BAL #24 Jason Pridie (X - X - 21)
b4.new_ab()
b4.pitch_list("f f b")
b4.out("F7")

# 1. BAL #1  Brian Roberts (X - X - 21)
b4.new_ab()
b4.pitch_list("c d b d")
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #16 Wei-Yin Chen
t5 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("L8")

# 2. BOS #7  Stephen Drew (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(2)
t5.advance(4, "15 1B")

# 3. BOS #15 Dustin Pedroia (X - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b f")
t5.hit(1, rbis=1)
t5.advance(2, "T")

# 4. BOS #12 Mike Napoli (X - 15 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b s s f c")
t5.out("!K")

# 5. BOS #5  Jonny Gomes (X - 15 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.out("F8")


# Bot 5th
# Pitching: BOS #31 Jon Lester
b5 = game.new_inning()

# 2. BAL #2  J.J. Hardy (X - X - X)
b5.new_ab()
b5.hit(1)
b5.advance(2, "10 1B")
b5.advance(4, "32 1B")

# 3. BAL #19 Chris Davis (X - X - 2)
b5.new_ab()
b5.pitch_list("c b s s")
b5.out("K")

# 4. BAL #10 Adam Jones (X - X - 2)
b5.new_ab()
b5.hit(1)
b5.advance(3, "32 1B")
b5.advance(4, "35 1B")

# 5. BAL #32 Matt Wieters (X - 2 - 10)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.hit(1, rbis=1)
b5.advance(2, "35 1B")

# 6. BAL #35 Danny Valencia (10 - X - 32)
b5.new_ab(is_risp=True)
b5.pitch_list("c s")
b5.hit(1, rbis=1)
b5.thrown_out(2, "21 DP6-3", 2, 31)

# 7. BAL #21 Nick Markakis (X - 32 - 35)
b5.new_ab(is_risp=True)
b5.pitch_list("c b c b f")
b5.out("DP6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #16 Wei-Yin Chen
t6 = game.new_inning()

# 6. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.advance(4, "3 2B")

# 7. BOS #23 Brandon Snyder (X - X - 29)
t6.new_ab()
t6.pitch_list("f f f s")
t6.out("K")

# 8. BOS #3  David Ross (X - X - 29)
t6.new_ab()
t6.hit(2, rbis=1)

# Pitching change (BAL): #60 Josh Stinson replaces #16 Wei-Yin Chen
t6.pitching_substitution(60)

# 9. BOS #16 Will Middlebrooks (X - 3 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c s f s")
t6.out("K")

# 1. BOS #18 Shane Victorino (X - 3 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.out("G3-1")


# Bot 6th
# Pitching: BOS #38 Matt Thornton
b6 = game.new_inning()

# Pitching change (BOS): #38 Matt Thornton replaces #31 Jon Lester
b6.pitching_substitution(38)

# 8. BAL #28 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("f b c f")
b6.out("P6")

# 9. BAL #24 Jason Pridie (X - X - X)
b6.new_ab()
b6.pitch_list("c s b f c")
b6.out("!K")

# 1. BAL #1  Brian Roberts (X - X - X)
b6.new_ab()
b6.pitch_list("b f c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #60 Josh Stinson
t7 = game.new_inning()

# 2. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("c f b")
t7.hit(1)
t7.advance(2, "15 1B")
t7.advance(4, "5 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 7)
t7.new_ab()
t7.pitch_list("c d f b")
t7.hit(1)
t7.advance(2, "5 1B")
t7.error(7)
t7.advance(3, "29 1B")
t7.advance("U", "29 E7")

# 4. BOS #12 Mike Napoli (X - 7 - 15)
t7.new_ab(is_risp=True)
t7.pitch_list("f s")
t7.out("P4")

# 5. BOS #5  Jonny Gomes (X - 7 - 15)
t7.new_ab(is_risp=True)
t7.pitch_list("s")
t7.hit(1, rbis=1)
t7.advance(2, "29 E7")
t7.thrown_out(3, "29 7-5", 2, 17)

# Pitching change (BAL): #17 Brian Matusz replaces #60 Josh Stinson
t7.pitching_substitution(17)

# 6. BOS #29 Daniel Nava (X - 15 - 5)
t7.new_ab(is_risp=True)
t7.pitch_list("b s b")
t7.hit(1)

# Pitching change (BAL): #39 Kevin Gausman replaces #17 Brian Matusz
t7.pitching_substitution(39)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #23 Brandon Snyder, batting 7th
t7.offensive_substitution(7, 37, "PH")

# 7. BOS #37 Mike Carp (X - X - 29)
t7.new_ab()
t7.pitch_list("b c s b c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #38 Matt Thornton
b7.pitching_substitution(36)

# Defensive switch (BOS): #37 Mike Carp moves to 1B
b7.defensive_switch(37, "3")

# 2. BAL #2  J.J. Hardy (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F8")

# 3. BAL #19 Chris Davis (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")

# 4. BAL #10 Adam Jones (X - X - X)
b7.new_ab()
b7.pitch_list("s s f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #39 Kevin Gausman
t8 = game.new_inning()

# 8. BOS #3  David Ross (X - X - X)
t8.new_ab()
t8.pitch_list("c b c s")
t8.out("K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
t8.new_ab()
t8.pitch_list("t f")
t8.out("L7")

# 1. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.out("P4")


# Bot 8th
# Pitching: BOS #36 Junichi Tazawa
b8 = game.new_inning()

# 5. BAL #32 Matt Wieters (X - X - X)
b8.new_ab()
b8.pitch_list("b f b s f")
b8.hit(1)
b8.advance(2, "35 1B")
# Offensive change (BAL): Pinch-runner #9 Nate McLouth replaces #32 Matt Wieters
b8.offensive_substitution(5, 9, "PR")
b8.atbase("PR")
b8.advance(4, "28 2B")

# 6. BAL #35 Danny Valencia (X - X - 32)
b8.new_ab()
b8.pitch_list("c d c")
b8.hit(1)
b8.advance(4, "28 2B")

# Pitching change (BOS): #56 Franklin Morales replaces #36 Junichi Tazawa
b8.pitching_substitution(56)

# 7. BAL #21 Nick Markakis (X - 32 - 35)
b8.new_ab(is_risp=True)
b8.pitch_list("s b d f t")
b8.out("KT")

# 8. BAL #28 Steve Pearce (X - 9 - 35)
b8.new_ab(is_risp=True)
b8.pitch_list("s d b f")
b8.hit(2, rbis=2)
b8.advance(3, "T")

# Pitching change (BOS): #67 Brandon Workman replaces #56 Franklin Morales
b8.pitching_substitution(67)

# Offensive change (BAL): Pinch-hitter #6 Jonathan Schoop replaces #24 Jason Pridie, batting 9th
b8.offensive_substitution(9, 6, "PH")

# Offensive change (BAL): Pinch-hitter #3 Ryan Flaherty replaces #6 Jonathan Schoop, batting 9th
b8.offensive_substitution(9, 3, "PH")

# 9. BAL #3  Ryan Flaherty (28 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c f b s")
b8.out("K")

# 1. BAL #1  Brian Roberts (28 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b b b c")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #43 Jim Johnson
t9 = game.new_inning()

# Pitching change (BAL): #43 Jim Johnson replaces #39 Kevin Gausman
t9.pitching_substitution(43)

# Defensive switch (BAL): #9 Nate McLouth moves to LF
t9.defensive_switch(9, "7")

# Defensive change (BAL): #48 Chris Snyder replaces #35 Danny Valencia (3B), playing C, batting 6th
t9.defensive_substitution(6, 48, "2")

# Defensive switch (BAL): #3 Ryan Flaherty moves to 3B
t9.defensive_switch(3, "5")

# 2. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t9.new_ab()
t9.pitch_list("b f c b f")
t9.out("F8")

# 4. BOS #12 Mike Napoli (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #12 Mike Napoli
t9.offensive_substitution(4, 50, "PR")
t9.atbase("PR")
t9.advance(2, "5 SB")

# 5. BOS #5  Jonny Gomes (X - X - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b c b b c c")
t9.out("!K")

# Winning team: BAL
# WP: BAL #39 Kevin Gausman
game.winning_pitcher(39)
# SV: BAL #43 Jim Johnson
game.save_pitcher(43)

# Loser team: BOS
# LP: BOS #36 Junichi Tazawa
game.losing_pitcher(36, is_away_team=True)

# print(game)
game.generate_scorecard()
