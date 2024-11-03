import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-08-07
# https://www.baseball-reference.com/boxes/TOR/TOR201808070.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/08/07/531106/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-07 19:08-22:35",
        "at": "Rogers Centre, Toronto, ON",
        "att": "31,855",
        "temp": "81F, Cloudy",
        "wind": "5mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                25: "Steve Pearce",
                68: "Dan Butler",
                38: "Tony Renda",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [19, "8"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
            ],
            "bench": [
                [25, "1B"],
                [68, "C"],
                [38, "2B"],
            ],
            "bullpen": [47, 44, 22, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 6,
            "roster": {
                # Lineup
                15: "Randal Grichuk",
                29: "Devon Travis",
                14: "Justin Smoak",
                37: "Teoscar Hernández",
                8: "Kendrys Morales",
                26: "Yangervis Solarte",
                1: "Aledmys Díaz",
                11: "Kevin Pillar",
                21: "Luke Maile",
                # Starting pitcher
                6: "Marcus Stroman",
                # Bench
                55: "Russell Martin",
                7: "Richard Urena",
                18: "Curtis Granderson",
                # Bullpen
                44: "Mike Hauschild",
                51: "Ken Giles",
                57: "Jaime García",
                31: "Joe Biagini",
                24: "Danny Barnes",
                71: "Luis Santos",
                25: "Marco Estrada",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                56: "Ryan Borucki",
                36: "Tyler Clippard",
                52: "Ryan Tepera",
            },
            "lefties": [57, 56],
            "lineup": [
                [15, "9"],
                [29, "4"],
                [14, "3"],
                [37, "7"],
                [8, "0"],
                [26, "5"],
                [1, "6"],
                [11, "8"],
                [21, "2"],
            ],
            "bench": [
                [55, "C"],
                [7, "SS"],
                [18, "CF"],
            ],
            "bullpen": [44, 51, 57, 31, 24, 71, 25, 39, 43, 56, 36, 52],
        },
        "umpires": {
            "HP": "Ed Hickox",
            "1B": "Ramon De Jesus",
            "2B": "Gabe Morales",
            "3B": "Jerry Meals",
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
# Pitching: TOR #6  Marcus Stroman
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c s b s")
t1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G5-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.pitch_list("b f s b c")
t1.out("!K")


# Bot 1st
# Pitching: BOS #31 Drew Pomeranz
b1 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.out("G4-3")

# 2. TOR #29 Devon Travis (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("F8")

# 3. TOR #14 Justin Smoak (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c f")
b1.hit(1)
b1.advance(2, "37 BB")

# 4. TOR #37 Teoscar Hernández (X - X - 14)
b1.new_ab()
b1.pitch_list("b b b c f b")
b1.reach("BB")

# 5. TOR #8  Kendrys Morales (X - 14 - 37)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #6  Marcus Stroman
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c c b")
t2.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")
t2.thrown_out(2, "19 DP4-6-3", 2, 6)

# 6. BOS #19 Jackie Bradley Jr. (X - X - 2)
t2.new_ab()
t2.pitch_list("c c")
t2.out("DP4-6-3")


# Bot 2nd
# Pitching: BOS #31 Drew Pomeranz
b2 = game.new_inning()

# 6. TOR #26 Yangervis Solarte (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b b")
b2.reach("BB")
b2.thrown_out(2, "1 DP6-4-3", 1, 31)

# 7. TOR #1  Aledmys Díaz (X - X - 26)
b2.new_ab()
b2.out("DP6-4-3")

# 8. TOR #11 Kevin Pillar (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #6  Marcus Stroman
t3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G3-1")

# 8. BOS #12 Brock Holt (X - X - X)
t3.new_ab()
t3.pitch_list("c s b b f")
t3.out("G4-3")

# 9. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #31 Drew Pomeranz
b3 = game.new_inning()

# 9. TOR #21 Luke Maile (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b f")
b3.out("P3")

# 1. TOR #15 Randal Grichuk (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(4, "29 HR")

# 2. TOR #29 Devon Travis (X - X - 15)
b3.new_ab()
b3.pitch_list("b b b c f")
b3.hit(4, rbis=2)

# 3. TOR #14 Justin Smoak (X - X - X)
b3.new_ab()
b3.pitch_list("c f b")
b3.out("G5-3")

# 4. TOR #37 Teoscar Hernández (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.hit(1)

# 5. TOR #8  Kendrys Morales (X - X - 37)
b3.new_ab()
b3.pitch_list("b 1 b c f")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #6  Marcus Stroman
t4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.error(4)
t4.reach("E4")
t4.advance(2, "18 BB")
t4.advance("U", "28 1B")

# 3. BOS #18 Mitch Moreland (X - X - 16)
t4.new_ab()
t4.pitch_list("b b d b")
t4.reach("BB")
t4.advance(2, "28 1B")

# 4. BOS #28 J.D. Martinez (X - 16 - 18)
t4.new_ab(is_risp=True)
t4.pitch_list("f")
t4.hit(1, rbis=1)
t4.thrown_out(2, "2 DP6-4-3", 2, 6)

# 5. BOS #2  Xander Bogaerts (X - 18 - 28)
t4.new_ab(is_risp=True)
t4.pitch_list("b b c")
t4.out("DP6-4-3")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 6. TOR #26 Yangervis Solarte (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L1")

# 7. TOR #1  Aledmys Díaz (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")
b4.thrown_out(2, "11 DP6-4-3", 2, 31)

# 8. TOR #11 Kevin Pillar (X - X - 1)
b4.new_ab()
b4.pitch_list("b f s 1 d")
b4.out("DP6-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #6  Marcus Stroman
t5 = game.new_inning()

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("f b s f f b c")
t5.out("!K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("f b b f b s")
t5.out("K")

# 8. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 9. TOR #21 Luke Maile (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)

# 1. TOR #15 Randal Grichuk (X - 21 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b s d c s")
b5.out("K")

# 2. TOR #29 Devon Travis (X - 21 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("L6")

# 3. TOR #14 Justin Smoak (X - 21 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d d d c b")
b5.reach("BB")

# Pitching change (BOS): #37 Heath Hembree replaces #31 Drew Pomeranz
b5.pitching_substitution(37)

# 4. TOR #37 Teoscar Hernández (X - 21 - 14)
b5.new_ab(is_risp=True)
b5.pitch_list("s b")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #6  Marcus Stroman
t6 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("b b b f")
t6.out("G1-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c t")
t6.out("G3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")

# 3. BOS #18 Mitch Moreland (X - X - 16)
t6.new_ab()
t6.pitch_list("b s")
t6.out("G3")


# Bot 6th
# Pitching: BOS #44 Brandon Workman
b6 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree
b6.pitching_substitution(44)

# 5. TOR #8  Kendrys Morales (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.advance(2, "26 BB")
b6.advance(3, "1 1B")
b6.thrown_out(4, "21 FC2", 2, 44)

# 6. TOR #26 Yangervis Solarte (X - X - 8)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "1 1B")
b6.advance(3, "21 FC2")
b6.thrown_out(4, "15 FC1-2", 3, 44)

# 7. TOR #1  Aledmys Díaz (X - 8 - 26)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.hit(1)
b6.advance(2, "21 FC2")

# 8. TOR #11 Kevin Pillar (8 - 26 - 1)
b6.new_ab(is_risp=True)
b6.out("F9")

# 9. TOR #21 Luke Maile (8 - 26 - 1)
b6.new_ab(is_risp=True)
b6.reach("FC2")

# 1. TOR #15 Randal Grichuk (26 - 1 - 21)
b6.new_ab(is_risp=True)
b6.pitch_list("b b s f f")
b6.reach("FC1-2")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #6  Marcus Stroman
t7 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(2)
t7.advance(3, "19 G3")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b c b 2 f")
t7.out("G6-3")

# 6. BOS #19 Jackie Bradley Jr. (X - 28 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.out("G3")

# 7. BOS #36 Eduardo Núñez (28 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b")
t7.out("G1-3")


# Bot 7th
# Pitching: BOS #56 Joe Kelly
b7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
b7.pitching_substitution(56)

# 2. TOR #29 Devon Travis (X - X - X)
b7.new_ab()
b7.pitch_list("f b")
b7.hit(1)
b7.error(7)
b7.advance(2, "E7")
b7.error(1)
b7.advance(3, "37 POE1")
b7.advance("U", "37 SF8")

# 3. TOR #14 Justin Smoak (X - 29 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s c s")
b7.out("K")

# 4. TOR #37 Teoscar Hernández (X - 29 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("2 c s b 2 f b")
b7.out("SF8", rbis=1)

# 5. TOR #8  Kendrys Morales (X - X - X)
b7.new_ab()
b7.pitch_list("b c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #52 Ryan Tepera
t8 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #6  Marcus Stroman
t8.pitching_substitution(52)

# 8. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("c f b s")
t8.out("K")

# 9. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.hit(2)
t8.advance(3, "16 1B")
t8.advance(4, "18 FC4-6")

# 1. BOS #50 Mookie Betts (X - 3 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c b t b f b")
t8.reach("BB")
t8.advance(2, "16 1B")
t8.advance(3, "18 FC4-6")
t8.advance(4, "28 HR")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.hit(1)
t8.thrown_out(2, "18 FC4-6", 2, 52)

# 3. BOS #18 Mitch Moreland (3 - 50 - 16)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.reach("FC4-6", rbis=1)
t8.advance(4, "28 HR")

# 4. BOS #28 J.D. Martinez (50 - X - 18)
t8.new_ab(is_risp=True)
t8.pitch_list("b b")
t8.hit(4, rbis=3)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.out("G3")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
b8.pitching_substitution(32)

# 6. TOR #26 Yangervis Solarte (X - X - X)
b8.new_ab()
b8.pitch_list("b c b s f")
b8.hit(1)
b8.advance(4, "21 2B")

# 7. TOR #1  Aledmys Díaz (X - X - 26)
b8.new_ab()
b8.pitch_list("b f s")
b8.out("F9")

# 8. TOR #11 Kevin Pillar (X - X - 26)
b8.new_ab()
b8.pitch_list("b s t s")
b8.out("K")

# 9. TOR #21 Luke Maile (X - X - 26)
b8.new_ab()
b8.hit(2, rbis=1)

# 1. TOR #15 Randal Grichuk (X - 21 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c b")
b8.out("(F)P3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #36 Tyler Clippard
t9 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #52 Ryan Tepera
t9.pitching_substitution(36)

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("s f b f")
t9.out("F9")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# 8. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c b s f c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b9.pitching_substitution(46)

# 2. TOR #29 Devon Travis (X - X - X)
b9.new_ab()
b9.pitch_list("b f s b f s")
b9.out("K")

# 3. TOR #14 Justin Smoak (X - X - X)
b9.new_ab()
b9.pitch_list("b b b")
b9.hit(4)

# 4. TOR #37 Teoscar Hernández (X - X - X)
b9.new_ab()
b9.pitch_list("s s b b f s")
b9.out("K")

# 5. TOR #8  Kendrys Morales (X - X - X)
b9.new_ab()
b9.pitch_list("b c s b b s")
b9.out("K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: TOR #51 Ken Giles
t10 = game.new_inning()

# Pitching change (TOR): #51 Ken Giles replaces #36 Tyler Clippard
t10.pitching_substitution(51)

# 9. BOS #3  Sandy León (X - X - X)
t10.new_ab()
t10.pitch_list("c c b s")
t10.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t10.new_ab()
t10.pitch_list("c b b c")
t10.hit(3)
t10.advance(4, "18 HR")

# 2. BOS #16 Andrew Benintendi (50 - X - X)
t10.new_ab(is_risp=True)
t10.pitch_list("b c b b b")
t10.reach("BB")
t10.advance(4, "18 HR")

# 3. BOS #18 Mitch Moreland (50 - X - 16)
t10.new_ab(is_risp=True)
t10.hit(4, rbis=3)

# 4. BOS #28 J.D. Martinez (X - X - X)
t10.new_ab()
t10.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t10.new_ab()
t10.pitch_list("c f f")
t10.hit(1)
t10.advance(2, "19 SB")
t10.advance(4, "19 HR")

# 6. BOS #19 Jackie Bradley Jr. (X - X - 2)
t10.new_ab(is_risp=True)
t10.pitch_list("c s")
t10.hit(4, rbis=2)

# Pitching change (TOR): #71 Luis Santos replaces #51 Ken Giles
t10.pitching_substitution(71)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t10.new_ab()
t10.pitch_list("c")
t10.out("(F)P3")


# Bot 10th
# Pitching: BOS #47 Tyler Thornburg
b10 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #46 Craig Kimbrel
b10.pitching_substitution(47)

# 6. TOR #26 Yangervis Solarte (X - X - X)
b10.new_ab()
b10.pitch_list("c")
b10.hit(1)
b10.advance(4, "11 HR")

# 7. TOR #1  Aledmys Díaz (X - X - 26)
b10.new_ab()
b10.pitch_list("f c b")
b10.out("P6")

# 8. TOR #11 Kevin Pillar (X - X - 26)
b10.new_ab()
b10.pitch_list("c f f f")
b10.hit(4, rbis=2)

# 9. TOR #21 Luke Maile (X - X - X)
b10.new_ab()
b10.pitch_list("b b c")
b10.out("P2")

# 1. TOR #15 Randal Grichuk (X - X - X)
b10.new_ab()
b10.hit(1)

# 2. TOR #29 Devon Travis (X - X - 15)
b10.new_ab()
b10.out("F7")

# Winning team: BOS
# WP: BOS #46 Craig Kimbrel
game.winning_pitcher(46, is_away_team=True)

# Loser team: TOR
# LP: TOR #51 Ken Giles
game.losing_pitcher(51)

# print(game)
game.generate_scorecard()
