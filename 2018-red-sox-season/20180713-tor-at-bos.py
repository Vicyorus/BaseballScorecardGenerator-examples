import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-07-13
# https://www.baseball-reference.com/boxes/BOS/BOS201807130.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/07/13/530824/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-13 19:10-22:53",
        "at": "Fenway Park, Boston, MA",
        "att": "37,018",
        "temp": "71F, Cloudy",
        "wind": "18mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                18: "Curtis Granderson",
                13: "Lourdes Gurriel Jr.",
                26: "Yangervis Solarte",
                14: "Justin Smoak",
                8: "Kendrys Morales",
                55: "Russell Martin",
                11: "Kevin Pillar",
                27: "Dwight Smith Jr.",
                29: "Devon Travis",
                # Starting pitcher
                56: "Ryan Borucki",
                # Bench
                15: "Randal Grichuk",
                37: "Teoscar Hernández",
                21: "Luke Maile",
                1: "Aledmys Díaz",
                # Bullpen
                62: "Aaron Loup",
                31: "Joe Biagini",
                58: "Tim Mayza",
                71: "Luis Santos",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                6: "Marcus Stroman",
                77: "John Axford",
                33: "J.A. Happ",
            },
            "lefties": [56, 62, 58, 33],
            "lineup": [
                [18, "9"],
                [13, "6"],
                [26, "5"],
                [14, "0"],
                [8, "3"],
                [55, "2"],
                [11, "8"],
                [27, "7"],
                [29, "4"],
            ],
            "bench": [
                [15, "RF"],
                [37, "LF"],
                [21, "C"],
                [1, "SS"],
            ],
            "bullpen": [62, 31, 58, 71, 39, 43, 36, 22, 6, 77, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                5: "Tzu-Wei Lin",
                25: "Steve Pearce",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                41: "Chris Sale",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 63, 24],
            "lineup": [
                [50, "9"],
                [12, "4"],
                [28, "7"],
                [2, "6"],
                [18, "3"],
                [36, "5"],
                [59, "0"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [25, "1B"],
                [23, "C"],
            ],
            "bullpen": [47, 57, 44, 41, 37, 63, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Brian Gorman",
            "1B": "Mike Muchlinski",
            "2B": "Adrian Johnson",
            "3B": "Tripp Gibson",
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

# 1. TOR #18 Curtis Granderson (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F8")

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("c b s f b b")
t1.out("G6-3")

# 3. TOR #26 Yangervis Solarte (X - X - X)
t1.new_ab()
t1.pitch_list("f f")
t1.hit(1)

# 4. TOR #14 Justin Smoak (X - X - 26)
t1.new_ab()
t1.pitch_list("b c b f b c")
t1.out("!K")


# Bot 1st
# Pitching: TOR #56 Ryan Borucki
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b b")
b1.hit(3)
b1.error(6)
b1.advance("U", "28 E6")

# 2. BOS #12 Brock Holt (50 - X - X)
b1.new_ab()
b1.pitch_list("c f d b c")
b1.out("!K")

# 3. BOS #28 J.D. Martinez (50 - X - X)
b1.new_ab()
b1.pitch_list("b f")
b1.reach("FC6")
b1.advance(2, "18 PB")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b1.new_ab()
b1.pitch_list("b b f b c s")
b1.out("K")

# 5. BOS #18 Mitch Moreland (X - X - 28)
b1.new_ab()
b1.pitch_list("c b b")
b1.pb()
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 5. TOR #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.pitch_list("c b s f b f b b")
t2.reach("BB")
t2.advance(2, "55 BB")
t2.advance(4, "11 2B")

# 6. TOR #55 Russell Martin (X - X - 8)
t2.new_ab()
t2.pitch_list("s b b b b")
t2.reach("BB")
t2.advance(3, "11 2B")
t2.advance(4, "27 SF7")

# 7. TOR #11 Kevin Pillar (X - 8 - 55)
t2.new_ab()
t2.pitch_list("b")
t2.hit(2, rbis=1)
t2.advance(3, "27 SF7")
t2.advance(4, "13 1B")

# 8. TOR #27 Dwight Smith Jr. (55 - 11 - X)
t2.new_ab()
t2.out("SF7", rbis=1)

# 9. TOR #29 Devon Travis (11 - X - X)
t2.new_ab()
t2.pitch_list("b b d c b")
t2.reach("BB")
t2.advance(2, "13 1B")

# 1. TOR #18 Curtis Granderson (11 - X - 29)
t2.new_ab()
t2.pitch_list("c c s")
t2.out("K")

# 2. TOR #13 Lourdes Gurriel Jr. (11 - X - 29)
t2.new_ab()
t2.hit(1, rbis=1)

# 3. TOR #26 Yangervis Solarte (X - 29 - 13)
t2.new_ab()
t2.out("G6-3")


# Bot 2nd
# Pitching: TOR #56 Ryan Borucki
b2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G4-3")

# 7. BOS #59 Sam Travis (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b t b")
b2.reach("BB")
b2.advance(2, "3 E6")
b2.advance(4, "19 1B")

# 8. BOS #3  Sandy León (X - X - 59)
b2.new_ab()
b2.pitch_list("f")
b2.error(6)
b2.reach("E6")
b2.advance(2, "19 1B")
b2.advance(3, "19 E8")
b2.advance("U", "50 3B")

# 9. BOS #19 Jackie Bradley Jr. (X - 59 - 3)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1, rbis=1)
b2.error(8)
b2.advance(2, "E8")
b2.advance(4, "50 3B")

# 1. BOS #50 Mookie Betts (3 - 19 - X)
b2.new_ab()
b2.pitch_list("c f b")
b2.hit(3, rbis=2)
b2.advance(4, "12 1B")

# 2. BOS #12 Brock Holt (50 - X - X)
b2.new_ab()
b2.hit(1, rbis=1)
b2.error(1)
b2.advance(2, "2 SB")
b2.advance(3, "2 E1")
b2.advance("U", "2 1B")

# 3. BOS #28 J.D. Martinez (X - X - 12)
b2.new_ab()
b2.pitch_list("b f")
b2.out("F8")

# 4. BOS #2  Xander Bogaerts (X - X - 12)
b2.new_ab()
b2.pitch_list("b c b f f 1")
b2.hit(1, rbis=1)
b2.advance(2, "18 BB")

# 5. BOS #18 Mitch Moreland (X - X - 2)
b2.new_ab()
b2.pitch_list("b f b b b")
b2.reach("BB")

# 6. BOS #36 Eduardo Núñez (X - 2 - 18)
b2.new_ab()
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 4. TOR #14 Justin Smoak (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.hit(4, rbis=1)

# 5. TOR #8  Kendrys Morales (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c b")
t3.reach("BB")
t3.advance(2, "55 1B")
t3.advance(4, "11 2B")

# 6. TOR #55 Russell Martin (X - X - 8)
t3.new_ab()
t3.pitch_list("b c b")
t3.hit(1)
t3.advance(4, "11 2B")

# 7. TOR #11 Kevin Pillar (X - 8 - 55)
t3.new_ab()
t3.pitch_list("c")
t3.hit(2, rbis=2)
t3.advance(4, "27 HR")

# 8. TOR #27 Dwight Smith Jr. (X - 11 - X)
t3.new_ab()
t3.pitch_list("d b c b")
t3.hit(4, rbis=2)

# Pitching change (BOS): #76 Hector Velázquez replaces #22 Rick Porcello
t3.pitching_substitution(76)

# 9. TOR #29 Devon Travis (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 1. TOR #18 Curtis Granderson (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f b s")
t3.out("K")

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("G5-3")


# Bot 3rd
# Pitching: TOR #56 Ryan Borucki
b3 = game.new_inning()

# 7. BOS #59 Sam Travis (X - X - X)
b3.new_ab()
b3.pitch_list("b c t")
b3.hit(2)

# 8. BOS #3  Sandy León (X - 59 - X)
b3.new_ab()
b3.pitch_list("b c f s")
b3.out("K2-3")

# 9. BOS #19 Jackie Bradley Jr. (X - 59 - X)
b3.new_ab()
b3.pitch_list("c b c f s")
b3.out("K")

# 1. BOS #50 Mookie Betts (X - 59 - X)
b3.new_ab()
b3.pitch_list("v v v v")
b3.reach("IBB")

# 2. BOS #12 Brock Holt (X - 59 - 50)
b3.new_ab()
b3.pitch_list("c f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #76 Hector Velázquez
t4 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
t4.new_ab()
t4.pitch_list("c f b f s")
t4.out("K")

# 4. TOR #14 Justin Smoak (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b b")
t4.reach("BB")
t4.advance(2, "8 BB")
t4.advance(3, "11 1B")

# 5. TOR #8  Kendrys Morales (X - X - 14)
t4.new_ab()
t4.pitch_list("c b b b s b")
t4.reach("BB")
t4.advance(2, "11 1B")

# 6. TOR #55 Russell Martin (X - 14 - 8)
t4.new_ab()
t4.pitch_list("c c d b s")
t4.out("K")

# 7. TOR #11 Kevin Pillar (X - 14 - 8)
t4.new_ab()
t4.pitch_list("c b c d")
t4.hit(1)
t4.thrown_out(2, "27 FC3-6", 3, 76)

# 8. TOR #27 Dwight Smith Jr. (14 - 8 - 11)
t4.new_ab()
t4.pitch_list("s b d")
t4.reach("FC3-6")


# Bot 4th
# Pitching: TOR #56 Ryan Borucki
b4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.hit(1)
b4.advance(2, "2 BB")
b4.advance(4, "18 1B")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b4.new_ab()
b4.pitch_list("b d b c b")
b4.reach("BB")
b4.advance(3, "18 1B")
b4.thrown_out(4, "59 FC3-5-2", 2, 39)

# 5. BOS #18 Mitch Moreland (X - 28 - 2)
b4.new_ab()
b4.hit(1, rbis=1)
b4.advance(3, "59 FC3-5-2")

# Pitching change (TOR): #39 Jake Petricka replaces #56 Ryan Borucki
b4.pitching_substitution(39)

# 6. BOS #36 Eduardo Núñez (2 - X - 18)
b4.new_ab()
b4.out("P4")

# 7. BOS #59 Sam Travis (2 - X - 18)
b4.new_ab()
b4.pitch_list("b c f")
b4.reach("FC3-5-2", end_base=2)

# 8. BOS #3  Sandy León (18 - 59 - X)
b4.new_ab()
b4.pitch_list("b f b b f b")
b4.reach("BB")

# 9. BOS #19 Jackie Bradley Jr. (18 - 59 - 3)
b4.new_ab()
b4.pitch_list("c s b b f")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #47 Tyler Thornburg
t5 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #76 Hector Velázquez
t5.pitching_substitution(47)

# 9. TOR #29 Devon Travis (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b f f f s")
t5.out("K")

# 1. TOR #18 Curtis Granderson (X - X - X)
t5.new_ab()
t5.pitch_list("b s s f f b f b s")
t5.out("K")

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.hit(1)

# 3. TOR #26 Yangervis Solarte (X - X - 13)
t5.new_ab()
t5.pitch_list("c b f")
t5.out("G4-3")


# Bot 5th
# Pitching: TOR #39 Jake Petricka
b5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.thrown_out(2, "12 DP6-4-3", 1, 39)

# 2. BOS #12 Brock Holt (X - X - 50)
b5.new_ab()
b5.pitch_list("d b f")
b5.out("DP6-4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("c b f f b b")
b5.hit(2)

# 4. BOS #2  Xander Bogaerts (X - 28 - X)
b5.new_ab()
b5.pitch_list("d c f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #70 Ryan Brasier
t6 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
t6.pitching_substitution(70)

# 4. TOR #14 Justin Smoak (X - X - X)
t6.new_ab()
t6.pitch_list("c f")
t6.out("F9")

# 5. TOR #8  Kendrys Morales (X - X - X)
t6.new_ab()
t6.pitch_list("c b s b b")
t6.out("G3-1")

# 6. TOR #55 Russell Martin (X - X - X)
t6.new_ab()
t6.pitch_list("f s b f f b f b b")
t6.reach("BB")

# 7. TOR #11 Kevin Pillar (X - X - 55)
t6.new_ab()
t6.pitch_list("c s s")
t6.out("K")


# Bot 6th
# Pitching: TOR #62 Aaron Loup
b6 = game.new_inning()

# Pitching change (TOR): #62 Aaron Loup replaces #39 Jake Petricka
b6.pitching_substitution(62)

# 5. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.out("G1-3")

# Pitching change (TOR): #77 John Axford replaces #62 Aaron Loup
b6.pitching_substitution(77)

# 6. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G6-3")

# 7. BOS #59 Sam Travis (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# 8. TOR #27 Dwight Smith Jr. (X - X - X)
t7.new_ab()
t7.out("F8")

# 9. TOR #29 Devon Travis (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")

# 1. TOR #18 Curtis Granderson (X - X - X)
t7.new_ab()
t7.pitch_list("b b f")
t7.out("L7")


# Bot 7th
# Pitching: TOR #77 John Axford
b7 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G1-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("f b b")
b7.out("G5-3")

# Pitching change (TOR): #22 Seunghwan Oh replaces #77 John Axford
b7.pitching_substitution(22)

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b b")
b7.out("L5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #70 Ryan Brasier
t8.pitching_substitution(56)

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - X)
t8.new_ab()
t8.reach("HBP")
t8.advance(2, "26 1B")
t8.advance(3, "14 PB")
t8.advance(4, "14 1B")

# 3. TOR #26 Yangervis Solarte (X - X - 13)
t8.new_ab()
t8.pitch_list("f 1")
t8.hit(1)
t8.advance(2, "14 1B")
t8.advance(4, "8 2B")

# 4. TOR #14 Justin Smoak (X - 13 - 26)
t8.new_ab()
t8.pitch_list("b c b f")
t8.pb()
t8.hit(1, rbis=1)
t8.advance(3, "8 2B")
t8.thrown_out(4, "55 FC4-2", 1, 63)

# Pitching change (BOS): #63 Robby Scott replaces #56 Joe Kelly
t8.pitching_substitution(63)

# 5. TOR #8  Kendrys Morales (X - 26 - 14)
t8.new_ab()
t8.hit(2, rbis=1)
t8.advance(3, "55 FC4-2")
t8.advance(4, "11 1B")

# 6. TOR #55 Russell Martin (14 - 8 - X)
t8.new_ab()
t8.reach("FC4-2")
t8.advance(2, "11 1B")

# 7. TOR #11 Kevin Pillar (8 - X - 55)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1, rbis=1)

# Offensive change (TOR): Pinch-hitter #15 Randal Grichuk replaces #27 Dwight Smith Jr., batting 8th
t8.offensive_substitution(8, 15, "PH")

# 8. TOR #15 Randal Grichuk (X - 55 - 11)
t8.new_ab()
t8.pitch_list("d f c f s")
t8.out("K")

# 9. TOR #29 Devon Travis (X - 55 - 11)
t8.new_ab()
t8.pitch_list("d b b c")
t8.out("(F)P2")


# Bot 8th
# Pitching: TOR #22 Seunghwan Oh
b8 = game.new_inning()

# Defensive switch (TOR): #18 Curtis Granderson moves to LF
b8.defensive_switch(18, "7")

# Defensive switch (TOR): #15 Randal Grichuk moves to RF
b8.defensive_switch(15, "9")

# 2. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("c c b")
b8.hit(2)

# 3. BOS #28 J.D. Martinez (X - 12 - X)
b8.new_ab()
b8.pitch_list("f b f f s")
b8.out("K")

# 4. BOS #2  Xander Bogaerts (X - 12 - X)
b8.new_ab()
b8.pitch_list("b b b c s c")
b8.out("!K")

# Pitching change (TOR): #58 Tim Mayza replaces #22 Seunghwan Oh
b8.pitching_substitution(58)

# 5. BOS #18 Mitch Moreland (X - 12 - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #63 Robby Scott
t9 = game.new_inning()

# 1. TOR #18 Curtis Granderson (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b")
t9.reach("HBP")
t9.thrown_out(2, "26 FC4-6", 2, 63)

# 2. TOR #13 Lourdes Gurriel Jr. (X - X - 18)
t9.new_ab()
t9.pitch_list("b f 1 f b b")
t9.out("F7")

# 3. TOR #26 Yangervis Solarte (X - X - 18)
t9.new_ab()
t9.pitch_list("s b")
t9.reach("FC4-6")
# Offensive change (TOR): Pinch-runner #1 Aledmys Díaz replaces #26 Yangervis Solarte
t9.offensive_substitution(3, 1, "PR")
t9.atbase("PR")
t9.advance(4, "14 HR")

# 4. TOR #14 Justin Smoak (X - X - 26)
t9.new_ab()
t9.pitch_list("b b s")
t9.hit(4, rbis=2)

# 5. TOR #8  Kendrys Morales (X - X - X)
t9.new_ab()
t9.pitch_list("b f f b s")
t9.out("K")


# Bot 9th
# Pitching: TOR #36 Tyler Clippard
b9 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #58 Tim Mayza
b9.pitching_substitution(36)

# Defensive switch (TOR): #1 Aledmys Díaz moves to 3B
b9.defensive_switch(1, "5")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("f")
b9.hit(1)

# 7. BOS #59 Sam Travis (X - X - 36)
b9.new_ab()
b9.pitch_list("c s s")
b9.out("K")

# 8. BOS #3  Sandy León (X - X - 36)
b9.new_ab()
b9.pitch_list("f f s")
b9.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 36)
b9.new_ab()
b9.pitch_list("s")
b9.out("G3-1")

# Winning team: TOR
# WP: TOR #39 Jake Petricka
game.winning_pitcher(39, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
