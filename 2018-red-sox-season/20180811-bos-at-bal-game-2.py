import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-08-11, game 2 of 2
# https://www.baseball-reference.com/boxes/BAL/BAL201808112.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/08/11/531158/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-11 19:25-23:24 (0:20 delay)",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "24,051",
        "temp": "83F, Cloudy",
        "wind": "3mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                68: "Dan Butler",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                18: "Mitch Moreland",
                16: "Andrew Benintendi",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [12, "4"],
                [25, "3"],
                [28, "7"],
                [2, "6"],
                [11, "5"],
                [36, "0"],
                [68, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [16, "LF"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 67, 22, 31, 61, 37, 24, 46, 70, 56, 17, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 32,
            "roster": {
                # Lineup
                29: "Jace Peterson",
                34: "Jonathan Villar",
                10: "Adam Jones",
                16: "Trey Mancini",
                19: "Chris Davis",
                39: "Renato Núñez",
                3: "Cedric Mullins",
                23: "Joey Rickard",
                36: "Caleb Joseph",
                # Starting pitcher
                32: "Yefry Ramírez",
                # Bench
                1: "Tim Beckham",
                61: "Austin Wynns",
                45: "Mark Trumbo",
                # Bullpen
                31: "Jimmy Yacabonis",
                63: "Sean Gilmartin",
                17: "Alex Cobb",
                41: "David Hess",
                49: "Cody Carroll",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                51: "Paul Fry",
                58: "Evan Phillips",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
            },
            "lefties": [63, 66, 51],
            "lineup": [
                [29, "4"],
                [34, "6"],
                [10, "9"],
                [16, "3"],
                [19, "0"],
                [39, "5"],
                [3, "8"],
                [23, "7"],
                [36, "2"],
            ],
            "bench": [
                [1, "SS"],
                [61, "C"],
                [45, "1B"],
            ],
            "bullpen": [31, 63, 17, 41, 49, 66, 54, 51, 58, 60, 37, 43, 50],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Adrian Johnson",
            "2B": "Marvin Hudson",
            "3B": "Andy Fletcher",
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
# Pitching: BAL #32 Yefry Ramírez
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b c")
t1.out("G6-3")

# 2. BOS #12 Brock Holt (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("P4")

# 3. BOS #25 Steve Pearce (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b b f c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #76 Hector Velázquez
b1 = game.new_inning()

# 1. BAL #29 Jace Peterson (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L4")

# 2. BAL #34 Jonathan Villar (X - X - X)
b1.new_ab()
b1.pitch_list("b b t")
b1.out("G4-3")

# 3. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #32 Yefry Ramírez
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c d")
t2.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t2.new_ab()
t2.pitch_list("b c")
t2.out("L9")

# 6. BOS #11 Rafael Devers (X - X - 28)
t2.new_ab()
t2.pitch_list("f b b f f")
t2.out("P6")

# 7. BOS #36 Eduardo Núñez (X - X - 28)
t2.new_ab()
t2.pitch_list("b b b c f f")
t2.out("L9")


# Bot 2nd
# Pitching: BOS #76 Hector Velázquez
b2 = game.new_inning()

# 4. BAL #16 Trey Mancini (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.advance(2, "19 HBP")
b2.advance(4, "39 2B")

# 5. BAL #19 Chris Davis (X - X - 16)
b2.new_ab()
b2.reach("HBP")
b2.advance(3, "39 2B")

# 6. BAL #39 Renato Núñez (X - 16 - 19)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(2, rbis=1)

# 7. BAL #3  Cedric Mullins (19 - 39 - X)
b2.new_ab()
b2.pitch_list("d d s b c")
b2.out("G4-3")

# 8. BAL #23 Joey Rickard (19 - 39 - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("(F)F9")

# 9. BAL #36 Caleb Joseph (19 - 39 - X)
b2.new_ab()
b2.pitch_list("d")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #32 Yefry Ramírez
t3 = game.new_inning()

# 8. BOS #68 Dan Butler (X - X - X)
t3.new_ab()
t3.pitch_list("c b c s")
t3.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.out("L1-5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("f b f f b")
t3.hit(1)
t3.advance(2, "12 SB")

# 2. BOS #12 Brock Holt (X - X - 50)
t3.new_ab()
t3.pitch_list("1 c b 1 1 b c b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #76 Hector Velázquez
b3 = game.new_inning()

# 1. BAL #29 Jace Peterson (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b s b")
b3.reach("BB")
b3.advance(2, "34 G4-3")
b3.advance(4, "16 1B")

# 2. BAL #34 Jonathan Villar (X - X - 29)
b3.new_ab()
b3.pitch_list("l b 1 1 b s")
b3.out("G4-3")

# 3. BAL #10 Adam Jones (X - 29 - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("G5-3")

# Pitching change (BOS): #44 Brandon Workman replaces #76 Hector Velázquez
b3.pitching_substitution(44)

# 4. BAL #16 Trey Mancini (X - 29 - X)
b3.new_ab()
b3.pitch_list("f b b c d")
b3.hit(1, rbis=1)
b3.advance(2, "19 BB")
b3.advance(3, "39 BB")

# 5. BAL #19 Chris Davis (X - X - 16)
b3.new_ab()
b3.pitch_list("b c b b c b")
b3.reach("BB")
b3.advance(2, "39 BB")

# 6. BAL #39 Renato Núñez (X - 16 - 19)
b3.new_ab()
b3.pitch_list("b b b c c d")
b3.reach("BB")
b3.thrown_out(2, "3 FC6-4", 3, 44)

# 7. BAL #3  Cedric Mullins (16 - 19 - 39)
b3.new_ab()
b3.pitch_list("c c")
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #32 Yefry Ramírez
t4 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f t")
t4.out("KT")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("s s f b b b f f f")
t4.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("s f b c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #44 Brandon Workman
b4.pitching_substitution(31)

# 8. BAL #23 Joey Rickard (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.hit(1)
b4.thrown_out(2, "34 POCS", 3, 31)

# 9. BAL #36 Caleb Joseph (X - X - 23)
b4.new_ab()
b4.pitch_list("b f")
b4.out("F9")

# 1. BAL #29 Jace Peterson (X - X - 23)
b4.new_ab()
b4.pitch_list("1 b")
b4.out("P6")

# 2. BAL #34 Jonathan Villar (X - X - 23)
b4.new_ab()
b4.pitch_list("b b s f 1")
b4.no_ab("POCS")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #32 Yefry Ramírez
t5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.hit(3)
t5.advance(4, "68 SF7")

# 8. BOS #68 Dan Butler (36 - X - X)
t5.new_ab()
t5.out("SF7", rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b c b b b")
t5.reach("BB")
t5.advance(2, "50 SB")

# 1. BOS #50 Mookie Betts (X - X - 19)
t5.new_ab()
t5.pitch_list("c 1 f b")
t5.out("L4")

# 2. BOS #12 Brock Holt (X - 19 - X)
t5.new_ab()
t5.pitch_list("d s c")
t5.out("F9")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 2. BAL #34 Jonathan Villar (X - X - X)
b5.new_ab()
b5.pitch_list("l m f")
b5.out("G6-3")

# 3. BAL #10 Adam Jones (X - X - X)
b5.new_ab()
b5.out("F9")

# 4. BAL #16 Trey Mancini (X - X - X)
b5.new_ab()
b5.pitch_list("b b c f b f f b")
b5.reach("BB")

# 5. BAL #19 Chris Davis (X - X - 16)
b5.new_ab()
b5.pitch_list("b f c")
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #49 Cody Carroll
t6 = game.new_inning()

# Pitching change (BAL): #49 Cody Carroll replaces #32 Yefry Ramírez
t6.pitching_substitution(49)

# 3. BOS #25 Steve Pearce (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c b")
t6.reach("BB")
t6.advance(2, "28 BB")
t6.advance(3, "2 DP6-4-3")
t6.advance(4, "11 WP")

# 4. BOS #28 J.D. Martinez (X - X - 25)
t6.new_ab()
t6.pitch_list("b b c b b")
t6.reach("BB")
t6.thrown_out(2, "2 DP6-4-3", 1, 49)

# 5. BOS #2  Xander Bogaerts (X - 25 - 28)
t6.new_ab()
t6.pitch_list("b c f f b f d f")
t6.out("DP6-4-3")

# 6. BOS #11 Rafael Devers (25 - X - X)
t6.new_ab()
t6.pitch_list("s b b d b")
t6.wp()
t6.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t6.new_ab()
t6.pitch_list("c 1 c")
t6.out("L9")


# Bot 6th
# Pitching: BOS #37 Heath Hembree
b6 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #31 Drew Pomeranz
b6.pitching_substitution(37)

# 6. BAL #39 Renato Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c b b s f")
b6.out("F7")

# 7. BAL #3  Cedric Mullins (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b b")
b6.reach("BB")
b6.thrown_out(2, "23 CS", 2, 37)

# 8. BAL #23 Joey Rickard (X - X - 3)
b6.new_ab()
b6.pitch_list("c b c 1 f b b")
b6.hit(4)

# 9. BAL #36 Caleb Joseph (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #43 Mike Wright Jr.
t7 = game.new_inning()

# Pitching change (BAL): #43 Mike Wright Jr. replaces #49 Cody Carroll
t7.pitching_substitution(43)

# 8. BOS #68 Dan Butler (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c")
t7.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b t b f f c")
t7.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("P4")


# Bot 7th
# Pitching: BOS #56 Joe Kelly
b7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b7.pitching_substitution(56)

# 1. BAL #29 Jace Peterson (X - X - X)
b7.new_ab()
b7.pitch_list("b b f")
b7.out("F7")

# 2. BAL #34 Jonathan Villar (X - X - X)
b7.new_ab()
b7.pitch_list("b f b b s")
b7.hit(1)
b7.thrown_out(2, "10 FC5-4", 2, 56)

# 3. BAL #10 Adam Jones (X - X - 34)
b7.new_ab()
b7.pitch_list("1 f b 1")
b7.reach("FC5-4")
b7.advance(2, "16 SB")

# 4. BAL #16 Trey Mancini (X - X - 10)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")

# 5. BAL #19 Chris Davis (X - 10 - 16)
b7.new_ab()
b7.pitch_list("b d 2 f c")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #43 Mike Wright Jr.
t8 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("L5")

# 3. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(4, "28 HR")

# 4. BOS #28 J.D. Martinez (X - X - 25)
t8.new_ab()
t8.pitch_list("f")
t8.hit(4, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b b c c f")
t8.out("G6-3")

# Pitching change (BAL): #51 Paul Fry replaces #43 Mike Wright Jr.
t8.pitching_substitution(51)

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c b")
t8.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t8.new_ab()
t8.pitch_list("b f b b")
t8.out("L9")


# Bot 8th
# Pitching: BOS #67 William Cuevas
b8 = game.new_inning()

# Pitching change (BOS): #67 William Cuevas replaces #56 Joe Kelly
b8.pitching_substitution(67)

# 6. BAL #39 Renato Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G5-3")

# 7. BAL #3  Cedric Mullins (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c c b")
b8.reach("BB")
b8.advance(2, "45 BB")
b8.advance(3, "29 WP")

# 8. BAL #23 Joey Rickard (X - X - 3)
b8.new_ab()
b8.pitch_list("b")
b8.out("L8")

# Offensive change (BAL): Pinch-hitter #45 Mark Trumbo replaces #36 Caleb Joseph, batting 9th
b8.offensive_substitution(9, 45, "PH")

# 9. BAL #45 Mark Trumbo (X - X - 3)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
# Offensive change (BAL): Pinch-runner #61 Austin Wynns replaces #45 Mark Trumbo
b8.offensive_substitution(9, 61, "PR")
b8.atbase("PR")
b8.advance(2, "29 WP")

# 1. BAL #29 Jace Peterson (X - 3 - 45)
b8.new_ab()
b8.pitch_list("b b f c s")
b8.wp()
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #51 Paul Fry
t9 = game.new_inning()

# Defensive switch (BAL): #61 Austin Wynns moves to C
t9.defensive_switch(61, "2")

# Offensive change (BOS): Pinch-hitter #16 Andrew Benintendi replaces #68 Dan Butler, batting 8th
t9.offensive_substitution(8, 16, "PH")

# 8. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("c b t s")
t9.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("s b c")
t9.reach("HBP")
t9.thrown_out(2, "50 CS", 2, 51)

# 1. BOS #50 Mookie Betts (X - X - 19)
t9.new_ab()
t9.pitch_list("b f c b")
t9.hit(2)
t9.advance(4, "12 1B")

# 2. BOS #12 Brock Holt (X - 50 - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(1, rbis=1)
t9.thrown_out(2, "8-2-6", 3, 51)


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #67 William Cuevas
b9.pitching_substitution(46)

# Defensive change (BOS): #3 Sandy León replaces #16 Andrew Benintendi (PH), playing C, batting 8th
b9.defensive_substitution(8, 3, "2")

# 2. BAL #34 Jonathan Villar (X - X - X)
b9.new_ab()
b9.pitch_list("c b f f c")
b9.out("!K")

# 3. BAL #10 Adam Jones (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b f s")
b9.out("K")

# 4. BAL #16 Trey Mancini (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c s")
b9.hit(4)

# 5. BAL #19 Chris Davis (X - X - X)
b9.new_ab()
b9.pitch_list("c b s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #56 Joe Kelly
game.winning_pitcher(56, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: BAL
# LP: BAL #43 Mike Wright Jr.
game.losing_pitcher(43)

# print(game)
game.generate_scorecard()
