import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2018-05-31
# https://www.baseball-reference.com/boxes/HOU/HOU201805310.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2018/05/31/530244/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-31 20:10-23:07",
        "at": "Minute Maid Park, Houston, TX",
        "att": "30,658",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                36: "Eduardo Núñez",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                41: "Chris Sale",
                56: "Joe Kelly",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [31, 57, 24, 41, 61],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [28, "0"],
                [11, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
                [23, "9"],
            ],
            "bench": [
                [36, "SS"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 24, 46, 76, 22, 41, 56, 61, 32, 37],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 43,
            "roster": {
                # Lineup
                4: "George Springer",
                2: "Alex Bregman",
                27: "Jose Altuve",
                1: "Carlos Correa",
                28: "J.D. Davis",
                9: "Marwin Gonzalez",
                19: "Tim Federowicz",
                18: "Tony Kemp",
                6: "Jake Marisnick",
                # Starting pitcher
                43: "Lance McCullers Jr.",
                # Bench
                11: "Evan Gattis",
                10: "Yuli Gurriel",
                12: "Max Stassi",
                # Bullpen
                53: "Ken Giles",
                30: "Héctor Rondón",
                36: "Will Harris",
                47: "Chris Devenski",
                31: "Collin McHugh",
                38: "Joe Smith",
                29: "Tony Sipp",
                60: "Dallas Keuchel",
                41: "Brad Peacock",
                45: "Gerrit Cole",
                35: "Justin Verlander",
                50: "Charlie Morton",
            },
            "lefties": [29, 60],
            "lineup": [
                [4, "9"],
                [2, "5"],
                [27, "0"],
                [1, "6"],
                [28, "3"],
                [9, "4"],
                [19, "2"],
                [18, "7"],
                [6, "8"],
            ],
            "bench": [
                [11, "DH"],
                [10, "1B"],
                [12, "C"],
            ],
            "bullpen": [53, 30, 36, 47, 31, 38, 29, 60, 41, 45, 35, 50],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Phil Cuzzi",
            "2B": "Chris Guccione",
            "3B": "Ben May",
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
# Pitching: HOU #43 Lance McCullers Jr.
t1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b c b")
t1.out("F8")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b f")
t1.out("G6-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.pitch_list("c b c f b c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #31 Drew Pomeranz
b1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b")
b1.out("G4-3")

# 2. HOU #2  Alex Bregman (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b b")
b1.reach("BB")
b1.advance(4, "1 HR")

# 3. HOU #27 Jose Altuve (X - X - 2)
b1.new_ab()
b1.pitch_list("b")
b1.out("P4")

# 4. HOU #1  Carlos Correa (X - X - 2)
b1.new_ab()
b1.pitch_list("c d b")
b1.hit(4, rbis=2)

# 5. HOU #28 J.D. Davis (X - X - X)
b1.new_ab()
b1.pitch_list("b c f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #43 Lance McCullers Jr.
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.advance(2, "11 G3-1")

# 5. BOS #11 Rafael Devers (X - X - 28)
t2.new_ab()
t2.pitch_list("b")
t2.out("G3-1")

# 6. BOS #12 Brock Holt (X - 28 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b s s d")
t2.out("G5-3")

# 7. BOS #3  Sandy León (X - 28 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b b b c")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #31 Drew Pomeranz
b2 = game.new_inning()

# 6. HOU #9  Marwin Gonzalez (X - X - X)
b2.new_ab()
b2.pitch_list("c s b s")
b2.out("K")

# 7. HOU #19 Tim Federowicz (X - X - X)
b2.new_ab()
b2.pitch_list("s c")
b2.out("F9")

# 8. HOU #18 Tony Kemp (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.advance(2, "6 1B")

# 9. HOU #6  Jake Marisnick (X - X - 18)
b2.new_ab()
b2.pitch_list("1 c f f")
b2.hit(1)

# 1. HOU #4  George Springer (X - 18 - 6)
b2.new_ab(is_risp=True)
b2.pitch_list("f b b b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #43 Lance McCullers Jr.
t3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("s f b b f f b f")
t3.hit(2)
t3.advance(4, "2 2B")

# 9. BOS #23 Blake Swihart (X - 19 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c c s")
t3.out("K")

# 1. BOS #16 Andrew Benintendi (X - 19 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b b b b")
t3.reach("BB")
t3.advance(4, "2 2B")

# 2. BOS #2  Xander Bogaerts (X - 19 - 16)
t3.new_ab(is_risp=True)
t3.pitch_list("c d f")
t3.hit(2, rbis=2)
t3.advance(3, "T")

# 3. BOS #18 Mitch Moreland (2 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f f d s")
t3.out("K")

# 4. BOS #28 J.D. Martinez (2 - X - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #31 Drew Pomeranz
b3 = game.new_inning()

# 2. HOU #2  Alex Bregman (X - X - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.out("P5")

# 3. HOU #27 Jose Altuve (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f f f f b f")
b3.hit(1)
b3.thrown_out(2, "1 DP4-3", 3, 31)

# 4. HOU #1  Carlos Correa (X - X - 27)
b3.new_ab()
b3.pitch_list("1 c f f b")
b3.out("DP4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #43 Lance McCullers Jr.
t4 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f")
t4.out("G1-3")

# 6. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("b b c b f")
t4.out("G1-3")

# 7. BOS #3  Sandy León (X - X - X)
t4.new_ab()
t4.pitch_list("b c s")
t4.out("L9")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 5. HOU #28 J.D. Davis (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)
b4.advance(3, "19 2B")
b4.advance(4, "18 1B")

# 6. HOU #9  Marwin Gonzalez (X - X - 28)
b4.new_ab()
b4.pitch_list("c f f s")
b4.out("K")

# 7. HOU #19 Tim Federowicz (X - X - 28)
b4.new_ab()
b4.hit(2)
b4.advance(3, "18 1B")
b4.advance(4, "6 FC3-6")

# 8. HOU #18 Tony Kemp (28 - 19 - X)
b4.new_ab(is_risp=True)
b4.hit(1, rbis=1)
b4.thrown_out(2, "6 FC3-6", 2, 31)

# 9. HOU #6  Jake Marisnick (19 - X - 18)
b4.new_ab(is_risp=True)
b4.reach("FC3-6", rbis=1)
b4.thrown_out(2, "4 CS", 3, 31)

# 1. HOU #4  George Springer (X - X - 6)
b4.new_ab()
b4.pitch_list("c b")
b4.no_ab("CS")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #43 Lance McCullers Jr.
t5 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b s b b c f c")
t5.out("!K")

# 9. BOS #23 Blake Swihart (X - X - X)
t5.new_ab()
t5.pitch_list("b b c s")
t5.out("F8")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.hit(1)
t5.advance(2, "2 SB")

# 2. BOS #2  Xander Bogaerts (X - X - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("c d 1 f b")
t5.out("L8")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("G5-3")

# 2. HOU #2  Alex Bregman (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b c")
b5.out("L7")

# 3. HOU #27 Jose Altuve (X - X - X)
b5.new_ab()
b5.pitch_list("f b c s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #43 Lance McCullers Jr.
t6 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("b t")
t6.out("F9")

# 5. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("s b b")
t6.hit(2)

# 6. BOS #12 Brock Holt (X - 11 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("b c")
t6.out("L4")


# Bot 6th
# Pitching: BOS #35 Steven Wright
b6 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #31 Drew Pomeranz
b6.pitching_substitution(35)

# 4. HOU #1  Carlos Correa (X - X - X)
b6.new_ab()
b6.pitch_list("c c b c")
b6.out("!K")

# 5. HOU #28 J.D. Davis (X - X - X)
b6.new_ab()
b6.pitch_list("b c s b b b")
b6.reach("BB")
b6.thrown_out(2, "9 FC1-4", 2, 35)

# 6. HOU #9  Marwin Gonzalez (X - X - 28)
b6.new_ab()
b6.pitch_list("c f")
b6.reach("FC1-4")
b6.thrown_out(2, "19 CS", 3, 35)

# 7. HOU #19 Tim Federowicz (X - X - 9)
b6.new_ab()
b6.pitch_list("b b c s")
b6.no_ab("CS")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #36 Will Harris
t7 = game.new_inning()

# Pitching change (HOU): #36 Will Harris replaces #43 Lance McCullers Jr.
t7.pitching_substitution(36)

# 7. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("f l s")
t7.out("K")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.out("G6-3")

# 9. BOS #23 Blake Swihart (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #35 Steven Wright
b7 = game.new_inning()

# 7. HOU #19 Tim Federowicz (X - X - X)
b7.new_ab()
b7.pitch_list("f c b f f b f s")
b7.out("K2-3")

# 8. HOU #18 Tony Kemp (X - X - X)
b7.new_ab()
b7.pitch_list("b b c c s")
b7.out("K")

# 9. HOU #6  Jake Marisnick (X - X - X)
b7.new_ab()
b7.pitch_list("b c c f")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #36 Will Harris
t8 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.hit(1)

# 2. BOS #2  Xander Bogaerts (X - X - 16)
t8.new_ab()
t8.pitch_list("b 1 b 1")
t8.out("(F)P3")

# 3. BOS #18 Mitch Moreland (X - X - 16)
t8.new_ab()
t8.out("L8")

# Pitching change (HOU): #30 Héctor Rondón replaces #36 Will Harris
t8.pitching_substitution(30)

# 4. BOS #28 J.D. Martinez (X - X - 16)
t8.new_ab()
t8.pitch_list("1 s 1 f b f")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #35 Steven Wright
b8 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c b")
b8.reach("BB")
b8.thrown_out(2, "2 FC6-4", 1, 35)

# 2. HOU #2  Alex Bregman (X - X - 4)
b8.new_ab()
b8.pitch_list("d 1 c")
b8.reach("FC6-4")
b8.advance(2, "27 1B")
b8.advance(3, "1 PB")
b8.thrown_out(4, "28 FC5-2", 2, 35)

# 3. HOU #27 Jose Altuve (X - X - 2)
b8.new_ab()
b8.pitch_list("s")
b8.hit(1)
b8.advance(2, "1 PB")
b8.advance(3, "28 FC5-2")

# 4. HOU #1  Carlos Correa (X - 2 - 27)
b8.new_ab(is_risp=True)
b8.pitch_list("b v v v")
b8.pb()
b8.reach("IBB")
b8.advance(2, "28 FC5-2")

# 5. HOU #28 J.D. Davis (2 - 27 - 1)
b8.new_ab(is_risp=True)
b8.pitch_list("b b c")
b8.reach("FC5-2")

# 6. HOU #9  Marwin Gonzalez (27 - 1 - 28)
b8.new_ab(is_risp=True)
b8.pitch_list("b d b c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #53 Ken Giles
t9 = game.new_inning()

# Pitching change (HOU): #53 Ken Giles replaces #30 Héctor Rondón
t9.pitching_substitution(53)

# 5. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("f s b s")
t9.out("K")

# 6. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("s f c")
t9.out("!K")

# 7. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "19 DI")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 3)
t9.new_ab(is_risp=True)
t9.pitch_list("d b b b")
t9.reach("BB")

# 9. BOS #23 Blake Swihart (X - 3 - 19)
t9.new_ab(is_risp=True)
t9.pitch_list("b c b b")
t9.out("L8")

# Winning team: HOU
# WP: HOU #43 Lance McCullers Jr.
game.winning_pitcher(43)
# SV: HOU #53 Ken Giles
game.save_pitcher(53)

# Loser team: BOS
# LP: BOS #31 Drew Pomeranz
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
