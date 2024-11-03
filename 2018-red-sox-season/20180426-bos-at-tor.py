import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-04-26
# https://www.baseball-reference.com/boxes/TOR/TOR201804260.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/04/26/529777/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-26 19:08-22:16",
        "at": "Rogers Centre, Toronto, ON",
        "att": "23,571",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                12: "Brock Holt",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                39: "Carson Smith",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [41, 57, 24, 31, 61],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [13, "0"],
                [28, "9"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [57, 24, 46, 76, 39, 22, 31, 61, 32, 37],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 25,
            "roster": {
                # Lineup
                28: "Steve Pearce",
                37: "Teoscar Hernández",
                14: "Justin Smoak",
                26: "Yangervis Solarte",
                11: "Kevin Pillar",
                13: "Lourdes Gurriel Jr.",
                15: "Randal Grichuk",
                21: "Luke Maile",
                29: "Devon Travis",
                # Starting pitcher
                25: "Marco Estrada",
                # Bench
                55: "Russell Martin",
                1: "Aledmys Díaz",
                18: "Curtis Granderson",
                8: "Kendrys Morales",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                24: "Danny Barnes",
                58: "Tim Mayza",
                54: "Roberto Osuna",
                41: "Aaron Sanchez",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 58, 33],
            "lineup": [
                [28, "0"],
                [37, "7"],
                [14, "3"],
                [26, "5"],
                [11, "8"],
                [13, "6"],
                [15, "9"],
                [21, "2"],
                [29, "4"],
            ],
            "bench": [
                [55, "C"],
                [1, "SS"],
                [18, "CF"],
                [8, "DH"],
            ],
            "bullpen": [62, 57, 24, 58, 54, 41, 36, 22, 6, 52, 33],
        },
        "umpires": {
            "HP": "Ramon De Jesus",
            "1B": "Kerwin Danley",
            "2B": "Dan Iassogna",
            "3B": "Scott Barry",
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
# Pitching: TOR #25 Marco Estrada
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("(F)P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c f s")
t1.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("s c b b b f")
t1.hit(1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t1.new_ab()
t1.pitch_list("b")
t1.out("F7")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. TOR #28 Steve Pearce (X - X - X)
b1.new_ab()
b1.pitch_list("c s b")
b1.out("(F)L3")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b b")
b1.reach("BB")
b1.advance(3, "14 1B")
b1.advance(4, "11 SF9")

# 3. TOR #14 Justin Smoak (X - X - 37)
b1.new_ab()
b1.hit(1)
b1.advance(2, "26 HBP")

# 4. TOR #26 Yangervis Solarte (37 - X - 14)
b1.new_ab(is_risp=True)
b1.pitch_list("f")
b1.reach("HBP")

# 5. TOR #11 Kevin Pillar (37 - 14 - 26)
b1.new_ab(is_risp=True)
b1.pitch_list("s s")
b1.out("SF9", rbis=1)

# 6. TOR #13 Lourdes Gurriel Jr. (X - 14 - 26)
b1.new_ab(is_risp=True)
b1.pitch_list("c f f")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #25 Marco Estrada
t2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b c f f b b s")
t2.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c f b b f b s")
t2.out("K")

# 7. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 7. TOR #15 Randal Grichuk (X - X - X)
b2.new_ab()
b2.pitch_list("f c b b f")
b2.out("(F)P2")

# 8. TOR #21 Luke Maile (X - X - X)
b2.new_ab()
b2.pitch_list("c s b c")
b2.out("!K")

# 9. TOR #29 Devon Travis (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(4)

# 1. TOR #28 Steve Pearce (X - X - X)
b2.new_ab()
b2.out("(F)P2")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #25 Marco Estrada
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b f f c")
t3.out("!K")

# 9. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b")
t3.hit(2)
# Offensive change (BOS): Pinch-runner #5 Tzu-Wei Lin replaces #12 Brock Holt
t3.offensive_substitution(9, 5, "PR")
t3.atbase("PR")
t3.advance(4, "16 2B")

# 1. BOS #50 Mookie Betts (X - 12 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("d")
t3.out("F8")

# 2. BOS #16 Andrew Benintendi (X - 5 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.hit(2, rbis=1)
t3.thrown_out(2, "28 PO", 3, 25)

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f b s b d d")
t3.reach("BB")

# 4. BOS #28 J.D. Martinez (X - 16 - 13)
t3.new_ab(is_risp=True)
t3.pitch_list("b 2")
t3.no_ab("PO")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# Defensive switch (BOS): #5 Tzu-Wei Lin moves to SS
b3.defensive_switch(5, "6")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b3.new_ab()
b3.pitch_list("c s s")
b3.out("K")

# 3. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.hit(4)

# 4. TOR #26 Yangervis Solarte (X - X - X)
b3.new_ab()
b3.pitch_list("b b s")
b3.out("L8")

# 5. TOR #11 Kevin Pillar (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(2)

# 6. TOR #13 Lourdes Gurriel Jr. (X - 11 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b s b f")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #25 Marco Estrada
t4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.hit(1)
t4.thrown_out(2, "18 FC4-6", 1, 25)

# 5. BOS #18 Mitch Moreland (X - X - 28)
t4.new_ab()
t4.pitch_list("c")
t4.reach("FC4-6")
t4.advance(3, "36 2B")
t4.advance(4, "11 SF8")

# 6. BOS #36 Eduardo Núñez (X - X - 18)
t4.new_ab()
t4.pitch_list("c f b f")
t4.hit(2)
t4.advance(3, "11 SF8")

# 7. BOS #11 Rafael Devers (18 - 36 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b c s")
t4.out("SF8", rbis=1)

# 8. BOS #7  Christian Vázquez (36 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f b b c")
t4.out("P4")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 7. TOR #15 Randal Grichuk (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("G4-3")

# 8. TOR #21 Luke Maile (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b b s")
b4.out("K")

# 9. TOR #29 Devon Travis (X - X - X)
b4.new_ab()
b4.pitch_list("b f c b b")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #25 Marco Estrada
t5 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t5.new_ab()
t5.pitch_list("c c f b")
t5.out("P3")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c c b")
t5.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("f f b f b")
t5.hit(1)
t5.advance(3, "13 1B")
t5.advance(4, "28 HR")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t5.new_ab()
t5.pitch_list("b 1 c f f 1")
t5.hit(1)
t5.advance(4, "28 HR")

# 4. BOS #28 J.D. Martinez (16 - X - 13)
t5.new_ab(is_risp=True)
t5.hit(4, rbis=3)

# 5. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("b s b f")
t5.out("F7")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 1. TOR #28 Steve Pearce (X - X - X)
b5.new_ab()
b5.pitch_list("b b c s f b f f f")
b5.out("P6")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b5.new_ab()
b5.pitch_list("b s s f b f f b f b")
b5.reach("BB")

# 3. TOR #14 Justin Smoak (X - X - 37)
b5.new_ab()
b5.pitch_list("f f f b s")
b5.out("K")

# 4. TOR #26 Yangervis Solarte (X - X - 37)
b5.new_ab()
b5.pitch_list("f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #62 Aaron Loup
t6 = game.new_inning()

# Pitching change (TOR): #62 Aaron Loup replaces #25 Marco Estrada
t6.pitching_substitution(62)

# 6. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("c c b f f")
t6.out("F9")

# 7. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b s b s s")
t6.out("K")

# 8. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("L9")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 5. TOR #11 Kevin Pillar (X - X - X)
b6.new_ab()
b6.pitch_list("b f s b")
b6.out("F9")

# 6. TOR #13 Lourdes Gurriel Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("s f b f f")
b6.out("G5-3")

# 7. TOR #15 Randal Grichuk (X - X - X)
b6.new_ab()
b6.out("(F)P2")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #62 Aaron Loup
t7 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t7.new_ab()
t7.pitch_list("c b s")
t7.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b c f")
t7.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("c f c")
t7.out("!K")


# Bot 7th
# Pitching: BOS #39 Carson Smith
b7 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #41 Chris Sale
b7.pitching_substitution(39)

# 8. TOR #21 Luke Maile (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G6-3")

# 9. TOR #29 Devon Travis (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b")
b7.hit(3)
b7.advance(4, "8 G1-6-3")

# Offensive change (TOR): Pinch-hitter #8 Kendrys Morales replaces #28 Steve Pearce, batting 1st
b7.offensive_substitution(1, 8, "PH")

# 1. TOR #8  Kendrys Morales (29 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f b 3 f")
b7.out("G1-6-3", rbis=1)

# 2. TOR #37 Teoscar Hernández (X - X - X)
b7.new_ab()
b7.hit(2)

# Pitching change (BOS): #32 Matt Barnes replaces #39 Carson Smith
b7.pitching_substitution(32)

# 3. TOR #14 Justin Smoak (X - 37 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c d c b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #22 Seunghwan Oh
t8 = game.new_inning()

# Pitching change (TOR): #22 Seunghwan Oh replaces #62 Aaron Loup
t8.pitching_substitution(22)

# Defensive switch (TOR): #8 Kendrys Morales moves to DH
t8.defensive_switch(8, "0")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.pitch_list("c f b s")
t8.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("f b b f f b")
t8.out("F8")

# 5. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b s")
t8.out("F8")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# 4. TOR #26 Yangervis Solarte (X - X - X)
b8.new_ab()
b8.pitch_list("s s b b b c")
b8.out("!K")

# 5. TOR #11 Kevin Pillar (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b f b")
b8.reach("BB")
b8.advance(2, "18 BB")
b8.advance(3, "15 G6-3")

# Offensive change (TOR): Pinch-hitter #18 Curtis Granderson replaces #13 Lourdes Gurriel Jr., batting 6th
b8.offensive_substitution(6, 18, "PH")

# 6. TOR #18 Curtis Granderson (X - X - 11)
b8.new_ab()
b8.pitch_list("b c b b b")
b8.reach("BB")
b8.advance(2, "15 G6-3")

# 7. TOR #15 Randal Grichuk (X - 11 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b c")
b8.out("G6-3")

# 8. TOR #21 Luke Maile (11 - 18 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #24 Danny Barnes
t9 = game.new_inning()

# Pitching change (TOR): #24 Danny Barnes replaces #22 Seunghwan Oh
t9.pitching_substitution(24)

# Defensive change (TOR): #1 Aledmys Díaz replaces #18 Curtis Granderson (PH), playing SS, batting 6th
t9.defensive_substitution(6, 1, "6")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 7. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b b b")
t9.reach("BB")
t9.advance(2, "5 SB")

# 8. BOS #7  Christian Vázquez (X - X - 11)
t9.new_ab()
t9.out("L8")

# 9. BOS #5  Tzu-Wei Lin (X - X - 11)
t9.new_ab(is_risp=True)
t9.pitch_list("b b f 1 b s f b")
t9.reach("BB")

# 1. BOS #50 Mookie Betts (X - 11 - 5)
t9.new_ab(is_risp=True)
t9.out("F8")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b9.pitching_substitution(46)

# Defensive switch (BOS): #50 Mookie Betts moves to RF
b9.defensive_switch(50, "9")

# Defensive change (BOS): #19 Jackie Bradley Jr. replaces #28 J.D. Martinez (RF), playing CF, batting 4th
b9.defensive_substitution(4, 19, "8")

# 9. TOR #29 Devon Travis (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b s s")
b9.out("K")

# 1. TOR #8  Kendrys Morales (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("(F)P5")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b9.new_ab()
b9.pitch_list("c b s f f b b")
b9.out("P3")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TOR
# LP: TOR #25 Marco Estrada
game.losing_pitcher(25)

# print(game)
game.generate_scorecard()
