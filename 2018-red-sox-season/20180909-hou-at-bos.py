import os
from baseball_scorecard.baseball_scorecard import Scorecard

# HOU @ BOS, 2018-09-09
# https://www.baseball-reference.com/boxes/BOS/BOS201809090.shtml
# https://www.mlb.com/gameday/astros-vs-red-sox/2018/09/09/531544/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-09 20:09-23:44",
        "at": "Fenway Park, Boston, MA",
        "att": "32,787",
        "temp": "60F, Partly Cloudy",
        "wind": "13mph, In From CF",
        "away": {
            "team": "Houston Astros",
            "starter": 60,
            "roster": {
                # Lineup
                4: "George Springer",
                27: "Jose Altuve",
                2: "Alex Bregman",
                10: "Yuli Gurriel",
                1: "Carlos Correa",
                9: "Marwin Gonzalez",
                13: "Tyler White",
                16: "Brian McCann",
                22: "Josh Reddick",
                # Starting pitcher
                60: "Dallas Keuchel",
                # Bench
                11: "Evan Gattis",
                15: "Martín Maldonado",
                18: "Tony Kemp",
                28: "J.D. Davis",
                6: "Jake Marisnick",
                12: "Max Stassi",
                # Bullpen
                65: "Framber Valdez",
                30: "Héctor Rondón",
                36: "Will Harris",
                47: "Chris Devenski",
                31: "Collin McHugh",
                59: "Cionel Pérez",
                54: "Roberto Osuna",
                38: "Joe Smith",
                55: "Ryan Pressly",
                29: "Tony Sipp",
                41: "Brad Peacock",
                45: "Gerrit Cole",
                67: "Dean Deetz",
                35: "Justin Verlander",
                50: "Charlie Morton",
                63: "Josh James",
            },
            "lefties": [60, 65, 59, 29],
            "lineup": [
                [4, "8"],
                [27, "4"],
                [2, "5"],
                [10, "3"],
                [1, "6"],
                [9, "7"],
                [13, "0"],
                [16, "2"],
                [22, "9"],
            ],
            "bench": [
                [11, "DH"],
                [15, "C"],
                [18, "2B"],
                [28, "1B"],
                [6, "CF"],
                [12, "C"],
            ],
            "bullpen": [65, 30, 36, 47, 31, 59, 54, 38, 55, 29, 41, 45, 67, 35, 50, 63],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                5: "Ian Kinsler",
                0: "Brandon Phillips",
                36: "Eduardo Núñez",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                30: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                12: "Brock Holt",
                59: "Sam Travis",
                11: "Rafael Devers",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "9"],
                [2, "6"],
                [25, "3"],
                [5, "4"],
                [0, "5"],
                [36, "0"],
                [3, "2"],
            ],
            "bench": [
                [30, "OF"],
                [18, "1B"],
                [12, "2B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [19, "CF"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Quinn Wolcott",
            "1B": "Paul Nauert",
            "2B": "James Hoye",
            "3B": "David Rackley",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
t1.new_ab()
t1.pitch_list("c b c")
t1.hit(1)
t1.advance(2, "2 PB")

# 2. HOU #27 Jose Altuve (X - X - 4)
t1.new_ab()
t1.out("(F)P3")

# 3. HOU #2  Alex Bregman (X - X - 4)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b b")
t1.pb()
t1.reach("BB")

# 4. HOU #10 Yuli Gurriel (X - 4 - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("c b t c")
t1.out("!K")

# 5. HOU #1  Carlos Correa (X - 4 - 2)
t1.new_ab(is_risp=True)
t1.pitch_list("b c b s s")
t1.out("K")


# Bot 1st
# Pitching: HOU #60 Dallas Keuchel
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2)
b1.advance(3, "28 G2-3")
b1.advance(4, "2 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("F7")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("G2-3")

# 4. BOS #2  Xander Bogaerts (50 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b s")
b1.hit(1, rbis=1)

# 5. BOS #25 Steve Pearce (X - X - 2)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 6. HOU #9  Marwin Gonzalez (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b s f f")
t2.hit(4)

# 7. HOU #13 Tyler White (X - X - X)
t2.new_ab()
t2.pitch_list("b b f c c")
t2.out("!K")

# 8. HOU #16 Brian McCann (X - X - X)
t2.new_ab()
t2.pitch_list("b f b")
t2.out("P4")

# 9. HOU #22 Josh Reddick (X - X - X)
t2.new_ab()
t2.pitch_list("f b b")
t2.out("F8")


# Bot 2nd
# Pitching: HOU #60 Dallas Keuchel
b2 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f b b")
b2.out("G6-3")

# 7. BOS #0  Brandon Phillips (X - X - X)
b2.new_ab()
b2.pitch_list("c s")
b2.out("G3-1")

# 8. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(1)

# 9. BOS #3  Sandy León (X - X - 36)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 1. HOU #4  George Springer (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("G4-3")

# 2. HOU #27 Jose Altuve (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 3. HOU #2  Alex Bregman (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(2)

# 4. HOU #10 Yuli Gurriel (X - 2 - X)
t3.new_ab(is_risp=True)
t3.out("P5")


# Bot 3rd
# Pitching: HOU #60 Dallas Keuchel
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(2)
b3.advance(3, "16 G4-3")
b3.advance(4, "28 SF7")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b3.new_ab(is_risp=True)
b3.out("G4-3")

# 3. BOS #28 J.D. Martinez (50 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b f d")
b3.out("SF7", rbis=1)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c b")
b3.reach("BB")
b3.thrown_out(2, "25 FC6-4", 3, 60)

# 5. BOS #25 Steve Pearce (X - X - 2)
b3.new_ab()
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 5. HOU #1  Carlos Correa (X - X - X)
t4.new_ab()
t4.pitch_list("f f b b")
t4.out("G6-3")

# 6. HOU #9  Marwin Gonzalez (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G4-3")

# 7. HOU #13 Tyler White (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c s")
t4.out("K")


# Bot 4th
# Pitching: HOU #60 Dallas Keuchel
b4 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "0 DP6-4-3", 1, 60)

# 7. BOS #0  Brandon Phillips (X - X - 5)
b4.new_ab()
b4.pitch_list("b")
b4.out("DP6-4-3")

# 8. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1)
b4.thrown_out(2, "3 FC6-4", 3, 60)

# 9. BOS #3  Sandy León (X - X - 36)
b4.new_ab()
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 8. HOU #16 Brian McCann (X - X - X)
t5.new_ab()
t5.pitch_list("b b c f f")
t5.hit(1)
t5.thrown_out(2, "27 CS", 3, 22)

# 9. HOU #22 Josh Reddick (X - X - 16)
t5.new_ab()
t5.pitch_list("c b f s")
t5.out("K")

# 1. HOU #4  George Springer (X - X - 16)
t5.new_ab()
t5.pitch_list("f b f s")
t5.out("K")

# 2. HOU #27 Jose Altuve (X - X - 16)
t5.new_ab()
t5.pitch_list("b c b")
t5.no_ab("CS")


# Bot 5th
# Pitching: HOU #60 Dallas Keuchel
b5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b b")
b5.reach("BB")
b5.advance(2, "16 1B")
b5.advance(4, "28 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b5.new_ab()
b5.pitch_list("c d b f b")
b5.hit(1)
b5.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b5.new_ab(is_risp=True)
b5.hit(4, rbis=3)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.hit(1)
b5.thrown_out(2, "5 DP6-4-3", 2, 60)

# 5. BOS #25 Steve Pearce (X - X - 2)
b5.new_ab()
b5.pitch_list("b c f f b s")
b5.out("K")

# 6. BOS #5  Ian Kinsler (X - X - 2)
b5.new_ab()
b5.pitch_list("b f c b")
b5.out("DP6-4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 2. HOU #27 Jose Altuve (X - X - X)
t6.new_ab()
t6.hit(4)

# 3. HOU #2  Alex Bregman (X - X - X)
t6.new_ab()
t6.pitch_list("c f b f b f b")
t6.out("G4-3")

# 4. HOU #10 Yuli Gurriel (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "1 1B")
t6.advance(4, "13 2B")

# 5. HOU #1  Carlos Correa (X - X - 10)
t6.new_ab()
t6.pitch_list("b b c")
t6.hit(1)
t6.advance(4, "13 2B")

# 6. HOU #9  Marwin Gonzalez (X - 10 - 1)
t6.new_ab(is_risp=True)
t6.pitch_list("s b c f f")
t6.out("L9")

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
t6.pitching_substitution(37)

# 7. HOU #13 Tyler White (X - 10 - 1)
t6.new_ab(is_risp=True)
t6.pitch_list("f s b b f")
t6.hit(2, rbis=2)
t6.advance(4, "22 2B")

# Pitching change (BOS): #61 Brian Johnson replaces #37 Heath Hembree
t6.pitching_substitution(61)

# 8. HOU #16 Brian McCann (X - 13 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("d s d d d")
t6.reach("BB")
t6.advance(3, "22 2B")

# 9. HOU #22 Josh Reddick (X - 13 - 16)
t6.new_ab(is_risp=True)
t6.pitch_list("f d b f f b")
t6.hit(2, rbis=1)

# Pitching change (BOS): #70 Ryan Brasier replaces #61 Brian Johnson
t6.pitching_substitution(70)

# 1. HOU #4  George Springer (16 - 22 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("c t t")
t6.out("KT")


# Bot 6th
# Pitching: HOU #60 Dallas Keuchel
b6 = game.new_inning()

# 7. BOS #0  Brandon Phillips (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G3-1")

# 8. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("f b b")
b6.out("F7")

# 9. BOS #3  Sandy León (X - X - X)
b6.new_ab()
b6.pitch_list("b s c b b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #70 Ryan Brasier
t7.pitching_substitution(35)

# 2. HOU #27 Jose Altuve (X - X - X)
t7.new_ab()
t7.pitch_list("s")
t7.hit(1)
t7.error(5)
t7.advance(2, "E5")
t7.advance(3, "10 PB")
t7.thrown_out(4, "10 FC6-2", 2, 35)

# 3. HOU #2  Alex Bregman (X - 27 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("l f f f")
t7.out("F8")

# 4. HOU #10 Yuli Gurriel (X - 27 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.pb()
t7.reach("FC6-2")

# 5. HOU #1  Carlos Correa (X - X - 10)
t7.new_ab()
t7.pitch_list("1 s f")
t7.out("F8")


# Bot 7th
# Pitching: HOU #38 Joe Smith
b7 = game.new_inning()

# Pitching change (HOU): #38 Joe Smith replaces #60 Dallas Keuchel
b7.pitching_substitution(38)

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("t")
b7.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("s b f")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #35 Steven Wright
t8 = game.new_inning()

# 6. HOU #9  Marwin Gonzalez (X - X - X)
t8.new_ab()
t8.out("F8")

# 7. HOU #13 Tyler White (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(2)
# Offensive change (HOU): Pinch-runner #6 Jake Marisnick replaces #13 Tyler White
t8.offensive_substitution(7, 6, "PR")
t8.atbase("PR")

# 8. HOU #16 Brian McCann (X - 13 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b b b c b")
t8.reach("BB")
# Offensive change (HOU): Pinch-runner #28 J.D. Davis replaces #16 Brian McCann
t8.offensive_substitution(8, 28, "PR")
t8.atbase("PR")
t8.thrown_out(2, "22 DP4-6-3", 2, 35)

# 9. HOU #22 Josh Reddick (X - 6 - 16)
t8.new_ab(is_risp=True)
t8.pitch_list("b f b")
t8.out("DP4-6-3")


# Bot 8th
# Pitching: HOU #31 Collin McHugh
b8 = game.new_inning()

# Pitching change (HOU): #31 Collin McHugh replaces #38 Joe Smith
b8.pitching_substitution(31)

# Defensive switch (HOU): #6 Jake Marisnick moves to DH
b8.defensive_switch(6, "0")

# Defensive change (HOU): #15 Martín Maldonado replaces #28 J.D. Davis (PR), playing C, batting 8th
b8.defensive_substitution(8, 15, "2")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f f")
b8.hit(1)
b8.advance(2, "18 1B")
b8.advance(3, "12 BB")

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #25 Steve Pearce, batting 5th
b8.offensive_substitution(5, 18, "PH")

# 5. BOS #18 Mitch Moreland (X - X - 2)
b8.new_ab()
b8.pitch_list("b b c s f")
b8.hit(1)
b8.advance(2, "12 BB")

# 6. BOS #5  Ian Kinsler (X - 2 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b b f f s")
b8.out("K")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #0 Brandon Phillips, batting 7th
b8.offensive_substitution(7, 12, "PH")

# 7. BOS #12 Brock Holt (X - 2 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b b c f b f f b")
b8.reach("BB")

# Pitching change (HOU): #29 Tony Sipp replaces #31 Collin McHugh
b8.pitching_substitution(29)

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #36 Eduardo Núñez, batting 8th
b8.offensive_substitution(8, 23, "PH")

# 8. BOS #23 Blake Swihart (2 - 18 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("c b c s")
b8.out("K")

# Offensive change (BOS): Pinch-hitter #7 Christian Vázquez replaces #3 Sandy León, batting 9th
b8.offensive_substitution(9, 7, "PH")

# 9. BOS #7  Christian Vázquez (2 - 18 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("c c d s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #35 Steven Wright
t9.pitching_substitution(46)

# Defensive switch (BOS): #18 Mitch Moreland moves to 1B
t9.defensive_switch(18, "3")

# Defensive switch (BOS): #12 Brock Holt moves to 3B
t9.defensive_switch(12, "5")

# Defensive switch (BOS): #23 Blake Swihart moves to DH
t9.defensive_switch(23, "0")

# Defensive switch (BOS): #7 Christian Vázquez moves to C
t9.defensive_switch(7, "2")

# 1. HOU #4  George Springer (X - X - X)
t9.new_ab()
t9.pitch_list("b f b s b s")
t9.out("K")

# 2. HOU #27 Jose Altuve (X - X - X)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# 3. HOU #2  Alex Bregman (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("L8")


# Bot 9th
# Pitching: HOU #30 Héctor Rondón
b9 = game.new_inning()

# Pitching change (HOU): #30 Héctor Rondón replaces #29 Tony Sipp
b9.pitching_substitution(30)

# 1. BOS #50 Mookie Betts (X - X - X)
b9.new_ab()
b9.pitch_list("b b f c b")
b9.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(1)
b9.thrown_out(2, "28 FC4-6", 2, 30)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b9.new_ab()
b9.pitch_list("1 b")
b9.reach("FC4-6")
b9.advance(2, "2 1B")
# Offensive change (BOS): Pinch-runner #30 Tzu-Wei Lin replaces #28 J.D. Martinez
b9.offensive_substitution(3, 30, "PR")
b9.atbase("PR")
b9.advance(4, "18 1B")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b9.new_ab()
b9.pitch_list("c b f b")
b9.hit(1)
b9.advance(2, "18 1B")

# 5. BOS #18 Mitch Moreland (X - 28 - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("b f b")
b9.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #46 Craig Kimbrel
game.winning_pitcher(46)

# Loser team: HOU
# LP: HOU #30 Héctor Rondón
game.losing_pitcher(30, is_away_team=True)

# print(game)
game.generate_scorecard()
