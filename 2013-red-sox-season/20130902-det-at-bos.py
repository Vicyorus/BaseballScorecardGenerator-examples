import os
from baseball_scorecard.baseball_scorecard import Scorecard

# DET @ BOS, 2013-09-02
# https://www.baseball-reference.com/boxes/BOS/BOS201309020.shtml
# https://www.mlb.com/gameday/tigers-vs-red-sox/2013/09/02/348789/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-02 13:37-16:36",
        "at": "Fenway Park, Boston, MA",
        "att": "36,188",
        "temp": "81F, Cloudy",
        "wind": "7mph, Out To LF",
        "away": {
            "team": "Detroit Tigers",
            "starter": 58,
            "roster": {
                # Lineup
                14: "Austin Jackson",
                48: "Torii Hunter",
                28: "Prince Fielder",
                41: "Victor Martinez",
                12: "Andy Dirks",
                4: "Omar Infante",
                32: "Don Kelly",
                13: "Alex Avila",
                1: "Jose Iglesias",
                # Starting pitcher
                58: "Doug Fister",
                # Bench
                29: "Danny Worth",
                39: "Ramon Santiago",
                30: "Nick Castellanos",
                18: "Matt Tuiasosopo",
                24: "Miguel Cabrera",
                26: "Hernán Pérez",
                55: "Brayan Peña",
                # Bullpen
                40: "Phil Coke",
                33: "Drew Smyly",
                53: "Joaquín Benoit",
                21: "Rick Porcello",
                36: "Luke Putkonen",
                31: "Jose Veras",
                37: "Max Scherzer",
                62: "Al Alburquerque",
                57: "Evan Reed",
                19: "Aníbal Sánchez",
                35: "Justin Verlander",
                43: "Bruce Rondón",
            },
            "lefties": [40, 33],
            "lineup": [
                [14, "8"],
                [48, "9"],
                [28, "3"],
                [41, "0"],
                [12, "7"],
                [4, "4"],
                [32, "5"],
                [13, "2"],
                [1, "6"],
            ],
            "bench": [
                [29, "2B"],
                [39, "SS"],
                [30, "RF"],
                [18, "LF"],
                [24, "1B"],
                [26, "SS"],
                [55, "C"],
            ],
            "bullpen": [40, 33, 53, 21, 36, 31, 37, 62, 57, 19, 35, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                50: "Quintin Berry",
                37: "Mike Carp",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                67: "Brandon Workman",
                56: "Franklin Morales",
                32: "Craig Breslow",
                66: "Drake Britton",
                44: "Jake Peavy",
                31: "Jon Lester",
                36: "Junichi Tazawa",
                11: "Clay Buchholz",
                19: "Koji Uehara",
                38: "Matt Thornton",
                62: "Rubby De La Rosa",
                22: "Felix Doubront",
                46: "Ryan Dempster",
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [12, "3"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [37, "1B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 62, 22, 46],
        },
        "umpires": {
            "HP": "Eric Cooper",
            "1B": "Paul Schrieber",
            "2B": "Jeff Kellogg",
            "3B": "Angel Hernandez",
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

# 1. DET #14 Austin Jackson (X - X - X)
t1.new_ab()
t1.pitch_list("b c b")
t1.hit(2)

# 2. DET #48 Torii Hunter (X - 14 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b s t")
t1.out("KT")

# 3. DET #28 Prince Fielder (X - 14 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.out("F8")

# 4. DET #41 Victor Martinez (X - 14 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b b")
t1.out("G4-3")


# Bot 1st
# Pitching: DET #58 Doug Fister
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("c b c b f f f b b")
b1.reach("BB")
b1.advance(2, "18 HBP")
b1.advance(3, "15 DP1-6-3")

# 2. BOS #18 Shane Victorino (X - X - 2)
b1.new_ab()
b1.pitch_list("c")
b1.reach("HBP")
b1.thrown_out(2, "15 DP1-6-3", 1, 58)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("c c")
b1.out("DP1-6-3")

# 4. BOS #34 David Ortiz (2 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b s b")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 John Lackey
t2 = game.new_inning()

# 5. DET #12 Andy Dirks (X - X - X)
t2.new_ab()
t2.pitch_list("c s f")
t2.out("G4-3")

# 6. DET #4  Omar Infante (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F8")

# 7. DET #32 Don Kelly (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")


# Bot 2nd
# Pitching: DET #58 Doug Fister
b2 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.advance(2, "12 BB")
b2.advance(3, "39 DP4-6-3")

# 6. BOS #12 Mike Napoli (X - X - 29)
b2.new_ab()
b2.pitch_list("b b c b b")
b2.reach("BB")
b2.thrown_out(2, "39 DP4-6-3", 1, 58)

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - 12)
b2.new_ab(is_risp=True)
b2.pitch_list("c c d b")
b2.out("DP4-6-3")

# 8. BOS #7  Stephen Drew (29 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b b")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 John Lackey
t3 = game.new_inning()

# 8. DET #13 Alex Avila (X - X - X)
t3.new_ab()
t3.pitch_list("c s f c")
t3.out("!K")

# 9. DET #1  Jose Iglesias (X - X - X)
t3.new_ab()
t3.hit(2)

# 1. DET #14 Austin Jackson (X - 1 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b c d s")
t3.out("K")

# 2. DET #48 Torii Hunter (X - 1 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b f s b d")
t3.out("G2-3")


# Bot 3rd
# Pitching: DET #58 Doug Fister
b3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("G6-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("f f b b f s")
b3.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 John Lackey
t4 = game.new_inning()

# 3. DET #28 Prince Fielder (X - X - X)
t4.new_ab()
t4.pitch_list("c f")
t4.hit(2)
t4.advance(3, "41 PB")

# 4. DET #41 Victor Martinez (X - 28 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("s")
t4.pb()
t4.out("G1-3")

# 5. DET #12 Andy Dirks (28 - X - X)
t4.new_ab(is_risp=True)
t4.out("F9")

# 6. DET #4  Omar Infante (28 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b")
t4.out("F8")


# Bot 4th
# Pitching: DET #58 Doug Fister
b4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("F7")

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b")
b4.out("P4")

# 5. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(1)

# 6. BOS #12 Mike Napoli (X - X - 29)
b4.new_ab()
b4.pitch_list("c b c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 John Lackey
t5 = game.new_inning()

# 7. DET #32 Don Kelly (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("P3")

# 8. DET #13 Alex Avila (X - X - X)
t5.new_ab()
t5.pitch_list("c f b f f b b f f c")
t5.out("!K")

# 9. DET #1  Jose Iglesias (X - X - X)
t5.new_ab()
t5.pitch_list("b c b")
t5.out("F8")


# Bot 5th
# Pitching: DET #58 Doug Fister
b5 = game.new_inning()

# 7. BOS #39 Jarrod Saltalamacchia (X - X - X)
b5.new_ab()
b5.pitch_list("f f f b b c")
b5.out("!K")

# 8. BOS #7  Stephen Drew (X - X - X)
b5.new_ab()
b5.pitch_list("c b s c")
b5.out("!K")

# 9. BOS #16 Will Middlebrooks (X - X - X)
b5.new_ab()
b5.pitch_list("b f c b b")
b5.hit(1)

# 1. BOS #2  Jacoby Ellsbury (X - X - 16)
b5.new_ab()
b5.pitch_list("b f b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 John Lackey
t6 = game.new_inning()

# 1. DET #14 Austin Jackson (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F9")

# 2. DET #48 Torii Hunter (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 3. DET #28 Prince Fielder (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b")
t6.out("G4-3")


# Bot 6th
# Pitching: DET #58 Doug Fister
b6 = game.new_inning()

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b b f b f")
b6.hit(1)
b6.thrown_out(2, "15 DP6-3", 1, 58)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b6.new_ab()
b6.out("DP6-3")

# 4. BOS #34 David Ortiz (X - X - X)
b6.new_ab()
b6.pitch_list("f b f")
b6.out("G3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 John Lackey
t7 = game.new_inning()

# 4. DET #41 Victor Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b c f f")
t7.hit(1)
t7.advance(4, "12 3B")

# 5. DET #12 Andy Dirks (X - X - 41)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(3, rbis=1)
t7.advance(4, "32 DP4-3-6")

# 6. DET #4  Omar Infante (12 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("s b b f f f b b")
t7.reach("BB")
t7.thrown_out(2, "32 DP4-3-6", 2, 41)

# 7. DET #32 Don Kelly (12 - X - 4)
t7.new_ab(is_risp=True)
t7.pitch_list("b b f f b")
t7.out("DP4-3-6")

# 8. DET #13 Alex Avila (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("L8")


# Bot 7th
# Pitching: DET #58 Doug Fister
b7 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2)
b7.thrown_out(3, "39 FC2-5", 1, 58)

# 6. BOS #12 Mike Napoli (X - 29 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d c b b b")
b7.reach("BB")
b7.advance(2, "39 FC2-5")
b7.advance(3, "7 G3-1")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("d")
b7.reach("FC2-5")
b7.advance(2, "7 G3-1")

# 8. BOS #7  Stephen Drew (X - 12 - 39)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b")
b7.out("G3-1")

# 9. BOS #16 Will Middlebrooks (12 - 39 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #41 John Lackey
t8 = game.new_inning()

# 9. DET #1  Jose Iglesias (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F9")

# 1. DET #14 Austin Jackson (X - X - X)
t8.new_ab()
t8.pitch_list("c b b s f f b")
t8.hit(1)
t8.advance(2, "48 SB")
t8.advance(3, "48 1B")
t8.advance(4, "28 SF9")

# 2. DET #48 Torii Hunter (X - X - 14)
t8.new_ab(is_risp=True)
t8.pitch_list("1 b b")
t8.hit(1)
t8.advance(2, "T")

# Pitching change (BOS): #38 Matt Thornton replaces #41 John Lackey
t8.pitching_substitution(38)

# 3. DET #28 Prince Fielder (14 - 48 - X)
t8.new_ab(is_risp=True)
t8.out("SF9", rbis=1)

# 4. DET #41 Victor Martinez (X - 48 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c")
t8.out("G6-3")


# Bot 8th
# Pitching: DET #40 Phil Coke
b8 = game.new_inning()

# Pitching change (DET): #40 Phil Coke replaces #58 Doug Fister
b8.pitching_substitution(40)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G6-3")

# Pitching change (DET): #43 Bruce Rondón replaces #40 Phil Coke
b8.pitching_substitution(43)

# 2. BOS #18 Shane Victorino (X - X - X)
b8.new_ab()
b8.pitch_list("b b f s s")
b8.out("K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f b f")
b8.hit(2)
b8.advance(3, "34 WP")

# 4. BOS #34 David Ortiz (X - 15 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b s f b f t")
b8.wp()
b8.out("KT")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #38 Matt Thornton
t9 = game.new_inning()

# 5. DET #12 Andy Dirks (X - X - X)
t9.new_ab()
t9.out("L8")

# 6. DET #4  Omar Infante (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G6-3")

# 7. DET #32 Don Kelly (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b")
t9.hit(1)
t9.error(7)
t9.advance(2, "E7")

# 8. DET #13 Alex Avila (X - 32 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("s f f s")
t9.out("K")


# Bot 9th
# Pitching: DET #31 Jose Veras
b9 = game.new_inning()

# Pitching change (DET): #31 Jose Veras replaces #43 Bruce Rondón
b9.pitching_substitution(31)

# 5. BOS #29 Daniel Nava (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c c")
b9.hit(2)
b9.advance(3, "39 G4-3")

# 6. BOS #12 Mike Napoli (X - 29 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c b b c d")
b9.out("P4")

# 7. BOS #39 Jarrod Saltalamacchia (X - 29 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c b b s f b")
b9.out("G4-3")

# 8. BOS #7  Stephen Drew (29 - X - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c c d s")
b9.out("K")

# Winning team: DET
# WP: DET #58 Doug Fister
game.winning_pitcher(58, is_away_team=True)
# SV: DET #31 Jose Veras
game.save_pitcher(31, is_away_team=True)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41)

# print(game)
game.generate_scorecard()
