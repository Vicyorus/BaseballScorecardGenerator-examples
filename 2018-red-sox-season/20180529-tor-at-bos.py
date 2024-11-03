import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TOR @ BOS, 2018-05-29
# https://www.baseball-reference.com/boxes/BOS/BOS201805290.shtml
# https://www.mlb.com/gameday/blue-jays-vs-red-sox/2018/05/29/530227/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-29 19:15-22:14",
        "at": "Fenway Park, Boston, MA",
        "att": "33,380",
        "temp": "74F, Clear",
        "wind": "6mph, In From RF",
        "away": {
            "team": "Toronto Blue Jays",
            "starter": 25,
            "roster": {
                # Lineup
                18: "Curtis Granderson",
                11: "Kevin Pillar",
                26: "Yangervis Solarte",
                14: "Justin Smoak",
                37: "Teoscar Hernández",
                55: "Russell Martin",
                8: "Kendrys Morales",
                29: "Devon Travis",
                21: "Luke Maile",
                # Starting pitcher
                25: "Marco Estrada",
                # Bench
                27: "Dwight Smith Jr.",
                3: "Gio Urshela",
                # Bullpen
                43: "Sam Gaviglio",
                41: "Aaron Sanchez",
                62: "Aaron Loup",
                36: "Tyler Clippard",
                22: "Seunghwan Oh",
                57: "Jaime García",
                31: "Joe Biagini",
                24: "Danny Barnes",
                39: "Jake Petricka",
                77: "John Axford",
                52: "Ryan Tepera",
                33: "J.A. Happ",
            },
            "lefties": [62, 57, 33],
            "lineup": [
                [18, "7"],
                [11, "8"],
                [26, "6"],
                [14, "3"],
                [37, "9"],
                [55, "5"],
                [8, "0"],
                [29, "4"],
                [21, "2"],
            ],
            "bench": [
                [27, "LF"],
                [3, "3B"],
            ],
            "bullpen": [43, 41, 62, 36, 22, 57, 31, 24, 39, 77, 52, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                15: "Dustin Pedroia",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                41: "Chris Sale",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [57, 24, 41, 31, 61],
            "lineup": [
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [28, "0"],
                [11, "5"],
                [15, "4"],
                [12, "9"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 24, 46, 76, 41, 56, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Jerry Layne",
            "2B": "Jansen Visconti",
            "3B": "Jordan Baker",
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
t1.pitch_list("c b b b b")
t1.reach("BB")
t1.thrown_out(2, "11 2-4", 1, 22)

# 2. TOR #11 Kevin Pillar (X - X - 18)
t1.new_ab()
t1.pitch_list("s f d f d f f b s")
t1.out("K")

# 3. TOR #26 Yangervis Solarte (X - X - X)
t1.new_ab()
t1.pitch_list("f b")
t1.out("F9")


# Bot 1st
# Pitching: TOR #25 Marco Estrada
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("f b b")
b1.out("L7")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(4, "18 2B")

# 3. BOS #18 Mitch Moreland (X - X - 2)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(2, rbis=1)
b1.advance(4, "28 2B")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
b1.new_ab(is_risp=True)
b1.hit(2, rbis=1)

# 5. BOS #11 Rafael Devers (X - 28 - X)
b1.new_ab(is_risp=True)
b1.out("F8")

# 6. BOS #15 Dustin Pedroia (X - 28 - X)
b1.new_ab(is_risp=True)
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. TOR #14 Justin Smoak (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.out("G3")

# 5. TOR #37 Teoscar Hernández (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("(F)P3")

# 6. TOR #55 Russell Martin (X - X - X)
t2.new_ab()
t2.hit(1)
t2.advance(3, "8 1B")

# 7. TOR #8  Kendrys Morales (X - X - 55)
t2.new_ab()
t2.pitch_list("c c b 1")
t2.hit(1)
t2.thrown_out(2, "29 FC5-4", 3, 22)

# 8. TOR #29 Devon Travis (55 - X - 8)
t2.new_ab(is_risp=True)
t2.pitch_list("f")
t2.reach("FC5-4")


# Bot 2nd
# Pitching: TOR #25 Marco Estrada
b2 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c b")
b2.out("G4-3")

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(2)
b2.advance(4, "16 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 3 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("F7")

# 1. BOS #16 Andrew Benintendi (X - 3 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(2, rbis=1)
b2.advance(3, "2 WP")

# 2. BOS #2  Xander Bogaerts (X - 16 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c d c f b b")
b2.wp()
b2.out("P4")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 9. TOR #21 Luke Maile (X - X - X)
t3.new_ab()
t3.pitch_list("c f b c")
t3.out("!K")

# 1. TOR #18 Curtis Granderson (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("L4")

# 2. TOR #11 Kevin Pillar (X - X - X)
t3.new_ab()
t3.pitch_list("c f b")
t3.out("(F)P3")


# Bot 3rd
# Pitching: TOR #25 Marco Estrada
b3 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("F8")

# 4. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("s s b")
b3.out("F8")

# 5. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("b f b f b t")
b3.out("KT")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
t4.new_ab()
t4.out("F7")

# 4. TOR #14 Justin Smoak (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b f")
t4.hit(4)

# 5. TOR #37 Teoscar Hernández (X - X - X)
t4.new_ab()
t4.pitch_list("b f f")
t4.out("G6-3")

# 6. TOR #55 Russell Martin (X - X - X)
t4.new_ab()
t4.out("G6-3")


# Bot 4th
# Pitching: TOR #25 Marco Estrada
b4 = game.new_inning()

# 6. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f f")
b4.out("G6-3")

# 7. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.hit(1)
b4.advance(2, "3 SB")
b4.advance(3, "3 G3")
b4.advance(4, "19 1B")

# 8. BOS #3  Sandy León (X - X - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("d s 2 f f b")
b4.out("G3")

# 9. BOS #19 Jackie Bradley Jr. (12 - X - X)
b4.new_ab(is_risp=True)
b4.hit(1, rbis=1)

# Pitching change (TOR): #62 Aaron Loup replaces #25 Marco Estrada
b4.pitching_substitution(62)

# 1. BOS #16 Andrew Benintendi (X - X - 19)
b4.new_ab()
b4.pitch_list("f c")
b4.out("G3-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 7. TOR #8  Kendrys Morales (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G3")

# 8. TOR #29 Devon Travis (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G6-3")

# 9. TOR #21 Luke Maile (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("L7")


# Bot 5th
# Pitching: TOR #62 Aaron Loup
b5 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("c f f b f b b f b")
b5.reach("BB")
b5.thrown_out(2, "18 DP1-6-3", 1, 62)

# 3. BOS #18 Mitch Moreland (X - X - 2)
b5.new_ab()
b5.pitch_list("b f")
b5.out("DP1-6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b s b s b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 1. TOR #18 Curtis Granderson (X - X - X)
t6.new_ab()
t6.pitch_list("c c b f")
t6.out("G5-3")

# 2. TOR #11 Kevin Pillar (X - X - X)
t6.new_ab()
t6.pitch_list("f b f f s")
t6.out("K")

# 3. TOR #26 Yangervis Solarte (X - X - X)
t6.new_ab()
t6.reach("HBP")

# 4. TOR #14 Justin Smoak (X - X - 26)
t6.new_ab()
t6.pitch_list("c b f d f s")
t6.out("K")


# Bot 6th
# Pitching: TOR #31 Joe Biagini
b6 = game.new_inning()

# Pitching change (TOR): #31 Joe Biagini replaces #62 Aaron Loup
b6.pitching_substitution(31)

# 5. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)
b6.advance(3, "15 1B")
b6.advance(4, "3 2B")

# 6. BOS #15 Dustin Pedroia (X - X - 11)
b6.new_ab()
b6.pitch_list("c f")
b6.hit(1)
b6.advance(3, "3 2B")

# 7. BOS #12 Brock Holt (11 - X - 15)
b6.new_ab(is_risp=True)
b6.pitch_list("c c f f f c")
b6.out("!K")

# 8. BOS #3  Sandy León (11 - X - 15)
b6.new_ab(is_risp=True)
b6.pitch_list("d")
b6.hit(2, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (15 - 3 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b s d d b")
b6.reach("BB")
b6.thrown_out(2, "16 DP4-6-3", 2, 31)

# 1. BOS #16 Andrew Benintendi (15 - 3 - 19)
b6.new_ab(is_risp=True)
b6.pitch_list("f b c f d f")
b6.out("DP4-6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Rick Porcello
t7 = game.new_inning()

# 5. TOR #37 Teoscar Hernández (X - X - X)
t7.new_ab()
t7.pitch_list("c s")
t7.out("F8")

# 6. TOR #55 Russell Martin (X - X - X)
t7.new_ab()
t7.reach("HBP")
t7.advance(2, "8 BB")
t7.advance(3, "29 1B")
t7.advance(4, "18 1B")

# 7. TOR #8  Kendrys Morales (X - X - 55)
t7.new_ab()
t7.pitch_list("b b c f b b")
t7.reach("BB")
t7.advance(2, "29 1B")
t7.error(1)
t7.advance(3, "18 1B")
t7.advance("U", "18 E1")

# 8. TOR #29 Devon Travis (X - 55 - 8)
t7.new_ab(is_risp=True)
t7.hit(1)
t7.advance(3, "18 E1")

# 9. TOR #21 Luke Maile (55 - 8 - 29)
t7.new_ab(is_risp=True)
t7.pitch_list("b s f b s")
t7.out("K")

# 1. TOR #18 Curtis Granderson (55 - 8 - 29)
t7.new_ab(is_risp=True)
t7.pitch_list("b c d f")
t7.hit(1, rbis=1)
t7.advance(2, "E1")

# Pitching change (BOS): #56 Joe Kelly replaces #22 Rick Porcello
t7.pitching_substitution(56)

# 2. TOR #11 Kevin Pillar (29 - 18 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("f c s")
t7.out("K")


# Bot 7th
# Pitching: TOR #31 Joe Biagini
b7 = game.new_inning()

# 2. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(4)

# Pitching change (TOR): #36 Tyler Clippard replaces #31 Joe Biagini
b7.pitching_substitution(36)

# 3. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("f f f")
b7.hit(2)

# 5. BOS #11 Rafael Devers (X - 28 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("d b")
b7.out("F8")

# 6. BOS #15 Dustin Pedroia (X - 28 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# 3. TOR #26 Yangervis Solarte (X - X - X)
t8.new_ab()
t8.pitch_list("b f s b")
t8.out("P5")

# 4. TOR #14 Justin Smoak (X - X - X)
t8.new_ab()
t8.pitch_list("b c b")
t8.out("G6-3")

# 5. TOR #37 Teoscar Hernández (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.reach("HBP")

# 6. TOR #55 Russell Martin (X - X - 37)
t8.new_ab()
t8.pitch_list("b c s b b")
t8.out("P4")


# Bot 8th
# Pitching: TOR #24 Danny Barnes
b8 = game.new_inning()

# Pitching change (TOR): #24 Danny Barnes replaces #36 Tyler Clippard
b8.pitching_substitution(24)

# 7. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.reach("HBP")
b8.advance(4, "3 HR")

# 8. BOS #3  Sandy León (X - X - 12)
b8.new_ab()
b8.pitch_list("1 c 1 b f b 1 f f f f 1")
b8.hit(4, rbis=2)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("F8")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.out("F8")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #56 Joe Kelly
t9.pitching_substitution(76)

# 7. TOR #8  Kendrys Morales (X - X - X)
t9.new_ab()
t9.pitch_list("c s b")
t9.hit(2)
t9.advance(3, "27 1B")

# 8. TOR #29 Devon Travis (X - 8 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c")
t9.hit(1)
t9.advance(2, "27 1B")

# Offensive change (TOR): Pinch-hitter #27 Dwight Smith Jr. replaces #21 Luke Maile, batting 9th
t9.offensive_substitution(9, 27, "PH")

# 9. TOR #27 Dwight Smith Jr. (X - 8 - 29)
t9.new_ab(is_risp=True)
t9.hit(1)
t9.thrown_out(2, "26 FC5-4", 3, 46)

# 1. TOR #18 Curtis Granderson (8 - 29 - 27)
t9.new_ab(is_risp=True)
t9.pitch_list("c f d")
t9.out("F7")

# Pitching change (BOS): #46 Craig Kimbrel replaces #76 Hector Velázquez
t9.pitching_substitution(46)

# 2. TOR #11 Kevin Pillar (8 - 29 - 27)
t9.new_ab(is_risp=True)
t9.pitch_list("s f f f b b t")
t9.out("KT")

# 3. TOR #26 Yangervis Solarte (8 - 29 - 27)
t9.new_ab(is_risp=True)
t9.pitch_list("s f b")
t9.reach("FC5-4")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TOR
# LP: TOR #25 Marco Estrada
game.losing_pitcher(25, is_away_team=True)

# print(game)
game.generate_scorecard()
