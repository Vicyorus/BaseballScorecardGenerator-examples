import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-07-12
# https://www.baseball-reference.com/boxes/BOS/BOS201807120.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/07/12/530809/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-12 19:11-22:30",
        "at": "Fenway Park, Boston, MA",
        "att": "37,182",
        "temp": "69F, Clear",
        "wind": "10mph, Out To RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 33,
            "roster": {
                # Lineup
                15: "Randal Grichuk",
                13: "Lourdes Gurriel Jr.",
                14: "Justin Smoak",
                37: "Teoscar Hernández",
                8: "Kendrys Morales",
                55: "Russell Martin",
                11: "Kevin Pillar",
                29: "Devon Travis",
                1: "Aledmys Díaz",
                # Starting pitcher
                33: "J.A. Happ",
                # Bench
                26: "Yangervis Solarte",
                21: "Luke Maile",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                31: "Joe Biagini",
                58: "Tim Mayza",
                71: "Luis Santos",
                25: "Marco Estrada",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                56: "Ryan Borucki",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                6: "Marcus Stroman",
                77: "John Axford",
            },
            "lefties": [33, 62, 58, 56],
            "lineup": [
                [15, "9"],
                [13, "6"],
                [14, "3"],
                [37, "7"],
                [8, "0"],
                [55, "2"],
                [11, "8"],
                [29, "4"],
                [1, "5"],
            ],
            "bench": [
                [26, "3B"],
                [21, "C"],
                [18, "CF"],
            ],
            "bullpen": [62, 31, 58, 71, 25, 39, 43, 56, 36, 22, 6, 77],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                37: "Heath Hembree",
                63: "Robby Scott",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 63],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [25, "3"],
                [2, "6"],
                [12, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
            ],
            "bullpen": [47, 57, 44, 22, 41, 37, 63, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Tripp Gibson",
            "1B": "Brian Gorman",
            "2B": "Mike Muchlinski",
            "3B": "Adrian Johnson",
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

# 1. TOR #15 Randal Grichuk (X - X - X)
t1.new_ab()
t1.pitch_list("f c f t")
t1.out("KT")

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(2)
t1.advance(4, "37 HR")

# 3. TOR #14 Justin Smoak (X - 13 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("s s b b f s")
t1.out("K")

# 4. TOR #37 Teoscar Hernández (X - 13 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.hit(4, rbis=2)

# 5. TOR #8  Kendrys Morales (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c s s")
t1.out("K")


# Bot 1st
# Pitching: TOR #33 J.A. Happ
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b b")
b1.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "25 HBP")

# 4. BOS #25 Steve Pearce (X - X - 28)
b1.new_ab()
b1.pitch_list("b b b c t f f")
b1.reach("HBP")

# 5. BOS #2  Xander Bogaerts (X - 28 - 25)
b1.new_ab(is_risp=True)
b1.pitch_list("b b c f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 6. TOR #55 Russell Martin (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 7. TOR #11 Kevin Pillar (X - X - X)
t2.new_ab()
t2.pitch_list("b b f s f t")
t2.out("KT")

# 8. TOR #29 Devon Travis (X - X - X)
t2.new_ab()
t2.pitch_list("f")
t2.hit(1)
t2.thrown_out(2, "5-4", 3, 24)


# Bot 2nd
# Pitching: TOR #33 J.A. Happ
b2 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("c f c")
b2.out("!K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b b s c f")
b2.out("G4-3")

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("b f s f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# Defensive change (BOS): #23 Blake Swihart replaces #25 Steve Pearce (1B), playing 1B, batting 4th
t3.defensive_substitution(4, 23, "3")

# 9. TOR #1  Aledmys Díaz (X - X - X)
t3.new_ab()
t3.pitch_list("c c s")
t3.out("K")

# 1. TOR #15 Randal Grichuk (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("L9")

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c f")
t3.hit(1)
t3.thrown_out(2, "14 FC5-4", 3, 24)

# 3. TOR #14 Justin Smoak (X - X - 13)
t3.new_ab()
t3.pitch_list("s b c")
t3.reach("FC5-4")


# Bot 3rd
# Pitching: TOR #33 J.A. Happ
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b b l")
b3.hit(1)
b3.advance(2, "50 SB")
b3.advance(3, "50 G6-3")

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("c s")
b3.out("G6-3")

# 2. BOS #16 Andrew Benintendi (19 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b s")
b3.out("K2-3")

# 3. BOS #28 J.D. Martinez (19 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b c c s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 4. TOR #37 Teoscar Hernández (X - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.out("F9")

# 5. TOR #8  Kendrys Morales (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G1-3")

# 6. TOR #55 Russell Martin (X - X - X)
t4.new_ab()
t4.pitch_list("f c b b b f c")
t4.out("!K")


# Bot 4th
# Pitching: TOR #33 J.A. Happ
b4 = game.new_inning()

# 4. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.pitch_list("b c s s")
b4.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("s b s f f b")
b4.hit(1)
b4.error(4)
b4.advance(2, "12 E4")
b4.advance(3, "36 1B")
b4.advance("U", "3 FC6-5")

# 6. BOS #12 Brock Holt (X - X - 2)
b4.new_ab()
b4.pitch_list("f b f")
b4.reach("FC6")
b4.advance(2, "36 1B")
b4.thrown_out(3, "3 FC6-5", 2, 33)

# 7. BOS #36 Eduardo Núñez (X - 2 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("b t t f")
b4.hit(1)
b4.advance(2, "3 FC6-5")
b4.advance(3, "19 WP")
b4.advance("U", "50 HR")

# 8. BOS #3  Sandy León (2 - 12 - 36)
b4.new_ab(is_risp=True)
b4.pitch_list("b f f f d f")
b4.reach("FC6-5", rbis=1)
b4.advance(2, "19 WP")
b4.advance("U", "50 HR")

# 9. BOS #19 Jackie Bradley Jr. (X - 36 - 3)
b4.new_ab(is_risp=True)
b4.pitch_list("c c b b b d")
b4.wp()
b4.reach("BB")
b4.advance("U", "50 HR")

# 1. BOS #50 Mookie Betts (36 - 3 - 19)
b4.new_ab(is_risp=True)
b4.pitch_list("c b s f f f f f f d f d")
b4.hit("U", rbis=4)

# Pitching change (TOR): #31 Joe Biagini replaces #33 J.A. Happ
b4.pitching_substitution(31)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("s b f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 7. TOR #11 Kevin Pillar (X - X - X)
t5.new_ab()
t5.pitch_list("f c b b f b f")
t5.out("L8")

# 8. TOR #29 Devon Travis (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.thrown_out(2, "15 FC6-4", 3, 24)

# 9. TOR #1  Aledmys Díaz (X - X - 29)
t5.new_ab()
t5.pitch_list("s c f s")
t5.out("K")

# 1. TOR #15 Randal Grichuk (X - X - 29)
t5.new_ab()
t5.pitch_list("b f b f")
t5.reach("FC6-4")


# Bot 5th
# Pitching: TOR #31 Joe Biagini
b5 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.out("G5-3")

# 4. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("L8")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c s b b f")
b5.out("(F)P3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("b b c c f")
t6.out("L7")

# 3. TOR #14 Justin Smoak (X - X - X)
t6.new_ab()
t6.pitch_list("b c c")
t6.out("G6-3")

# 4. TOR #37 Teoscar Hernández (X - X - X)
t6.new_ab()
t6.pitch_list("c f b t")
t6.out("KT")


# Bot 6th
# Pitching: TOR #31 Joe Biagini
b6 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.out("F8")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G6-3")

# 8. BOS #3  Sandy León (X - X - X)
b6.new_ab()
b6.pitch_list("f b f b s")
b6.out("K2-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 5. TOR #8  Kendrys Morales (X - X - X)
t7.new_ab()
t7.hit(4)

# 6. TOR #55 Russell Martin (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b")
t7.out("G5-3")

# 7. TOR #11 Kevin Pillar (X - X - X)
t7.new_ab()
t7.pitch_list("b f s f f f")
t7.out("(F)P3")

# Pitching change (BOS): #44 Brandon Workman replaces #24 David Price
t7.pitching_substitution(44)

# 8. TOR #29 Devon Travis (X - X - X)
t7.new_ab()
t7.pitch_list("b c b")
t7.hit(1)

# Offensive change (TOR): Pinch-hitter #26 Yangervis Solarte replaces #1 Aledmys Díaz, batting 9th
t7.offensive_substitution(9, 26, "PH")

# 9. TOR #26 Yangervis Solarte (X - X - 29)
t7.new_ab()
t7.pitch_list("1 b b c")
t7.out("L9")


# Bot 7th
# Pitching: TOR #77 John Axford
b7 = game.new_inning()

# Pitching change (TOR): #77 John Axford replaces #31 Joe Biagini
b7.pitching_substitution(77)

# Defensive switch (TOR): #26 Yangervis Solarte moves to 3B
b7.defensive_switch(26, "5")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b c b b")
b7.hit(2)
b7.advance(3, "50 WP")
b7.advance(4, "50 1B")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b c b c d")
b7.wp()
b7.hit(1, rbis=1)
b7.thrown_out(2, "16 DP4-6-3", 1, 77)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b7.new_ab()
b7.pitch_list("f d")
b7.out("DP4-6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("s b b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #44 Brandon Workman
t8.pitching_substitution(32)

# 1. TOR #15 Randal Grichuk (X - X - X)
t8.new_ab()
t8.pitch_list("b f b s")
t8.hit(1)
t8.advance(4, "14 2B")

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - 15)
t8.new_ab()
t8.pitch_list("c 1 f b f d 1")
t8.out("F8")

# 3. TOR #14 Justin Smoak (X - X - 15)
t8.new_ab()
t8.hit(2, rbis=1)
t8.advance(3, "37 1B")
# Offensive change (TOR): Pinch-runner #18 Curtis Granderson replaces #14 Justin Smoak
t8.offensive_substitution(3, 18, "PR")
t8.atbase("PR")

# 4. TOR #37 Teoscar Hernández (X - 14 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c b b")
t8.hit(1)

# 5. TOR #8  Kendrys Morales (14 - X - 37)
t8.new_ab(is_risp=True)
t8.pitch_list("b b s s f s")
t8.out("K")

# 6. TOR #55 Russell Martin (18 - X - 37)
t8.new_ab(is_risp=True)
t8.pitch_list("b b c f s")
t8.out("K")


# Bot 8th
# Pitching: TOR #22 Seunghwan Oh
b8 = game.new_inning()

# Pitching change (TOR): #22 Seunghwan Oh replaces #77 John Axford
b8.pitching_substitution(22)

# Defensive switch (TOR): #18 Curtis Granderson moves to LF
b8.defensive_switch(18, "7")

# Defensive change (TOR): #21 Luke Maile replaces #37 Teoscar Hernández (LF), playing C, batting 4th
b8.defensive_substitution(4, 21, "2")

# Defensive switch (TOR): #55 Russell Martin moves to 3B
b8.defensive_switch(55, "5")

# Defensive switch (TOR): #26 Yangervis Solarte moves to 1B
b8.defensive_switch(26, "3")

# 4. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("f f b b f")
b8.hit(2)
b8.advance(3, "2 G6-3")

# 5. BOS #2  Xander Bogaerts (X - 23 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("d c")
b8.out("G6-3")

# 6. BOS #12 Brock Holt (23 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f f f t")
b8.out("KT")

# 7. BOS #36 Eduardo Núñez (23 - X - X)
b8.new_ab(is_risp=True)
b8.pitch_list("f s b d f b f f")
b8.out("L9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# Defensive change (BOS): #18 Mitch Moreland replaces #23 Blake Swihart (1B), playing 1B, batting 4th
t9.defensive_substitution(4, 18, "3")

# 7. TOR #11 Kevin Pillar (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G5-3")

# 8. TOR #29 Devon Travis (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(1)
t9.advance(2, "26 WP")

# 9. TOR #26 Yangervis Solarte (X - X - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("d s f f")
t9.wp()
t9.out("G5-3")

# 1. TOR #15 Randal Grichuk (X - 29 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("d b s f")
t9.out("F9")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TOR
# LP: TOR #33 J.A. Happ
game.losing_pitcher(33, is_away_team=True)

# print(game)
game.generate_scorecard()
