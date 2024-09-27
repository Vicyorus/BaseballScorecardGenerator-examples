import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CLE, 2018-09-23
# https://www.baseball-reference.com/boxes/CLE/CLE201809230.shtml
# https://www.mlb.com/gameday/red-sox-vs-indians/2018/09/23/531729/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-23 19:07-23:27",
        "at": "Progressive Field, Cleveland, OH",
        "att": "27,879",
        "temp": "68F, Clear",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                25: "Steve Pearce",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                30: "Tzu-Wei Lin",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                59: "Sam Travis",
                28: "J.D. Martinez",
                23: "Blake Swihart",
                3: "Sandy León",
                0: "Brandon Phillips",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [2, "6"],
                [11, "5"],
                [25, "0"],
                [18, "3"],
                [5, "4"],
                [19, "8"],
                [7, "2"],
            ],
            "bench": [
                [30, "OF"],
                [36, "SS"],
                [12, "2B"],
                [59, "1B"],
                [28, "DH"],
                [23, "C"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 24, 46, 70, 56, 17, 32],
        },
        "home": {
            "team": "Cleveland Indians",
            "starter": 45,
            "roster": {
                # Lineup
                12: "Francisco Lindor",
                23: "Michael Brantley",
                11: "José Ramírez",
                10: "Edwin Encarnación",
                27: "Josh Donaldson",
                17: "Yonder Alonso",
                53: "Melky Cabrera",
                22: "Jason Kipnis",
                55: "Roberto Pérez",
                # Starting pitcher
                45: "Adam Plutko",
                # Bench
                1: "Greg Allen",
                9: "Erik González",
                6: "Brandon Guyer",
                7: "Yan Gomes",
                0: "Brandon Barnes",
                38: "Eric Haase",
                32: "Adam Rosales",
                36: "Yandy Díaz",
                26: "Rajai Davis",
                # Bullpen
                57: "Shane Bieber",
                46: "Jon Edwards",
                37: "Cody Allen",
                49: "Tyler Olson",
                24: "Andrew Miller",
                59: "Carlos Carrasco",
                58: "Neil Ramírez",
                39: "Oliver Pérez",
                52: "Mike Clevinger",
                90: "Adam Cimber",
                61: "Dan Otero",
                33: "Brad Hand",
                47: "Trevor Bauer",
                28: "Corey Kluber",
                43: "Josh Tomlin",
            },
            "lefties": [49, 24, 39, 33],
            "lineup": [
                [12, "6"],
                [23, "7"],
                [11, "4"],
                [10, "0"],
                [27, "5"],
                [17, "3"],
                [53, "9"],
                [22, "8"],
                [55, "2"],
            ],
            "bench": [
                [1, "CF"],
                [9, "SS"],
                [6, "LF"],
                [7, "C"],
                [0, "CF"],
                [38, "C"],
                [32, "SS"],
                [36, "1B"],
                [26, "CF"],
            ],
            "bullpen": [57, 46, 37, 49, 24, 59, 58, 39, 52, 90, 61, 33, 47, 28, 43],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Jerry Layne",
            "2B": "Jordan Baker",
            "3B": "Greg Gibson",
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
# Pitching: CLE #45 Adam Plutko
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c c b f f b")
t1.hit(2)
t1.advance(3, "16 SAC1-3")
t1.advance(4, "11 WP")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t1.new_ab()
t1.out("SAC1-3")

# 3. BOS #2  Xander Bogaerts (50 - X - X)
t1.new_ab()
t1.pitch_list("b f b b d")
t1.reach("BB")
t1.advance(2, "11 WP")

# 4. BOS #11 Rafael Devers (50 - X - 2)
t1.new_ab()
t1.pitch_list("s d s")
t1.wp()
t1.out("P6")

# 5. BOS #25 Steve Pearce (X - 2 - X)
t1.new_ab()
t1.pitch_list("s")
t1.out("F9")


# Bot 1st
# Pitching: BOS #76 Hector Velázquez
b1 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
b1.new_ab()
b1.pitch_list("c f b s")
b1.out("K")

# 2. CLE #23 Michael Brantley (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c f f f")
b1.out("G6-3")

# 3. CLE #11 José Ramírez (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CLE #45 Adam Plutko
t2 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b f f b f")
t2.out("F7")

# 7. BOS #5  Ian Kinsler (X - X - X)
t2.new_ab()
t2.pitch_list("c b b")
t2.out("P3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s f")
t2.out("L7")


# Bot 2nd
# Pitching: BOS #76 Hector Velázquez
b2 = game.new_inning()

# 4. CLE #10 Edwin Encarnación (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(3)
b2.thrown_out(4, "27 FC6-2", 1, 76)

# 5. CLE #27 Josh Donaldson (10 - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.reach("FC6-2")
b2.advance(2, "17 1B")

# 6. CLE #17 Yonder Alonso (X - X - 27)
b2.new_ab()
b2.hit(1)
b2.thrown_out(2, "53 DP4-6-3", 2, 76)

# 7. CLE #53 Melky Cabrera (X - 27 - 17)
b2.new_ab()
b2.pitch_list("f b b")
b2.out("DP4-6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CLE #45 Adam Plutko
t3 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b f f b")
t3.hit(1)
t3.advance(2, "50 1B")
t3.advance(3, "2 BB")
t3.advance(4, "11 G3")

# 1. BOS #50 Mookie Betts (X - X - 7)
t3.new_ab()
t3.pitch_list("b b f b f")
t3.hit(1)
t3.advance(2, "2 BB")
t3.advance(3, "11 G3")

# 2. BOS #16 Andrew Benintendi (X - 7 - 50)
t3.new_ab()
t3.pitch_list("b 2 b")
t3.out("IF6")

# 3. BOS #2  Xander Bogaerts (X - 7 - 50)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(2, "11 G3")

# 4. BOS #11 Rafael Devers (7 - 50 - 2)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G3", rbis=1)

# 5. BOS #25 Steve Pearce (50 - 2 - X)
t3.new_ab()
t3.pitch_list("s b b f")
t3.out("G3-1")


# Bot 3rd
# Pitching: BOS #76 Hector Velázquez
b3 = game.new_inning()

# 8. CLE #22 Jason Kipnis (X - X - X)
b3.new_ab()
b3.pitch_list("c b c")
b3.out("L7")

# 9. CLE #55 Roberto Pérez (X - X - X)
b3.new_ab()
b3.pitch_list("c c f b c")
b3.out("!K")

# 1. CLE #12 Francisco Lindor (X - X - X)
b3.new_ab()
b3.pitch_list("s f")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CLE #45 Adam Plutko
t4 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b c b f b b")
t4.reach("BB")

# 7. BOS #5  Ian Kinsler (X - X - 18)
t4.new_ab()
t4.pitch_list("b f f")
t4.out("(F)P3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 18)
t4.new_ab()
t4.pitch_list("b")
t4.out("F8")

# 9. BOS #7  Christian Vázquez (X - X - 18)
t4.new_ab()
t4.pitch_list("f")
t4.out("F9")


# Bot 4th
# Pitching: BOS #76 Hector Velázquez
b4 = game.new_inning()

# 2. CLE #23 Michael Brantley (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f b")
b4.hit(1)
b4.error(1)
b4.advance(2, "10 POE1")
b4.advance(3, "10 WP")
b4.advance(4, "10 1B")

# 3. CLE #11 José Ramírez (X - X - 23)
b4.new_ab()
b4.pitch_list("c f 1 s")
b4.out("K")

# 4. CLE #10 Edwin Encarnación (X - X - 23)
b4.new_ab()
b4.pitch_list("b 1 1 b s s")
b4.wp()
b4.hit(1, rbis=1)
b4.advance(2, "27 PB")
b4.advance(3, "17 E8")
b4.advance(4, "53 2B")

# Pitching change (BOS): #35 Steven Wright replaces #76 Hector Velázquez
b4.pitching_substitution(35)

# 5. CLE #27 Josh Donaldson (X - X - 10)
b4.new_ab()
b4.pitch_list("b c f s")
b4.pb()
b4.out("K")

# 6. CLE #17 Yonder Alonso (X - 10 - X)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1)
b4.error(8)
b4.advance(2, "E8")
b4.advance("U", "53 2B")

# 7. CLE #53 Melky Cabrera (10 - 17 - X)
b4.new_ab()
b4.pitch_list("c f")
b4.hit(2, rbis=2)

# 8. CLE #22 Jason Kipnis (X - 53 - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.out("P6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CLE #45 Adam Plutko
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c c b b b")
t5.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c b s")
t5.out("G6-3")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("f b f")
t5.hit(1)

# 4. BOS #11 Rafael Devers (X - X - 2)
t5.new_ab()
t5.pitch_list("f f c")
t5.out("!K")

# 5. BOS #25 Steve Pearce (X - X - 2)
t5.new_ab()
t5.pitch_list("f t")
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #66 Bobby Poyner
b5 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #35 Steven Wright
b5.pitching_substitution(66)

# Offensive change (CLE): Pinch-hitter #38 Eric Haase replaces #55 Roberto Pérez, batting 9th
b5.offensive_substitution(9, 38, "PH")

# 9. CLE #38 Eric Haase (X - X - X)
b5.new_ab()
b5.pitch_list("c s s")
b5.out("K")

# 1. CLE #12 Francisco Lindor (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G1-3")

# 2. CLE #23 Michael Brantley (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b f f f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CLE #45 Adam Plutko
t6 = game.new_inning()

# Defensive switch (CLE): #38 Eric Haase moves to C
t6.defensive_switch(38, "2")

# 6. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.out("F7")

# 7. BOS #5  Ian Kinsler (X - X - X)
t6.new_ab()
t6.pitch_list("b f b")
t6.out("F9")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("f b f f f c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #66 Bobby Poyner
b6 = game.new_inning()

# 3. CLE #11 José Ramírez (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f b f b b")
b6.reach("BB")
b6.thrown_out(2, "27 DP6-4-3", 2, 67)

# Pitching change (BOS): #67 William Cuevas replaces #66 Bobby Poyner
b6.pitching_substitution(67)

# 4. CLE #10 Edwin Encarnación (X - X - 11)
b6.new_ab()
b6.pitch_list("d c c b s")
b6.out("K")

# 5. CLE #27 Josh Donaldson (X - X - 11)
b6.new_ab()
b6.out("DP6-4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CLE #61 Dan Otero
t7 = game.new_inning()

# Pitching change (CLE): #61 Dan Otero replaces #45 Adam Plutko
t7.pitching_substitution(61)

# 9. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.hit(2)
t7.advance(3, "16 G4-3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("G4-3")

# 3. BOS #30 Tzu-Wei Lin (50 - X - X)
t7.new_ab()
t7.pitch_list("b c s f f d s")
t7.out("K")

# Offensive change (BOS): Pinch-hitter #30 Tzu-Wei Lin replaces #2 Xander Bogaerts, batting 3rd
# Note: this substitution came under a 2-strike count and ended with a strikeout.
t7.offensive_substitution(3, 30, "PH")


# Bot 7th
# Pitching: BOS #67 William Cuevas
b7 = game.new_inning()

# Defensive switch (BOS): #30 Tzu-Wei Lin moves to SS
b7.defensive_switch(30, "6")

# 6. CLE #17 Yonder Alonso (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 7. CLE #53 Melky Cabrera (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
# Offensive change (CLE): Pinch-runner #1 Greg Allen replaces #53 Melky Cabrera
b7.offensive_substitution(7, 1, "PR")
b7.atbase("PR")
b7.thrown_out(2, "22 CS", 3, 67)

# 8. CLE #22 Jason Kipnis (X - X - 53)
b7.new_ab()
b7.pitch_list("s 1 b s 1 b b s")
b7.out("KDP2-6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CLE #46 Jon Edwards
t8 = game.new_inning()

# Pitching change (CLE): #46 Jon Edwards replaces #61 Dan Otero
t8.pitching_substitution(46)

# Defensive switch (CLE): #1 Greg Allen moves to RF
t8.defensive_switch(1, "9")

# 4. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c b")
t8.reach("BB")
t8.advance(2, "25 BB")
t8.advance(3, "19 HBP")

# 5. BOS #25 Steve Pearce (X - X - 11)
t8.new_ab()
t8.pitch_list("b 1 b f 1 b b")
t8.reach("BB")
t8.advance(2, "19 HBP")

# 6. BOS #18 Mitch Moreland (X - 11 - 25)
t8.new_ab()
t8.pitch_list("d c b s")
t8.out("F9")

# Pitching change (CLE): #58 Neil Ramírez replaces #46 Jon Edwards
t8.pitching_substitution(58)

# 7. BOS #5  Ian Kinsler (X - 11 - 25)
t8.new_ab()
t8.pitch_list("c f f f f s")
t8.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - 25)
t8.new_ab()
t8.pitch_list("c b f")
t8.reach("HBP")

# 9. BOS #7  Christian Vázquez (11 - 25 - 19)
t8.new_ab()
t8.pitch_list("f f f")
t8.out("P4")


# Bot 8th
# Pitching: BOS #67 William Cuevas
b8 = game.new_inning()

# 9. CLE #38 Eric Haase (X - X - X)
b8.new_ab()
b8.pitch_list("s s b f f b f b f f s")
b8.out("K")

# 1. CLE #12 Francisco Lindor (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.reach("HBP")

# 2. CLE #23 Michael Brantley (X - X - 12)
b8.new_ab()
b8.pitch_list("b b f f f f f")
b8.out("P5")

# 3. CLE #11 José Ramírez (X - X - 12)
b8.new_ab()
b8.pitch_list("c")
b8.out("(F)P5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CLE #90 Adam Cimber
t9 = game.new_inning()

# Pitching change (CLE): #90 Adam Cimber replaces #58 Neil Ramírez
t9.pitching_substitution(90)

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("b c f f b s")
t9.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b s f f b")
t9.out("F8")

# 3. BOS #30 Tzu-Wei Lin (X - X - X)
t9.new_ab()
t9.pitch_list("c f b")
t9.hit(2)

# 4. BOS #11 Rafael Devers (X - 30 - X)
t9.new_ab()
t9.pitch_list("v v v v")
t9.reach("IBB")

# 5. BOS #25 Steve Pearce (X - 30 - 11)
t9.new_ab()
t9.pitch_list("b")
t9.out("G1-3")


# Bot 9th
# Pitching: BOS #67 William Cuevas
b9 = game.new_inning()

# 4. CLE #10 Edwin Encarnación (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c b")
b9.reach("BB")
# Offensive change (CLE): Pinch-runner #26 Rajai Davis replaces #10 Edwin Encarnación
b9.offensive_substitution(4, 26, "PR")
b9.atbase("PR")
b9.thrown_out(2, "27 CS", 1, 67)

# 5. CLE #27 Josh Donaldson (X - X - 10)
b9.new_ab()
b9.pitch_list("1 c 1 f f b 1 b b c")
b9.out("!K")

# 6. CLE #17 Yonder Alonso (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("L9")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: CLE #43 Josh Tomlin
t10 = game.new_inning()

# Pitching change (CLE): #43 Josh Tomlin replaces #90 Adam Cimber
t10.pitching_substitution(43)

# Defensive switch (CLE): #26 Rajai Davis moves to DH
t10.defensive_switch(26, "0")

# Defensive change (CLE): #9 Erik González replaces #27 Josh Donaldson (3B), playing 3B, batting 5th
t10.defensive_substitution(5, 9, "5")

# 6. BOS #18 Mitch Moreland (X - X - X)
t10.new_ab()
t10.pitch_list("c f b b s")
t10.out("K")

# 7. BOS #5  Ian Kinsler (X - X - X)
t10.new_ab()
t10.out("G5-3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t10.new_ab()
t10.pitch_list("f b b")
t10.hit(1)

# 9. BOS #7  Christian Vázquez (X - X - 19)
t10.new_ab()
t10.pitch_list("b 1 c s")
t10.out("F8")


# Bot 10th
# Pitching: BOS #67 William Cuevas
b10 = game.new_inning()

# 7. CLE #1  Greg Allen (X - X - X)
b10.new_ab()
b10.pitch_list("c f")
b10.out("G3-1")

# 8. CLE #22 Jason Kipnis (X - X - X)
b10.new_ab()
b10.pitch_list("b b c b c f")
b10.hit(2)
# Offensive change (CLE): Pinch-runner #0 Brandon Barnes replaces #22 Jason Kipnis
b10.offensive_substitution(8, 0, "PR")
b10.atbase("PR")
b10.advance(3, "12 G4-3")

# 9. CLE #38 Eric Haase (X - 22 - X)
b10.new_ab()
b10.pitch_list("s s b")
b10.hit(1)
b10.advance(2, "12 G4-3")

# 1. CLE #12 Francisco Lindor (X - 0 - 38)
b10.new_ab()
b10.pitch_list("f d f f f f")
b10.out("G4-3")

# 2. CLE #23 Michael Brantley (0 - 38 - X)
b10.new_ab()
b10.pitch_list("s b d")
b10.out("G3-1")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: CLE #43 Josh Tomlin
t11 = game.new_inning()

# Defensive change (CLE): #6 Brandon Guyer replaces #23 Michael Brantley (LF), playing LF, batting 2nd
t11.defensive_substitution(2, 6, "7")

# Defensive switch (CLE): #1 Greg Allen moves to CF
t11.defensive_switch(1, "8")

# Defensive switch (CLE): #0 Brandon Barnes moves to RF
t11.defensive_switch(0, "9")

# 1. BOS #50 Mookie Betts (X - X - X)
t11.new_ab()
t11.pitch_list("b b f c c")
t11.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t11.new_ab()
t11.pitch_list("b c f b")
t11.out("F7")

# 3. BOS #30 Tzu-Wei Lin (X - X - X)
t11.new_ab()
t11.pitch_list("b b b c b")
t11.reach("BB")

# 4. BOS #11 Rafael Devers (X - X - 30)
t11.new_ab()
t11.pitch_list("c 1")
t11.out("G1-3")


# Bot 11th
# Pitching: BOS #67 William Cuevas
b11 = game.new_inning()

# Defensive change (BOS): #23 Blake Swihart replaces #50 Mookie Betts (RF), playing RF, batting 1st
b11.defensive_substitution(1, 23, "9")

# Defensive change (BOS): #59 Sam Travis replaces #16 Andrew Benintendi (LF), playing LF, batting 2nd
b11.defensive_substitution(2, 59, "7")

# 3. CLE #11 José Ramírez (X - X - X)
b11.new_ab()
b11.pitch_list("c b b b c f f b")
b11.reach("BB")
b11.advance(2, "26 SAC2-4")
b11.advance(3, "9 E6")
b11.advance(4, "1 1B")

# 4. CLE #26 Rajai Davis (X - X - 11)
b11.new_ab()
b11.pitch_list("l")
b11.out("SAC2-4")

# 5. CLE #9  Erik González (X - 11 - X)
b11.new_ab()
b11.pitch_list("s b")
b11.error(6)
b11.reach("E6")
b11.advance(2, "36 IBB")
b11.advance(3, "1 1B")

# Pitching change (BOS): #63 Robby Scott replaces #67 William Cuevas
b11.pitching_substitution(63)

# Offensive change (CLE): Pinch-hitter #36 Yandy Díaz replaces #17 Yonder Alonso, batting 6th
b11.offensive_substitution(6, 36, "PH")

# 6. CLE #36 Yandy Díaz (11 - X - 9)
b11.new_ab()
b11.pitch_list("v v v v")
b11.reach("IBB")
b11.advance(2, "1 1B")

# 7. CLE #1  Greg Allen (11 - 9 - 36)
b11.new_ab()
b11.pitch_list("c b f f b b f")
b11.hit(1, rbis=1)

# Winning team: CLE
# WP: CLE #43 Josh Tomlin
game.winning_pitcher(43)

# Loser team: BOS
# LP: BOS #67 William Cuevas
game.losing_pitcher(67, is_away_team=True)

# print(game)
game.generate_scorecard()
