import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-09-13
# https://www.baseball-reference.com/boxes/BOS/BOS201809130.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/09/13/531603/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-13 19:10-22:00",
        "at": "Fenway Park, Boston, MA",
        "att": "36,427",
        "temp": "68F, Partly Cloudy",
        "wind": "6mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 43,
            "roster": {
                # Lineup
                13: "Lourdes Gurriel Jr.",
                26: "Yangervis Solarte",
                14: "Justin Smoak",
                8: "Kendrys Morales",
                15: "Randal Grichuk",
                11: "Kevin Pillar",
                37: "Teoscar Hernández",
                1: "Aledmys Díaz",
                70: "Reese McGuire",
                # Starting pitcher
                43: "Sam Gaviglio",
                # Bench
                7: "Richard Urena",
                68: "Rowdy Tellez",
                28: "Billy McKinney",
                29: "Devon Travis",
                21: "Luke Maile",
                9: "Danny Jansen",
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
                56: "Ryan Borucki",
                41: "Aaron Sanchez",
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
                [13, "6"],
                [26, "4"],
                [14, "3"],
                [8, "0"],
                [15, "9"],
                [11, "8"],
                [37, "7"],
                [1, "5"],
                [70, "2"],
            ],
            "bench": [
                [7, "SS"],
                [68, "1B"],
                [28, "LF"],
                [29, "2B"],
                [21, "C"],
                [9, "C"],
                [67, "CF"],
                [27, "LF"],
            ],
            "bullpen": [51, 24, 58, 25, 39, 54, 22, 50, 56, 41, 36, 45, 65, 62, 66, 6, 52],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                5: "Ian Kinsler",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                23: "Blake Swihart",
                36: "Eduardo Núñez",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                12: "Brock Holt",
                59: "Sam Travis",
                11: "Rafael Devers",
                50: "Mookie Betts",
                3: "Sandy León",
                0: "Brandon Phillips",
                # Bullpen
                47: "Tyler Thornburg",
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
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [16, "7"],
                [5, "4"],
                [18, "3"],
                [28, "9"],
                [2, "6"],
                [23, "0"],
                [36, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [12, "2B"],
                [59, "1B"],
                [11, "3B"],
                [50, "SS"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Chris Segal",
            "1B": "Alfonso Márquez",
            "2B": "Jim Wolf",
            "3B": "D.J. Reyburn",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("f b c c")
t1.out("!K")

# 2. TOR #26 Yangervis Solarte (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F7")

# 3. TOR #14 Justin Smoak (X - X - X)
t1.new_ab()
t1.pitch_list("s b b c b f s")
t1.out("K")


# Bot 1st
# Pitching: TOR #43 Sam Gaviglio
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.out("G4-3")

# 2. BOS #5  Ian Kinsler (X - X - X)
b1.new_ab()
b1.pitch_list("c c")
b1.out("P3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 4. TOR #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.hit(2)
t2.advance(3, "37 1B")

# 5. TOR #15 Randal Grichuk (X - 8 - X)
t2.new_ab()
t2.pitch_list("b b s c s")
t2.out("K")

# 6. TOR #11 Kevin Pillar (X - 8 - X)
t2.new_ab()
t2.pitch_list("f")
t2.out("F8")

# 7. TOR #37 Teoscar Hernández (X - 8 - X)
t2.new_ab()
t2.hit(1)

# 8. TOR #1  Aledmys Díaz (8 - X - 37)
t2.new_ab()
t2.out("G5-3")


# Bot 2nd
# Pitching: TOR #43 Sam Gaviglio
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b c c f b")
b2.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b f")
b2.out("G5-3")

# 6. BOS #23 Blake Swihart (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.thrown_out(2, "36 FC4", 2, 43)

# 7. BOS #36 Eduardo Núñez (X - X - 23)
b2.new_ab()
b2.pitch_list("d f b f")
b2.reach("FC4")
b2.thrown_out(2, "7 FC6-4", 3, 43)

# 8. BOS #7  Christian Vázquez (X - X - 36)
b2.new_ab()
b2.pitch_list("b f 1 b")
b2.reach("FC6-4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 9. TOR #70 Reese McGuire (X - X - X)
t3.new_ab()
t3.pitch_list("c b b c b")
t3.out("G5-3")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t3.new_ab()
t3.hit(1)
t3.advance(2, "26 G1-3")
t3.advance(4, "14 1B")

# 2. TOR #26 Yangervis Solarte (X - X - 13)
t3.new_ab()
t3.out("G1-3")

# 3. TOR #14 Justin Smoak (X - 13 - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1, rbis=1)

# 4. TOR #8  Kendrys Morales (X - X - 14)
t3.new_ab()
t3.pitch_list("c b b d s")
t3.out("G6-3")


# Bot 3rd
# Pitching: TOR #43 Sam Gaviglio
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.hit(2)
b3.advance(3, "16 G6-3")
b3.advance(4, "5 SF7")

# 1. BOS #16 Andrew Benintendi (X - 19 - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G6-3")

# 2. BOS #5  Ian Kinsler (19 - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("SF7", rbis=1)

# 3. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("b f b")
b3.hit(1)
b3.advance(2, "28 1B")
b3.advance(3, "2 1B")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b3.new_ab()
b3.hit(1)
b3.advance(2, "2 1B")
b3.thrown_out(3, "23 FC5", 3, 43)

# 5. BOS #2  Xander Bogaerts (X - 18 - 28)
b3.new_ab()
b3.pitch_list("c b b")
b3.hit(1)
b3.advance(2, "23 FC5")

# 6. BOS #23 Blake Swihart (18 - 28 - 2)
b3.new_ab()
b3.pitch_list("c b")
b3.reach("FC5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 5. TOR #15 Randal Grichuk (X - X - X)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(2, "11 G5-3")

# 6. TOR #11 Kevin Pillar (X - X - 15)
t4.new_ab()
t4.pitch_list("b")
t4.out("G5-3")

# 7. TOR #37 Teoscar Hernández (X - 15 - X)
t4.new_ab()
t4.pitch_list("f b")
t4.out("F7")

# 8. TOR #1  Aledmys Díaz (X - 15 - X)
t4.new_ab()
t4.pitch_list("b b d f")
t4.out("F9")


# Bot 4th
# Pitching: TOR #43 Sam Gaviglio
b4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.hit(2)
# Offensive change (BOS): Pinch-runner #11 Rafael Devers replaces #36 Eduardo Núñez
b4.offensive_substitution(7, 11, "PR")
b4.atbase("PR")
b4.advance(3, "19 G4-3")

# 8. BOS #7  Christian Vázquez (X - 36 - X)
b4.new_ab()
b4.pitch_list("d d")
b4.out("G5-3")

# Pitching change (TOR): #50 José Manuel Fernández replaces #43 Sam Gaviglio
b4.pitching_substitution(50)

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b4.new_ab()
b4.pitch_list("f b b f")
b4.out("G4-3")

# 1. BOS #16 Andrew Benintendi (11 - X - X)
b4.new_ab()
b4.pitch_list("s b")
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# Defensive switch (BOS): #11 Rafael Devers moves to 3B
t5.defensive_switch(11, "5")

# 9. TOR #70 Reese McGuire (X - X - X)
t5.new_ab()
t5.pitch_list("c b c c")
t5.out("!K")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c c f f s")
t5.out("K")

# 2. TOR #26 Yangervis Solarte (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("L4")


# Bot 5th
# Pitching: TOR #50 José Manuel Fernández
b5 = game.new_inning()

# 2. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.out("F9")

# 3. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("c b s b")
b5.out("G4-3")

# Pitching change (TOR): #62 Mark Leiter Jr. replaces #50 José Manuel Fernández
b5.pitching_substitution(62)

# 4. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("c f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 3. TOR #14 Justin Smoak (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f f b c")
t6.out("!K")

# 4. TOR #8  Kendrys Morales (X - X - X)
t6.new_ab()
t6.pitch_list("b c s")
t6.out("L7")

# 5. TOR #15 Randal Grichuk (X - X - X)
t6.new_ab()
t6.pitch_list("b c s s")
t6.out("K")


# Bot 6th
# Pitching: TOR #62 Mark Leiter Jr.
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f f s")
b6.out("K")

# 6. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("b s c s")
b6.out("K")

# 7. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("c b b")
b6.hit(4)

# 8. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("f b f b")
b6.hit(1)
b6.advance(2, "19 SB")

# Pitching change (TOR): #58 Tim Mayza replaces #62 Mark Leiter Jr.
b6.pitching_substitution(58)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
b6.new_ab()
b6.pitch_list("b b f s d s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #57 Eduardo Rodriguez
t7.pitching_substitution(70)

# 6. TOR #11 Kevin Pillar (X - X - X)
t7.new_ab()
t7.pitch_list("c s f f")
t7.out("L9")

# 7. TOR #37 Teoscar Hernández (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("G4-3")

# 8. TOR #1  Aledmys Díaz (X - X - X)
t7.new_ab()
t7.out("F8")


# Bot 7th
# Pitching: TOR #58 Tim Mayza
b7 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c b b s f")
b7.out("G6-3")

# 2. BOS #5  Ian Kinsler (X - X - X)
b7.new_ab()
b7.out("G4-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #66 Bobby Poyner
t8 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #70 Ryan Brasier
t8.pitching_substitution(66)

# Offensive change (TOR): Pinch-hitter #9 Danny Jansen replaces #70 Reese McGuire, batting 9th
t8.offensive_substitution(9, 9, "PH")

# 9. TOR #9  Danny Jansen (X - X - X)
t8.new_ab()
t8.pitch_list("c s b")
t8.out("P4")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t8.new_ab()
t8.hit(4)

# 2. TOR #26 Yangervis Solarte (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("(F)P2")

# Pitching change (BOS): #56 Joe Kelly replaces #66 Bobby Poyner
t8.pitching_substitution(56)

# 3. TOR #14 Justin Smoak (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
# Offensive change (TOR): Pinch-runner #67 Jonathan Davis replaces #14 Justin Smoak
t8.offensive_substitution(3, 67, "PR")
t8.atbase("PR")
t8.advance(2, "8 1B")
t8.advance(3, "15 HBP")
t8.advance(4, "11 HBP")

# 4. TOR #8  Kendrys Morales (X - X - 14)
t8.new_ab()
t8.pitch_list("b f")
t8.hit(1)
# Offensive change (TOR): Pinch-runner #27 Dwight Smith Jr. replaces #8 Kendrys Morales
t8.offensive_substitution(4, 27, "PR")
t8.atbase("PR")
t8.advance(2, "15 HBP")
t8.advance(3, "11 HBP")

# 5. TOR #15 Randal Grichuk (X - 67 - 8)
t8.new_ab()
t8.pitch_list("c d b")
t8.reach("HBP")
t8.advance(2, "11 HBP")

# 6. TOR #11 Kevin Pillar (67 - 27 - 15)
t8.new_ab()
t8.pitch_list("f s b")
t8.reach("HBP", rbis=1)

# Pitching change (BOS): #44 Brandon Workman replaces #56 Joe Kelly
t8.pitching_substitution(44)

# Offensive change (TOR): Pinch-hitter #28 Billy McKinney replaces #37 Teoscar Hernández, batting 7th
t8.offensive_substitution(7, 28, "PH")

# 7. TOR #28 Billy McKinney (27 - 15 - 11)
t8.new_ab()
t8.pitch_list("f s s")
t8.out("K")


# Bot 8th
# Pitching: TOR #24 Danny Barnes
b8 = game.new_inning()

# Pitching change (TOR): #24 Danny Barnes replaces #58 Tim Mayza
b8.pitching_substitution(24)

# Defensive change (TOR): #68 Rowdy Tellez replaces #67 Jonathan Davis (PR), playing 1B, batting 3rd
b8.defensive_substitution(3, 68, "3")

# Defensive switch (TOR): #27 Dwight Smith Jr. moves to DH
b8.defensive_switch(27, "0")

# Defensive switch (TOR): #28 Billy McKinney moves to LF
b8.defensive_switch(28, "7")

# Defensive switch (TOR): #9 Danny Jansen moves to C
b8.defensive_switch(9, "2")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("f b f")
b8.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b c b")
b8.hit(2)
b8.advance(3, "23 SB")
b8.advance("U", "23 E4")

# 6. BOS #23 Blake Swihart (X - 2 - X)
b8.new_ab()
b8.pitch_list("d f s b")
b8.error(4)
b8.reach("E4")
b8.advance(2, "11 SB")

# 7. BOS #11 Rafael Devers (X - X - 23)
b8.new_ab()
b8.pitch_list("1 1 f s b 1 b b s")
b8.out("K")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #7 Christian Vázquez, batting 8th
b8.offensive_substitution(8, 12, "PH")

# 8. BOS #12 Brock Holt (X - 23 - X)
b8.new_ab()
b8.pitch_list("b b 2 c c d c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #44 Brandon Workman
t9.pitching_substitution(46)

# Defensive change (BOS): #3 Sandy León replaces #12 Brock Holt (PH), playing C, batting 8th
t9.defensive_substitution(8, 3, "2")

# 8. TOR #1  Aledmys Díaz (X - X - X)
t9.new_ab()
t9.out("F7")

# 9. TOR #9  Danny Jansen (X - X - X)
t9.new_ab()
t9.pitch_list("c f b s")
t9.out("K")

# 1. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("s s")
t9.out("F9")

# Winning team: BOS
# WP: BOS #44 Brandon Workman
game.winning_pitcher(44)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TOR
# LP: TOR #24 Danny Barnes
game.losing_pitcher(24, is_away_team=True)

# print(game)
game.generate_scorecard()
