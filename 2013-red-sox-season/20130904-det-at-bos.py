import os
from baseball_scorecard.baseball_scorecard import Scorecard

# DET @ BOS, 2013-09-04
# https://www.baseball-reference.com/boxes/BOS/BOS201309040.shtml
# https://www.mlb.com/gameday/tigers-vs-red-sox/2013/09/04/348819/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-04 19:10-22:43",
        "at": "Fenway Park, Boston, MA",
        "att": "33,720",
        "temp": "77F, Cloudy",
        "wind": "11mph, Out To RF",
        "away": {
            "team": "Detroit Tigers",
            "starter": 21,
            "roster": {
                # Lineup
                14: "Austin Jackson",
                48: "Torii Hunter",
                28: "Prince Fielder",
                41: "Victor Martinez",
                12: "Andy Dirks",
                32: "Don Kelly",
                4: "Omar Infante",
                13: "Alex Avila",
                1: "Jose Iglesias",
                # Starting pitcher
                21: "Rick Porcello",
                # Bench
                50: "Bryan Holaday",
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
                36: "Luke Putkonen",
                52: "Jose Alvarez",
                31: "Jose Veras",
                37: "Max Scherzer",
                62: "Al Alburquerque",
                58: "Doug Fister",
                38: "Jeremy Bonderman",
                57: "Evan Reed",
                19: "Aníbal Sánchez",
                35: "Justin Verlander",
                43: "Bruce Rondón",
            },
            "lefties": [40, 33, 52],
            "lineup": [
                [14, "8"],
                [48, "9"],
                [28, "3"],
                [41, "0"],
                [12, "7"],
                [32, "5"],
                [4, "4"],
                [13, "2"],
                [1, "6"],
            ],
            "bench": [
                [50, "C"],
                [29, "2B"],
                [39, "SS"],
                [30, "RF"],
                [18, "LF"],
                [24, "1B"],
                [26, "SS"],
                [55, "C"],
            ],
            "bullpen": [40, 33, 53, 36, 52, 31, 37, 62, 58, 38, 57, 19, 35, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 46,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                12: "Mike Napoli",
                7: "Stephen Drew",
                3: "David Ross",
                16: "Will Middlebrooks",
                # Starting pitcher
                46: "Ryan Dempster",
                # Bench
                50: "Quintin Berry",
                39: "Jarrod Saltalamacchia",
                37: "Mike Carp",
                5: "Jonny Gomes",
                72: "Xander Bogaerts",
                20: "Ryan Lavarnway",
                10: "John McDonald",
                23: "Brandon Snyder",
                # Bullpen
                41: "John Lackey",
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
            },
            "lefties": [56, 32, 66, 31, 38, 22],
            "lineup": [
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "0"],
                [29, "7"],
                [12, "3"],
                [7, "6"],
                [3, "2"],
                [16, "5"],
            ],
            "bench": [
                [50, "LF"],
                [39, "C"],
                [37, "1B"],
                [5, "LF"],
                [72, "2B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [41, 67, 56, 32, 66, 44, 31, 36, 11, 19, 38, 62, 22],
        },
        "umpires": {
            "HP": "Jeff Kellogg",
            "1B": "Mike Muchlinski",
            "2B": "Eric Cooper",
            "3B": "Paul Schrieber",
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

# 1. DET #14 Austin Jackson (X - X - X)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")

# 2. DET #48 Torii Hunter (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G1-3")

# 3. DET #28 Prince Fielder (X - X - X)
t1.new_ab()
t1.pitch_list("f b f")
t1.hit(1)
t1.thrown_out(2, "41 FC4-6", 3, 46)

# 4. DET #41 Victor Martinez (X - X - 28)
t1.new_ab()
t1.pitch_list("b c d b")
t1.reach("FC4-6")


# Bot 1st
# Pitching: DET #21 Rick Porcello
b1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("L7")

# 2. BOS #18 Shane Victorino (X - X - X)
b1.new_ab()
b1.pitch_list("c c c")
b1.out("!K")

# 3. BOS #15 Dustin Pedroia (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #46 Ryan Dempster
t2 = game.new_inning()

# 5. DET #12 Andy Dirks (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.out("G4-3")

# 6. DET #32 Don Kelly (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b")
t2.out("P4")

# 7. DET #4  Omar Infante (X - X - X)
t2.new_ab()
t2.pitch_list("f f b b s")
t2.out("K")


# Bot 2nd
# Pitching: DET #21 Rick Porcello
b2 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G4-3")

# 5. BOS #29 Daniel Nava (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(1)
b2.advance(4, "7 HR")

# 6. BOS #12 Mike Napoli (X - X - 29)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("L8")

# 7. BOS #7  Stephen Drew (X - X - 29)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(4, rbis=2)

# 8. BOS #3  David Ross (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #46 Ryan Dempster
t3 = game.new_inning()

# 8. DET #13 Alex Avila (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b f s")
t3.out("K")

# 9. DET #1  Jose Iglesias (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.advance(3, "14 1B")
t3.advance(4, "48 G4-3")

# 1. DET #14 Austin Jackson (X - X - 1)
t3.new_ab()
t3.pitch_list("b 1 c")
t3.hit(1)
t3.advance(2, "48 G4-3")
t3.advance(4, "28 HR")

# 2. DET #48 Torii Hunter (1 - X - 14)
t3.new_ab()
t3.out("G4-3", rbis=1)

# 3. DET #28 Prince Fielder (X - 14 - X)
t3.new_ab()
t3.pitch_list("d b")
t3.hit(4, rbis=2)

# 4. DET #41 Victor Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("b f f f f f b f b f")
t3.out("G4-3")


# Bot 3rd
# Pitching: DET #21 Rick Porcello
b3 = game.new_inning()

# 9. BOS #16 Will Middlebrooks (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G4-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b3.new_ab()
b3.pitch_list("s b b")
b3.hit(4)

# 2. BOS #18 Shane Victorino (X - X - X)
b3.new_ab()
b3.pitch_list("f f")
b3.reach("HBP")
b3.thrown_out(2, "15 DP1-6-3", 2, 21)

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b3.new_ab()
b3.pitch_list("b f 1")
b3.out("DP1-6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #46 Ryan Dempster
t4 = game.new_inning()

# 5. DET #12 Andy Dirks (X - X - X)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")

# 6. DET #32 Don Kelly (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(3, "4 2B")
t4.advance(4, "1 FC5-4")

# 7. DET #4  Omar Infante (X - X - 32)
t4.new_ab()
t4.pitch_list("c")
t4.hit(2)
t4.advance(3, "1 FC5-4")

# 8. DET #13 Alex Avila (32 - 4 - X)
t4.new_ab()
t4.pitch_list("b f b b b")
t4.reach("BB")
t4.thrown_out(2, "1 FC5-4", 2, 46)

# 9. DET #1  Jose Iglesias (32 - 4 - 13)
t4.new_ab()
t4.pitch_list("c f d")
t4.reach("FC5-4", rbis=1)

# 1. DET #14 Austin Jackson (4 - X - 1)
t4.new_ab()
t4.pitch_list("s c")
t4.out("(F)F9")


# Bot 4th
# Pitching: DET #21 Rick Porcello
b4 = game.new_inning()

# 4. BOS #34 David Ortiz (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.hit(4)

# 5. BOS #29 Daniel Nava (X - X - X)
b4.new_ab()
b4.pitch_list("c c f c")
b4.out("!K")

# 6. BOS #12 Mike Napoli (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f c")
b4.out("!K")

# 7. BOS #7  Stephen Drew (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b b")
b4.reach("BB")
b4.advance(3, "3 1B")

# 8. BOS #3  David Ross (X - X - 7)
b4.new_ab()
b4.hit(1)

# 9. BOS #16 Will Middlebrooks (7 - X - 3)
b4.new_ab()
b4.pitch_list("f f b 1 b d f")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #46 Ryan Dempster
t5 = game.new_inning()

# 2. DET #48 Torii Hunter (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L4")

# 3. DET #28 Prince Fielder (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")

# 4. DET #41 Victor Martinez (X - X - 28)
t5.new_ab()
t5.pitch_list("b")
t5.out("L7")

# 5. DET #12 Andy Dirks (X - X - 28)
t5.new_ab()
t5.pitch_list("b")
t5.out("P4")


# Bot 5th
# Pitching: DET #21 Rick Porcello
b5 = game.new_inning()

# Defensive change (DET): #39 Ramon Santiago replaces #1 Jose Iglesias (SS), playing SS, batting 9th
b5.defensive_substitution(9, 39, "6")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b5.new_ab()
b5.pitch_list("f b")
b5.out("L7")

# 2. BOS #18 Shane Victorino (X - X - X)
b5.new_ab()
b5.pitch_list("c b s b")
b5.hit(1)
b5.error(2)
b5.advance(2, "15 SB")
b5.advance(3, "15 E2")
b5.advance("U", "15 SF7")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b5.new_ab()
b5.pitch_list("1 b b 1 f f 1 f f b f f f")
b5.out("SF7", rbis=1)

# 4. BOS #34 David Ortiz (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #46 Ryan Dempster
t6 = game.new_inning()

# 6. DET #32 Don Kelly (X - X - X)
t6.new_ab()
t6.pitch_list("b f s b c")
t6.out("!K")

# 7. DET #4  Omar Infante (X - X - X)
t6.new_ab()
t6.pitch_list("c b s s")
t6.out("K")

# 8. DET #13 Alex Avila (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c s s")
t6.out("K")


# Bot 6th
# Pitching: DET #21 Rick Porcello
b6 = game.new_inning()

# 5. BOS #29 Daniel Nava (X - X - X)
b6.new_ab()
b6.pitch_list("b c f f b b b")
b6.reach("BB")
b6.advance(3, "12 2B")
b6.advance(4, "37 BB")

# 6. BOS #12 Mike Napoli (X - X - 29)
b6.new_ab()
b6.hit(2)
b6.advance(3, "37 BB")
b6.advance(4, "16 HR")

# 7. BOS #7  Stephen Drew (29 - 12 - X)
b6.new_ab()
b6.pitch_list("i i i i")
b6.reach("IBB")
b6.advance(2, "37 BB")
b6.advance(4, "16 HR")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #3 David Ross, batting 8th
b6.offensive_substitution(8, 37, "PH")

# 8. BOS #37 Mike Carp (29 - 12 - 7)
b6.new_ab()
b6.pitch_list("b b f b b")
b6.reach("BB", rbis=1)
b6.advance(4, "16 HR")

# Pitching change (DET): #62 Al Alburquerque replaces #21 Rick Porcello
b6.pitching_substitution(62)

# 9. BOS #16 Will Middlebrooks (12 - 7 - 37)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4, rbis=4)

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
b6.new_ab()
b6.pitch_list("b c c f f b f b s")
b6.out("K")

# 2. BOS #18 Shane Victorino (X - X - X)
b6.new_ab()
b6.pitch_list("b s")
b6.reach("HBP")
# Offensive change (BOS): Pinch-runner #50 Quintin Berry replaces #18 Shane Victorino
b6.offensive_substitution(2, 50, "PR")
b6.atbase("PR")
b6.advance(4, "34 2B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
b6.new_ab()
b6.pitch_list("c f 1 c")
b6.out("!K")

# 4. BOS #34 David Ortiz (X - X - 50)
b6.new_ab()
b6.pitch_list("f d d")
b6.hit(2, rbis=1)
b6.advance(4, "29 HR")

# 5. BOS #29 Daniel Nava (X - 34 - X)
b6.new_ab()
b6.pitch_list("c c f f b")
b6.hit(4, rbis=2)

# Pitching change (DET): #38 Jeremy Bonderman replaces #62 Al Alburquerque
b6.pitching_substitution(38)

# 6. BOS #12 Mike Napoli (X - X - X)
b6.new_ab()
b6.pitch_list("b c s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #67 Brandon Workman
t7 = game.new_inning()

# Pitching change (BOS): #67 Brandon Workman replaces #46 Ryan Dempster
t7.pitching_substitution(67)

# Defensive switch (BOS): #50 Quintin Berry moves to RF
t7.defensive_switch(50, "9")

# Defensive change (BOS): #10 John McDonald replaces #15 Dustin Pedroia (2B), playing 2B, batting 3rd
t7.defensive_substitution(3, 10, "4")

# Defensive change (BOS): #20 Ryan Lavarnway replaces #37 Mike Carp (PH), playing C, batting 8th
t7.defensive_substitution(8, 20, "2")

# 9. DET #39 Ramon Santiago (X - X - X)
t7.new_ab()
t7.pitch_list("c b c b")
t7.hit(1)
t7.thrown_out(2, "14 FC6-4", 1, 67)

# 1. DET #14 Austin Jackson (X - X - 39)
t7.new_ab()
t7.pitch_list("c")
t7.reach("FC6-4")

# 2. DET #48 Torii Hunter (X - X - 14)
t7.new_ab()
t7.pitch_list("c f s")
t7.out("K")

# 3. DET #28 Prince Fielder (X - X - 14)
t7.new_ab()
t7.pitch_list("c b b")
t7.out("G4-3")


# Bot 7th
# Pitching: DET #38 Jeremy Bonderman
b7 = game.new_inning()

# Defensive change (DET): #30 Nick Castellanos replaces #48 Torii Hunter (RF), playing LF, batting 2nd
b7.defensive_substitution(2, 30, "7")

# Defensive change (DET): #29 Danny Worth replaces #14 Austin Jackson (CF), playing 3B, batting 1st
b7.defensive_substitution(1, 29, "5")

# Defensive change (DET): #18 Matt Tuiasosopo replaces #28 Prince Fielder (1B), playing 1B, batting 3rd
b7.defensive_substitution(3, 18, "3")

# Defensive switch (DET): #12 Andy Dirks moves to RF
b7.defensive_switch(12, "9")

# Defensive switch (DET): #32 Don Kelly moves to CF
b7.defensive_switch(32, "8")

# 7. BOS #7  Stephen Drew (X - X - X)
b7.new_ab()
b7.hit(2)
# Offensive change (BOS): Pinch-runner #72 Xander Bogaerts replaces #7 Stephen Drew
b7.offensive_substitution(7, 72, "PR")
b7.atbase("PR")
b7.advance(4, "20 HR")

# 8. BOS #20 Ryan Lavarnway (X - 7 - X)
b7.new_ab()
b7.pitch_list("c d b f")
b7.hit(4, rbis=2)

# 9. BOS #16 Will Middlebrooks (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.hit(2)
b7.advance(3, "2 L8")
b7.advance(4, "50 1B")

# 1. BOS #2  Jacoby Ellsbury (X - 16 - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("L8")

# 2. BOS #50 Quintin Berry (16 - X - X)
b7.new_ab()
b7.hit(1, rbis=1)
b7.advance(4, "34 HR")

# 3. BOS #10 John McDonald (X - X - 50)
b7.new_ab()
b7.pitch_list("d f d b f t")
b7.out("KT")

# 4. BOS #34 David Ortiz (X - X - 50)
b7.new_ab()
b7.pitch_list("b b b c")
b7.hit(4, rbis=2)

# Pitching change (DET): #57 Evan Reed replaces #38 Jeremy Bonderman
b7.pitching_substitution(57)

# 5. BOS #29 Daniel Nava (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Franklin Morales
t8 = game.new_inning()

# Pitching change (BOS): #56 Franklin Morales replaces #67 Brandon Workman
t8.pitching_substitution(56)

# Defensive change (BOS): #23 Brandon Snyder replaces #2 Jacoby Ellsbury (CF), playing LF, batting 1st
t8.defensive_substitution(1, 23, "7")

# Defensive switch (BOS): #50 Quintin Berry moves to CF
t8.defensive_switch(50, "8")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
t8.defensive_switch(29, "9")

# Defensive switch (BOS): #72 Xander Bogaerts moves to SS
t8.defensive_switch(72, "6")

# 4. DET #41 Victor Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b f c b")
t8.out("F8")

# 5. DET #12 Andy Dirks (X - X - X)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K")

# 6. DET #32 Don Kelly (X - X - X)
t8.new_ab()
t8.pitch_list("s c b b b s")
t8.out("K")


# Bot 8th
# Pitching: DET #57 Evan Reed
b8 = game.new_inning()

# Defensive change (DET): #26 Hernán Pérez replaces #4 Omar Infante (2B), playing 2B, batting 7th
b8.defensive_substitution(7, 26, "4")

# Defensive change (DET): #50 Bryan Holaday replaces #13 Alex Avila (C), playing C, batting 8th
b8.defensive_substitution(8, 50, "2")

# 6. BOS #12 Mike Napoli (X - X - X)
b8.new_ab()
b8.pitch_list("b s b b")
b8.hit(4)

# 7. BOS #72 Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c f b")
b8.out("G5-3")

# 8. BOS #20 Ryan Lavarnway (X - X - X)
b8.new_ab()
b8.pitch_list("b f c")
b8.hit(1)
b8.advance(2, "16 1B")
b8.advance(4, "50 1B")

# 9. BOS #16 Will Middlebrooks (X - X - 20)
b8.new_ab()
b8.hit(1)
b8.advance(2, "50 1B")

# 1. BOS #23 Brandon Snyder (X - 20 - 16)
b8.new_ab()
b8.pitch_list("b f f f s")
b8.out("K")

# 2. BOS #50 Quintin Berry (X - 20 - 16)
b8.new_ab()
b8.hit(1, rbis=1)

# 3. BOS #10 John McDonald (X - 16 - 50)
b8.new_ab()
b8.pitch_list("c s d c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #62 Rubby De La Rosa
t9 = game.new_inning()

# Pitching change (BOS): #62 Rubby De La Rosa replaces #56 Franklin Morales
t9.pitching_substitution(62)

# 7. DET #26 Hernán Pérez (X - X - X)
t9.new_ab()
t9.pitch_list("c f")
t9.out("F9")

# 8. DET #50 Bryan Holaday (X - X - X)
t9.new_ab()
t9.pitch_list("b s c b f")
t9.hit(1)

# 9. DET #39 Ramon Santiago (X - X - 50)
t9.new_ab()
t9.out("F9")

# 1. DET #29 Danny Worth (X - X - 50)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# Winning team: BOS
# WP: BOS #46 Ryan Dempster
game.winning_pitcher(46)

# Loser team: DET
# LP: DET #21 Rick Porcello
game.losing_pitcher(21, is_away_team=True)

# print(game)
game.generate_scorecard()
