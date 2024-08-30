import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ HOU, 2018-06-01
# https://www.baseball-reference.com/boxes/HOU/HOU201806010.shtml
# https://www.mlb.com/gameday/red-sox-vs-astros/2018/06/01/530255/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-01 20:10-23:05",
        "at": "Minute Maid Park, Houston, TX",
        "att": "37,244",
        "temp": "73F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [41, 57, 24, 31, 61],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [28, "9"],
                [11, "5"],
                [36, "0"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 24, 46, 76, 22, 56, 31, 61, 32, 37],
        },
        "home": {
            "team": "Houston Astros",
            "starter": 45,
            "roster": {
                # Lineup
                4: "George Springer",
                2: "Alex Bregman",
                27: "Jose Altuve",
                1: "Carlos Correa",
                10: "Yuli Gurriel",
                11: "Evan Gattis",
                12: "Max Stassi",
                28: "J.D. Davis",
                6: "Jake Marisnick",
                # Starting pitcher
                45: "Gerrit Cole",
                # Bench
                19: "Tim Federowicz",
                18: "Tony Kemp",
                9: "Marwin Gonzalez",
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
                35: "Justin Verlander",
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
                [28, "7"],
                [6, "8"],
            ],
            "bench": [
                [19, "C"],
                [18, "2B"],
                [9, "SS"],
            ],
            "bullpen": [53, 30, 36, 47, 31, 38, 43, 29, 60, 41, 35, 50],
        },
        "umpires": {
            "HP": "Phil Cuzzi",
            "1B": "Chris Guccione",
            "2B": "Ben May",
            "3B": "Hunter Wendelstedt",
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
# Pitching: HOU #45 Gerrit Cole
t1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("f b c s")
t1.out("K")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c")
t1.out("P6")

# 3. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.pitch_list("b b c")
t1.out("F7")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b f f b b")
b1.reach("BB")
b1.advance(2, "2 1B")
b1.advance(4, "1 WP")

# 2. HOU #2  Alex Bregman (X - X - 4)
b1.new_ab()
b1.pitch_list("b b t")
b1.hit(1)
b1.advance(3, "1 WP")
b1.advance(4, "10 1B")

# 3. HOU #27 Jose Altuve (X - 4 - 2)
b1.new_ab()
b1.pitch_list("s b c f b c")
b1.out("!K")

# 4. HOU #1  Carlos Correa (X - 4 - 2)
b1.new_ab()
b1.pitch_list("b c b f s")
b1.wp()
b1.out("K")

# 5. HOU #10 Yuli Gurriel (2 - X - X)
b1.new_ab()
b1.pitch_list("b c s f f d")
b1.hit(1, rbis=1)

# 6. HOU #11 Evan Gattis (X - X - 10)
b1.new_ab()
b1.pitch_list("d b c")
b1.out("P4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: HOU #45 Gerrit Cole
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G1-3")

# 5. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b f s f s")
t2.out("K2-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)
t2.advance(4, "12 2B")

# 7. BOS #12 Brock Holt (X - X - 36)
t2.new_ab()
t2.pitch_list("c b b b")
t2.hit(2, rbis=1)

# 8. BOS #3  Sandy León (X - 12 - X)
t2.new_ab()
t2.pitch_list("b f b b")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 7. HOU #12 Max Stassi (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("L8")

# 8. HOU #28 J.D. Davis (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 9. HOU #6  Jake Marisnick (X - X - X)
b2.new_ab()
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: HOU #45 Gerrit Cole
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("s b b f c")
t3.out("!K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.out("G3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("b t")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b3.new_ab()
b3.pitch_list("b c c b")
b3.hit(4, rbis=1)

# 2. HOU #2  Alex Bregman (X - X - X)
b3.new_ab()
b3.pitch_list("c f f b s")
b3.out("K")

# 3. HOU #27 Jose Altuve (X - X - X)
b3.new_ab()
b3.pitch_list("s b s b b f")
b3.out("F9")

# 4. HOU #1  Carlos Correa (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1)
b3.advance(2, "10 WP")
b3.advance(4, "10 1B")

# 5. HOU #10 Yuli Gurriel (X - X - 1)
b3.new_ab()
b3.pitch_list("b f b")
b3.wp()
b3.hit(1, rbis=1)

# 6. HOU #11 Evan Gattis (X - X - 10)
b3.new_ab()
b3.pitch_list("c f f")
b3.out("L9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: HOU #45 Gerrit Cole
t4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(4, rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f")
t4.hit(4, rbis=1)

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("c b f f f s")
t4.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("F9")

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("F8")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 7. HOU #12 Max Stassi (X - X - X)
b4.new_ab()
b4.pitch_list("c b s c")
b4.out("!K")

# 8. HOU #28 J.D. Davis (X - X - X)
b4.new_ab()
b4.out("G1-3")

# 9. HOU #6  Jake Marisnick (X - X - X)
b4.new_ab()
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: HOU #45 Gerrit Cole
t5 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("L8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.hit(1)
t5.advance(2, "16 SB")

# 1. BOS #16 Andrew Benintendi (X - X - 19)
t5.new_ab()
t5.pitch_list("s 1 1 b b c d b")
t5.reach("BB")

# 2. BOS #2  Xander Bogaerts (X - 19 - 16)
t5.new_ab()
t5.pitch_list("c s b s")
t5.out("K")

# 3. BOS #18 Mitch Moreland (X - 19 - 16)
t5.new_ab()
t5.pitch_list("s s c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
b5.new_ab()
b5.pitch_list("b b c")
b5.hit(1)
b5.thrown_out(2, "27 FC6-4", 2, 41)

# 2. HOU #2  Alex Bregman (X - X - 4)
b5.new_ab()
b5.pitch_list("c b b b c s")
b5.out("K")

# 3. HOU #27 Jose Altuve (X - X - 4)
b5.new_ab()
b5.pitch_list("s")
b5.reach("FC6-4")

# 4. HOU #1  Carlos Correa (X - X - 27)
b5.new_ab()
b5.pitch_list("1 1 c")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: HOU #45 Gerrit Cole
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L7")

# 5. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.out("L8")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f b")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 5. HOU #10 Yuli Gurriel (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("F9")

# 6. HOU #11 Evan Gattis (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("P3")

# 7. HOU #12 Max Stassi (X - X - X)
b6.new_ab()
b6.pitch_list("b f c b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: HOU #45 Gerrit Cole
t7 = game.new_inning()

# Defensive change (HOU): #18 Tony Kemp replaces #28 J.D. Davis (LF), playing LF, batting 8th
t7.defensive_substitution(8, 18, "7")

# 7. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.out("G1-3")

# 8. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("s b c c")
t7.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c s b")
t7.out("L9")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
b7.pitching_substitution(32)

# 8. HOU #18 Tony Kemp (X - X - X)
b7.new_ab()
b7.pitch_list("b f s b")
b7.hit(1)
b7.advance(2, "6 1B")
b7.advance(3, "4 DP5-4-3")

# 9. HOU #6  Jake Marisnick (X - X - 18)
b7.new_ab()
b7.pitch_list("c l 1")
b7.hit(1)
b7.thrown_out(2, "4 DP5-4-3", 1, 32)

# 1. HOU #4  George Springer (X - 18 - 6)
b7.new_ab()
b7.pitch_list("d")
b7.out("DP5-4-3")

# 2. HOU #2  Alex Bregman (18 - X - X)
b7.new_ab()
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: HOU #47 Chris Devenski
t8 = game.new_inning()

# Pitching change (HOU): #47 Chris Devenski replaces #45 Gerrit Cole
t8.pitching_substitution(47)

# 1. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b b c f f b s")
t8.out("K")

# 2. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(2, "18 WP")
t8.advance(3, "18 G3")

# 3. BOS #18 Mitch Moreland (X - X - 2)
t8.new_ab()
t8.pitch_list("c 1 s b")
t8.wp()
t8.out("G3")

# 4. BOS #28 J.D. Martinez (2 - X - X)
t8.new_ab()
t8.pitch_list("v v v v")
t8.reach("IBB")
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #28 J.D. Martinez
t8.offensive_substitution(4, 23, "PR")
t8.atbase("PR")
t8.advance(2, "11 SB")

# 5. BOS #11 Rafael Devers (2 - X - 28)
t8.new_ab()
t8.pitch_list("c")
t8.out("L8")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b8.pitching_substitution(56)

# Defensive switch (BOS): #23 Blake Swihart moves to RF
b8.defensive_switch(23, "9")

# 3. HOU #27 Jose Altuve (X - X - X)
b8.new_ab()
b8.out("G6-3")

# 4. HOU #1  Carlos Correa (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.hit(4, rbis=1)

# 5. HOU #10 Yuli Gurriel (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b b")
b8.reach("BB")
b8.advance(4, "11 HR")

# 6. HOU #11 Evan Gattis (X - X - 10)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(4, rbis=2)

# 7. HOU #12 Max Stassi (X - X - X)
b8.new_ab()
b8.pitch_list("b b s b s b")
b8.reach("BB")
b8.advance(2, "6 1B")
b8.advance(3, "4 1B")

# Pitching change (BOS): #61 Brian Johnson replaces #56 Joe Kelly
b8.pitching_substitution(61)

# 8. HOU #18 Tony Kemp (X - X - 12)
b8.new_ab()
b8.out("F7")

# 9. HOU #6  Jake Marisnick (X - X - 12)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)
b8.advance(2, "4 1B")

# 1. HOU #4  George Springer (X - 12 - 6)
b8.new_ab()
b8.pitch_list("b d f")
b8.hit(1)

# 2. HOU #2  Alex Bregman (12 - 6 - 4)
b8.new_ab()
b8.pitch_list("c c f b f d b")
b8.out("(F)P5")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: HOU #41 Brad Peacock
t9 = game.new_inning()

# Pitching change (HOU): #41 Brad Peacock replaces #47 Chris Devenski
t9.pitching_substitution(41)

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c c b b c")
t9.out("!K")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b f c s")
t9.out("K")

# 8. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("f c")
t9.hit(1)
t9.advance(2, "19 DI")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t9.new_ab()
t9.pitch_list("f c s")
t9.out("K")

# Winning team: HOU
# WP: HOU #45 Gerrit Cole
game.winning_pitcher(45)

# Loser team: BOS
# LP: BOS #41 Chris Sale
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
