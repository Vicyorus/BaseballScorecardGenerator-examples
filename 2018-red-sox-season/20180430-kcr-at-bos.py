import os
from baseball_scorecard.baseball_scorecard import Scorecard

# KCR @ BOS, 2018-04-30
# https://www.baseball-reference.com/boxes/BOS/BOS201804300.shtml
# https://www.mlb.com/gameday/royals-vs-red-sox/2018/04/30/529831/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-30 19:10-22:23",
        "at": "Fenway Park, Boston, MA",
        "att": "31,314",
        "temp": "45F, Cloudy",
        "wind": "5mph, R To L",
        "away": {
            "team": "Kansas City Royals",
            "starter": 39,
            "roster": {
                # Lineup
                15: "Whit Merrifield",
                12: "Jorge Soler",
                8: "Mike Moustakas",
                13: "Salvador Perez",
                19: "Cheslor Cuthbert",
                21: "Lucas Duda",
                25: "Jon Jay",
                4: "Alex Gordon",
                2: "Alcides Escobar",
                # Starting pitcher
                39: "Jason Hammel",
                # Bench
                1: "Ryan Goins",
                9: "Drew Butera",
                45: "Abraham Almonte",
                # Bullpen
                31: "Ian Kennedy",
                58: "Scott Barlow",
                41: "Danny Duffy",
                61: "Kevin McCarthy",
                53: "Eric Skoglund",
                64: "Burch Smith",
                33: "Brian Flynn",
                54: "Tim Hill",
                51: "Blaine Boyer",
                40: "Kelvin Herrera",
                65: "Jakob Junis",
                56: "Brad Keller",
            },
            "lefties": [41, 53, 33, 54],
            "lineup": [
                [15, "4"],
                [12, "9"],
                [8, "0"],
                [13, "2"],
                [19, "5"],
                [21, "3"],
                [25, "8"],
                [4, "7"],
                [2, "6"],
            ],
            "bench": [
                [1, "2B"],
                [9, "C"],
                [45, "OF"],
            ],
            "bullpen": [31, 58, 41, 61, 53, 64, 33, 54, 51, 40, 65, 56],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                5: "Tzu-Wei Lin",
                23: "Blake Swihart",
                50: "Mookie Betts",
                3: "Sandy León",
                # Bullpen
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [57, 24, 41, 31, 61],
            "lineup": [
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "9"],
                [7, "2"],
            ],
            "bench": [
                [5, "OF"],
                [23, "C"],
                [50, "SS"],
                [3, "C"],
            ],
            "bullpen": [24, 46, 76, 39, 22, 41, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "CB Bucknor",
            "1B": "Chris Conroy",
            "2B": "Brian O'Nora",
            "3B": "Fieldin Culbreth",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
t1.new_ab()
t1.pitch_list("c f f b f")
t1.hit(1)
t1.advance(2, "12 BB")
t1.advance(3, "8 HBP")
t1.advance(4, "13 BB")

# 2. KCR #12 Jorge Soler (X - X - 15)
t1.new_ab()
t1.pitch_list("t t b f f b f b f b")
t1.reach("BB")
t1.advance(2, "8 HBP")
t1.advance(3, "13 BB")
t1.advance(4, "21 BB")

# 3. KCR #8  Mike Moustakas (X - 15 - 12)
t1.new_ab(is_risp=True)
t1.reach("HBP")
t1.advance(2, "13 BB")
t1.advance(3, "21 BB")
t1.advance(4, "25 1B")

# 4. KCR #13 Salvador Perez (15 - 12 - 8)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b b")
t1.reach("BB", rbis=1)
t1.advance(2, "21 BB")
t1.advance(3, "25 1B")

# 5. KCR #19 Cheslor Cuthbert (12 - 8 - 13)
t1.new_ab(is_risp=True)
t1.pitch_list("c f b s")
t1.out("K")

# 6. KCR #21 Lucas Duda (12 - 8 - 13)
t1.new_ab(is_risp=True)
t1.pitch_list("c f b b b b")
t1.reach("BB", rbis=1)
t1.advance(2, "25 1B")

# 7. KCR #25 Jon Jay (8 - 13 - 21)
t1.new_ab(is_risp=True)
t1.pitch_list("c c")
t1.hit(1, rbis=1)
t1.thrown_out(2, "4 DP4-6-3", 2, 57)

# 8. KCR #4  Alex Gordon (13 - 21 - 25)
t1.new_ab(is_risp=True)
t1.out("DP4-6-3")


# Bot 1st
# Pitching: KCR #39 Jason Hammel
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b f")
b1.out("L8")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.out("F9")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b b f")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 9. KCR #2  Alcides Escobar (X - X - X)
t2.new_ab()
t2.out("F8")

# 1. KCR #15 Whit Merrifield (X - X - X)
t2.new_ab()
t2.pitch_list("c t s")
t2.out("K")

# 2. KCR #12 Jorge Soler (X - X - X)
t2.new_ab()
t2.hit(1)

# Offensive change (KCR): Pinch-hitter #45 Abraham Almonte replaces #8 Mike Moustakas, batting 3rd
t2.offensive_substitution(3, 45, "PH")

# 3. KCR #45 Abraham Almonte (X - X - 12)
t2.new_ab()
t2.pitch_list("b s c b")
t2.out("F9")


# Bot 2nd
# Pitching: KCR #39 Jason Hammel
b2 = game.new_inning()

# Defensive switch (KCR): #45 Abraham Almonte moves to DH
b2.defensive_switch(45, "0")

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b s")
b2.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.out("F8")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b f b")
b2.out("G1-5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 4. KCR #13 Salvador Perez (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b f f s")
t3.out("K")

# 5. KCR #19 Cheslor Cuthbert (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("F8")

# 6. KCR #21 Lucas Duda (X - X - X)
t3.new_ab()
t3.pitch_list("f b f b")
t3.out("F7")


# Bot 3rd
# Pitching: KCR #39 Jason Hammel
b3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b f b s f")
b3.out("G3")

# 9. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G6-3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("f b f")
b3.hit(1)
b3.advance(3, "13 2B")
b3.advance(4, "18 BB")

# 2. BOS #13 Hanley Ramirez (X - X - 16)
b3.new_ab()
b3.pitch_list("1 1 b")
b3.hit(2)
b3.advance(3, "18 BB")
b3.advance(4, "2 HR")

# 3. BOS #28 J.D. Martinez (16 - 13 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f b f d d d")
b3.reach("BB")
b3.advance(2, "18 BB")
b3.advance(4, "2 HR")

# 4. BOS #18 Mitch Moreland (16 - 13 - 28)
b3.new_ab(is_risp=True)
b3.pitch_list("c s d b d f f b")
b3.reach("BB", rbis=1)
b3.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (13 - 28 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("b c c b f d f")
b3.hit(4, rbis=4)

# 6. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("f b b s b f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 7. KCR #25 Jon Jay (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b t")
t4.out("KT")

# 8. KCR #4  Alex Gordon (X - X - X)
t4.new_ab()
t4.pitch_list("c b s")
t4.reach("HBP")
t4.advance(4, "2 2B")

# 9. KCR #2  Alcides Escobar (X - X - 4)
t4.new_ab()
t4.pitch_list("b c f")
t4.hit(2, rbis=1)
t4.advance(4, "15 2B")

# 1. KCR #15 Whit Merrifield (X - 2 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b f b")
t4.hit(2, rbis=1)

# 2. KCR #12 Jorge Soler (X - 15 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b s t b b s")
t4.out("K")

# 3. KCR #45 Abraham Almonte (X - 15 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("t t b d s")
t4.out("K")


# Bot 4th
# Pitching: KCR #39 Jason Hammel
b4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("P4")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("f b b b b")
b4.reach("BB")
b4.advance(3, "7 1B")
b4.advance(4, "16 SF8")

# 9. BOS #7  Christian Vázquez (X - X - 19)
b4.new_ab()
b4.pitch_list("c d f b")
b4.hit(1)

# 1. BOS #16 Andrew Benintendi (19 - X - 7)
b4.new_ab(is_risp=True)
b4.pitch_list("b d")
b4.out("SF8", rbis=1)

# 2. BOS #13 Hanley Ramirez (X - X - 7)
b4.new_ab()
b4.pitch_list("b")
b4.out("G1-6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #76 Hector Velázquez
t5 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #57 Eduardo Rodriguez
t5.pitching_substitution(76)

# 4. KCR #13 Salvador Perez (X - X - X)
t5.new_ab()
t5.pitch_list("s b")
t5.out("F9")

# 5. KCR #19 Cheslor Cuthbert (X - X - X)
t5.new_ab()
t5.out("G6-3")

# 6. KCR #21 Lucas Duda (X - X - X)
t5.new_ab()
t5.pitch_list("c b b t f f s")
t5.out("K")


# Bot 5th
# Pitching: KCR #39 Jason Hammel
b5 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("b f t")
b5.hit(2)
b5.advance(3, "2 1B")
b5.advance(4, "36 1B")

# 4. BOS #18 Mitch Moreland (X - 28 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f")
b5.out("F8")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c s b")
b5.hit(1)
b5.advance(3, "36 1B")

# 6. BOS #11 Rafael Devers (28 - X - 2)
b5.new_ab(is_risp=True)
b5.pitch_list("c s b s")
b5.out("K")

# 7. BOS #36 Eduardo Núñez (28 - X - 2)
b5.new_ab(is_risp=True)
b5.pitch_list("c b f")
b5.hit(1, rbis=1)

# Pitching change (KCR): #54 Tim Hill replaces #39 Jason Hammel
b5.pitching_substitution(54)

# 8. BOS #19 Jackie Bradley Jr. (2 - X - 36)
b5.new_ab(is_risp=True)
b5.pitch_list("f b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #76 Hector Velázquez
t6 = game.new_inning()

# 7. KCR #25 Jon Jay (X - X - X)
t6.new_ab()
t6.pitch_list("c f f f s")
t6.out("K")

# 8. KCR #4  Alex Gordon (X - X - X)
t6.new_ab()
t6.pitch_list("b b c c s")
t6.out("K")

# 9. KCR #2  Alcides Escobar (X - X - X)
t6.new_ab()
t6.hit(1)
t6.thrown_out(2, "15 FC5-4", 3, 76)

# 1. KCR #15 Whit Merrifield (X - X - 2)
t6.new_ab()
t6.pitch_list("c")
t6.reach("FC5-4")


# Bot 6th
# Pitching: KCR #58 Scott Barlow
b6 = game.new_inning()

# Pitching change (KCR): #58 Scott Barlow replaces #54 Tim Hill
b6.pitching_substitution(58)

# 9. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("c s c")
b6.out("!K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.out("F7")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b6.new_ab()
b6.pitch_list("s f")
b6.hit(1)
b6.thrown_out(2, "28 FC6-4", 3, 58)

# 3. BOS #28 J.D. Martinez (X - X - 13)
b6.new_ab()
b6.pitch_list("c b s")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #39 Carson Smith
t7 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #76 Hector Velázquez
t7.pitching_substitution(39)

# 2. KCR #12 Jorge Soler (X - X - X)
t7.new_ab()
t7.pitch_list("c b c b")
t7.out("F8")

# 3. KCR #45 Abraham Almonte (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c c c")
t7.out("!K")

# 4. KCR #13 Salvador Perez (X - X - X)
t7.new_ab()
t7.pitch_list("c f")
t7.hit(1)

# 5. KCR #19 Cheslor Cuthbert (X - X - 13)
t7.new_ab()
t7.pitch_list("d c s b f s")
t7.out("K")


# Bot 7th
# Pitching: KCR #58 Scott Barlow
b7 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("b b f b")
b7.hit(2)
b7.advance(3, "2 1B")
b7.advance(4, "11 FC3-6")

# 5. BOS #2  Xander Bogaerts (X - 18 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c f")
b7.hit(1)
b7.thrown_out(2, "11 FC3-6", 1, 58)

# 6. BOS #11 Rafael Devers (18 - X - 2)
b7.new_ab(is_risp=True)
b7.pitch_list("b s f")
b7.reach("FC3-6", rbis=1)
b7.advance(2, "36 G2-3")
b7.advance("U", "19 E5")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
b7.new_ab()
b7.pitch_list("c")
b7.out("G2-3")

# 8. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f")
b7.error(5)
b7.reach("E5")

# 9. BOS #7  Christian Vázquez (X - X - 19)
b7.new_ab()
b7.pitch_list("1 c b 1 b b")
b7.out("L5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #61 Brian Johnson
t8 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #39 Carson Smith
t8.pitching_substitution(61)

# 6. KCR #21 Lucas Duda (X - X - X)
t8.new_ab()
t8.pitch_list("c b b b")
t8.out("P4")

# 7. KCR #25 Jon Jay (X - X - X)
t8.new_ab()
t8.pitch_list("f b")
t8.out("L7")

# 8. KCR #4  Alex Gordon (X - X - X)
t8.new_ab()
t8.pitch_list("c c f b f f c")
t8.out("!K")


# Bot 8th
# Pitching: KCR #58 Scott Barlow
b8 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("c b f")
b8.out("F7")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(3, "18 1B")

# 4. BOS #18 Mitch Moreland (X - X - 28)
b8.new_ab()
b8.hit(1)

# 5. BOS #2  Xander Bogaerts (28 - X - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b c c")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# 9. KCR #2  Alcides Escobar (X - X - X)
t9.new_ab()
t9.pitch_list("b b")
t9.hit(2)
t9.advance(4, "15 2B")

# 1. KCR #15 Whit Merrifield (X - 2 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.hit(2, rbis=1)

# 2. KCR #12 Jorge Soler (X - 15 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c b")
t9.out("F8")

# 3. KCR #45 Abraham Almonte (X - 15 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("s")
t9.out("L8")

# 4. KCR #13 Salvador Perez (X - 15 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c s f b f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76)

# Loser team: KCR
# LP: KCR #39 Jason Hammel
game.losing_pitcher(39, is_away_team=True)

# print(game)
game.generate_scorecard()
