import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-04-25
# https://www.baseball-reference.com/boxes/TOR/TOR201804250.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/04/25/529762/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-25 19:08-22:12",
        "at": "Rogers Centre, Toronto, ON",
        "att": "18,914",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                12: "Brock Holt",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
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
                [7, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [39, 22, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 41,
            "roster": {
                # Lineup
                28: "Steve Pearce",
                37: "Teoscar Hernández",
                14: "Justin Smoak",
                26: "Yangervis Solarte",
                8: "Kendrys Morales",
                55: "Russell Martin",
                11: "Kevin Pillar",
                13: "Lourdes Gurriel Jr.",
                1: "Aledmys Díaz",
                # Starting pitcher
                41: "Aaron Sanchez",
                # Bench
                15: "Randal Grichuk",
                29: "Devon Travis",
                21: "Luke Maile",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                24: "Danny Barnes",
                58: "Tim Mayza",
                25: "Marco Estrada",
                54: "Roberto Osuna",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 58, 33],
            "lineup": [
                [28, "7"],
                [37, "9"],
                [14, "3"],
                [26, "5"],
                [8, "0"],
                [55, "2"],
                [11, "8"],
                [13, "4"],
                [1, "6"],
            ],
            "bench": [
                [15, "RF"],
                [29, "2B"],
                [21, "C"],
                [18, "CF"],
            ],
            "bullpen": [62, 57, 24, 58, 25, 54, 36, 22, 6, 52, 33],
        },
        "umpires": {
            "HP": "Scott Barry",
            "1B": "Ramon De Jesus",
            "2B": "Kerwin Danley",
            "3B": "Dan Iassogna",
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
# Pitching: TOR #41 Aaron Sanchez
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c f")
t1.out("F8")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.error(9)
t1.reach("E9")
t1.thrown_out(2, "28 FC5-4", 2, 41)

# 4. BOS #28 J.D. Martinez (X - X - 13)
t1.new_ab()
t1.pitch_list("c f f f")
t1.reach("FC5-4")

# 5. BOS #11 Rafael Devers (X - X - 28)
t1.new_ab()
t1.pitch_list("b b f f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. TOR #28 Steve Pearce (X - X - X)
b1.new_ab()
b1.hit(2)
b1.error(5)
b1.advance(4, "14 E5")

# 2. TOR #37 Teoscar Hernández (X - 28 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b b")
b1.out("F9")

# 3. TOR #14 Justin Smoak (X - 28 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b")
b1.hit(1)
b1.advance(2, "E5")

# 4. TOR #26 Yangervis Solarte (X - 14 - X)
b1.new_ab(is_risp=True)
b1.out("F7")

# 5. TOR #8  Kendrys Morales (X - 14 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("s b f b d s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #41 Aaron Sanchez
t2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("s f s")
t2.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("c s b f")
t2.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("c c b b b s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 6. TOR #55 Russell Martin (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("G4-3")

# 7. TOR #11 Kevin Pillar (X - X - X)
b2.new_ab()
b2.pitch_list("b c f f f")
b2.out("L7")

# 8. TOR #13 Lourdes Gurriel Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b f b")
b2.error(5)
b2.reach("E5")

# 9. TOR #1  Aledmys Díaz (X - X - 13)
b2.new_ab()
b2.pitch_list("b f s 1")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #41 Aaron Sanchez
t3 = game.new_inning()

# 9. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("b c f")
t3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b s")
t3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G3")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 1. TOR #28 Steve Pearce (X - X - X)
b3.new_ab()
b3.pitch_list("f s s")
b3.out("K")

# 2. TOR #37 Teoscar Hernández (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F7")

# 3. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.out("G1-5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #41 Aaron Sanchez
t4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("b s s s")
t4.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("f")
t4.hit(1)

# 5. BOS #11 Rafael Devers (X - X - 28)
t4.new_ab()
t4.pitch_list("b s")
t4.out("F7")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
t4.new_ab()
t4.pitch_list("s b")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 4. TOR #26 Yangervis Solarte (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G4-3")

# 5. TOR #8  Kendrys Morales (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 6. TOR #55 Russell Martin (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #41 Aaron Sanchez
t5 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b b l b b")
t5.reach("BB")
t5.advance(2, "7 HBP")
t5.advance(4, "12 2B")

# 8. BOS #7  Christian Vázquez (X - X - 19)
t5.new_ab()
t5.pitch_list("c")
t5.reach("HBP")
t5.advance(3, "12 2B")

# 9. BOS #12 Brock Holt (X - 19 - 7)
t5.new_ab(is_risp=True)
t5.pitch_list("b c b")
t5.hit(2, rbis=1)

# 1. BOS #50 Mookie Betts (7 - 12 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("d c")
t5.out("F9")

# 2. BOS #16 Andrew Benintendi (7 - 12 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c f b b")
t5.reach("BB")
t5.thrown_out(2, "13 DP4-6-3", 2, 41)

# 3. BOS #13 Hanley Ramirez (7 - 12 - 16)
t5.new_ab(is_risp=True)
t5.out("DP4-6-3")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 7. TOR #11 Kevin Pillar (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("G5-3")

# 8. TOR #13 Lourdes Gurriel Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b")
b5.hit(1)
b5.advance(2, "1 SB")
b5.advance(4, "28 1B")

# 9. TOR #1  Aledmys Díaz (X - X - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("b s s d b")
b5.out("G5-3")

# 1. TOR #28 Steve Pearce (X - 13 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b b c s")
b5.hit(1, rbis=1)
b5.advance(2, "37 1B")

# 2. TOR #37 Teoscar Hernández (X - X - 28)
b5.new_ab()
b5.pitch_list("s f b")
b5.hit(1)
b5.thrown_out(2, "14 FC5-4", 3, 57)

# 3. TOR #14 Justin Smoak (X - 28 - 37)
b5.new_ab(is_risp=True)
b5.pitch_list("b f b")
b5.reach("FC5-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #41 Aaron Sanchez
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.reach("HBP")

# 5. BOS #11 Rafael Devers (X - X - 28)
t6.new_ab()
t6.pitch_list("s s s")
t6.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
t6.new_ab()
t6.pitch_list("f c s")
t6.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 28)
t6.new_ab()
t6.pitch_list("b b s s f c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 4. TOR #26 Yangervis Solarte (X - X - X)
b6.new_ab()
b6.hit(4)

# 5. TOR #8  Kendrys Morales (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 6. TOR #55 Russell Martin (X - X - X)
b6.new_ab()
b6.pitch_list("c b f f b b f b")
b6.reach("BB")

# 7. TOR #11 Kevin Pillar (X - X - 55)
b6.new_ab()
b6.pitch_list("b f b")
b6.out("F7")

# 8. TOR #13 Lourdes Gurriel Jr. (X - X - 55)
b6.new_ab()
b6.pitch_list("f b s")
b6.out("L7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #24 Danny Barnes
t7 = game.new_inning()

# Pitching change (TOR): #24 Danny Barnes replaces #41 Aaron Sanchez
t7.pitching_substitution(24)

# Defensive change (TOR): #15 Randal Grichuk replaces #28 Steve Pearce (LF), playing RF, batting 1st
t7.defensive_substitution(1, 15, "9")

# Defensive switch (TOR): #37 Teoscar Hernández moves to LF
t7.defensive_switch(37, "7")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("F8")

# 9. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.hit(1)
t7.advance(4, "50 HR")

# 1. BOS #50 Mookie Betts (X - X - 12)
t7.new_ab()
t7.pitch_list("c")
t7.hit(4, rbis=2)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c s b")
t7.reach("BB")
t7.advance(2, "13 SB")
t7.advance(3, "13 SB")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t7.new_ab(is_risp=True)
t7.pitch_list("b 1 b s s b f b")
t7.reach("BB")
t7.advance(2, "28 BB")

# Pitching change (TOR): #22 Seunghwan Oh replaces #24 Danny Barnes
t7.pitching_substitution(22)

# 4. BOS #28 J.D. Martinez (16 - X - 13)
t7.new_ab(is_risp=True)
t7.pitch_list("d f f b b b")
t7.reach("BB")

# 5. BOS #11 Rafael Devers (16 - 13 - 28)
t7.new_ab(is_risp=True)
t7.pitch_list("b b")
t7.out("F9")

# 6. BOS #36 Eduardo Núñez (16 - 13 - 28)
t7.new_ab(is_risp=True)
t7.out("G3")


# Bot 7th
# Pitching: BOS #57 Eduardo Rodriguez
b7 = game.new_inning()

# 9. TOR #1  Aledmys Díaz (X - X - X)
b7.new_ab()
b7.pitch_list("b s c f b")
b7.out("G3")

# 1. TOR #15 Randal Grichuk (X - X - X)
b7.new_ab()
b7.pitch_list("b f c f f b b s")
b7.out("K")

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
b7.pitching_substitution(37)

# 2. TOR #37 Teoscar Hernández (X - X - X)
b7.new_ab()
b7.pitch_list("s b b s s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #58 Tim Mayza
t8 = game.new_inning()

# Pitching change (TOR): #58 Tim Mayza replaces #22 Seunghwan Oh
t8.pitching_substitution(58)

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("f c b c")
t8.out("!K")

# 8. BOS #7  Christian Vázquez (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("F8")

# 9. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)

# Pitching change (TOR): #52 Ryan Tepera replaces #58 Tim Mayza
t8.pitching_substitution(52)

# 1. BOS #50 Mookie Betts (X - X - 12)
t8.new_ab()
t8.pitch_list("b c 1 1")
t8.out("F7")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
b8.pitching_substitution(56)

# 3. TOR #14 Justin Smoak (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G4-3")

# 4. TOR #26 Yangervis Solarte (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G4-3")

# 5. TOR #8  Kendrys Morales (X - X - X)
b8.new_ab()
b8.pitch_list("s b b s b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #36 Tyler Clippard
t9 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #52 Ryan Tepera
t9.pitching_substitution(36)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("s")
t9.out("F8")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("s b b f b f f f b")
t9.reach("BB")

# 5. BOS #11 Rafael Devers (X - X - 28)
t9.new_ab()
t9.pitch_list("s s s")
t9.out("K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
b9.pitching_substitution(46)

# 6. TOR #55 Russell Martin (X - X - X)
b9.new_ab()
b9.pitch_list("b c f b")
b9.out("(F)P2")

# 7. TOR #11 Kevin Pillar (X - X - X)
b9.new_ab()
b9.pitch_list("b b c s f")
b9.out("G6-3")

# 8. TOR #13 Lourdes Gurriel Jr. (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("F9")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: TOR
# LP: TOR #24 Danny Barnes
game.losing_pitcher(24)

# print(game)
game.generate_scorecard()
