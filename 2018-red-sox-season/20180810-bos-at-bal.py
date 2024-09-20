import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-08-10
# https://www.baseball-reference.com/boxes/BAL/BAL201808100.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/08/10/531143/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-10 19:08-23:09",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "23,649",
        "temp": "89F, Partly Cloudy",
        "wind": "4mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                68: "Dan Butler",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [68, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 37,
            "roster": {
                # Lineup
                34: "Jonathan Villar",
                1: "Tim Beckham",
                10: "Adam Jones",
                45: "Mark Trumbo",
                16: "Trey Mancini",
                19: "Chris Davis",
                39: "Renato Núñez",
                36: "Caleb Joseph",
                3: "Cedric Mullins",
                # Starting pitcher
                37: "Dylan Bundy",
                # Bench
                29: "Jace Peterson",
                61: "Austin Wynns",
                23: "Joey Rickard",
                # Bullpen
                17: "Alex Cobb",
                32: "Yefry Ramírez",
                41: "David Hess",
                49: "Cody Carroll",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                51: "Paul Fry",
                58: "Evan Phillips",
                60: "Mychal Givens",
                57: "Donnie Hart",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
            },
            "lefties": [66, 51, 57],
            "lineup": [
                [34, "4"],
                [1, "6"],
                [10, "9"],
                [45, "0"],
                [16, "7"],
                [19, "3"],
                [39, "5"],
                [36, "2"],
                [3, "8"],
            ],
            "bench": [
                [29, "SS"],
                [61, "C"],
                [23, "RF"],
            ],
            "bullpen": [17, 32, 41, 49, 66, 54, 51, 58, 60, 57, 43, 50],
        },
        "umpires": {
            "HP": "Marvin Hudson",
            "1B": "Tripp Gibson",
            "2B": "Hunter Wendelstedt",
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
# Pitching: BAL #37 Dylan Bundy
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.thrown_out(2, "18 FC5-6", 2, 37)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.out("L7")

# 3. BOS #18 Mitch Moreland (X - X - 50)
t1.new_ab()
t1.pitch_list("1 c b s f 1")
t1.reach("FC5-6")
t1.advance(3, "28 2B")
t1.advance(4, "2 HR")

# 4. BOS #28 J.D. Martinez (X - X - 18)
t1.new_ab()
t1.pitch_list("b b s")
t1.hit(2)
t1.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (18 - 28 - X)
t1.new_ab()
t1.pitch_list("b s f f f")
t1.hit(4, rbis=3)

# 6. BOS #11 Rafael Devers (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #17 Nathan Eovaldi
b1 = game.new_inning()

# 1. BAL #34 Jonathan Villar (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b b b")
b1.reach("BB")
b1.thrown_out(2, "1 DP4-6-3", 1, 17)

# 2. BAL #1  Tim Beckham (X - X - 34)
b1.new_ab()
b1.pitch_list("c")
b1.out("DP4-6-3")

# 3. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.hit(1)
b1.advance(2, "45 1B")

# 4. BAL #45 Mark Trumbo (X - X - 10)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)

# 5. BAL #16 Trey Mancini (X - 10 - 45)
b1.new_ab()
b1.pitch_list("b b c f b f f")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #37 Dylan Bundy
t2 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(3, "50 2B")

# 8. BOS #68 Dan Butler (X - X - 12)
t2.new_ab()
t2.pitch_list("c c t")
t2.out("KT")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 12)
t2.new_ab()
t2.pitch_list("1")
t2.out("P6")

# 1. BOS #50 Mookie Betts (X - X - 12)
t2.new_ab()
t2.pitch_list("d c f 1")
t2.hit(2)

# 2. BOS #16 Andrew Benintendi (12 - 50 - X)
t2.new_ab()
t2.out("P4")


# Bot 2nd
# Pitching: BOS #17 Nathan Eovaldi
b2 = game.new_inning()

# 6. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(4)

# 7. BAL #39 Renato Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b b f b b")
b2.reach("BB")
b2.advance(2, "36 1B")
b2.advance(4, "3 2B")

# 8. BAL #36 Caleb Joseph (X - X - 39)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(3, "3 2B")
b2.advance(4, "10 1B")

# 9. BAL #3  Cedric Mullins (X - 39 - 36)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(2, rbis=1)
b2.advance(4, "10 1B")

# 1. BAL #34 Jonathan Villar (36 - 3 - X)
b2.new_ab()
b2.pitch_list("f b s f")
b2.out("F8")

# 2. BAL #1  Tim Beckham (36 - 3 - X)
b2.new_ab()
b2.pitch_list("d b")
b2.out("P4")

# 3. BAL #10 Adam Jones (36 - 3 - X)
b2.new_ab()
b2.hit(1, rbis=2)

# 4. BAL #45 Mark Trumbo (X - X - 10)
b2.new_ab()
b2.pitch_list("b c f b")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #37 Dylan Bundy
t3 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
t3.new_ab()
t3.pitch_list("b c b s s")
t3.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f f s")
t3.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #17 Nathan Eovaldi
b3 = game.new_inning()

# 5. BAL #16 Trey Mancini (X - X - X)
b3.new_ab()
b3.out("L9")

# 6. BAL #19 Chris Davis (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "39 1B")
b3.advance("U", "36 E8")

# 7. BAL #39 Renato Núñez (X - X - 19)
b3.new_ab()
b3.pitch_list("b c")
b3.hit(1)
b3.advance(3, "36 E8")
b3.advance("U", "3 1B")

# 8. BAL #36 Caleb Joseph (X - 19 - 39)
b3.new_ab()
b3.pitch_list("c f b b")
b3.error(8)
b3.reach("E8", end_base=2)
b3.advance(3, "3 1B")
b3.advance("U", "34 SAC1-3")

# 9. BAL #3  Cedric Mullins (39 - 36 - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1, rbis=1)
b3.advance(2, "34 SAC1-3")
b3.advance("U", "1 1B")

# 1. BAL #34 Jonathan Villar (36 - X - 3)
b3.new_ab()
b3.pitch_list("b b f 1")
b3.out("SAC1-3", rbis=1)

# 2. BAL #1  Tim Beckham (X - 3 - X)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(1, rbis=1)
b3.thrown_out(2, "10 CS", 3, 44)

# Pitching change (BOS): #44 Brandon Workman replaces #17 Nathan Eovaldi
b3.pitching_substitution(44)

# 3. BAL #10 Adam Jones (X - X - 1)
b3.new_ab()
b3.pitch_list("c b")
b3.no_ab("CS")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #37 Dylan Bundy
t4 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G3-1")

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")
t4.advance(4, "19 3B")

# 8. BOS #68 Dan Butler (X - X - 12)
t4.new_ab()
t4.pitch_list("c")
t4.out("F8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 12)
t4.new_ab()
t4.pitch_list("c")
t4.hit(3, rbis=1)
t4.advance("U", "50 PB")

# 1. BOS #50 Mookie Betts (19 - X - X)
t4.new_ab()
t4.pitch_list("c f b f")
t4.pb()
t4.out("F9")


# Bot 4th
# Pitching: BOS #44 Brandon Workman
b4 = game.new_inning()

# 3. BAL #10 Adam Jones (X - X - X)
b4.new_ab()
b4.pitch_list("f b s b f b")
b4.hit(1)
b4.advance(2, "45 SB")

# 4. BAL #45 Mark Trumbo (X - X - 10)
b4.new_ab()
b4.pitch_list("b b c b c s")
b4.out("K")

# 5. BAL #16 Trey Mancini (X - 10 - X)
b4.new_ab()
b4.pitch_list("b b c s s")
b4.out("K")

# 6. BAL #19 Chris Davis (X - 10 - X)
b4.new_ab()
b4.pitch_list("b f c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #37 Dylan Bundy
t5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b")
t5.out("(F)P5")

# 3. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(2)
t5.advance(3, "28 G4-3")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
t5.new_ab()
t5.pitch_list("s c b")
t5.out("G4-3")

# 5. BOS #2  Xander Bogaerts (18 - X - X)
t5.new_ab()
t5.pitch_list("b b d b")
t5.reach("BB")
t5.advance(2, "11 SB")

# 6. BOS #11 Rafael Devers (18 - X - 2)
t5.new_ab()
t5.pitch_list("c b s b")
t5.out("F8")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #44 Brandon Workman
b5.pitching_substitution(31)

# 7. BAL #39 Renato Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("G5-3")

# 8. BAL #36 Caleb Joseph (X - X - X)
b5.new_ab()
b5.pitch_list("c b f f s")
b5.out("K")

# 9. BAL #3  Cedric Mullins (X - X - X)
b5.new_ab()
b5.pitch_list("b c f b b b")
b5.reach("BB")

# 1. BAL #34 Jonathan Villar (X - X - 3)
b5.new_ab()
b5.pitch_list("c b f d f f 1")
b5.out("L7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #37 Dylan Bundy
t6 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.hit(4)

# 8. BOS #68 Dan Butler (X - X - X)
t6.new_ab()
t6.pitch_list("s c")
t6.hit(1)
t6.advance(2, "19 BB")
t6.advance(3, "50 BB")
t6.thrown_out(4, "16 FC3-2", 1, 50)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 68)
t6.new_ab()
t6.pitch_list("c b b d b")
t6.reach("BB")
t6.advance(2, "50 BB")
t6.advance(3, "16 FC3-2")
t6.advance(4, "18 SF8")

# Pitching change (BAL): #50 Miguel Castro replaces #37 Dylan Bundy
t6.pitching_substitution(50)

# 1. BOS #50 Mookie Betts (X - 68 - 19)
t6.new_ab()
t6.pitch_list("c d b b s b")
t6.reach("BB")
t6.advance(2, "16 FC3-2")
t6.advance(3, "18 SF8")
t6.advance(4, "2 BB")

# 2. BOS #16 Andrew Benintendi (68 - 19 - 50)
t6.new_ab()
t6.pitch_list("d")
t6.reach("FC3-2")
t6.advance(2, "18 SF8")
t6.advance(3, "2 BB")
t6.advance(4, "11 BB")

# 3. BOS #18 Mitch Moreland (19 - 50 - 16)
t6.new_ab()
t6.pitch_list("f b f f b")
t6.out("SF8", rbis=1)

# 4. BOS #28 J.D. Martinez (50 - 16 - X)
t6.new_ab()
t6.pitch_list("v v v v")
t6.reach("IBB")
t6.advance(2, "2 BB")
t6.advance(3, "11 BB")
t6.advance(4, "12 1B")

# 5. BOS #2  Xander Bogaerts (50 - 16 - 28)
t6.new_ab()
t6.pitch_list("b b b c b")
t6.reach("BB", rbis=1)
t6.advance(2, "11 BB")
t6.advance(4, "12 1B")

# Pitching change (BAL): #57 Donnie Hart replaces #50 Miguel Castro
t6.pitching_substitution(57)

# 6. BOS #11 Rafael Devers (16 - 28 - 2)
t6.new_ab()
t6.pitch_list("b b c c b b")
t6.reach("BB", rbis=1)
t6.advance(3, "12 1B")

# 7. BOS #12 Brock Holt (28 - 2 - 11)
t6.new_ab()
t6.pitch_list("b b c")
t6.hit(1, rbis=2)

# 8. BOS #68 Dan Butler (11 - X - 12)
t6.new_ab()
t6.pitch_list("b c")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #37 Heath Hembree
b6 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #31 Drew Pomeranz
b6.pitching_substitution(37)

# 2. BAL #1  Tim Beckham (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(4)

# 3. BAL #10 Adam Jones (X - X - X)
b6.new_ab()
b6.pitch_list("s b")
b6.out("G5-3")

# 4. BAL #45 Mark Trumbo (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.hit(1)
b6.advance(3, "16 2B")
b6.advance(4, "19 SF9")

# 5. BAL #16 Trey Mancini (X - X - 45)
b6.new_ab()
b6.pitch_list("s")
b6.hit(2)
b6.advance(3, "39 PB")

# 6. BAL #19 Chris Davis (45 - 16 - X)
b6.new_ab()
b6.pitch_list("s f f b f b")
b6.out("SF9", rbis=1)

# 7. BAL #39 Renato Núñez (X - 16 - X)
b6.new_ab()
b6.pitch_list("c b f b b f f b")
b6.pb()
b6.reach("BB")

# 8. BAL #36 Caleb Joseph (16 - X - 39)
b6.new_ab()
b6.pitch_list("b s")
b6.out("L8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #57 Donnie Hart
t7 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.hit(2)
t7.advance(3, "50 1B")
t7.advance(4, "16 HR")

# 1. BOS #50 Mookie Betts (X - 19 - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(4, "16 HR")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
t7.new_ab()
t7.pitch_list("f")
t7.hit(4, rbis=3)

# 3. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("b f b s")
t7.hit(1)
t7.thrown_out(2, "28 DP6-4-3", 1, 58)

# Pitching change (BAL): #58 Evan Phillips replaces #57 Donnie Hart
t7.pitching_substitution(58)

# 4. BOS #28 J.D. Martinez (X - X - 18)
t7.new_ab()
t7.pitch_list("b b")
t7.out("DP6-4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #70 Ryan Brasier
b7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #37 Heath Hembree
b7.pitching_substitution(70)

# 9. BAL #3  Cedric Mullins (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F7")

# 1. BAL #34 Jonathan Villar (X - X - X)
b7.new_ab()
b7.pitch_list("f s s")
b7.out("K")

# 2. BAL #1  Tim Beckham (X - X - X)
b7.new_ab()
b7.pitch_list("f s c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #58 Evan Phillips
t8 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("b b f b")
t8.out("G6-3")

# 7. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b b")
t8.reach("BB")
t8.advance(2, "25 HBP")
t8.advance(3, "19 1B")
t8.advance(4, "50 2B")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #68 Dan Butler, batting 8th
t8.offensive_substitution(8, 25, "PH")

# 8. BOS #25 Steve Pearce (X - X - 12)
t8.new_ab()
t8.pitch_list("b")
t8.reach("HBP")
t8.advance(2, "19 1B")
t8.advance(4, "50 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - 25)
t8.new_ab()
t8.hit(1)
t8.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (12 - 25 - 19)
t8.new_ab()
t8.pitch_list("c f b")
t8.hit(2, rbis=3)
t8.advance(3, "16 WP")
t8.advance(4, "28 1B")

# Pitching change (BAL): #66 Tanner Scott replaces #58 Evan Phillips
t8.pitching_substitution(66)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t8.new_ab()
t8.pitch_list("c b b b b")
t8.wp()
t8.reach("BB")
t8.advance(2, "18 WP")
t8.advance(4, "28 1B")

# 3. BOS #18 Mitch Moreland (50 - X - 16)
t8.new_ab()
t8.pitch_list("c s b f")
t8.wp()
t8.out("G3")

# 4. BOS #28 J.D. Martinez (50 - 16 - X)
t8.new_ab()
t8.hit(1, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t8.new_ab()
t8.pitch_list("c s b f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #70 Ryan Brasier
b8.pitching_substitution(32)

# Defensive change (BOS): #3 Sandy León replaces #16 Andrew Benintendi (LF), playing C, batting 2nd
b8.defensive_substitution(2, 3, "2")

# Defensive switch (BOS): #25 Steve Pearce moves to LF
b8.defensive_switch(25, "7")

# 3. BAL #10 Adam Jones (X - X - X)
b8.new_ab()
b8.out("F9")

# 4. BAL #45 Mark Trumbo (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(4)

# 5. BAL #16 Trey Mancini (X - X - X)
b8.new_ab()
b8.pitch_list("b c s b f c")
b8.out("!K")

# 6. BAL #19 Chris Davis (X - X - X)
b8.new_ab()
b8.pitch_list("b c s s")
b8.out("K2-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #66 Tanner Scott
t9 = game.new_inning()

# Defensive change (BAL): #23 Joey Rickard replaces #10 Adam Jones (RF), playing RF, batting 3rd
t9.defensive_substitution(3, 23, "9")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b s f b s")
t9.out("K2-3")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("s c s")
t9.out("K")

# 8. BOS #25 Steve Pearce (X - X - X)
t9.new_ab()
t9.pitch_list("b c b")
t9.out("F9")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b9.pitching_substitution(56)

# 7. BAL #39 Renato Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("c c f b f s")
b9.out("K2-3")

# 8. BAL #36 Caleb Joseph (X - X - X)
b9.new_ab()
b9.pitch_list("f f b s")
b9.out("K")

# 9. BAL #3  Cedric Mullins (X - X - X)
b9.new_ab()
b9.pitch_list("f b")
b9.hit(2)
b9.advance(4, "34 1B")

# 1. BAL #34 Jonathan Villar (X - 3 - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1, rbis=1)

# 2. BAL #1  Tim Beckham (X - X - 34)
b9.new_ab()
b9.out("G3")

# Winning team: BOS
# WP: BOS #31 Drew Pomeranz
game.winning_pitcher(31, is_away_team=True)

# Loser team: BAL
# LP: BAL #50 Miguel Castro
game.losing_pitcher(50)

# print(game)
game.generate_scorecard()
