import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2018-06-02
# https://www.baseball-reference.com/boxes/HOU/HOU201806020.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2018/06/02/530270/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-02 19:16-22:57",
        "at": "Minute Maid Park, Houston, TX",
        "att": "38,640",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                12: "Brock Holt",
                59: "Sam Travis",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                41: "Chris Sale",
                56: "Joe Kelly",
                61: "Brian Johnson",
                32: "Matt Barnes",
                66: "Bobby Poyner",
                37: "Heath Hembree",
            },
            "lefties": [24, 57, 41, 61, 66],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [28, "0"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [23, "9"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [12, "2B"],
                [59, "1B"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 46, 76, 22, 41, 56, 61, 32, 66, 37],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 35,
            "roster": {
                # Lineup
                4: "George Springer",
                2: "Alex Bregman",
                27: "Jose Altuve",
                1: "Carlos Correa",
                10: "Yuli Gurriel",
                11: "Evan Gattis",
                12: "Max Stassi",
                9: "Marwin Gonzalez",
                6: "Jake Marisnick",
                # Starting pitcher
                35: "Justin Verlander",
                # Bench
                19: "Tim Federowicz",
                18: "Tony Kemp",
                28: "J.D. Davis",
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
                50: "Charlie Morton",
            },
            "lefties": [29, 60],
            "lineup": [
                [4, "9"],
                [2, "5"],
                [27, "4"],
                [1, "6"],
                [10, "3"],
                [11, "0"],
                [12, "2"],
                [9, "7"],
                [6, "8"],
            ],
            "bench": [
                [19, "C"],
                [18, "2B"],
                [28, "1B"],
            ],
            "bullpen": [53, 30, 36, 47, 31, 38, 43, 29, 60, 41, 45, 50],
        },
        "umpires": {
            "HP": "Chris Guccione",
            "1B": "Ben May",
            "2B": "Hunter Wendelstedt",
            "3B": "Phil Cuzzi",
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
# Pitching: HOU #35 Justin Verlander
t1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b f f f b")
t1.reach("BB")
t1.advance(2, "28 WP")
t1.advance(4, "28 1B")

# 2. BOS #2  Xander Bogaerts (X - X - 16)
t1.new_ab()
t1.pitch_list("1 1 f f b f f 1 1 1")
t1.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c f d")
t1.wp()
t1.hit(1, rbis=1)

# 4. BOS #18 Mitch Moreland (X - X - 28)
t1.new_ab()
t1.pitch_list("c t s")
t1.out("K")

# 5. BOS #36 Eduardo Núñez (X - X - 28)
t1.new_ab()
t1.out("(F)F9")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b1.new_ab()
b1.pitch_list("c c s")
b1.out("K")

# 2. HOU #2  Alex Bregman (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c f c")
b1.out("!K")

# 3. HOU #27 Jose Altuve (X - X - X)
b1.new_ab()
b1.pitch_list("f b b f")
b1.hit(1)

# 4. HOU #1  Carlos Correa (X - X - 27)
b1.new_ab()
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #35 Justin Verlander
t2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b s")
t2.out("K")

# 7. BOS #23 Blake Swihart (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b")
t2.out("(F)P5")

# 8. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("c f f b f f f f b")
t2.out("L9")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. HOU #10 Yuli Gurriel (X - X - X)
b2.new_ab()
b2.pitch_list("f b b")
b2.hit(1)
b2.advance(2, "12 SB")
b2.advance(4, "9 3B")

# 6. HOU #11 Evan Gattis (X - X - 10)
b2.new_ab()
b2.pitch_list("c f b")
b2.out("L4")

# 7. HOU #12 Max Stassi (X - X - 10)
b2.new_ab()
b2.pitch_list("b s b b c s")
b2.out("K")

# 8. HOU #9  Marwin Gonzalez (X - 10 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(3, rbis=1)

# 9. HOU #6  Jake Marisnick (9 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #35 Justin Verlander
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("f b s b b")
t3.out("L8")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c s")
t3.out("F7")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b3.new_ab()
b3.pitch_list("f b t")
b3.hit(1)
b3.advance(4, "2 HR")

# 2. HOU #2  Alex Bregman (X - X - 4)
b3.new_ab()
b3.pitch_list("b")
b3.hit(4, rbis=2)

# 3. HOU #27 Jose Altuve (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b b")
b3.out("G5-3")

# 4. HOU #1  Carlos Correa (X - X - X)
b3.new_ab()
b3.pitch_list("b c b b b")
b3.reach("BB")

# 5. HOU #10 Yuli Gurriel (X - X - 1)
b3.new_ab()
b3.pitch_list("s b b s")
b3.out("G1-3")

# 6. HOU #11 Evan Gattis (X - X - 1)
b3.new_ab()
b3.pitch_list("b b b")
b3.out("P6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #35 Justin Verlander
t4 = game.new_inning()

# Defensive change (HOU): #18 Tony Kemp replaces #9 Marwin Gonzalez (LF), playing LF, batting 8th
t4.defensive_substitution(8, 18, "7")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b b f f s")
t4.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G3")

# 5. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)

# 6. BOS #11 Rafael Devers (X - X - 36)
t4.new_ab()
t4.pitch_list("b f s f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 7. HOU #12 Max Stassi (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("L7")

# 8. HOU #18 Tony Kemp (X - X - X)
b4.new_ab()
b4.pitch_list("c s b b s")
b4.out("K")

# 9. HOU #6  Jake Marisnick (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #35 Justin Verlander
t5 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
t5.new_ab()
t5.pitch_list("b b f c")
t5.out("L7")

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.out("(F)F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G3")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b f t")
b5.out("KT")

# 2. HOU #2  Alex Bregman (X - X - X)
b5.new_ab()
b5.pitch_list("c b c f b b f f f f")
b5.out("P4")

# 3. HOU #27 Jose Altuve (X - X - X)
b5.new_ab()
b5.pitch_list("s b f b b c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #35 Justin Verlander
t6 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("s c f c")
t6.out("!K")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b f f b")
t6.reach("BB")
t6.advance(2, "28 SB")
t6.advance(4, "28 1B")

# 3. BOS #28 J.D. Martinez (X - X - 2)
t6.new_ab(is_risp=True)
t6.pitch_list("s d c")
t6.hit(1, rbis=1)
t6.advance(2, "18 SB")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t6.new_ab(is_risp=True)
t6.pitch_list("c 1 b d")
t6.out("L4")

# 5. BOS #36 Eduardo Núñez (X - 28 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c s s")
t6.out("K2-3")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 4. HOU #1  Carlos Correa (X - X - X)
b6.new_ab()
b6.pitch_list("b b c b")
b6.out("F9")

# 5. HOU #10 Yuli Gurriel (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.out("L9")

# 6. HOU #11 Evan Gattis (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #36 Will Harris
t7 = game.new_inning()

# Pitching change (HOU): #36 Will Harris replaces #35 Justin Verlander
t7.pitching_substitution(36)

# 6. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("c s s")
t7.out("K")

# 7. BOS #23 Blake Swihart (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.out("G6-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b c b b")
t7.hit(4)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b b b")
t7.reach("BB")
t7.advance(4, "16 HR")

# 1. BOS #16 Andrew Benintendi (X - X - 19)
t7.new_ab()
t7.pitch_list("1 c 1 1 b 1 s f")
t7.hit(4, rbis=2)

# Pitching change (HOU): #30 Héctor Rondón replaces #36 Will Harris
t7.pitching_substitution(30)

# 2. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c b b s b b")
t7.reach("BB")

# 3. BOS #28 J.D. Martinez (X - X - 2)
t7.new_ab()
t7.pitch_list("b f f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #37 Heath Hembree
b7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
b7.pitching_substitution(37)

# 7. HOU #12 Max Stassi (X - X - X)
b7.new_ab()
b7.out("G6-3")

# 8. HOU #18 Tony Kemp (X - X - X)
b7.new_ab()
b7.pitch_list("c f")
b7.out("G1-3")

# 9. HOU #6  Jake Marisnick (X - X - X)
b7.new_ab()
b7.pitch_list("b s s f b b b")
b7.reach("BB")

# 1. HOU #4  George Springer (X - X - 6)
b7.new_ab()
b7.pitch_list("f s b b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #29 Tony Sipp
t8 = game.new_inning()

# Pitching change (HOU): #29 Tony Sipp replaces #30 Héctor Rondón
t8.pitching_substitution(29)

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("c b f s")
t8.out("K")

# 5. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("f f s")
t8.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.out("(F)P3")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b8.pitching_substitution(56)

# 2. HOU #2  Alex Bregman (X - X - X)
b8.new_ab()
b8.pitch_list("b f c b b")
b8.out("F8")

# 3. HOU #27 Jose Altuve (X - X - X)
b8.new_ab()
b8.pitch_list("f b b c b f b")
b8.reach("BB")
b8.advance(2, "1 SB")
b8.advance(3, "10 SB")
b8.advance(4, "10 1B")

# 4. HOU #1  Carlos Correa (X - X - 27)
b8.new_ab(is_risp=True)
b8.pitch_list("f b 1 c b b f")
b8.out("G5-3")

# 5. HOU #10 Yuli Gurriel (X - 27 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b")
b8.hit(1, rbis=1)

# 6. HOU #11 Evan Gattis (X - X - 10)
b8.new_ab()
b8.pitch_list("f b b c")
b8.out("P4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #29 Tony Sipp
t9 = game.new_inning()

# 7. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b f")
t9.out("F9")

# Pitching change (HOU): #38 Joe Smith replaces #29 Tony Sipp
t9.pitching_substitution(38)

# 8. BOS #7  Christian Vázquez (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b b")
t9.reach("BB")
t9.advance(2, "16 SB")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
t9.new_ab()
t9.pitch_list("s")
t9.out("F7")

# 1. BOS #16 Andrew Benintendi (X - X - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("c f")
t9.out("G3-1")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# Defensive change (BOS): #12 Brock Holt replaces #23 Blake Swihart (RF), playing RF, batting 7th
b9.defensive_substitution(7, 12, "9")

# 7. HOU #12 Max Stassi (X - X - X)
b9.new_ab()
b9.pitch_list("c c b b s")
b9.out("K")

# 8. HOU #18 Tony Kemp (X - X - X)
b9.new_ab()
b9.pitch_list("c s")
b9.out("F7")

# Offensive change (HOU): Pinch-hitter #28 J.D. Davis replaces #6 Jake Marisnick, batting 9th
b9.offensive_substitution(9, 28, "PH")

# 9. HOU #28 J.D. Davis (X - X - X)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: HOU
# LP: HOU #36 Will Harris
game.losing_pitcher(36)

# print(game)
game.generate_scorecard()
