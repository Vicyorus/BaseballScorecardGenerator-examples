import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2018-06-03
# https://www.baseball-reference.com/boxes/HOU/HOU201806030.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2018/06/03/530285/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-03 19:38-23:03",
        "at": "Minute Maid Park, Houston, TX",
        "att": "33,431",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                11: "Rafael Devers",
                59: "Sam Travis",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                41: "Chris Sale",
                56: "Joe Kelly",
                61: "Brian Johnson",
                32: "Matt Barnes",
                66: "Bobby Poyner",
                37: "Heath Hembree",
            },
            "lefties": [57, 24, 41, 61, 66],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [18, "3"],
                [36, "5"],
                [19, "8"],
                [12, "4"],
                [23, "9"],
                [3, "2"],
            ],
            "bench": [
                [11, "3B"],
                [59, "1B"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 24, 46, 76, 41, 56, 61, 32, 66, 37],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 50,
            "roster": {
                # Lineup
                4: "George Springer",
                2: "Alex Bregman",
                27: "Jose Altuve",
                1: "Carlos Correa",
                10: "Yuli Gurriel",
                11: "Evan Gattis",
                28: "J.D. Davis",
                12: "Max Stassi",
                18: "Tony Kemp",
                # Starting pitcher
                50: "Charlie Morton",
                # Bench
                19: "Tim Federowicz",
                9: "Marwin Gonzalez",
                6: "Jake Marisnick",
                # Bullpen
                53: "Ken Giles",
                30: "Héctor Rondón",
                36: "Will Harris",
                47: "Chris Devenski",
                31: "Collin McHugh",
                38: "Joe Smith",
                43: "Lance McCullers Jr.",
                29: "Tony Sipp",
                60: "Dallas Keuchel",
                41: "Brad Peacock",
                45: "Gerrit Cole",
                35: "Justin Verlander",
            },
            "lefties": [29, 60],
            "lineup": [
                [4, "9"],
                [2, "5"],
                [27, "4"],
                [1, "6"],
                [10, "3"],
                [11, "0"],
                [28, "7"],
                [12, "2"],
                [18, "8"],
            ],
            "bench": [
                [19, "C"],
                [9, "SS"],
                [6, "CF"],
            ],
            "bullpen": [53, 30, 36, 47, 31, 38, 43, 29, 60, 41, 45, 35],
        },
        "umpires": {
            "HP": "Ben May",
            "1B": "Hunter Wendelstedt",
            "2B": "Phil Cuzzi",
            "3B": "Chris Guccione",
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
# Pitching: HOU #50 Charlie Morton
t1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b f b s")
t1.hit(2)
t1.advance(3, "28 G1-3")
t1.advance(4, "18 HR")

# 2. BOS #2  Xander Bogaerts (X - 16 - X)
t1.new_ab()
t1.pitch_list("b c b")
t1.out("G5-3")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
t1.new_ab()
t1.pitch_list("f t f b b f")
t1.out("G1-3")

# 4. BOS #18 Mitch Moreland (16 - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(4, rbis=2)

# 5. BOS #36 Eduardo Núñez (X - X - X)
t1.new_ab()
t1.pitch_list("b b f f b")
t1.hit(1)

# 6. BOS #19 Jackie Bradley Jr. (X - X - 36)
t1.new_ab()
t1.pitch_list("1 c c")
t1.out("F9")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.hit(4, rbis=1)

# 2. HOU #2  Alex Bregman (X - X - X)
b1.new_ab()
b1.out("F8")

# 3. HOU #27 Jose Altuve (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b b c")
b1.out("!K")

# 4. HOU #1  Carlos Correa (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #50 Charlie Morton
t2 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c b b s b c")
t2.out("!K")

# 8. BOS #23 Blake Swihart (X - X - X)
t2.new_ab()
t2.pitch_list("b s c b b s")
t2.out("K")

# 9. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("b c c c")
t2.out("!K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. HOU #10 Yuli Gurriel (X - X - X)
b2.new_ab()
b2.hit(2)
b2.advance(3, "28 F8")

# 6. HOU #11 Evan Gattis (X - 10 - X)
b2.new_ab()
b2.pitch_list("c c f d d")
b2.out("F8")

# 7. HOU #28 J.D. Davis (X - 10 - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F8")

# 8. HOU #12 Max Stassi (10 - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #50 Charlie Morton
t3 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("s b f b s")
t3.out("K")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(2)
t3.thrown_out(3, "28 DP8-6-5", 3, 50)

# 3. BOS #28 J.D. Martinez (X - 2 - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("DP8-6-5")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 9. HOU #18 Tony Kemp (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.error(3)
b3.reach("E3")
b3.advance(2, "4 BB")

# 1. HOU #4  George Springer (X - X - 18)
b3.new_ab()
b3.pitch_list("b c c 1 1 b b b")
b3.reach("BB")

# 2. HOU #2  Alex Bregman (X - 18 - 4)
b3.new_ab()
b3.pitch_list("c f b c")
b3.out("!K")

# 3. HOU #27 Jose Altuve (X - 18 - 4)
b3.new_ab()
b3.pitch_list("c f b s")
b3.out("K")

# 4. HOU #1  Carlos Correa (X - 18 - 4)
b3.new_ab()
b3.pitch_list("c b t s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #50 Charlie Morton
t4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b b")
t4.reach("BB")
t4.advance(2, "36 1B")
t4.advance(3, "12 G3")

# 5. BOS #36 Eduardo Núñez (X - X - 18)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)
t4.advance(2, "12 G3")

# 6. BOS #19 Jackie Bradley Jr. (X - 18 - 36)
t4.new_ab()
t4.pitch_list("c c b s")
t4.out("K")

# 7. BOS #12 Brock Holt (X - 18 - 36)
t4.new_ab()
t4.pitch_list("f b f b f")
t4.out("G3")

# 8. BOS #23 Blake Swihart (18 - 36 - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("L4")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 5. HOU #10 Yuli Gurriel (X - X - X)
b4.new_ab()
b4.out("L7")

# 6. HOU #11 Evan Gattis (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P3")

# 7. HOU #28 J.D. Davis (X - X - X)
b4.new_ab()
b4.pitch_list("c c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #50 Charlie Morton
t5 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("f b b s f f s")
t5.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.hit(4, rbis=1)

# 2. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.out("(F)P3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.out("L8")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 8. HOU #12 Max Stassi (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.reach("HBP")
b5.advance(2, "18 SAC1-3")

# 9. HOU #18 Tony Kemp (X - X - 12)
b5.new_ab()
b5.out("SAC1-3")

# 1. HOU #4  George Springer (X - 12 - X)
b5.new_ab()
b5.pitch_list("b c b b s")
b5.out("P4")

# 2. HOU #2  Alex Bregman (X - 12 - X)
b5.new_ab()
b5.out("L4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #50 Charlie Morton
t6 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.hit(1)
t6.advance(2, "36 HBP")
t6.advance(4, "12 3B")

# 5. BOS #36 Eduardo Núñez (X - X - 18)
t6.new_ab()
t6.reach("HBP")
t6.advance(4, "12 3B")

# 6. BOS #19 Jackie Bradley Jr. (X - 18 - 36)
t6.new_ab()
t6.pitch_list("f b b s f t")
t6.out("KT")

# 7. BOS #12 Brock Holt (X - 18 - 36)
t6.new_ab()
t6.pitch_list("c b d b c")
t6.hit(3, rbis=2)
t6.advance(4, "23 1B")

# 8. BOS #23 Blake Swihart (12 - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1, rbis=1)
t6.thrown_out(2, "16 CS", 3, 29)

# Pitching change (HOU): #29 Tony Sipp replaces #50 Charlie Morton
t6.pitching_substitution(29)

# 9. BOS #3  Sandy León (X - X - 23)
t6.new_ab()
t6.pitch_list("b 1 c")
t6.out("L7")

# 1. BOS #16 Andrew Benintendi (X - X - 23)
t6.new_ab()
t6.pitch_list("s c b")
t6.no_ab("CS")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 3. HOU #27 Jose Altuve (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(2, "1 1B")
b6.advance(3, "10 FC4-6")

# 4. HOU #1  Carlos Correa (X - X - 27)
b6.new_ab()
b6.hit(1)
b6.thrown_out(2, "10 FC4-6", 1, 22)

# 5. HOU #10 Yuli Gurriel (X - 27 - 1)
b6.new_ab()
b6.pitch_list("b c f f d")
b6.reach("FC4-6")
b6.thrown_out(2, "11 DP4-6-3", 2, 22)

# 6. HOU #11 Evan Gattis (27 - X - 10)
b6.new_ab()
b6.pitch_list("c b")
b6.out("DP4-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #29 Tony Sipp
t7 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b c c f f c")
t7.out("!K")

# Pitching change (HOU): #31 Collin McHugh replaces #29 Tony Sipp
t7.pitching_substitution(31)

# 2. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("b b s")
t7.out("F9")

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("c s b b f f b s")
t7.out("K")


# Bot 7th
# Pitching: BOS #22 Rick Porcello
b7 = game.new_inning()

# 7. HOU #28 J.D. Davis (X - X - X)
b7.new_ab()
b7.out("G6-3")

# 8. HOU #12 Max Stassi (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b")
b7.error(5)
b7.reach("E5")
b7.advance(2, "18 BB")
b7.advance(3, "4 HBP")
b7.advance("U", "2 1B")

# 9. HOU #18 Tony Kemp (X - X - 12)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "4 HBP")
b7.advance(4, "2 1B")

# 1. HOU #4  George Springer (X - 12 - 18)
b7.new_ab()
b7.reach("HBP")
b7.advance(2, "2 1B")

# 2. HOU #2  Alex Bregman (12 - 18 - 4)
b7.new_ab()
b7.pitch_list("b")
b7.hit(1, rbis=2)
b7.thrown_out(2, "1 FC6", 3, 32)

# Pitching change (BOS): #32 Matt Barnes replaces #22 Rick Porcello
b7.pitching_substitution(32)

# 3. HOU #27 Jose Altuve (X - 4 - 2)
b7.new_ab()
b7.pitch_list("f c f b c")
b7.out("!K")

# 4. HOU #1  Carlos Correa (X - 4 - 2)
b7.new_ab()
b7.pitch_list("c c d d")
b7.reach("FC6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #31 Collin McHugh
t8 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.thrown_out(2, "7-6", 1, 31)

# 5. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.hit(1)
t8.advance(2, "12 SB")
t8.advance(4, "12 1B")

# 6. BOS #19 Jackie Bradley Jr. (X - X - 36)
t8.new_ab()
t8.pitch_list("c b c t")
t8.out("KT")

# 7. BOS #12 Brock Holt (X - X - 36)
t8.new_ab()
t8.pitch_list("b b c c f")
t8.hit(1, rbis=1)

# 8. BOS #23 Blake Swihart (X - X - 12)
t8.new_ab()
t8.pitch_list("c c b s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# 5. HOU #10 Yuli Gurriel (X - X - X)
b8.new_ab()
b8.out("G6-3")

# 6. HOU #11 Evan Gattis (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f b b s")
b8.out("K")

# 7. HOU #28 J.D. Davis (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f b b")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #53 Ken Giles
t9 = game.new_inning()

# Pitching change (HOU): #53 Ken Giles replaces #31 Collin McHugh
t9.pitching_substitution(53)

# 9. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("s s b f")
t9.hit(1)
t9.advance(3, "2 2B")
t9.advance(4, "59 1B")

# 1. BOS #16 Andrew Benintendi (X - X - 3)
t9.new_ab()
t9.pitch_list("s c d b f f s")
t9.out("K")

# 2. BOS #2  Xander Bogaerts (X - X - 3)
t9.new_ab()
t9.pitch_list("c")
t9.hit(2)
t9.advance(4, "59 1B")

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #28 J.D. Martinez, batting 3rd
t9.offensive_substitution(3, 59, "PH")

# 3. BOS #59 Sam Travis (3 - 2 - X)
t9.new_ab()
t9.pitch_list("s d")
t9.hit(1, rbis=2)
t9.advance(2, "18 G4-3")

# 4. BOS #18 Mitch Moreland (X - X - 59)
t9.new_ab()
t9.pitch_list("s b")
t9.out("G4-3")

# 5. BOS #36 Eduardo Núñez (X - 59 - X)
t9.new_ab()
t9.pitch_list("f f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #37 Heath Hembree
b9 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #32 Matt Barnes
b9.pitching_substitution(37)

# Defensive switch (BOS): #59 Sam Travis moves to DH
b9.defensive_switch(59, "0")

# 8. HOU #12 Max Stassi (X - X - X)
b9.new_ab()
b9.pitch_list("b s c b b c")
b9.out("!K")

# 9. HOU #18 Tony Kemp (X - X - X)
b9.new_ab()
b9.pitch_list("b f")
b9.out("P4")

# 1. HOU #4  George Springer (X - X - X)
b9.new_ab()
b9.pitch_list("c b b f b f b")
b9.reach("BB")
b9.advance(2, "2 BB")

# 2. HOU #2  Alex Bregman (X - X - 4)
b9.new_ab()
b9.pitch_list("b f s f b f f b b")
b9.reach("BB")

# 3. HOU #27 Jose Altuve (X - 4 - 2)
b9.new_ab()
b9.pitch_list("b c")
b9.out("F9")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)

# Loser team: HOU
# LP: HOU #50 Charlie Morton
game.losing_pitcher(50)

# print(game)
game.generate_scorecard()
