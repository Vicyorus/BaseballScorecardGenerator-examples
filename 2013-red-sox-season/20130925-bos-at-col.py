import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ COL, 2013-09-25
# https://www.baseball-reference.com/boxes/COL/COL201309250.shtml
# https://www.mlb.com/gameday/red-sox-vs-rockies/2013/09/25/349106/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2013-09-25 20:52-00:34 +1 (0:12 delay)",
        "at": "Coors Field, Denver, CO",
        "att": "48,775",
        "temp": "79F, Clear",
        "wind": "6mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 44,
            "roster": {
                # Lineup
                2: "Jacoby Ellsbury",
                18: "Shane Victorino",
                15: "Dustin Pedroia",
                34: "David Ortiz",
                29: "Daniel Nava",
                39: "Jarrod Saltalamacchia",
                7: "Stephen Drew",
                16: "Will Middlebrooks",
                44: "Jake Peavy",
                # Starting pitcher
                44: "Jake Peavy",
                # Bench
                50: "Quintin Berry",
                37: "Mike Carp",
                26: "Brock Holt",
                5: "Jonny Gomes",
                3: "David Ross",
                72: "Xander Bogaerts",
                25: "Jackie Bradley Jr.",
                12: "Mike Napoli",
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
                [2, "8"],
                [18, "9"],
                [15, "4"],
                [34, "3"],
                [29, "7"],
                [39, "2"],
                [7, "6"],
                [16, "5"],
                [44, "1"],
            ],
            "bench": [
                [50, "LF"],
                [37, "1B"],
                [26, "2B"],
                [5, "LF"],
                [3, "C"],
                [72, "2B"],
                [25, "CF"],
                [12, "1B"],
                [20, "C"],
                [10, "SS"],
                [23, "1B"],
            ],
            "bullpen": [35, 41, 67, 56, 60, 32, 66, 31, 36, 11, 64, 19, 38, 62, 22, 46],
        },
        "home": {
            "team": "Colorado Rockies",
            "starter": 45,
            "roster": {
                # Lineup
                19: "Charlie Blackmon",
                14: "Josh Rutledge",
                2: "Troy Tulowitzki",
                3: "Michael Cuddyer",
                17: "Todd Helton",
                28: "Nolan Arenado",
                6: "Corey Dickerson",
                8: "Yorvit Torrealba",
                45: "Jhoulys Chacín",
                # Starting pitcher
                45: "Jhoulys Chacín",
                # Bench
                24: "Dexter Fowler",
                9: "DJ LeMahieu",
                15: "Jordan Pacheco",
                20: "Wilin Rosario",
                23: "Charlie Culberson",
                5: "Carlos González",
                18: "Jonathan Herrera",
                4: "Ryan Wheeler",
                # Bullpen
                44: "Roy Oswalt",
                34: "Matt Belisle",
                35: "Chad Bettis",
                49: "Rex Brothers",
                0: "Adam Ottavino",
                32: "Tyler Chatwood",
                59: "Wilton Lopez",
                13: "Drew Pomeranz",
                43: "Collin McHugh",
                50: "Jeff Manship",
                12: "Juan Nicasio",
                62: "Rob Scahill",
                60: "Manny Corpas",
                29: "Jorge De La Rosa",
                88: "Josh Outman",
                26: "Jeff Francis",
                41: "Mitchell Boggs",
            },
            "lefties": [49, 13, 29, 88, 26],
            "lineup": [
                [19, "8"],
                [14, "4"],
                [2, "6"],
                [3, "9"],
                [17, "3"],
                [28, "5"],
                [6, "7"],
                [8, "2"],
                [45, "1"],
            ],
            "bench": [
                [24, "CF"],
                [9, "3B"],
                [15, "1B"],
                [20, "1B"],
                [23, "1B"],
                [5, "RF"],
                [18, "2B"],
                [4, "3B"],
            ],
            "bullpen": [44, 34, 35, 49, 0, 32, 59, 13, 43, 50, 12, 62, 60, 29, 88, 26, 41],
        },
        "umpires": {
            "HP": "Andy Fletcher",
            "1B": "Rob Drake",
            "2B": "Joe West",
            "3B": "Sam Holbrook",
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
# Pitching: COL #45 Jhoulys Chacín
t1 = game.new_inning()

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t1.new_ab()
t1.pitch_list("c c b f f f")
t1.hit(1)
t1.advance(2, "18 1B")
t1.advance(3, "15 FC6")
t1.advance(4, "34 2B")

# 2. BOS #18 Shane Victorino (X - X - 2)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.thrown_out(2, "15 FC6", 1, 45)

# 3. BOS #15 Dustin Pedroia (X - 2 - 18)
t1.new_ab(is_risp=True)
t1.pitch_list("c s")
t1.reach("FC6")
t1.advance(4, "34 2B")

# 4. BOS #34 David Ortiz (2 - X - 15)
t1.new_ab(is_risp=True)
t1.pitch_list("b f b b")
t1.hit(2, rbis=2)
t1.advance(4, "39 1B")

# 5. BOS #29 Daniel Nava (X - 34 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("L8")

# 6. BOS #39 Jarrod Saltalamacchia (X - 34 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b")
t1.hit(1, rbis=1)
t1.advance(3, "7 1B")

# 7. BOS #7  Stephen Drew (X - X - 39)
t1.new_ab()
t1.hit(1)

# 8. BOS #16 Will Middlebrooks (39 - X - 7)
t1.new_ab(is_risp=True)
t1.pitch_list("s b")
t1.out("G1-3")


# Bot 1st
# Pitching: BOS #44 Jake Peavy
b1 = game.new_inning()

# 1. COL #19 Charlie Blackmon (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G6-3")

# 2. COL #14 Josh Rutledge (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K")

# 3. COL #2  Troy Tulowitzki (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("L9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: COL #45 Jhoulys Chacín
t2 = game.new_inning()

# 9. BOS #44 Jake Peavy (X - X - X)
t2.new_ab()
t2.pitch_list("b c f")
t2.out("G5-3")

# 1. BOS #2  Jacoby Ellsbury (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("G4-3")

# 2. BOS #18 Shane Victorino (X - X - X)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("(F)P2")


# Bot 2nd
# Pitching: BOS #44 Jake Peavy
b2 = game.new_inning()

# 4. COL #3  Michael Cuddyer (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("L9")

# 5. COL #17 Todd Helton (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.hit(4)

# 6. COL #28 Nolan Arenado (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("L9")

# 7. COL #6  Corey Dickerson (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b f f b")
b2.reach("BB")
b2.advance(4, "8 2B")

# 8. COL #8  Yorvit Torrealba (X - X - 6)
b2.new_ab()
b2.pitch_list("s f")
b2.hit(2, rbis=1)

# 9. COL #45 Jhoulys Chacín (X - 8 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: COL #45 Jhoulys Chacín
t3 = game.new_inning()

# 3. BOS #15 Dustin Pedroia (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.out("G6-3")

# 4. BOS #34 David Ortiz (X - X - X)
t3.new_ab()
t3.pitch_list("c s b t")
t3.out("KT")

# 5. BOS #29 Daniel Nava (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.advance(4, "39 2B")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 29)
t3.new_ab()
t3.pitch_list("1 f b s")
t3.hit(2, rbis=1)

# 7. BOS #7  Stephen Drew (X - 39 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b d f b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #44 Jake Peavy
b3 = game.new_inning()

# 1. COL #19 Charlie Blackmon (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(3, "14 1B")
b3.advance(4, "17 SF7")

# 2. COL #14 Josh Rutledge (X - X - 19)
b3.new_ab()
b3.hit(1)
b3.advance(2, "2 SB")
b3.advance(3, "17 SF7")
b3.advance(4, "28 2B")

# 3. COL #2  Troy Tulowitzki (19 - X - 14)
b3.new_ab(is_risp=True)
b3.pitch_list("b b f b b")
b3.reach("BB")
b3.advance(3, "28 2B")

# 4. COL #3  Michael Cuddyer (19 - 14 - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("s b f f s")
b3.out("K")

# 5. COL #17 Todd Helton (19 - 14 - 2)
b3.new_ab(is_risp=True)
b3.out("SF7", rbis=1)

# 6. COL #28 Nolan Arenado (14 - X - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("b f s d f b")
b3.hit(2, rbis=1)

# 7. COL #6  Corey Dickerson (2 - 28 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b b c f b f b")
b3.reach("BB")

# 8. COL #8  Yorvit Torrealba (2 - 28 - 6)
b3.new_ab(is_risp=True)
b3.pitch_list("f")
b3.out("L9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: COL #45 Jhoulys Chacín
t4 = game.new_inning()

# 8. BOS #16 Will Middlebrooks (X - X - X)
t4.new_ab()
t4.pitch_list("c b b s s")
t4.out("K")

# 9. BOS #44 Jake Peavy (X - X - X)
t4.new_ab()
t4.hit(2)
t4.advance(4, "18 HR")

# 1. BOS #2  Jacoby Ellsbury (X - 44 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c b b b")
t4.reach("BB")
t4.advance(4, "18 HR")

# 2. BOS #18 Shane Victorino (X - 44 - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b c c f f d b")
t4.hit(4, rbis=3)

# 3. BOS #15 Dustin Pedroia (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("P3")

# 4. BOS #34 David Ortiz (X - X - X)
t4.new_ab()
t4.pitch_list("f b b b b")
t4.reach("BB")

# 5. BOS #29 Daniel Nava (X - X - 34)
t4.new_ab()
t4.pitch_list("b f f b b")
t4.out("L3")


# Bot 4th
# Pitching: BOS #44 Jake Peavy
b4 = game.new_inning()

# Defensive change (BOS): #25 Jackie Bradley Jr. replaces #2 Jacoby Ellsbury (CF), playing CF, batting 1st
b4.defensive_substitution(1, 25, "8")

# Offensive change (COL): Pinch-hitter #23 Charlie Culberson replaces #45 Jhoulys Chacín, batting 9th
b4.offensive_substitution(9, 23, "PH")

# 9. COL #23 Charlie Culberson (X - X - X)
b4.new_ab()
b4.out("G6-3")

# 1. COL #19 Charlie Blackmon (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L8")

# 2. COL #14 Josh Rutledge (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)

# 3. COL #2  Troy Tulowitzki (X - X - 14)
b4.new_ab()
b4.pitch_list("s b c c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: COL #62 Rob Scahill
t5 = game.new_inning()

# Pitching change (COL): #62 Rob Scahill replaces #45 Jhoulys Chacín, batting 9th
t5.pitching_substitution(62)
t5.defensive_substitution(9, 62, "1")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - X)
t5.new_ab()
t5.pitch_list("f f b b")
t5.hit(1)
t5.advance(3, "7 2B")
t5.advance(4, "16 HR")

# 7. BOS #7  Stephen Drew (X - X - 39)
t5.new_ab()
t5.pitch_list("f b f f f")
t5.hit(2)
t5.advance(4, "16 HR")

# 8. BOS #16 Will Middlebrooks (39 - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("d b c b c f")
t5.hit(4, rbis=3)

# 9. BOS #44 Jake Peavy (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("G6-3")

# 1. BOS #25 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("L3")

# 2. BOS #18 Shane Victorino (X - X - X)
t5.new_ab()
t5.pitch_list("c b s")
t5.out("G5-3")


# Bot 5th
# Pitching: BOS #44 Jake Peavy
b5 = game.new_inning()

# 4. COL #3  Michael Cuddyer (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f b f b f f f f f f b")
b5.reach("BB")
b5.advance(4, "17 2B")

# 5. COL #17 Todd Helton (X - X - 3)
b5.new_ab()
b5.hit(2, rbis=1)
b5.advance(3, "28 1B")

# 6. COL #28 Nolan Arenado (X - 17 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d f f d")
b5.hit(1)
b5.thrown_out(2, "8 DP5-4-3", 2, 44)

# 7. COL #6  Corey Dickerson (17 - X - 28)
b5.new_ab(is_risp=True)
b5.pitch_list("b s f b s")
b5.out("K")

# 8. COL #8  Yorvit Torrealba (17 - X - 28)
b5.new_ab(is_risp=True)
b5.pitch_list("b b s")
b5.out("DP5-4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: COL #13 Drew Pomeranz
t6 = game.new_inning()

# Pitching change (COL): #13 Drew Pomeranz replaces #62 Rob Scahill, batting 9th
t6.pitching_substitution(13)
t6.defensive_substitution(9, 13, "1")

# Defensive change (COL): #15 Jordan Pacheco replaces #8 Yorvit Torrealba (C), playing C, batting 8th
t6.defensive_substitution(8, 15, "2")

# 3. BOS #15 Dustin Pedroia (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b")
t6.error(6)
t6.reach("E6")
t6.thrown_out(2, "39 FC5-4", 3, 13)

# 4. BOS #34 David Ortiz (X - X - 15)
t6.new_ab()
t6.pitch_list("s f s")
t6.out("K")

# 5. BOS #29 Daniel Nava (X - X - 15)
t6.new_ab()
t6.pitch_list("b f c f s")
t6.out("K")

# 6. BOS #39 Jarrod Saltalamacchia (X - X - 15)
t6.new_ab()
t6.pitch_list("c")
t6.reach("FC5-4")


# Bot 6th
# Pitching: BOS #44 Jake Peavy
b6 = game.new_inning()

# Defensive change (BOS): #23 Brandon Snyder replaces #34 David Ortiz (1B), playing 1B, batting 4th
b6.defensive_substitution(4, 23, "3")

# Offensive change (COL): Pinch-hitter #18 Jonathan Herrera replaces #13 Drew Pomeranz, batting 9th
b6.offensive_substitution(9, 18, "PH")

# 9. COL #18 Jonathan Herrera (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G3")

# 1. COL #19 Charlie Blackmon (X - X - X)
b6.new_ab()
b6.pitch_list("c b s f f b")
b6.out("P5")

# 2. COL #14 Josh Rutledge (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: COL #34 Matt Belisle
t7 = game.new_inning()

# Pitching change (COL): #34 Matt Belisle replaces #13 Drew Pomeranz, batting 9th
t7.pitching_substitution(34)
t7.defensive_substitution(9, 34, "1")

# 7. BOS #7  Stephen Drew (X - X - X)
t7.new_ab()
t7.out("F7")

# 8. BOS #16 Will Middlebrooks (X - X - X)
t7.new_ab()
t7.pitch_list("c b c f c")
t7.out("!K")

# Offensive change (BOS): Pinch-hitter #37 Mike Carp replaces #44 Jake Peavy, batting 9th
t7.offensive_substitution(9, 37, "PH")

# 9. BOS #37 Mike Carp (X - X - X)
t7.new_ab()
t7.pitch_list("t f b b b b")
t7.reach("BB")

# 1. BOS #25 Jackie Bradley Jr. (X - X - 37)
t7.new_ab()
t7.pitch_list("c b f d f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #36 Junichi Tazawa
b7 = game.new_inning()

# Pitching change (BOS): #36 Junichi Tazawa replaces #44 Jake Peavy, batting 9th
b7.pitching_substitution(36)
b7.defensive_substitution(9, 36, "1")

# 3. COL #2  Troy Tulowitzki (X - X - X)
b7.new_ab()
b7.pitch_list("c c s")
b7.out("K")

# 4. COL #3  Michael Cuddyer (X - X - X)
b7.new_ab()
b7.pitch_list("b b f f")
b7.hit(1)
b7.thrown_out(1, "17 PO", 2, 56)

# Pitching change (BOS): #56 Franklin Morales replaces #36 Junichi Tazawa, batting 9th
b7.pitching_substitution(56)
b7.defensive_substitution(9, 56, "1")

# 5. COL #17 Todd Helton (X - X - 3)
b7.new_ab()
b7.pitch_list("1 b b f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: COL #44 Roy Oswalt
t8 = game.new_inning()

# Pitching change (COL): #44 Roy Oswalt replaces #34 Matt Belisle, batting 9th
t8.pitching_substitution(44)
t8.defensive_substitution(9, 44, "1")

# 2. BOS #18 Shane Victorino (X - X - X)
t8.new_ab()
t8.pitch_list("b c f b")
t8.hit(1)
t8.advance(2, "23 HBP")
t8.advance(3, "29 1B")
t8.advance(4, "39 1B")

# 3. BOS #15 Dustin Pedroia (X - X - 18)
t8.new_ab()
t8.pitch_list("b")
t8.out("F9")

# 4. BOS #23 Brandon Snyder (X - X - 18)
t8.new_ab()
t8.pitch_list("c s f")
t8.reach("HBP")
t8.advance(2, "29 1B")
t8.advance(3, "39 1B")
t8.advance(4, "16 HR")

# 5. BOS #29 Daniel Nava (X - 18 - 23)
t8.new_ab(is_risp=True)
t8.pitch_list("f b b f")
t8.hit(1)
t8.advance(2, "39 1B")
t8.advance(4, "16 HR")

# 6. BOS #39 Jarrod Saltalamacchia (18 - 23 - 29)
t8.new_ab(is_risp=True)
t8.pitch_list("c c f f f")
t8.hit(1, rbis=1)
t8.advance(4, "16 HR")

# 7. BOS #7  Stephen Drew (23 - 29 - 39)
t8.new_ab(is_risp=True)
t8.out("IF6")

# 8. BOS #16 Will Middlebrooks (23 - 29 - 39)
t8.new_ab(is_risp=True)
t8.pitch_list("c f f")
t8.hit(4, rbis=4)

# Offensive change (BOS): Pinch-hitter #72 Xander Bogaerts replaces #56 Franklin Morales, batting 9th
t8.offensive_substitution(9, 72, "PH")

# 9. BOS #72 Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("t b s f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Craig Breslow
b8 = game.new_inning()

# Pitching change (BOS): #32 Craig Breslow replaces #56 Franklin Morales, batting 9th
b8.pitching_substitution(32)
b8.defensive_substitution(9, 32, "1")

# Defensive change (BOS): #10 John McDonald replaces #15 Dustin Pedroia (2B), playing 2B, batting 3rd
b8.defensive_substitution(3, 10, "4")

# Defensive change (BOS): #50 Quintin Berry replaces #18 Shane Victorino (RF), playing RF, batting 2nd
b8.defensive_substitution(2, 50, "9")

# 6. COL #28 Nolan Arenado (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F8")

# 7. COL #6  Corey Dickerson (X - X - X)
b8.new_ab()
b8.out("G4-3")

# 8. COL #15 Jordan Pacheco (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: COL #49 Rex Brothers
t9 = game.new_inning()

# Pitching change (COL): #49 Rex Brothers replaces #44 Roy Oswalt, batting 9th
t9.pitching_substitution(49)
t9.defensive_substitution(9, 49, "1")

# 1. BOS #25 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("f s b b b")
t9.out("F7")

# 2. BOS #50 Quintin Berry (X - X - X)
t9.new_ab()
t9.pitch_list("b f b b b")
t9.reach("BB")
t9.thrown_out(2, "10 FC5-4", 2, 49)

# 3. BOS #10 John McDonald (X - X - 50)
t9.new_ab()
t9.pitch_list("c b b f")
t9.reach("FC5-4")

# 4. BOS #23 Brandon Snyder (X - X - 10)
t9.new_ab()
t9.pitch_list("d c f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #46 Ryan Dempster
b9 = game.new_inning()

# Pitching change (BOS): #46 Ryan Dempster replaces #32 Craig Breslow, batting 9th
b9.pitching_substitution(46)
b9.defensive_substitution(9, 46, "1")

# Offensive change (COL): Pinch-hitter #4 Ryan Wheeler replaces #49 Rex Brothers, batting 9th
b9.offensive_substitution(9, 4, "PH")

# 9. COL #4  Ryan Wheeler (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c")
b9.hit(1)
b9.thrown_out(1, "19 DP3", 2, 46)

# 1. COL #19 Charlie Blackmon (X - X - 4)
b9.new_ab()
b9.out("DP3")

# 2. COL #14 Josh Rutledge (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("F7")

# Winning team: BOS
# WP: BOS #44 Jake Peavy
game.winning_pitcher(44, is_away_team=True)

# Loser team: COL
# LP: COL #45 Jhoulys Chacín
game.losing_pitcher(45)

# print(game)
game.generate_scorecard()
