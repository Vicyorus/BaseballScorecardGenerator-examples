import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-13
# https://www.baseball-reference.com/boxes/BAL/BAL201806130.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/06/13/530411/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-13 15:07-18:27",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "17,217",
        "temp": "81F, Cloudy",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [12, "3"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 44, 22, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 32,
            "roster": {
                # Lineup
                23: "Joey Rickard",
                16: "Trey Mancini",
                13: "Manny Machado",
                2: "Danny Valencia",
                6: "Jonathan Schoop",
                45: "Mark Trumbo",
                14: "Craig Gentry",
                61: "Austin Wynns",
                29: "Jace Peterson",
                # Starting pitcher
                32: "Yefry Ramírez",
                # Bench
                19: "Chris Davis",
                10: "Adam Jones",
                24: "Pedro Alvarez",
                15: "Chance Sisco",
                # Bullpen
                17: "Alex Cobb",
                48: "Richard Bleier",
                41: "David Hess",
                34: "Kevin Gausman",
                56: "Darren O'Day",
                53: "Zack Britton",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                35: "Brad Brach",
            },
            "lefties": [48, 53],
            "lineup": [
                [23, "9"],
                [16, "3"],
                [13, "6"],
                [2, "5"],
                [6, "4"],
                [45, "0"],
                [14, "8"],
                [61, "2"],
                [29, "7"],
            ],
            "bench": [
                [19, "1B"],
                [10, "CF"],
                [24, "3B"],
                [15, "C"],
            ],
            "bullpen": [17, 48, 41, 34, 56, 53, 60, 37, 43, 50, 35],
        },
        "umpires": {
            "HP": "Brian Knight",
            "1B": "Pat Hoberg",
            "2B": "Nic Lentz",
            "3B": "Mark Carlson",
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
t1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f f")
t1.hit(1)
t1.error(7)
t1.advance(2, "E7")

# 3. BOS #2  Xander Bogaerts (X - 16 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c s f s")
t1.out("K")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b")
t1.out("P3")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b1.new_ab()
b1.out("G6-3")

# 2. BAL #16 Trey Mancini (X - X - X)
b1.new_ab()
b1.pitch_list("b f b s s")
b1.out("K")

# 3. BAL #13 Manny Machado (X - X - X)
b1.new_ab()
b1.pitch_list("c b c f b b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #32 Yefry Ramírez
t2 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("s b b")
t2.out("P5")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("f b f f f b")
t2.out("G6-3")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.reach("HBP")

# 8. BOS #3  Sandy León (X - X - 12)
t2.new_ab()
t2.pitch_list("b b b c 1 f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. BAL #2  Danny Valencia (X - X - X)
b2.new_ab()
b2.pitch_list("b c b c f s")
b2.out("K")

# 5. BAL #6  Jonathan Schoop (X - X - X)
b2.new_ab()
b2.pitch_list("c b b s s")
b2.out("K")

# 6. BAL #45 Mark Trumbo (X - X - X)
b2.new_ab()
b2.reach("HBP")
b2.thrown_out(2, "14 FC5-4", 3, 41)

# 7. BAL #14 Craig Gentry (X - X - 45)
b2.new_ab()
b2.pitch_list("b")
b2.reach("FC5-4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #32 Yefry Ramírez
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("L8")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b f b b c f")
t3.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b f f f s")
t3.out("K")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("b c s")
t3.error(6)
t3.reach("E6")

# 4. BOS #28 J.D. Martinez (X - X - 2)
t3.new_ab()
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 8. BAL #61 Austin Wynns (X - X - X)
b3.new_ab()
b3.pitch_list("c c s")
b3.out("K")

# 9. BAL #29 Jace Peterson (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "16 SB")

# 1. BAL #23 Joey Rickard (X - X - 29)
b3.new_ab()
b3.pitch_list("c b b c f s")
b3.out("K")

# 2. BAL #16 Trey Mancini (X - X - 29)
b3.new_ab(is_risp=True)
b3.pitch_list("1 f b 1 1 s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #32 Yefry Ramírez
t4 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("f s b c")
t4.out("!K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b b c f f")
t4.hit(1)
t4.thrown_out(2, "12 CS", 2, 32)

# 7. BOS #12 Brock Holt (X - X - 36)
t4.new_ab()
t4.pitch_list("1 1 c b 1 f b b")
t4.hit(1)

# 8. BOS #3  Sandy León (X - X - 12)
t4.new_ab()
t4.pitch_list("m b f b b s")
t4.out("K")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 3. BAL #13 Manny Machado (X - X - X)
b4.new_ab()
b4.pitch_list("s")
b4.out("F7")

# 4. BAL #2  Danny Valencia (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "45 BB")

# 5. BAL #6  Jonathan Schoop (X - X - 2)
b4.new_ab()
b4.pitch_list("c f f t")
b4.out("KT")

# 6. BAL #45 Mark Trumbo (X - X - 2)
b4.new_ab()
b4.pitch_list("c c b f b f f b b")
b4.reach("BB")

# 7. BAL #14 Craig Gentry (X - 2 - 45)
b4.new_ab(is_risp=True)
b4.pitch_list("c b f f b f")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #32 Yefry Ramírez
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b s f b f s")
t5.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c f b b b b")
t5.reach("BB")
t5.advance(2, "16 BB")
t5.advance(3, "2 WP")
t5.advance(4, "2 SF9")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("1 b b b c 1 b")
t5.reach("BB")
t5.advance(2, "28 BB")
t5.advance(4, "11 1B")

# Pitching change (BAL): #43 Mike Wright Jr. replaces #32 Yefry Ramírez
t5.pitching_substitution(43)

# 3. BOS #2  Xander Bogaerts (X - 50 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.wp()
t5.out("SF9", rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - 16)
t5.new_ab()
t5.pitch_list("c c b b b f f f d")
t5.reach("BB")
t5.advance(2, "11 1B")
t5.advance(4, "36 1B")

# 5. BOS #11 Rafael Devers (X - 16 - 28)
t5.new_ab(is_risp=True)
t5.pitch_list("c b b s")
t5.hit(1, rbis=1)
t5.advance(3, "36 1B")

# 6. BOS #36 Eduardo Núñez (X - 28 - 11)
t5.new_ab(is_risp=True)
t5.pitch_list("b")
t5.hit(1, rbis=1)
t5.advance(2, "T")

# 7. BOS #12 Brock Holt (11 - 36 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c s b c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 8. BAL #61 Austin Wynns (X - X - X)
b5.new_ab()
b5.pitch_list("c c b s")
b5.out("K")

# 9. BAL #29 Jace Peterson (X - X - X)
b5.new_ab()
b5.pitch_list("c c")
b5.out("L7")

# 1. BAL #23 Joey Rickard (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #43 Mike Wright Jr.
t6 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("c f f b b")
t6.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("t b c f b f f b")
t6.out("(F)P2")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F8")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 2. BAL #16 Trey Mancini (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.hit(1)
b6.advance(2, "13 G5-3")

# 3. BAL #13 Manny Machado (X - X - 16)
b6.new_ab()
b6.pitch_list("b c c f f b b f")
b6.out("G5-3")

# 4. BAL #2  Danny Valencia (X - 16 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c c f b s")
b6.out("K")

# 5. BAL #6  Jonathan Schoop (X - 16 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #43 Mike Wright Jr.
t7 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b f b b b")
t7.reach("BB")
t7.thrown_out(2, "2 DP5-4-3", 1, 43)

# 3. BOS #2  Xander Bogaerts (X - X - 16)
t7.new_ab()
t7.pitch_list("f b f f")
t7.out("DP5-4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("f f")
t7.hit(4)

# Pitching change (BAL): #48 Richard Bleier replaces #43 Mike Wright Jr.
t7.pitching_substitution(48)

# 5. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("f s b")
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 6. BAL #45 Mark Trumbo (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
b7.advance(2, "14 BB")
b7.advance(3, "15 G3-1")
b7.advance(4, "29 SF7")

# 7. BAL #14 Craig Gentry (X - X - 45)
b7.new_ab()
b7.pitch_list("c s f b f b b b")
b7.reach("BB")
b7.advance(2, "15 G3-1")

# Pitching change (BOS): #44 Brandon Workman replaces #41 Chris Sale
b7.pitching_substitution(44)

# Offensive change (BAL): Pinch-hitter #15 Chance Sisco replaces #61 Austin Wynns, batting 8th
b7.offensive_substitution(8, 15, "PH")

# 8. BAL #15 Chance Sisco (X - 45 - 14)
b7.new_ab(is_risp=True)
b7.pitch_list("b f c d")
b7.out("G3-1")

# 9. BAL #29 Jace Peterson (45 - 14 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.out("SF7", rbis=1)

# 1. BAL #23 Joey Rickard (X - 14 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c d b c d f f")
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #48 Richard Bleier
t8 = game.new_inning()

# Defensive switch (BAL): #15 Chance Sisco moves to C
t8.defensive_switch(15, "2")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.out("G4-3")

# Pitching change (BAL): #35 Brad Brach replaces #48 Richard Bleier
t8.pitching_substitution(35)

# 7. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b f")
t8.hit(1)
t8.thrown_out(2, "3 DP4-6-3", 2, 35)

# 8. BOS #3  Sandy León (X - X - 12)
t8.new_ab()
t8.pitch_list("f b 1 d")
t8.out("DP4-6-3")


# Bot 8th
# Pitching: BOS #65 Justin Haley
b8 = game.new_inning()

# Pitching change (BOS): #65 Justin Haley replaces #44 Brandon Workman
b8.pitching_substitution(65)

# 2. BAL #16 Trey Mancini (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")

# 3. BAL #13 Manny Machado (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b b")
b8.reach("BB")
b8.thrown_out(2, "2 FC6-4", 2, 65)

# 4. BAL #2  Danny Valencia (X - X - 13)
b8.new_ab()
b8.pitch_list("c f f b d")
b8.reach("FC6-4")

# 5. BAL #6  Jonathan Schoop (X - X - 2)
b8.new_ab()
b8.pitch_list("c f b b")
b8.out("L9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #60 Mychal Givens
t9 = game.new_inning()

# Pitching change (BAL): #60 Mychal Givens replaces #35 Brad Brach
t9.pitching_substitution(60)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("b f c f")
t9.out("L3")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f s")
t9.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)

# 3. BOS #2  Xander Bogaerts (X - X - 16)
t9.new_ab()
t9.pitch_list("1 c")
t9.out("(F)P3")


# Bot 9th
# Pitching: BOS #65 Justin Haley
b9 = game.new_inning()

# 6. BAL #45 Mark Trumbo (X - X - X)
b9.new_ab()
b9.pitch_list("s s b")
b9.out("L1")

# 7. BAL #14 Craig Gentry (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("G5-3")

# 8. BAL #15 Chance Sisco (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.advance(3, "29 2B")

# 9. BAL #29 Jace Peterson (X - X - 15)
b9.new_ab()
b9.pitch_list("b")
b9.hit(2)

# 1. BAL #23 Joey Rickard (15 - 29 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("c")
b9.out("G5-3")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)

# Loser team: BAL
# LP: BAL #32 Yefry Ramírez
game.losing_pitcher(32)

# print(game)
game.generate_scorecard()
