import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ TOR, 2018-08-09
# https://www.baseball-reference.com/boxes/TOR/TOR201808090.shtml
# https://www.mlb.com/gameday/red-sox-vs-blue-jays/2018/08/09/531135/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-09 19:07-21:56",
        "at": "Rogers Centre, Toronto, ON",
        "att": "28,415",
        "temp": "68F, Roof Closed",
        "wind": "0mph, None",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                18: "Mitch Moreland",
                68: "Dan Butler",
                11: "Rafael Devers",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                31: "Drew Pomeranz",
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
                [25, "3"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [68, "C"],
                [11, "3B"],
            ],
            "bullpen": [47, 44, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Toronto Blue Jays",
            "starter": 56,
            "roster": {
                # Lineup
                18: "Curtis Granderson",
                29: "Devon Travis",
                14: "Justin Smoak",
                15: "Randal Grichuk",
                26: "Yangervis Solarte",
                37: "Teoscar Hernández",
                55: "Russell Martin",
                1: "Aledmys Díaz",
                11: "Kevin Pillar",
                # Starting pitcher
                56: "Ryan Borucki",
                # Bench
                7: "Richard Urena",
                21: "Luke Maile",
                8: "Kendrys Morales",
                # Bullpen
                51: "Ken Giles",
                57: "Jaime García",
                31: "Joe Biagini",
                24: "Danny Barnes",
                71: "Luis Santos",
                25: "Marco Estrada",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                36: "Tyler Clippard",
                45: "Thomas Pannone",
                6: "Marcus Stroman",
                52: "Ryan Tepera",
            },
            "lefties": [56, 57, 45],
            "lineup": [
                [18, "0"],
                [29, "4"],
                [14, "3"],
                [15, "9"],
                [26, "5"],
                [37, "7"],
                [55, "2"],
                [1, "6"],
                [11, "8"],
            ],
            "bench": [
                [7, "SS"],
                [21, "C"],
                [8, "DH"],
            ],
            "bullpen": [51, 57, 31, 24, 71, 25, 39, 43, 36, 45, 6, 52],
        },
        "umpires": {
            "HP": "Gabe Morales",
            "1B": "Jerry Meals",
            "2B": "Ed Hickox",
            "3B": "Ramon De Jesus",
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
# Pitching: TOR #56 Ryan Borucki
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)
t1.advance(2, "16 1B")
t1.advance(3, "28 F9")
t1.advance(4, "36 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("d b c")
t1.hit(1)
t1.advance(2, "2 BB")
t1.advance(4, "36 1B")

# 3. BOS #25 Steve Pearce (X - 50 - 16)
t1.new_ab()
t1.out("(F)P3")

# 4. BOS #28 J.D. Martinez (X - 50 - 16)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 5. BOS #2  Xander Bogaerts (50 - X - 16)
t1.new_ab()
t1.pitch_list("b b b d")
t1.reach("BB")
t1.advance(3, "36 1B")

# 6. BOS #36 Eduardo Núñez (50 - 16 - 2)
t1.new_ab()
t1.pitch_list("c b f f")
t1.hit(1, rbis=2)

# 7. BOS #12 Brock Holt (2 - X - 36)
t1.new_ab()
t1.out("G4-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. TOR #18 Curtis Granderson (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.advance(2, "29 BB")
b1.advance(4, "14 1B")

# 2. TOR #29 Devon Travis (X - X - 18)
b1.new_ab()
b1.pitch_list("b f b b b")
b1.reach("BB")
b1.advance(3, "14 1B")
b1.advance(4, "15 FC6-4")

# 3. TOR #14 Justin Smoak (X - 18 - 29)
b1.new_ab()
b1.pitch_list("c f b")
b1.hit(1, rbis=1)
b1.thrown_out(2, "15 FC6-4", 1, 22)

# 4. TOR #15 Randal Grichuk (29 - X - 14)
b1.new_ab()
b1.pitch_list("b c c")
b1.reach("FC6-4", rbis=1)
b1.advance(2, "26 G6-3")

# 5. TOR #26 Yangervis Solarte (X - X - 15)
b1.new_ab()
b1.out("G6-3")

# 6. TOR #37 Teoscar Hernández (X - 15 - X)
b1.new_ab()
b1.pitch_list("f s b f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: TOR #56 Ryan Borucki
t2 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c f b")
t2.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("f b")
t2.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f")
t2.hit(3)

# 2. BOS #16 Andrew Benintendi (50 - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G3")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 7. TOR #55 Russell Martin (X - X - X)
b2.new_ab()
b2.pitch_list("b c b c b b")
b2.reach("BB")
b2.advance(3, "1 1B")
b2.advance(4, "11 E5")

# 8. TOR #1  Aledmys Díaz (X - X - 55)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.advance(2, "11 E5")
b2.advance(3, "18 F8")
b2.thrown_out(4, "29 FC5-2-5", 2, 22)

# 9. TOR #11 Kevin Pillar (55 - X - 1)
b2.new_ab()
b2.error(5)
b2.reach("E5", rbis=1)
b2.advance(2, "29 SB")
b2.advance(3, "29 FC5-2-5")

# 1. TOR #18 Curtis Granderson (X - 1 - 11)
b2.new_ab()
b2.pitch_list("c c")
b2.out("F8")

# 2. TOR #29 Devon Travis (1 - X - 11)
b2.new_ab()
b2.pitch_list("1 d d f")
b2.reach("FC5-2-5", end_base=2)

# 3. TOR #14 Justin Smoak (11 - 29 - X)
b2.new_ab()
b2.pitch_list("c f b d s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: TOR #56 Ryan Borucki
t3 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b c b")
t3.reach("BB")
t3.thrown_out(2, "28 DP6-4-3", 1, 56)

# 4. BOS #28 J.D. Martinez (X - X - 25)
t3.new_ab()
t3.out("DP6-4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b c f f f b")
t3.reach("BB")
t3.advance(2, "36 1B")

# 6. BOS #36 Eduardo Núñez (X - X - 2)
t3.new_ab()
t3.pitch_list("b b")
t3.hit(1)

# 7. BOS #12 Brock Holt (X - 2 - 36)
t3.new_ab()
t3.pitch_list("c c d b c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 4. TOR #15 Randal Grichuk (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("(F)P5")

# 5. TOR #26 Yangervis Solarte (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G3")

# 6. TOR #37 Teoscar Hernández (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(4, rbis=1)

# 7. TOR #55 Russell Martin (X - X - X)
b3.new_ab()
b3.pitch_list("c f b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: TOR #56 Ryan Borucki
t4 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t4.new_ab()
t4.pitch_list("c c b b")
t4.out("F8")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c b b c b f t")
t4.out("KT")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f")
t4.hit(2)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t4.new_ab()
t4.pitch_list("c f")
t4.out("G3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 8. TOR #1  Aledmys Díaz (X - X - X)
b4.new_ab()
b4.pitch_list("f s f")
b4.out("F8")

# 9. TOR #11 Kevin Pillar (X - X - X)
b4.new_ab()
b4.pitch_list("c f f s")
b4.out("K")

# 1. TOR #18 Curtis Granderson (X - X - X)
b4.new_ab()
b4.pitch_list("c f b f f f c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: TOR #56 Ryan Borucki
t5 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
t5.new_ab()
t5.pitch_list("b b f b c f")
t5.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b")
t5.hit(4, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b c b c f")
t5.out("F9")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(1)
t5.advance(2, "12 SB")
t5.advance(4, "12 1B")

# 7. BOS #12 Brock Holt (X - X - 36)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1, rbis=1)
t5.thrown_out(2, "3 POCS", 3, 56)

# 8. BOS #3  Sandy León (X - X - 12)
t5.new_ab()
t5.pitch_list("f 1 1")
t5.no_ab("POCS")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 2. TOR #29 Devon Travis (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(4, "14 2B")

# 3. TOR #14 Justin Smoak (X - X - 29)
b5.new_ab()
b5.hit(2, rbis=1)
b5.advance(4, "15 HR")

# 4. TOR #15 Randal Grichuk (X - 14 - X)
b5.new_ab()
b5.pitch_list("b f f b")
b5.hit(4, rbis=2)

# Pitching change (BOS): #44 Brandon Workman replaces #22 Rick Porcello
b5.pitching_substitution(44)

# 5. TOR #26 Yangervis Solarte (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.thrown_out(2, "55 CS", 3, 44)

# 6. TOR #37 Teoscar Hernández (X - X - 26)
b5.new_ab()
b5.out("F9")

# 7. TOR #55 Russell Martin (X - X - 26)
b5.new_ab()
b5.pitch_list("b c c b 1 f b s")
b5.out("KDP2-4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: TOR #57 Jaime García
t6 = game.new_inning()

# Pitching change (TOR): #57 Jaime García replaces #56 Ryan Borucki
t6.pitching_substitution(57)

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.out("G1-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c c b b b d")
t6.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t6.new_ab()
t6.pitch_list("b c f d f")
t6.out("G3")


# Bot 6th
# Pitching: BOS #76 Hector Velázquez
b6 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #44 Brandon Workman
b6.pitching_substitution(76)

# 8. TOR #1  Aledmys Díaz (X - X - X)
b6.new_ab()
b6.pitch_list("b f b")
b6.out("G6-3")

# 9. TOR #11 Kevin Pillar (X - X - X)
b6.new_ab()
b6.pitch_list("m f")
b6.out("L9")

# 1. TOR #18 Curtis Granderson (X - X - X)
b6.new_ab()
b6.pitch_list("b b c b")
b6.hit(2)
b6.advance(4, "29 1B")

# 2. TOR #29 Devon Travis (X - 18 - X)
b6.new_ab()
b6.pitch_list("b f b f f")
b6.hit(1, rbis=1)
b6.thrown_out(2, "7-2-4", 3, 76)


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: TOR #36 Tyler Clippard
t7 = game.new_inning()

# Pitching change (TOR): #36 Tyler Clippard replaces #57 Jaime García
t7.pitching_substitution(36)

# 3. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("G1-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b f t")
t7.out("KT")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("L5")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# 3. TOR #14 Justin Smoak (X - X - X)
b7.new_ab()
b7.hit(1)
b7.thrown_out(2, "15 DP6-4-3", 1, 76)

# 4. TOR #15 Randal Grichuk (X - X - 14)
b7.new_ab()
b7.out("DP6-4-3")

# 5. TOR #26 Yangervis Solarte (X - X - X)
b7.new_ab()
b7.pitch_list("b f f b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: TOR #52 Ryan Tepera
t8 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #36 Tyler Clippard
t8.pitching_substitution(52)

# 6. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("(F)P2")

# 7. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.out("F7")

# 8. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.out("F9")


# Bot 8th
# Pitching: BOS #47 Tyler Thornburg
b8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #76 Hector Velázquez
b8.pitching_substitution(47)

# 6. TOR #37 Teoscar Hernández (X - X - X)
b8.new_ab()
b8.pitch_list("s f b f c")
b8.out("!K")

# 7. TOR #55 Russell Martin (X - X - X)
b8.new_ab()
b8.pitch_list("b c t f s")
b8.out("K")

# 8. TOR #1  Aledmys Díaz (X - X - X)
b8.new_ab()
b8.pitch_list("f f b b b")
b8.hit(1)
b8.advance(2, "11 1B")
b8.advance(3, "18 SB")

# 9. TOR #11 Kevin Pillar (X - X - 1)
b8.new_ab()
b8.pitch_list("b")
b8.hit(1)

# 1. TOR #18 Curtis Granderson (X - 1 - 11)
b8.new_ab()
b8.pitch_list("b f b f b n s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: TOR #51 Ken Giles
t9 = game.new_inning()

# Pitching change (TOR): #51 Ken Giles replaces #52 Ryan Tepera
t9.pitching_substitution(51)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.out("F9")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b f")
t9.hit(4, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b s")
t9.out("K")

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #25 Steve Pearce, batting 3rd
t9.offensive_substitution(3, 18, "PH")

# 3. BOS #18 Mitch Moreland (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c s c")
t9.out("!K")

# Winning team: TOR
# WP: TOR #56 Ryan Borucki
game.winning_pitcher(56)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22, is_away_team=True)

# print(game)
game.generate_scorecard()
