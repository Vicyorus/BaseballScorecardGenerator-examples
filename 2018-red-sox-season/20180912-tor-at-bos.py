import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-09-12
# https://www.baseball-reference.com/boxes/BOS/BOS201809120.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/09/12/531595/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-12 19:10-21:51",
        "at": "Fenway Park, Boston, MA",
        "att": "35,178",
        "temp": "68F, Cloudy",
        "wind": "9mph, In From CF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 41,
            "roster": {
                # Lineup
                28: "Billy McKinney",
                29: "Devon Travis",
                13: "Lourdes Gurriel Jr.",
                8: "Kendrys Morales",
                26: "Yangervis Solarte",
                37: "Teoscar Hernández",
                68: "Rowdy Tellez",
                9: "Danny Jansen",
                67: "Jonathan Davis",
                # Starting pitcher
                41: "Aaron Sanchez",
                # Bench
                7: "Richard Urena",
                15: "Randal Grichuk",
                14: "Justin Smoak",
                70: "Reese McGuire",
                21: "Luke Maile",
                1: "Aledmys Díaz",
                11: "Kevin Pillar",
                27: "Dwight Smith Jr.",
                # Bullpen
                51: "Ken Giles",
                24: "Danny Barnes",
                58: "Tim Mayza",
                25: "Marco Estrada",
                39: "Jake Petricka",
                54: "Sean Reid-Foley",
                22: "David Paulino",
                50: "José Manuel Fernández",
                43: "Sam Gaviglio",
                56: "Ryan Borucki",
                36: "Tyler Clippard",
                45: "Thomas Pannone",
                65: "Taylor Guerrieri",
                62: "Mark Leiter Jr.",
                66: "Justin Shafer",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
            },
            "lefties": [58, 50, 56, 45],
            "lineup": [
                [28, "9"],
                [29, "4"],
                [13, "6"],
                [8, "0"],
                [26, "5"],
                [37, "7"],
                [68, "3"],
                [9, "2"],
                [67, "8"],
            ],
            "bench": [
                [7, "SS"],
                [15, "RF"],
                [14, "1B"],
                [70, "C"],
                [21, "C"],
                [1, "SS"],
                [11, "CF"],
                [27, "LF"],
            ],
            "bullpen": [51, 24, 58, 25, 39, 54, 22, 50, 43, 56, 36, 45, 65, 62, 66, 6, 52],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                5: "Ian Kinsler",
                23: "Blake Swihart",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
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
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61, 66, 63],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [11, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [59, "1B"],
                [5, "2B"],
                [23, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "D.J. Reyburn",
            "1B": "Chris Segal",
            "2B": "Alfonso Márquez",
            "3B": "Jim Wolf",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. TOR #28 Billy McKinney (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G4-3")

# 2. TOR #29 Devon Travis (X - X - X)
t1.new_ab()
t1.pitch_list("s b b f b")
t1.out("L8")

# 3. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("c c b b f")
t1.out("L6")


# Bot 1st
# Pitching: TOR #41 Aaron Sanchez
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(1)
b1.advance(2, "16 WP")
b1.advance(3, "16 G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("c b 1 1 c b d")
b1.wp()
b1.out("G6-3")

# 3. BOS #28 J.D. Martinez (50 - X - X)
b1.new_ab()
b1.pitch_list("c d s d t")
b1.out("KT")

# 4. BOS #2  Xander Bogaerts (50 - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 4. TOR #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("F9")

# 5. TOR #26 Yangervis Solarte (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("G6-3")

# 6. TOR #37 Teoscar Hernández (X - X - X)
t2.new_ab()
t2.pitch_list("b c b f f b s")
t2.out("K")


# Bot 2nd
# Pitching: TOR #41 Aaron Sanchez
b2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")
b2.thrown_out(2, "12 DP4-6-3", 2, 41)

# 6. BOS #11 Rafael Devers (X - X - 18)
b2.new_ab()
b2.pitch_list("s f s")
b2.out("K")

# 7. BOS #12 Brock Holt (X - X - 18)
b2.new_ab()
b2.pitch_list("b")
b2.out("DP4-6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 7. TOR #68 Rowdy Tellez (X - X - X)
t3.new_ab()
t3.pitch_list("c s b c")
t3.out("!K")

# 8. TOR #9  Danny Jansen (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("L6")

# 9. TOR #67 Jonathan Davis (X - X - X)
t3.new_ab()
t3.out("G5-3")


# Bot 3rd
# Pitching: TOR #41 Aaron Sanchez
b3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b f s")
b3.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("t b l f s")
b3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 1. TOR #28 Billy McKinney (X - X - X)
t4.new_ab()
t4.pitch_list("c f b c")
t4.out("!K")

# 2. TOR #29 Devon Travis (X - X - X)
t4.new_ab()
t4.pitch_list("c f f c")
t4.out("!K")

# 3. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("b f b b")
t4.out("F8")


# Bot 4th
# Pitching: TOR #41 Aaron Sanchez
b4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c f b")
b4.out("L4")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("f b f")
b4.hit(1)
b4.thrown_out(2, "7-4", 3, 41)


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 4. TOR #8  Kendrys Morales (X - X - X)
t5.new_ab()
t5.pitch_list("b f b")
t5.out("G6-3")

# 5. TOR #26 Yangervis Solarte (X - X - X)
t5.new_ab()
t5.pitch_list("c f b f")
t5.hit(1)

# 6. TOR #37 Teoscar Hernández (X - X - 26)
t5.new_ab()
t5.pitch_list("s b t b b")
t5.out("L7")

# 7. TOR #68 Rowdy Tellez (X - X - 26)
t5.new_ab()
t5.pitch_list("s c s")
t5.out("K")


# Bot 5th
# Pitching: TOR #41 Aaron Sanchez
b5 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("c b b b f b")
b5.reach("BB")
b5.thrown_out(2, "11 FC4", 1, 41)

# 6. BOS #11 Rafael Devers (X - X - 18)
b5.new_ab()
b5.pitch_list("c c f")
b5.reach("FC4")
b5.advance(3, "12 1B")
b5.advance(4, "19 WP")

# 7. BOS #12 Brock Holt (X - X - 11)
b5.new_ab()
b5.hit(1)
b5.advance(2, "19 SB")
b5.advance(3, "19 WP")

# 8. BOS #3  Sandy León (11 - X - 12)
b5.new_ab()
b5.pitch_list("b 1 b")
b5.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (11 - X - 12)
b5.new_ab()
b5.pitch_list("b s s b b d")
b5.wp()
b5.reach("BB")
b5.thrown_out(2, "50 FC6-4", 3, 41)

# 1. BOS #50 Mookie Betts (12 - X - 19)
b5.new_ab()
b5.reach("FC6-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 8. TOR #9  Danny Jansen (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("(F)P5")

# 9. TOR #67 Jonathan Davis (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(2, "29 PB")

# 1. TOR #28 Billy McKinney (X - X - 67)
t6.new_ab()
t6.out("F8")

# 2. TOR #29 Devon Travis (X - X - 67)
t6.new_ab()
t6.pitch_list("t b 1 f f b")
t6.pb()
t6.out("F8")


# Bot 6th
# Pitching: TOR #41 Aaron Sanchez
b6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b t s s")
b6.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 3. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("s b")
t7.out("G5-3")

# 4. TOR #8  Kendrys Morales (X - X - X)
t7.new_ab()
t7.pitch_list("c s b s")
t7.out("K")

# 5. TOR #26 Yangervis Solarte (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(1)
# Offensive change (TOR): Pinch-runner #1 Aledmys Díaz replaces #26 Yangervis Solarte
t7.offensive_substitution(5, 1, "PR")
t7.atbase("PR")

# 6. TOR #37 Teoscar Hernández (X - X - 26)
t7.new_ab()
t7.pitch_list("b f s b f s")
t7.out("K")


# Bot 7th
# Pitching: TOR #41 Aaron Sanchez
b7 = game.new_inning()

# Defensive switch (TOR): #1 Aledmys Díaz moves to 3B
b7.defensive_switch(1, "5")

# 5. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b")
b7.out("F7")

# 7. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #35 Steven Wright
t8 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #24 David Price
t8.pitching_substitution(35)

# 7. TOR #68 Rowdy Tellez (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(2)
t8.advance(3, "28 FC4-6")

# 8. TOR #9  Danny Jansen (X - 68 - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.thrown_out(2, "28 FC4-6", 2, 35)

# Offensive change (TOR): Pinch-hitter #11 Kevin Pillar replaces #67 Jonathan Davis, batting 9th
t8.offensive_substitution(9, 11, "PH")

# 9. TOR #11 Kevin Pillar (X - 68 - 9)
t8.new_ab()
t8.pitch_list("b b c f s")
t8.out("K")

# 1. TOR #28 Billy McKinney (X - 68 - 9)
t8.new_ab()
t8.reach("FC4-6")

# 2. TOR #29 Devon Travis (68 - X - 28)
t8.new_ab()
t8.pitch_list("s s")
t8.out("L9")


# Bot 8th
# Pitching: TOR #36 Tyler Clippard
b8 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #41 Aaron Sanchez
b8.pitching_substitution(36)

# Defensive switch (TOR): #11 Kevin Pillar moves to CF
b8.defensive_switch(11, "8")

# 8. BOS #3  Sandy León (X - X - X)
b8.new_ab()
b8.pitch_list("s s b f f f")
b8.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)
b8.advance(3, "50 SB")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b8.new_ab()
b8.pitch_list("b c b b b")
b8.reach("BB")
b8.advance(2, "28 SB")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b8.new_ab()
b8.pitch_list("b b c")
b8.out("L6")

# 3. BOS #28 J.D. Martinez (19 - X - 50)
b8.new_ab()
b8.pitch_list("1 b s s b d b")
b8.reach("BB")

# 4. BOS #2  Xander Bogaerts (19 - 50 - 28)
b8.new_ab()
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #35 Steven Wright
t9.pitching_substitution(46)

# 3. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c f")
t9.out("F9")

# 4. TOR #8  Kendrys Morales (X - X - X)
t9.new_ab()
t9.pitch_list("s b f b b s")
t9.out("K")

# Offensive change (TOR): Pinch-hitter #14 Justin Smoak replaces #1 Aledmys Díaz, batting 5th
t9.offensive_substitution(5, 14, "PH")

# 5. TOR #14 Justin Smoak (X - X - X)
t9.new_ab()
t9.pitch_list("b b b d")
t9.reach("BB")
# Offensive change (TOR): Pinch-runner #7 Richard Urena replaces #14 Justin Smoak
t9.offensive_substitution(5, 7, "PR")
t9.atbase("PR")

# Offensive change (TOR): Pinch-hitter #27 Dwight Smith Jr. replaces #37 Teoscar Hernández, batting 6th
t9.offensive_substitution(6, 27, "PH")

# 6. TOR #27 Dwight Smith Jr. (X - X - 14)
t9.new_ab()
t9.pitch_list("c f f c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TOR
# LP: TOR #41 Aaron Sanchez
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
