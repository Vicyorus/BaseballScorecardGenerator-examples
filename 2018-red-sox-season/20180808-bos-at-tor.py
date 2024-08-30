import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-08-08
# https://www.baseball-reference.com/boxes/TOR/TOR201808080.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/08/08/531121/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-08 19:07-22:09",
        "at": "Rogers Centre, Toronto, ON",
        "att": "36,798",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
                68: "Dan Butler",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [61, 31, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [19, "8"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [68, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 44,
            "roster": {
                # Lineup
                15: "Randal Grichuk",
                29: "Devon Travis",
                14: "Justin Smoak",
                37: "Teoscar Hernández",
                8: "Kendrys Morales",
                26: "Yangervis Solarte",
                55: "Russell Martin",
                1: "Aledmys Díaz",
                11: "Kevin Pillar",
                # Starting pitcher
                44: "Mike Hauschild",
                # Bench
                7: "Richard Urena",
                21: "Luke Maile",
                18: "Curtis Granderson",
                # Bullpen
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
                6: "Marcus Stroman",
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
                [55, "2"],
                [1, "6"],
                [11, "8"],
            ],
            "bench": [
                [7, "SS"],
                [21, "C"],
                [18, "CF"],
            ],
            "bullpen": [51, 57, 31, 24, 71, 25, 39, 43, 56, 36, 6, 52],
        },
        "umpires": {
            "HP": "Ramon De Jesus",
            "1B": "Gabe Morales",
            "2B": "Jerry Meals",
            "3B": "Ed Hickox",
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
# Pitching: TOR #44 Mike Hauschild
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c t b")
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b c b f b")
t1.reach("BB")
t1.thrown_out(2, "18 DP5-6-3", 2, 44)

# 3. BOS #18 Mitch Moreland (X - X - 16)
t1.new_ab()
t1.pitch_list("b s b")
t1.out("DP5-6-3")


# Bot 1st
# Pitching: BOS #61 Brian Johnson
b1 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G1-3")

# 2. TOR #29 Devon Travis (X - X - X)
b1.new_ab()
b1.out("L8")

# 3. TOR #14 Justin Smoak (X - X - X)
b1.new_ab()
b1.pitch_list("c s b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #44 Mike Hauschild
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("F7")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("b f b b b")
t2.reach("BB")
t2.thrown_out(2, "36 FC6-4", 3, 44)

# 7. BOS #36 Eduardo Núñez (X - X - 19)
t2.new_ab()
t2.pitch_list("b 1 b s")
t2.reach("FC6-4")


# Bot 2nd
# Pitching: BOS #61 Brian Johnson
b2 = game.new_inning()

# 4. TOR #37 Teoscar Hernández (X - X - X)
b2.new_ab()
b2.pitch_list("s b b c c")
b2.out("!K")

# 5. TOR #8  Kendrys Morales (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 6. TOR #26 Yangervis Solarte (X - X - X)
b2.new_ab()
b2.pitch_list("f f f")
b2.out("(F)P3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #44 Mike Hauschild
t3 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c c f")
t3.hit(2)
t3.advance(3, "50 HBP")
t3.advance(4, "16 SF8")

# 9. BOS #3  Sandy León (X - 11 - X)
t3.new_ab()
t3.pitch_list("c s d 2 b f b d")
t3.reach("BB")
t3.advance(2, "50 HBP")
t3.advance(3, "16 SF8")
t3.advance(4, "18 2B")

# 1. BOS #50 Mookie Betts (X - 11 - 3)
t3.new_ab()
t3.reach("HBP")
t3.advance(2, "18 SB")
t3.advance(4, "18 2B")

# 2. BOS #16 Andrew Benintendi (11 - 3 - 50)
t3.new_ab()
t3.pitch_list("f f")
t3.out("SF8", rbis=1)

# 3. BOS #18 Mitch Moreland (3 - X - 50)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(2, rbis=2)
t3.advance(3, "28 1B")
t3.advance(4, "2 SF9")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)

# Pitching change (TOR): #71 Luis Santos replaces #44 Mike Hauschild
t3.pitching_substitution(71)

# 5. BOS #2  Xander Bogaerts (18 - X - 28)
t3.new_ab()
t3.pitch_list("s")
t3.out("SF9", rbis=1)

# 6. BOS #19 Jackie Bradley Jr. (X - X - 28)
t3.new_ab()
t3.pitch_list("f s f f")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #61 Brian Johnson
b3 = game.new_inning()

# 7. TOR #55 Russell Martin (X - X - X)
b3.new_ab()
b3.pitch_list("b c b c b")
b3.hit(1)

# 8. TOR #1  Aledmys Díaz (X - X - 55)
b3.new_ab()
b3.pitch_list("c b c")
b3.out("F9")

# 9. TOR #11 Kevin Pillar (X - X - 55)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 1. TOR #15 Randal Grichuk (X - X - 55)
b3.new_ab()
b3.pitch_list("c s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #71 Luis Santos
t4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("L6")

# 8. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("c b b s b f d")
t4.reach("BB")
t4.thrown_out(2, "3 CS", 2, 71)

# 9. BOS #3  Sandy León (X - X - 11)
t4.new_ab()
t4.pitch_list("s c s")
t4.out("K")


# Bot 4th
# Pitching: BOS #61 Brian Johnson
b4 = game.new_inning()

# 2. TOR #29 Devon Travis (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.out("F8")

# 3. TOR #14 Justin Smoak (X - X - X)
b4.new_ab()
b4.pitch_list("b f b")
b4.hit(2)

# 4. TOR #37 Teoscar Hernández (X - 14 - X)
b4.new_ab()
b4.pitch_list("s c s")
b4.out("K")

# 5. TOR #8  Kendrys Morales (X - 14 - X)
b4.new_ab()
b4.pitch_list("c d")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #71 Luis Santos
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c f b f b")
t5.hit(1)
t5.advance(3, "16 2B")
t5.advance(4, "2 BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("d 1 f b")
t5.hit(2)
t5.advance(3, "2 BB")

# 3. BOS #18 Mitch Moreland (50 - 16 - X)
t5.new_ab()
t5.pitch_list("c s")
t5.out("F7")

# 4. BOS #28 J.D. Martinez (50 - 16 - X)
t5.new_ab()
t5.pitch_list("v v v v")
t5.reach("IBB")
t5.advance(2, "2 BB")

# 5. BOS #2  Xander Bogaerts (50 - 16 - 28)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB", rbis=1)
t5.thrown_out(2, "19 DP4-6-3", 2, 39)

# Pitching change (TOR): #39 Jake Petricka replaces #71 Luis Santos
t5.pitching_substitution(39)

# 6. BOS #19 Jackie Bradley Jr. (16 - 28 - 2)
t5.new_ab()
t5.pitch_list("d f c b f")
t5.out("DP4-6-3")


# Bot 5th
# Pitching: BOS #61 Brian Johnson
b5 = game.new_inning()

# 6. TOR #26 Yangervis Solarte (X - X - X)
b5.new_ab()
b5.pitch_list("c b t f")
b5.out("G5-3")

# 7. TOR #55 Russell Martin (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")
b5.thrown_out(2, "1 FC5-4", 2, 61)

# 8. TOR #1  Aledmys Díaz (X - X - 55)
b5.new_ab()
b5.pitch_list("c f b")
b5.reach("FC5-4")

# 9. TOR #11 Kevin Pillar (X - X - 1)
b5.new_ab()
b5.pitch_list("f b c")
b5.out("G1-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #39 Jake Petricka
t6 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.advance(4, "11 HR")

# 8. BOS #11 Rafael Devers (X - X - 36)
t6.new_ab()
t6.pitch_list("c b b f")
t6.hit(4, rbis=2)

# 9. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("f c b f")
t6.out("L4")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.hit(2)

# 3. BOS #18 Mitch Moreland (X - 16 - X)
t6.new_ab()
t6.out("L7")


# Bot 6th
# Pitching: BOS #61 Brian Johnson
b6 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
b6.new_ab()
b6.pitch_list("f b f b")
b6.out("(F)F9")

# 2. TOR #29 Devon Travis (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("P6")

# 3. TOR #14 Justin Smoak (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.hit(1)
b6.advance(4, "37 HR")

# 4. TOR #37 Teoscar Hernández (X - X - 14)
b6.new_ab()
b6.pitch_list("t")
b6.hit(4, rbis=2)

# 5. TOR #8  Kendrys Morales (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #24 Danny Barnes
t7 = game.new_inning()

# Pitching change (TOR): #24 Danny Barnes replaces #39 Jake Petricka
t7.pitching_substitution(24)

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b t")
t7.hit(2)
t7.advance(4, "2 2B")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t7.new_ab()
t7.pitch_list("s")
t7.hit(2, rbis=1)

# 6. BOS #19 Jackie Bradley Jr. (X - 2 - X)
t7.new_ab()
t7.pitch_list("b b c c s")
t7.out("K")

# 7. BOS #36 Eduardo Núñez (X - 2 - X)
t7.new_ab()
t7.pitch_list("b f")
t7.out("G6-3")

# 8. BOS #11 Rafael Devers (X - 2 - X)
t7.new_ab()
t7.pitch_list("b c b f f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #61 Brian Johnson
b7 = game.new_inning()

# 6. TOR #26 Yangervis Solarte (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("L8")

# 7. TOR #55 Russell Martin (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b b b")
b7.reach("BB")
b7.advance(2, "11 1B")
b7.advance(4, "15 HR")

# 8. TOR #1  Aledmys Díaz (X - X - 55)
b7.new_ab()
b7.pitch_list("b s f s")
b7.out("K")

# 9. TOR #11 Kevin Pillar (X - X - 55)
b7.new_ab()
b7.pitch_list("b d")
b7.hit(1)
b7.advance(4, "15 HR")

# 1. TOR #15 Randal Grichuk (X - 55 - 11)
b7.new_ab()
b7.hit(4, rbis=3)

# 2. TOR #29 Devon Travis (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #31 Joe Biagini
t8 = game.new_inning()

# Pitching change (TOR): #31 Joe Biagini replaces #24 Danny Barnes
t8.pitching_substitution(31)

# 9. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("b s s")
t8.hit(1)
t8.advance(2, "16 BB")
t8.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (X - X - 3)
t8.new_ab()
t8.pitch_list("b f b f d s")
t8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
t8.new_ab()
t8.pitch_list("d b f b b")
t8.reach("BB")
t8.advance(3, "28 1B")
t8.advance(4, "19 WP")

# 3. BOS #18 Mitch Moreland (X - 3 - 16)
t8.new_ab()
t8.pitch_list("s b")
t8.out("F8")

# 4. BOS #28 J.D. Martinez (X - 3 - 16)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1, rbis=1)
t8.advance(2, "2 BB")
t8.advance(3, "19 WP")

# 5. BOS #2  Xander Bogaerts (16 - X - 28)
t8.new_ab()
t8.pitch_list("b d b c b")
t8.reach("BB")
t8.advance(2, "19 WP")

# 6. BOS #19 Jackie Bradley Jr. (16 - 28 - 2)
t8.new_ab()
t8.pitch_list("f f b b s")
t8.wp()
t8.out("K")


# Bot 8th
# Pitching: BOS #70 Ryan Brasier
b8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #61 Brian Johnson
b8.pitching_substitution(70)

# 3. TOR #14 Justin Smoak (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b")
b8.hit(1)
b8.error(6)
b8.advance(2, "26 E6")

# 4. TOR #37 Teoscar Hernández (X - X - 14)
b8.new_ab()
b8.pitch_list("c s b b s")
b8.out("K")

# 5. TOR #8  Kendrys Morales (X - X - 14)
b8.new_ab()
b8.pitch_list("s c s")
b8.out("K")

# 6. TOR #26 Yangervis Solarte (X - X - 14)
b8.new_ab()
b8.pitch_list("c")
b8.reach("FC6")

# 7. TOR #55 Russell Martin (X - 14 - 26)
b8.new_ab()
b8.pitch_list("c")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #57 Jaime García
t9 = game.new_inning()

# Pitching change (TOR): #57 Jaime García replaces #31 Joe Biagini
t9.pitching_substitution(57)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("f s f")
t9.out("(F)P5")

# 8. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.out("G3")

# 9. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #70 Ryan Brasier
b9.pitching_substitution(56)

# 8. TOR #1  Aledmys Díaz (X - X - X)
b9.new_ab()
b9.hit(1)
b9.advance(2, "15 1B")

# 9. TOR #11 Kevin Pillar (X - X - 1)
b9.new_ab()
b9.pitch_list("c s f s")
b9.out("K")

# 1. TOR #15 Randal Grichuk (X - X - 1)
b9.new_ab()
b9.pitch_list("c c f b")
b9.hit(1)
b9.thrown_out(2, "29 DP6-3", 2, 56)

# 2. TOR #29 Devon Travis (X - 1 - 15)
b9.new_ab()
b9.pitch_list("f c b f d")
b9.out("DP6-3")

# Winning team: BOS
# WP: BOS #61 Brian Johnson
game.winning_pitcher(61, is_away_team=True)

# Loser team: TOR
# LP: TOR #44 Mike Hauschild
game.losing_pitcher(44)

# print(game)
game.generate_scorecard()
