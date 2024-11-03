import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-04-24
# https://www.baseball-reference.com/boxes/TOR/TOR201804240.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/04/24/529747/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-24 19:08-21:59",
        "at": "Rogers Centre, Toronto, ON",
        "att": "20,070",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                12: "Brock Holt",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [3, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 33,
            "roster": {
                # Lineup
                18: "Curtis Granderson",
                37: "Teoscar Hernández",
                14: "Justin Smoak",
                26: "Yangervis Solarte",
                28: "Steve Pearce",
                55: "Russell Martin",
                11: "Kevin Pillar",
                1: "Aledmys Díaz",
                29: "Devon Travis",
                # Starting pitcher
                33: "J.A. Happ",
                # Bench
                15: "Randal Grichuk",
                21: "Luke Maile",
                13: "Lourdes Gurriel Jr.",
                8: "Kendrys Morales",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                24: "Danny Barnes",
                58: "Tim Mayza",
                25: "Marco Estrada",
                54: "Roberto Osuna",
                41: "Aaron Sanchez",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
            },
            "lefties": [33, 62, 57, 58],
            "lineup": [
                [18, "9"],
                [37, "7"],
                [14, "3"],
                [26, "5"],
                [28, "0"],
                [55, "2"],
                [11, "8"],
                [1, "6"],
                [29, "4"],
            ],
            "bench": [
                [15, "RF"],
                [21, "C"],
                [13, "LF"],
                [8, "DH"],
            ],
            "bullpen": [62, 57, 24, 58, 25, 54, 41, 36, 22, 6, 52],
        },
        "umpires": {
            "HP": "Dan Iassogna",
            "1B": "Scott Barry",
            "2B": "Ramon De Jesus",
            "3B": "Kerwin Danley",
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
# Pitching: TOR #33 J.A. Happ
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.out("(F)P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b t c f s")
t1.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. TOR #18 Curtis Granderson (X - X - X)
b1.new_ab()
b1.pitch_list("c b b c s")
b1.out("K")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b1.new_ab()
b1.pitch_list("f b s f b f b b")
b1.reach("BB")

# 3. TOR #14 Justin Smoak (X - X - 37)
b1.new_ab()
b1.pitch_list("b b c c c")
b1.out("!K")

# 4. TOR #26 Yangervis Solarte (X - X - 37)
b1.new_ab()
b1.pitch_list("1 c f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #33 J.A. Happ
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G4-3")

# 5. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c b f")
t2.out("G6-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("(F)F9")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. TOR #28 Steve Pearce (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b b")
b2.reach("BB")
b2.advance(3, "55 1B")
b2.advance(4, "11 FC5")

# 6. TOR #55 Russell Martin (X - X - 28)
b2.new_ab()
b2.hit(1)
b2.advance(2, "11 FC5")
b2.advance(3, "1 FC6-4")
b2.thrown_out(4, "29 FC5-2", 2, 22)

# 7. TOR #11 Kevin Pillar (28 - X - 55)
b2.new_ab(is_risp=True)
b2.reach("FC5", rbis=1)
b2.thrown_out(2, "1 FC6-4", 1, 22)

# 8. TOR #1  Aledmys Díaz (X - 55 - 11)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.reach("FC6-4")
b2.advance(2, "29 FC5-2")
b2.advance(3, "18 WP")
b2.advance(4, "18 1B")

# 9. TOR #29 Devon Travis (55 - X - 1)
b2.new_ab(is_risp=True)
b2.reach("FC5-2")
b2.advance(2, "18 WP")
b2.advance(4, "18 1B")

# 1. TOR #18 Curtis Granderson (X - 1 - 29)
b2.new_ab(is_risp=True)
b2.pitch_list("b c c b")
b2.wp()
b2.hit(1, rbis=2)

# 2. TOR #37 Teoscar Hernández (X - X - 18)
b2.new_ab()
b2.pitch_list("b f s s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #33 J.A. Happ
t3 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)

# 8. BOS #3  Sandy León (X - X - 19)
t3.new_ab()
t3.pitch_list("c b b f s")
t3.out("K")

# 9. BOS #12 Brock Holt (X - X - 19)
t3.new_ab()
t3.pitch_list("c c f s")
t3.out("K")

# 1. BOS #50 Mookie Betts (X - X - 19)
t3.new_ab()
t3.pitch_list("c b b c b c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 3. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")

# 4. TOR #26 Yangervis Solarte (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 5. TOR #28 Steve Pearce (X - X - X)
b3.new_ab()
b3.pitch_list("f b s b b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #33 J.A. Happ
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("f f b b f s")
t4.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("f b")
t4.hit(1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t4.new_ab()
t4.pitch_list("b s f b s")
t4.out("K")

# 5. BOS #11 Rafael Devers (X - X - 13)
t4.new_ab()
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 6. TOR #55 Russell Martin (X - X - X)
b4.new_ab()
b4.pitch_list("f c b c")
b4.out("!K")

# 7. TOR #11 Kevin Pillar (X - X - X)
b4.new_ab()
b4.pitch_list("c f b f b f f s")
b4.out("K")

# 8. TOR #1  Aledmys Díaz (X - X - X)
b4.new_ab()
b4.pitch_list("s s b b c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #33 J.A. Happ
t5 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L8")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.out("F8")

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c b f c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 9. TOR #29 Devon Travis (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G5-3")

# 1. TOR #18 Curtis Granderson (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)

# 2. TOR #37 Teoscar Hernández (X - 18 - X)
b5.new_ab(is_risp=True)
b5.out("L9")

# 3. TOR #14 Justin Smoak (X - 18 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f b f d b b")
b5.reach("BB")

# 4. TOR #26 Yangervis Solarte (X - 18 - 14)
b5.new_ab(is_risp=True)
b5.out("L6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #33 J.A. Happ
t6 = game.new_inning()

# 9. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("c b c")
t6.hit(2)
t6.advance(4, "13 1B")

# 1. BOS #50 Mookie Betts (X - 12 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("d b f s")
t6.out("F8")

# 2. BOS #16 Andrew Benintendi (X - 12 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("s f b d s")
t6.out("K")

# 3. BOS #13 Hanley Ramirez (X - 12 - X)
t6.new_ab(is_risp=True)
t6.hit(1, rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t6.new_ab()
t6.pitch_list("b b f s s")
t6.out("K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 5. TOR #28 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("f b f")
b6.out("F8")

# 6. TOR #55 Russell Martin (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.out("(F)P2")

# 7. TOR #11 Kevin Pillar (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #33 J.A. Happ
t7 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b")
t7.out("F7")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("f s")
t7.out("G6-3")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("f b b f b f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #22 Rick Porcello
b7 = game.new_inning()

# 8. TOR #1  Aledmys Díaz (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c f")
b7.out("G5-3")

# 9. TOR #29 Devon Travis (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G6-3")

# 1. TOR #18 Curtis Granderson (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.out("L4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #52 Ryan Tepera
t8 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #33 J.A. Happ
t8.pitching_substitution(52)

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #3 Sandy León, batting 8th
t8.offensive_substitution(8, 18, "PH")

# 8. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b b s b c")
t8.out("G5-3")

# 9. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("f t b")
t8.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 12)
t8.new_ab()
t8.pitch_list("f b 1 f s")
t8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - 12)
t8.new_ab()
t8.pitch_list("c s f b d s")
t8.out("K")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #22 Rick Porcello
b8.pitching_substitution(56)

# Defensive change (BOS): #7 Christian Vázquez replaces #18 Mitch Moreland (PH), playing C, batting 8th
b8.defensive_substitution(8, 7, "2")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b8.new_ab()
b8.pitch_list("b s b")
b8.out("F9")

# 3. TOR #14 Justin Smoak (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")

# 4. TOR #26 Yangervis Solarte (X - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.out("P4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #54 Roberto Osuna
t9 = game.new_inning()

# Pitching change (TOR): #54 Roberto Osuna replaces #52 Ryan Tepera
t9.pitching_substitution(54)

# Defensive switch (TOR): #18 Curtis Granderson moves to LF
t9.defensive_switch(18, "7")

# Defensive change (TOR): #15 Randal Grichuk replaces #37 Teoscar Hernández (LF), playing RF, batting 2nd
t9.defensive_substitution(2, 15, "9")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t9.new_ab()
t9.pitch_list("b c f")
t9.hit(1)
t9.advance(2, "11 1B")
t9.advance(4, "36 1B")

# 4. BOS #28 J.D. Martinez (X - X - 13)
t9.new_ab()
t9.pitch_list("b s b f s")
t9.out("K")

# 5. BOS #11 Rafael Devers (X - X - 13)
t9.new_ab()
t9.pitch_list("c b f d")
t9.hit(1)
t9.advance(3, "36 1B")
t9.advance(4, "12 1B")

# 6. BOS #36 Eduardo Núñez (X - 13 - 11)
t9.new_ab(is_risp=True)
t9.pitch_list("f f f")
t9.hit(1, rbis=1)
t9.advance(2, "7 SB")
t9.advance(3, "12 1B")
t9.thrown_out(4, "12 7-2", 3, 54)

# 7. BOS #19 Jackie Bradley Jr. (11 - X - 36)
t9.new_ab(is_risp=True)
t9.pitch_list("s s b s")
t9.out("K")

# 8. BOS #7  Christian Vázquez (11 - X - 36)
t9.new_ab(is_risp=True)
t9.pitch_list("f c b d f b b")
t9.reach("BB")
t9.advance(2, "12 7-2")

# 9. BOS #12 Brock Holt (11 - 36 - 7)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.hit(1, rbis=1)


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Offensive change (TOR): Pinch-hitter #8 Kendrys Morales replaces #28 Steve Pearce, batting 5th
b9.offensive_substitution(5, 8, "PH")

# 5. TOR #8  Kendrys Morales (X - X - X)
b9.new_ab()
b9.pitch_list("c b b b")
b9.out("G6-3")

# 6. TOR #55 Russell Martin (X - X - X)
b9.new_ab()
b9.out("F9")

# 7. TOR #11 Kevin Pillar (X - X - X)
b9.new_ab()
b9.pitch_list("s s b")
b9.hit(2)

# 8. TOR #1  Aledmys Díaz (X - 11 - X)
b9.new_ab(is_risp=True)
b9.out("L9")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TOR #36 Tyler Clippard
t10 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #54 Roberto Osuna
t10.pitching_substitution(36)

# Defensive switch (TOR): #8 Kendrys Morales moves to DH
t10.defensive_switch(8, "0")

# 1. BOS #50 Mookie Betts (X - X - X)
t10.new_ab()
t10.pitch_list("b f b c b f b")
t10.reach("BB")
t10.thrown_out(2, "13 DP6-4-3", 2, 36)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t10.new_ab()
t10.pitch_list("b 1 1 l f b 1 f d")
t10.out("F8")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
t10.new_ab()
t10.out("DP6-4-3")


# Bot 10th
# Pitching: BOS #46 Craig Kimbrel
b10 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b10.pitching_substitution(46)

# 9. TOR #29 Devon Travis (X - X - X)
b10.new_ab()
b10.pitch_list("c s f b b c")
b10.out("!K")

# 1. TOR #18 Curtis Granderson (X - X - X)
b10.new_ab()
b10.pitch_list("b b")
b10.hit(4)

# Winning team: TOR
# WP: TOR #36 Tyler Clippard
game.winning_pitcher(36)

# Loser team: BOS
# LP: BOS #46 Craig Kimbrel
game.losing_pitcher(46, is_away_team=True)

# print(game)
game.generate_scorecard()
