import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-09-11
# https://www.baseball-reference.com/boxes/BOS/BOS201809110.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/09/11/531580/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-11 19:12-22:20",
        "at": "Fenway Park, Boston, MA",
        "att": "34,747",
        "temp": "68F, Cloudy",
        "wind": "7mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                13: "Lourdes Gurriel Jr.",
                29: "Devon Travis",
                14: "Justin Smoak",
                8: "Kendrys Morales",
                15: "Randal Grichuk",
                11: "Kevin Pillar",
                37: "Teoscar Hernández",
                1: "Aledmys Díaz",
                9: "Danny Jansen",
                # Starting pitcher
                56: "Ryan Borucki",
                # Bench
                7: "Richard Urena",
                26: "Yangervis Solarte",
                68: "Rowdy Tellez",
                28: "Billy McKinney",
                70: "Reese McGuire",
                21: "Luke Maile",
                67: "Jonathan Davis",
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
                41: "Aaron Sanchez",
                36: "Tyler Clippard",
                45: "Thomas Pannone",
                65: "Taylor Guerrieri",
                62: "Mark Leiter Jr.",
                66: "Justin Shafer",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
            },
            "lefties": [56, 58, 50, 45],
            "lineup": [
                [13, "6"],
                [29, "4"],
                [14, "3"],
                [8, "0"],
                [15, "9"],
                [11, "8"],
                [37, "7"],
                [1, "5"],
                [9, "2"],
            ],
            "bench": [
                [7, "SS"],
                [26, "3B"],
                [68, "1B"],
                [28, "LF"],
                [70, "C"],
                [21, "C"],
                [67, "CF"],
                [27, "LF"],
            ],
            "bullpen": [51, 24, 58, 25, 39, 54, 22, 50, 43, 41, 36, 45, 65, 62, 66, 6, 52],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                30: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                12: "Brock Holt",
                59: "Sam Travis",
                11: "Rafael Devers",
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
            "lefties": [41, 57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [25, "3"],
                [5, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [18, "1B"],
                [12, "2B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Jim Wolf",
            "1B": "D.J. Reyburn",
            "2B": "Chris Segal",
            "3B": "Alfonso Márquez",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("s b c b b")
t1.hit(2)

# 2. TOR #29 Devon Travis (X - 13 - X)
t1.new_ab()
t1.pitch_list("c d s f b s")
t1.out("K")

# 3. TOR #14 Justin Smoak (X - 13 - X)
t1.new_ab()
t1.pitch_list("b s b c t")
t1.out("KT")

# 4. TOR #8  Kendrys Morales (X - 13 - X)
t1.new_ab()
t1.pitch_list("d d s b")
t1.reach("HBP")

# 5. TOR #15 Randal Grichuk (X - 13 - 8)
t1.new_ab()
t1.pitch_list("c s b")
t1.out("P4")


# Bot 1st
# Pitching: TOR #56 Ryan Borucki
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b f f b s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b c t s")
b1.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #44 Brandon Workman
t2 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #41 Chris Sale
t2.pitching_substitution(44)

# 6. TOR #11 Kevin Pillar (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G3")

# 7. TOR #37 Teoscar Hernández (X - X - X)
t2.new_ab()
t2.pitch_list("s b b b c f")
t2.out("F8")

# 8. TOR #1  Aledmys Díaz (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b d")
t2.reach("BB")

# 9. TOR #9  Danny Jansen (X - X - 1)
t2.new_ab()
t2.pitch_list("b c f 1 s")
t2.out("K")


# Bot 2nd
# Pitching: TOR #56 Ryan Borucki
b2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c s b f s")
b2.out("K")

# 5. BOS #25 Steve Pearce (X - X - X)
b2.new_ab()
b2.pitch_list("b b c b b")
b2.reach("BB")
b2.thrown_out(2, "5 DP5-4-3", 2, 56)

# 6. BOS #5  Ian Kinsler (X - X - 25)
b2.new_ab()
b2.out("DP5-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #17 Nathan Eovaldi
t3 = game.new_inning()

# Pitching change (BOS): #17 Nathan Eovaldi replaces #44 Brandon Workman
t3.pitching_substitution(17)

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c b b")
t3.reach("BB")
t3.thrown_out(1, "29 PO", 1, 17)

# 2. TOR #29 Devon Travis (X - X - 13)
t3.new_ab()
t3.pitch_list("f s b b f b f 1")
t3.out("G6-3")

# 3. TOR #14 Justin Smoak (X - X - X)
t3.new_ab()
t3.pitch_list("f f b b f")
t3.out("G3")


# Bot 3rd
# Pitching: TOR #56 Ryan Borucki
b3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c b f")
b3.out("G5-3")

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c")
b3.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab()
b3.pitch_list("b f 1")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #17 Nathan Eovaldi
t4 = game.new_inning()

# 4. TOR #8  Kendrys Morales (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("P5")

# 5. TOR #15 Randal Grichuk (X - X - X)
t4.new_ab()
t4.pitch_list("b b f b s s")
t4.out("K")

# 6. TOR #11 Kevin Pillar (X - X - X)
t4.new_ab()
t4.pitch_list("b f f")
t4.out("F7")


# Bot 4th
# Pitching: TOR #56 Ryan Borucki
b4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b f b f")
b4.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.out("F8")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s b")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #17 Nathan Eovaldi
t5 = game.new_inning()

# 7. TOR #37 Teoscar Hernández (X - X - X)
t5.new_ab()
t5.pitch_list("b c b c b s")
t5.out("K")

# 8. TOR #1  Aledmys Díaz (X - X - X)
t5.new_ab()
t5.out("L8")

# 9. TOR #9  Danny Jansen (X - X - X)
t5.new_ab()
t5.hit(1)

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - 9)
t5.new_ab()
t5.pitch_list("c b f b f b s")
t5.out("K")


# Bot 5th
# Pitching: TOR #56 Ryan Borucki
b5 = game.new_inning()

# 5. BOS #25 Steve Pearce (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F9")

# 6. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c b s")
b5.out("G6-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.hit(1)
b5.thrown_out(2, "3 FC6-4", 3, 56)

# 8. BOS #3  Sandy León (X - X - 36)
b5.new_ab()
b5.pitch_list("c c")
b5.reach("FC6-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #17 Nathan Eovaldi
t6 = game.new_inning()

# 2. TOR #29 Devon Travis (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(2)
t6.advance(3, "14 F9")
t6.advance(4, "15 SB")

# 3. TOR #14 Justin Smoak (X - 29 - X)
t6.new_ab()
t6.pitch_list("f f b f f f f b f")
t6.out("F9")

# 4. TOR #8  Kendrys Morales (29 - X - X)
t6.new_ab()
t6.pitch_list("b d b d")
t6.reach("BB")
# Offensive change (TOR): Pinch-runner #67 Jonathan Davis replaces #8 Kendrys Morales
t6.offensive_substitution(4, 67, "PR")
t6.atbase("PR")
t6.error(4)
t6.advance(2, "15 SB")
t6.advance(3, "15 E4")
t6.advance(4, "11 1B")

# 5. TOR #15 Randal Grichuk (29 - X - 8)
t6.new_ab()
t6.pitch_list("b d f f 1 b s")
t6.out("K")

# 6. TOR #11 Kevin Pillar (67 - X - X)
t6.new_ab()
t6.pitch_list("s b f")
t6.hit(1, rbis=1)

# Pitching change (BOS): #70 Ryan Brasier replaces #17 Nathan Eovaldi
t6.pitching_substitution(70)

# 7. TOR #37 Teoscar Hernández (X - X - 11)
t6.new_ab()
t6.pitch_list("b 1 s f b s")
t6.out("K")


# Bot 6th
# Pitching: TOR #56 Ryan Borucki
b6 = game.new_inning()

# Defensive switch (TOR): #67 Jonathan Davis moves to DH
b6.defensive_switch(67, "0")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("b s c s")
b6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b b c c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# 8. TOR #1  Aledmys Díaz (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F8")

# 9. TOR #9  Danny Jansen (X - X - X)
t7.new_ab()
t7.pitch_list("b c s f b f b c")
t7.out("!K")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G5-3")


# Bot 7th
# Pitching: TOR #56 Ryan Borucki
b7 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("f f")
b7.out("G6-3")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b b")
b7.reach("BB")
b7.advance(4, "25 3B")

# 5. BOS #25 Steve Pearce (X - X - 2)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(3, rbis=1)
# Offensive change (BOS): Pinch-runner #30 Tzu-Wei Lin replaces #25 Steve Pearce
b7.offensive_substitution(5, 30, "PR")
b7.atbase("PR")
b7.advance(4, "12 HR")

# Pitching change (TOR): #52 Ryan Tepera replaces #56 Ryan Borucki
b7.pitching_substitution(52)

# 6. BOS #5  Ian Kinsler (25 - X - X)
b7.new_ab()
b7.pitch_list("s f b f f s")
b7.out("K")

# 7. BOS #36 Eduardo Núñez (30 - X - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(4, "12 HR")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #3 Sandy León, batting 8th
b7.offensive_substitution(8, 12, "PH")

# 8. BOS #12 Brock Holt (30 - X - 36)
b7.new_ab()
b7.pitch_list("b c b c 1")
b7.hit(4, rbis=3)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c f b")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #76 Hector Velázquez
t8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #70 Ryan Brasier
t8.pitching_substitution(76)

# Defensive change (BOS): #7 Christian Vázquez replaces #30 Tzu-Wei Lin (PR), playing C, batting 5th
t8.defensive_substitution(5, 7, "2")

# Defensive switch (BOS): #12 Brock Holt moves to 1B
t8.defensive_switch(12, "3")

# 2. TOR #29 Devon Travis (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G4-3")

# Pitching change (BOS): #66 Bobby Poyner replaces #76 Hector Velázquez
t8.pitching_substitution(66)

# 3. TOR #14 Justin Smoak (X - X - X)
t8.new_ab()
t8.pitch_list("c b s b f f b")
t8.out("F7")

# Offensive change (TOR): Pinch-hitter #26 Yangervis Solarte replaces #67 Jonathan Davis, batting 4th
t8.offensive_substitution(4, 26, "PH")

# 4. TOR #26 Yangervis Solarte (X - X - X)
t8.new_ab()
t8.pitch_list("f b f f b f f f b")
t8.hit(1)

# Pitching change (BOS): #56 Joe Kelly replaces #66 Bobby Poyner
t8.pitching_substitution(56)

# 5. TOR #15 Randal Grichuk (X - X - 26)
t8.new_ab()
t8.pitch_list("b c f b f b f s")
t8.out("K")


# Bot 8th
# Pitching: TOR #39 Jake Petricka
b8 = game.new_inning()

# Pitching change (TOR): #39 Jake Petricka replaces #52 Ryan Tepera
b8.pitching_substitution(39)

# Defensive switch (TOR): #26 Yangervis Solarte moves to DH
b8.defensive_switch(26, "0")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b b b")
b8.reach("BB")
b8.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b8.new_ab()
b8.pitch_list("l")
b8.hit(2, rbis=1)
b8.advance(3, "28 1B")
b8.advance(4, "5 1B")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b8.new_ab()
b8.pitch_list("f b")
b8.hit(1)
b8.advance(3, "5 1B")
b8.advance(4, "36 WP")

# 4. BOS #2  Xander Bogaerts (16 - X - 28)
b8.new_ab()
b8.pitch_list("f")
b8.out("(F)F9")

# 5. BOS #7  Christian Vázquez (16 - X - 28)
b8.new_ab()
b8.pitch_list("d b b c")
b8.out("L6")

# 6. BOS #5  Ian Kinsler (16 - X - 28)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1, rbis=1)
b8.advance(2, "36 SB")
b8.advance(3, "36 WP")

# Pitching change (TOR): #65 Taylor Guerrieri replaces #39 Jake Petricka
b8.pitching_substitution(65)

# 7. BOS #36 Eduardo Núñez (28 - X - 5)
b8.new_ab()
b8.pitch_list("f b b b c")
b8.wp()
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #37 Heath Hembree
t9 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #56 Joe Kelly
t9.pitching_substitution(37)

# 6. TOR #11 Kevin Pillar (X - X - X)
t9.new_ab()
t9.pitch_list("b b c c c")
t9.out("!K")

# Offensive change (TOR): Pinch-hitter #27 Dwight Smith Jr. replaces #37 Teoscar Hernández, batting 7th
t9.offensive_substitution(7, 27, "PH")

# 7. TOR #27 Dwight Smith Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("b b f")
t9.out("F7")

# Offensive change (TOR): Pinch-hitter #68 Rowdy Tellez replaces #1 Aledmys Díaz, batting 8th
t9.offensive_substitution(8, 68, "PH")

# 8. TOR #68 Rowdy Tellez (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c")
t9.out("F8")

# Winning team: BOS
# WP: BOS #70 Ryan Brasier
game.winning_pitcher(70)

# Loser team: TOR
# LP: TOR #52 Ryan Tepera
game.losing_pitcher(52, is_away_team=True)

# print(game)
game.generate_scorecard()
