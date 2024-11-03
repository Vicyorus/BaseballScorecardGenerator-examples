import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-07-15
# https://www.baseball-reference.com/boxes/BOS/BOS201807150.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/07/15/530854/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-15 13:07-16:19",
        "at": "Fenway Park, Boston, MA",
        "att": "36,940",
        "temp": "78F, Cloudy",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 6,
            "roster": {
                # Lineup
                15: "Randal Grichuk",
                26: "Yangervis Solarte",
                37: "Teoscar Hernández",
                14: "Justin Smoak",
                8: "Kendrys Morales",
                55: "Russell Martin",
                29: "Devon Travis",
                27: "Dwight Smith Jr.",
                1: "Aledmys Díaz",
                # Starting pitcher
                6: "Marcus Stroman",
                # Bench
                21: "Luke Maile",
                18: "Curtis Granderson",
                # Bullpen
                62: "Aaron Loup",
                57: "Jaime García",
                31: "Joe Biagini",
                58: "Tim Mayza",
                47: "Chris Rowley",
                71: "Luis Santos",
                39: "Jake Petricka",
                43: "Sam Gaviglio",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                77: "John Axford",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 58, 33],
            "lineup": [
                [15, "8"],
                [26, "5"],
                [37, "7"],
                [14, "3"],
                [8, "0"],
                [55, "2"],
                [29, "4"],
                [27, "9"],
                [1, "6"],
            ],
            "bench": [
                [21, "C"],
                [18, "CF"],
            ],
            "bullpen": [62, 57, 31, 58, 47, 71, 39, 43, 36, 22, 77, 52, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                2: "Xander Bogaerts",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                25: "Steve Pearce",
                12: "Brock Holt",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                5: "Tzu-Wei Lin",
                59: "Sam Travis",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [61, 41, 66, 24],
            "lineup": [
                [50, "9"],
                [2, "6"],
                [28, "7"],
                [18, "3"],
                [25, "0"],
                [12, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [59, "1B"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 22, 41, 66, 37, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Adrian Johnson",
            "1B": "Tripp Gibson",
            "2B": "Brian Gorman",
            "3B": "Mike Muchlinski",
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
# Pitching: BOS #61 Brian Johnson
t1 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
t1.new_ab()
t1.pitch_list("c s b f c")
t1.out("!K")

# 2. TOR #26 Yangervis Solarte (X - X - X)
t1.new_ab()
t1.pitch_list("f s b f")
t1.out("G6-3")

# 3. TOR #37 Teoscar Hernández (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 4. TOR #14 Justin Smoak (X - X - 37)
t1.new_ab()
t1.pitch_list("c f b b f s")
t1.out("K")


# Bot 1st
# Pitching: TOR #6  Marcus Stroman
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("f b f")
b1.out("G5-3")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(4)

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b b s s b f b")
b1.reach("BB")
b1.advance(2, "18 E4")
b1.advance(3, "25 FC1-4")
b1.advance("U", "12 1B")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b1.new_ab()
b1.pitch_list("b b f c")
b1.error(4)
b1.reach("E4")
b1.thrown_out(2, "25 FC1-4", 2, 6)

# 5. BOS #25 Steve Pearce (X - 28 - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("c c d b b")
b1.reach("FC1-4")
b1.advance(2, "12 1B")

# 6. BOS #12 Brock Holt (28 - X - 25)
b1.new_ab(is_risp=True)
b1.pitch_list("c")
b1.hit(1, rbis=1)
b1.thrown_out(2, "36 FC6", 3, 6)

# 7. BOS #36 Eduardo Núñez (X - 25 - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("c f f")
b1.reach("FC6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 5. TOR #8  Kendrys Morales (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b f b")
t2.reach("BB")
t2.advance(2, "27 BB")
t2.thrown_out(3, "1 FC5", 3, 61)

# 6. TOR #55 Russell Martin (X - X - 8)
t2.new_ab()
t2.pitch_list("s b b b")
t2.out("(F)P5")

# 7. TOR #29 Devon Travis (X - X - 8)
t2.new_ab()
t2.out("L8")

# 8. TOR #27 Dwight Smith Jr. (X - X - 8)
t2.new_ab()
t2.pitch_list("b d s b c b")
t2.reach("BB")
t2.advance(2, "1 FC5")

# 9. TOR #1  Aledmys Díaz (X - 8 - 27)
t2.new_ab(is_risp=True)
t2.pitch_list("s")
t2.reach("FC5")


# Bot 2nd
# Pitching: TOR #6  Marcus Stroman
b2 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("b b f f b f f")
b2.hit(1)
b2.thrown_out(2, "9-6", 1, 6)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b f b t f b")
b2.out("F9")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 1. TOR #15 Randal Grichuk (X - X - X)
t3.new_ab()
t3.pitch_list("c s b")
t3.hit(2)
t3.advance(4, "37 HR")

# 2. TOR #26 Yangervis Solarte (X - 15 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f s")
t3.out("P2")

# 3. TOR #37 Teoscar Hernández (X - 15 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c 2")
t3.hit(4, rbis=2)

# 4. TOR #14 Justin Smoak (X - X - X)
t3.new_ab()
t3.out("F8")

# 5. TOR #8  Kendrys Morales (X - X - X)
t3.new_ab()
t3.pitch_list("c c f")
t3.out("L8")


# Bot 3rd
# Pitching: TOR #6  Marcus Stroman
b3 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f")
b3.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("f b b f b s")
b3.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 6. TOR #55 Russell Martin (X - X - X)
t4.new_ab()
t4.pitch_list("b c b c")
t4.out("F8")

# 7. TOR #29 Devon Travis (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b f s")
t4.out("K")

# 8. TOR #27 Dwight Smith Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("c b b c s")
t4.out("K")


# Bot 4th
# Pitching: TOR #6  Marcus Stroman
b4 = game.new_inning()

# 5. BOS #25 Steve Pearce (X - X - X)
b4.new_ab()
b4.pitch_list("f b t b s")
b4.out("K")

# 6. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("c s f f s")
b4.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 9. TOR #1  Aledmys Díaz (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F7")

# 1. TOR #15 Randal Grichuk (X - X - X)
t5.new_ab()
t5.pitch_list("b b s b f f b")
t5.reach("BB")

# 2. TOR #26 Yangervis Solarte (X - X - 15)
t5.new_ab()
t5.pitch_list("b s 1 1 c s 1")
t5.out("K")

# Pitching change (BOS): #44 Brandon Workman replaces #61 Brian Johnson
t5.pitching_substitution(44)

# 3. TOR #37 Teoscar Hernández (X - X - 15)
t5.new_ab()
t5.pitch_list("c b b 1 c f b s")
t5.out("K")


# Bot 5th
# Pitching: TOR #6  Marcus Stroman
b5 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(2)
b5.advance(4, "19 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 3 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f b b")
b5.hit(2, rbis=1)
b5.advance(3, "50 F9")
b5.advance(4, "2 G1-6-3")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("F9")

# 2. BOS #2  Xander Bogaerts (19 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b b f")
b5.out("G1-6-3", rbis=1)

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b b s")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #47 Tyler Thornburg
t6 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #44 Brandon Workman
t6.pitching_substitution(47)

# 4. TOR #14 Justin Smoak (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("L8")

# 5. TOR #8  Kendrys Morales (X - X - X)
t6.new_ab()
t6.pitch_list("b s c")
t6.out("L4")

# 6. TOR #55 Russell Martin (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)

# 7. TOR #29 Devon Travis (X - X - 55)
t6.new_ab()
t6.pitch_list("c s d b f s")
t6.out("K")


# Bot 6th
# Pitching: TOR #62 Aaron Loup
b6 = game.new_inning()

# Pitching change (TOR): #62 Aaron Loup replaces #6  Marcus Stroman
b6.pitching_substitution(62)

# 4. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b f b")
b6.reach("BB")
b6.advance(2, "25 HBP")
b6.advance(4, "12 1B")

# 5. BOS #25 Steve Pearce (X - X - 18)
b6.new_ab()
b6.pitch_list("s b f b")
b6.reach("HBP")
b6.advance(2, "12 1B")

# 6. BOS #12 Brock Holt (X - 18 - 25)
b6.new_ab(is_risp=True)
b6.pitch_list("l c f b")
b6.hit(1, rbis=1)
b6.thrown_out(2, "3 DP4-6-3", 2, 39)

# Pitching change (TOR): #39 Jake Petricka replaces #62 Aaron Loup
b6.pitching_substitution(39)

# 7. BOS #36 Eduardo Núñez (X - 25 - 12)
b6.new_ab(is_risp=True)
b6.out("F7")

# 8. BOS #3  Sandy León (X - 25 - 12)
b6.new_ab(is_risp=True)
b6.pitch_list("b f b c f b")
b6.out("DP4-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
t7.pitching_substitution(70)

# 8. TOR #27 Dwight Smith Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b c c b")
t7.out("G5-3")

# 9. TOR #1  Aledmys Díaz (X - X - X)
t7.new_ab()
t7.pitch_list("b f")
t7.hit(1)
t7.advance(2, "15 1B")

# 1. TOR #15 Randal Grichuk (X - X - 1)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.thrown_out(2, "26 DP1-6-3", 2, 70)

# 2. TOR #26 Yangervis Solarte (X - 1 - 15)
t7.new_ab(is_risp=True)
t7.pitch_list("c b b s f")
t7.out("DP1-6-3")


# Bot 7th
# Pitching: TOR #52 Ryan Tepera
b7 = game.new_inning()

# Pitching change (TOR): #52 Ryan Tepera replaces #39 Jake Petricka
b7.pitching_substitution(52)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("f b b s f b")
b7.out("P4")

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c b s b b b")
b7.reach("BB")
b7.advance(2, "28 SB")
b7.thrown_out(3, "28 2-5", 3, 52)

# 2. BOS #2  Xander Bogaerts (X - X - 50)
b7.new_ab()
b7.pitch_list("c 1 1 f s")
b7.out("K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
b7.new_ab(is_risp=True)
b7.pitch_list("f s f 1 b d f f d")
b7.no_ab("2-5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #37 Heath Hembree
t8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #70 Ryan Brasier
t8.pitching_substitution(37)

# 3. TOR #37 Teoscar Hernández (X - X - X)
t8.new_ab()
t8.pitch_list("s s s")
t8.out("K")

# 4. TOR #14 Justin Smoak (X - X - X)
t8.new_ab()
t8.pitch_list("c b s")
t8.hit(1)
t8.advance(2, "55 1B")
t8.advance(3, "29 1B")

# 5. TOR #8  Kendrys Morales (X - X - 14)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")

# 6. TOR #55 Russell Martin (X - X - 14)
t8.new_ab()
t8.pitch_list("c c b f f")
t8.hit(1)
t8.advance(2, "29 1B")

# 7. TOR #29 Devon Travis (X - 14 - 55)
t8.new_ab(is_risp=True)
t8.hit(1)

# 8. TOR #27 Dwight Smith Jr. (14 - 55 - 29)
t8.new_ab(is_risp=True)
t8.pitch_list("s c s")
t8.out("K")


# Bot 8th
# Pitching: TOR #57 Jaime García
b8 = game.new_inning()

# Pitching change (TOR): #57 Jaime García replaces #52 Ryan Tepera
b8.pitching_substitution(57)

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")
b8.thrown_out(2, "18 DP5-6-3", 1, 57)

# 4. BOS #18 Mitch Moreland (X - X - 28)
b8.new_ab()
b8.pitch_list("d d c")
b8.out("DP5-6-3")

# 5. BOS #25 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("b c b c b b")
b8.reach("BB")
b8.advance(2, "12 BB")

# 6. BOS #12 Brock Holt (X - X - 25)
b8.new_ab()
b8.pitch_list("b b c c b b")
b8.reach("BB")
b8.thrown_out(2, "36 FC6-4", 3, 47)

# Pitching change (TOR): #47 Chris Rowley replaces #57 Jaime García
b8.pitching_substitution(47)

# 7. BOS #36 Eduardo Núñez (X - 25 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("b f f")
b8.reach("FC6-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree
t9.pitching_substitution(46)

# Offensive change (TOR): Pinch-hitter #18 Curtis Granderson replaces #1 Aledmys Díaz, batting 9th
t9.offensive_substitution(9, 18, "PH")

# 9. TOR #18 Curtis Granderson (X - X - X)
t9.new_ab()
t9.pitch_list("f t")
t9.out("F8")

# 1. TOR #15 Randal Grichuk (X - X - X)
t9.new_ab()
t9.pitch_list("b s f s")
t9.out("K")

# 2. TOR #26 Yangervis Solarte (X - X - X)
t9.new_ab()
t9.pitch_list("b c f b b f c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #44 Brandon Workman
game.winning_pitcher(44)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TOR
# LP: TOR #6 Marcus Stroman
game.losing_pitcher(6, is_away_team=True)

# print(game)
game.generate_scorecard()
