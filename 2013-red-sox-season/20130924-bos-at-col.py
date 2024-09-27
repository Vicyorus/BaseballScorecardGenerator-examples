import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ COL, 2013-09-24
# https://www.baseball-reference.com/boxes/COL/COL201309240.shtml
# https://www.mlb.com/gameday/red-sox-vs-rockies/2013/09/24/349091/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-24 20:41-23:21",
        "at": "Coors Field, Denver, CO",
        "att": "32,315",
        "temp": "70F, Clear",
        "wind": "4mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                18: "Shane Victorino",
                29: "Daniel Nava",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                25: "Jackie Bradley Jr.",
                41: "John Lackey",
                # Starting pitcher
                41: "John Lackey",
                # Bench
                50: "Quintin Berry",
                2: "Jacoby Ellsbury",
                37: "Mike Carp",
                26: "Brock Holt",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                12: "Mike Napoli",
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
                [18, "9"],
                [29, "7"],
                [15, "4"],
                [34, "3"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
                [25, "8"],
                [41, "1"],
            ],
            "bench": [
                [50, "LF"],
                [2, "CF"],
                [37, "1B"],
                [26, "2B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [12, "1B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 67, 56, 60, 32, 66, 44, 31, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Colorado Rockies",
            "starter": 32,
            "roster": {
                # Lineup
                19: "Charlie Blackmon",
                9: "DJ LeMahieu",
                2: "Troy Tulowitzki",
                3: "Michael Cuddyer",
                17: "Todd Helton",
                28: "Nolan Arenado",
                6: "Corey Dickerson",
                15: "Jordan Pacheco",
                32: "Tyler Chatwood",
                # Starting pitcher
                32: "Tyler Chatwood",
                # Bench
                24: "Dexter Fowler",
                20: "Wilin Rosario",
                8: "Yorvit Torrealba",
                23: "Charlie Culberson",
                14: "Josh Rutledge",
                5: "Carlos González",
                18: "Jonathan Herrera",
                4: "Ryan Wheeler",
                # Bullpen
                44: "Roy Oswalt",
                34: "Matt Belisle",
                35: "Chad Bettis",
                49: "Rex Brothers",
                0: "Adam Ottavino",
                59: "Wilton Lopez",
                13: "Drew Pomeranz",
                43: "Collin McHugh",
                50: "Jeff Manship",
                12: "Juan Nicasio",
                62: "Rob Scahill",
                60: "Manny Corpas",
                29: "Jorge De La Rosa",
                88: "Josh Outman",
                45: "Jhoulys Chacín",
                26: "Jeff Francis",
                41: "Mitchell Boggs",
            },
            "lefties": [49, 13, 29, 88, 26],
            "lineup": [
                [19, "8"],
                [9, "4"],
                [2, "6"],
                [3, "9"],
                [17, "3"],
                [28, "5"],
                [6, "7"],
                [15, "2"],
                [32, "1"],
            ],
            "bench": [
                [24, "CF"],
                [20, "1B"],
                [8, "C"],
                [23, "1B"],
                [14, "SS"],
                [5, "RF"],
                [18, "2B"],
                [4, "3B"],
            ],
            "bullpen": [44, 34, 35, 49, 0, 59, 13, 43, 50, 12, 62, 60, 29, 88, 45, 26, 41],
        },
        "umpires": {
            "HP": "Sam Holbrook",
            "1B": "Andy Fletcher",
            "2B": "Rob Drake",
            "3B": "Joe West",
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
# Pitching: COL #32 Tyler Chatwood
t1 = game.new_inning()

# 1. BOS #18 Shane Victorino (X - X - X)
t1.new_ab()
t1.pitch_list("b c c")
t1.out("G5-3")

# 2. BOS #29 Daniel Nava (X - X - X)
t1.new_ab()
t1.pitch_list("c b b c f")
t1.reach("HBP")
t1.advance(2, "15 G6-3")

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t1.new_ab()
t1.pitch_list("b")
t1.out("G6-3")

# 4. BOS #34 David Ortiz (X - 29 - X)
t1.new_ab()
t1.pitch_list("b b b i")
t1.reach("IBB")

# 5. BOS #39 Jarrod Saltalamacchia (X - 29 - 34)
t1.new_ab()
t1.pitch_list("c s b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #41 John Lackey
b1 = game.new_inning()

# 1. COL #19 Charlie Blackmon (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.hit(4)

# 2. COL #9  DJ LeMahieu (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G4-3")

# 3. COL #2  Troy Tulowitzki (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.out("F8")

# 4. COL #3  Michael Cuddyer (X - X - X)
b1.new_ab()
b1.hit(2)
b1.advance(4, "17 1B")

# 5. COL #17 Todd Helton (X - 3 - X)
b1.new_ab()
b1.hit(1, rbis=1)

# 6. COL #28 Nolan Arenado (X - X - 17)
b1.new_ab()
b1.pitch_list("b s b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: COL #32 Tyler Chatwood
t2 = game.new_inning()

# 6. BOS #7  Stephen Drew (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("L7")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t2.new_ab()
t2.pitch_list("b c s s")
t2.out("K")

# 8. BOS #25 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("b f b")
t2.out("G1-4-3")


# Bot 2nd
# Pitching: BOS #41 John Lackey
b2 = game.new_inning()

# 7. COL #6  Corey Dickerson (X - X - X)
b2.new_ab()
b2.pitch_list("c c f f")
b2.out("G5-3")

# 8. COL #15 Jordan Pacheco (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.out("G5-3")

# 9. COL #32 Tyler Chatwood (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: COL #32 Tyler Chatwood
t3 = game.new_inning()

# 9. BOS #41 John Lackey (X - X - X)
t3.new_ab()
t3.pitch_list("b t b b")
t3.out("P4")

# 1. BOS #18 Shane Victorino (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("L7")

# 2. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F7")


# Bot 3rd
# Pitching: BOS #41 John Lackey
b3 = game.new_inning()

# 1. COL #19 Charlie Blackmon (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G5-3")

# 2. COL #9  DJ LeMahieu (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")

# 3. COL #2  Troy Tulowitzki (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(4)

# 4. COL #3  Michael Cuddyer (X - X - X)
b3.new_ab()
b3.pitch_list("f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: COL #32 Tyler Chatwood
t4 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("b b f")
t4.hit(1)
t4.thrown_out(2, "34 FC6", 1, 32)

# 4. BOS #34 David Ortiz (X - X - 15)
t4.new_ab()
t4.reach("FC6")
t4.thrown_out(2, "39 FC6-4", 2, 32)

# 5. BOS #39 Jarrod Saltalamacchia (X - X - 34)
t4.new_ab()
t4.pitch_list("b c f")
t4.reach("FC6-4")

# 6. BOS #7  Stephen Drew (X - X - 39)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("G4-3")


# Bot 4th
# Pitching: BOS #41 John Lackey
b4 = game.new_inning()

# 5. COL #17 Todd Helton (X - X - X)
b4.new_ab()
b4.pitch_list("f b f f f s")
b4.out("K")

# 6. COL #28 Nolan Arenado (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s s")
b4.out("K")

# 7. COL #6  Corey Dickerson (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(4)

# 8. COL #15 Jordan Pacheco (X - X - X)
b4.new_ab()
b4.pitch_list("b f f b f b f b")
b4.reach("BB")

# 9. COL #32 Tyler Chatwood (X - X - 15)
b4.new_ab()
b4.pitch_list("f b")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: COL #32 Tyler Chatwood
t5 = game.new_inning()

# 7. BOS #16 Will Middlebrooks (X - X - X)
t5.new_ab()
t5.pitch_list("c b c f b")
t5.out("G6-3")

# 8. BOS #25 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b f f")
t5.hit(1)
t5.advance(2, "41 SB")

# 9. BOS #41 John Lackey (X - X - 25)
t5.new_ab()
t5.pitch_list("1 s b o s")
t5.out("K")

# 1. BOS #18 Shane Victorino (X - 25 - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("L8")


# Bot 5th
# Pitching: BOS #41 John Lackey
b5 = game.new_inning()

# 1. COL #19 Charlie Blackmon (X - X - X)
b5.new_ab()
b5.pitch_list("f b f b")
b5.out("F9")

# 2. COL #9  DJ LeMahieu (X - X - X)
b5.new_ab()
b5.pitch_list("c s f s")
b5.out("K")

# 3. COL #2  Troy Tulowitzki (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: COL #32 Tyler Chatwood
t6 = game.new_inning()

# 2. BOS #29 Daniel Nava (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("G4-3")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("G1-3")

# 4. BOS #34 David Ortiz (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F8")


# Bot 6th
# Pitching: BOS #41 John Lackey
b6 = game.new_inning()

# 4. COL #3  Michael Cuddyer (X - X - X)
b6.new_ab()
b6.out("G5-3")

# 5. COL #17 Todd Helton (X - X - X)
b6.new_ab()
b6.pitch_list("b f b f")
b6.hit(1)

# 6. COL #28 Nolan Arenado (X - X - 17)
b6.new_ab()
b6.pitch_list("c f")
b6.out("L8")

# 7. COL #6  Corey Dickerson (X - X - 17)
b6.new_ab()
b6.pitch_list("b f b b")
b6.out("L3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: COL #32 Tyler Chatwood
t7 = game.new_inning()

# 5. BOS #39 Jarrod Saltalamacchia (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.out("G1")

# 6. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G4-3")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("f c f b b")
t7.hit(2)
t7.advance("U", "25 E1")

# 8. BOS #25 Jackie Bradley Jr. (X - 16 - X)
t7.new_ab()
t7.pitch_list("c f b b b f f")
t7.error(1)
t7.reach("E1")
t7.error(1)
t7.advance(3, "E1")
t7.thrown_out(4, "37 2-1", 3, 32)

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #41 John Lackey, batting 9th
t7.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (25 - X - X)
t7.new_ab()
t7.pitch_list("c f b b b")
t7.no_ab("2-1")


# Bot 7th
# Pitching: BOS #66 Drake Britton
b7 = game.new_inning()

# Pitching change (BOS): #66 Drake Britton replaces #41 John Lackey, batting 8th
b7.pitching_substitution(66)
b7.defensive_substitution(8, 66, "1")

# Defensive switch (BOS): #18 Shane Victorino moves to CF
b7.defensive_switch(18, "8")

# Defensive switch (BOS): #29 Daniel Nava moves to RF
b7.defensive_switch(29, "9")

# Defensive switch (BOS): #37 Mike Carp moves to LF
b7.defensive_switch(37, "7")

# 8. COL #15 Jordan Pacheco (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c f")
b7.hit(2)
b7.advance(3, "14 1B")
b7.advance(4, "9 1B")

# Pitching change (BOS): #67 Brandon Workman replaces #66 Drake Britton, batting 8th
b7.pitching_substitution(67)
b7.defensive_substitution(8, 67, "1")

# Offensive change (COL): Pinch-hitter #14 Josh Rutledge replaces #32 Tyler Chatwood, batting 9th
b7.offensive_substitution(9, 14, "PH")

# 9. COL #14 Josh Rutledge (X - 15 - X)
b7.new_ab()
b7.pitch_list("b b f d")
b7.hit(1)
b7.advance(2, "19 BB")
b7.advance(4, "9 1B")

# 1. COL #19 Charlie Blackmon (15 - X - 14)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "9 1B")
b7.advance(3, "2 SB")
b7.advance(4, "3 1B")

# 2. COL #9  DJ LeMahieu (15 - 14 - 19)
b7.new_ab()
b7.pitch_list("d b f")
b7.hit(1, rbis=2)
b7.advance(2, "2 SB")
b7.advance(4, "3 1B")

# 3. COL #2  Troy Tulowitzki (X - 19 - 9)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G5-3")

# 4. COL #3  Michael Cuddyer (19 - 9 - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1, rbis=2)
b7.advance(2, "28 BB")

# Pitching change (BOS): #56 Franklin Morales replaces #67 Brandon Workman, batting 8th
b7.pitching_substitution(56)
b7.defensive_substitution(8, 56, "1")

# 5. COL #17 Todd Helton (X - X - 3)
b7.new_ab()
b7.pitch_list("b b t s t")
b7.out("KT")

# 6. COL #28 Nolan Arenado (X - X - 3)
b7.new_ab()
b7.pitch_list("b s b d b")
b7.reach("BB")

# 7. COL #6  Corey Dickerson (X - 3 - 28)
b7.new_ab()
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: COL #35 Chad Bettis
t8 = game.new_inning()

# Pitching change (COL): #35 Chad Bettis replaces #32 Tyler Chatwood, batting 9th
t8.pitching_substitution(35)
t8.defensive_substitution(9, 35, "1")

# 9. BOS #37 Mike Carp (X - X - X)
t8.new_ab()
t8.pitch_list("c c b s")
t8.out("K2-3")

# 1. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.thrown_out(2, "29 FC6-4", 2, 35)

# 2. BOS #29 Daniel Nava (X - X - 18)
t8.new_ab()
t8.pitch_list("b")
t8.reach("FC6-4")
t8.thrown_out(2, "15 FC4-6", 3, 35)

# 3. BOS #15 Dustin Pedroia (X - X - 29)
t8.new_ab()
t8.reach("FC4-6")


# Bot 8th
# Pitching: BOS #62 Rubby De La Rosa
b8 = game.new_inning()

# Pitching change (BOS): #62 Rubby De La Rosa replaces #56 Franklin Morales, batting 8th
b8.pitching_substitution(62)
b8.defensive_substitution(8, 62, "1")

# 8. COL #15 Jordan Pacheco (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("P3")

# Offensive change (COL): Pinch-hitter #4 Ryan Wheeler replaces #35 Chad Bettis, batting 9th
b8.offensive_substitution(9, 4, "PH")

# 9. COL #4  Ryan Wheeler (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")
b8.advance(2, "19 1B")
b8.advance(3, "9 G6-3")

# 1. COL #19 Charlie Blackmon (X - X - 4)
b8.new_ab()
b8.hit(1)
b8.advance(2, "9 G6-3")

# 2. COL #9  DJ LeMahieu (X - 4 - 19)
b8.new_ab()
b8.pitch_list("b")
b8.out("G6-3")

# 3. COL #2  Troy Tulowitzki (4 - 19 - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: COL #88 Josh Outman
t9 = game.new_inning()

# Pitching change (COL): #88 Josh Outman replaces #35 Chad Bettis, batting 9th
t9.pitching_substitution(88)
t9.defensive_substitution(9, 88, "1")

# 4. BOS #34 David Ortiz (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
# Offensive change (BOS): Pinch-runner #26 Brock Holt replaces #34 David Ortiz
t9.offensive_substitution(4, 26, "PR")
t9.atbase("PR")
t9.advance(4, "39 HR")

# 5. BOS #39 Jarrod Saltalamacchia (X - X - 34)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(4, rbis=2)

# 6. BOS #7  Stephen Drew (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# Pitching change (COL): #60 Manny Corpas replaces #88 Josh Outman, batting 9th
t9.pitching_substitution(60)
t9.defensive_substitution(9, 60, "1")

# 7. BOS #16 Will Middlebrooks (X - X - X)
t9.new_ab()
t9.pitch_list("b c f b s")
t9.out("K")

# Offensive change (BOS): Pinch-hitter #50 Quintin Berry replaces #62 Rubby De La Rosa, batting 8th
t9.offensive_substitution(8, 50, "PH")

# 8. BOS #50 Quintin Berry (X - X - X)
t9.new_ab()
t9.hit(1)
t9.advance(2, "37 DI")

# 9. BOS #37 Mike Carp (X - X - 50)
t9.new_ab()
t9.pitch_list("s b d b s f s")
t9.out("K")

# Winning team: COL
# WP: COL #32 Tyler Chatwood
game.winning_pitcher(32)

# Loser team: BOS
# LP: BOS #41 John Lackey
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
