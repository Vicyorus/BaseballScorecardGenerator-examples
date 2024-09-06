import os
from baseball_scorecard.baseball_scorecard import Scorecard

# KCR @ BOS, 2018-05-02
# https://www.baseball-reference.com/boxes/BOS/BOS201805020.shtml
# https://www.mlb.com/gameday/royals-vs-red-sox/2018/05/02/529860/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-02 13:05-15:50",
        "at": "Fenway Park, Boston, MA",
        "att": "32,267",
        "temp": "86F, Sunny",
        "wind": "14mph, Out To CF",
        "away": {
            "team": "Kansas City Royals",
            "starter": 41,
            "roster": {
                # Lineup
                15: "Whit Merrifield",
                12: "Jorge Soler",
                8: "Mike Moustakas",
                13: "Salvador Perez",
                19: "Cheslor Cuthbert",
                25: "Jon Jay",
                2: "Alcides Escobar",
                4: "Alex Gordon",
                9: "Drew Butera",
                # Starting pitcher
                41: "Danny Duffy",
                # Bench
                1: "Ryan Goins",
                21: "Lucas Duda",
                45: "Abraham Almonte",
                # Bullpen
                31: "Ian Kennedy",
                58: "Scott Barlow",
                61: "Kevin McCarthy",
                53: "Eric Skoglund",
                64: "Burch Smith",
                33: "Brian Flynn",
                54: "Tim Hill",
                39: "Jason Hammel",
                51: "Blaine Boyer",
                40: "Kelvin Herrera",
                65: "Jakob Junis",
                56: "Brad Keller",
            },
            "lefties": [41, 53, 33, 54],
            "lineup": [
                [15, "4"],
                [12, "9"],
                [8, "5"],
                [13, "0"],
                [19, "3"],
                [25, "7"],
                [2, "6"],
                [4, "8"],
                [9, "2"],
            ],
            "bench": [
                [1, "2B"],
                [21, "1B"],
                [45, "OF"],
            ],
            "bullpen": [31, 58, 61, 53, 64, 33, 54, 39, 51, 40, 65, 56],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                5: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [39, 22, 41, 61, 37, 24, 46, 76, 64, 56, 32],
        },
        "umpires": {
            "HP": "Brian O'Nora",
            "1B": "Fieldin Culbreth",
            "2B": "CB Bucknor",
            "3B": "Chris Conroy",
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
# Pitching: BOS #31 Drew Pomeranz
t1 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b b")
t1.reach("BB")
t1.advance(3, "12 2B")
t1.advance(4, "13 SFDP8-4-6")

# 2. KCR #12 Jorge Soler (X - X - 15)
t1.new_ab()
t1.pitch_list("b b f")
t1.hit(2)
t1.thrown_out(2, "13 SFDP8-4-6", 3, 31)

# 3. KCR #8  Mike Moustakas (15 - 12 - X)
t1.new_ab()
t1.pitch_list("b c f b f c")
t1.out("!K")

# 4. KCR #13 Salvador Perez (15 - 12 - X)
t1.new_ab()
t1.pitch_list("d b")
t1.out("SFDP8-4-6", rbis=1)


# Bot 1st
# Pitching: KCR #41 Danny Duffy
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)
b1.thrown_out(2, "13 DP6-4-3", 2, 41)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("1 c b f b b s")
b1.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
b1.new_ab()
b1.pitch_list("c s 1")
b1.out("DP6-4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Drew Pomeranz
t2 = game.new_inning()

# 5. KCR #19 Cheslor Cuthbert (X - X - X)
t2.new_ab()
t2.pitch_list("c b f f b f s")
t2.out("K")

# 6. KCR #25 Jon Jay (X - X - X)
t2.new_ab()
t2.pitch_list("s")
t2.hit(1)
t2.thrown_out(2, "2 FC3-6", 2, 31)

# 7. KCR #2  Alcides Escobar (X - X - 25)
t2.new_ab()
t2.pitch_list("s b t f")
t2.reach("FC3-6")
t2.advance(2, "4 1B")
t2.advance(4, "9 2B")

# 8. KCR #4  Alex Gordon (X - X - 2)
t2.new_ab()
t2.hit(1)
t2.advance(4, "9 2B")

# 9. KCR #9  Drew Butera (X - 2 - 4)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(2, rbis=2)

# 1. KCR #15 Whit Merrifield (X - 9 - X)
t2.new_ab()
t2.pitch_list("b f b d f")
t2.out("G4-3")


# Bot 2nd
# Pitching: KCR #41 Danny Duffy
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("b s b")
b2.out("P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Drew Pomeranz
t3 = game.new_inning()

# 2. KCR #12 Jorge Soler (X - X - X)
t3.new_ab()
t3.hit(2)
t3.advance(3, "8 1B")

# 3. KCR #8  Mike Moustakas (X - 12 - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.advance(2, "19 BB")

# 4. KCR #13 Salvador Perez (12 - X - 8)
t3.new_ab()
t3.out("F7")

# 5. KCR #19 Cheslor Cuthbert (12 - X - 8)
t3.new_ab()
t3.pitch_list("b b d b")
t3.reach("BB")
t3.thrown_out(2, "25 DP4-6-3", 2, 31)

# 6. KCR #25 Jon Jay (12 - 8 - 19)
t3.new_ab()
t3.out("DP4-6-3")


# Bot 3rd
# Pitching: KCR #41 Danny Duffy
b3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("b f f f")
b3.out("(F)P2")

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Drew Pomeranz
t4 = game.new_inning()

# 7. KCR #2  Alcides Escobar (X - X - X)
t4.new_ab()
t4.pitch_list("b s f b")
t4.hit(1)
t4.thrown_out(2, "15 FC5-4", 3, 31)

# 8. KCR #4  Alex Gordon (X - X - 2)
t4.new_ab()
t4.pitch_list("1 c t")
t4.out("F8")

# 9. KCR #9  Drew Butera (X - X - 2)
t4.new_ab()
t4.out("F7")

# 1. KCR #15 Whit Merrifield (X - X - 2)
t4.new_ab()
t4.pitch_list("b b c f")
t4.reach("FC5-4")


# Bot 4th
# Pitching: KCR #41 Danny Duffy
b4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(4, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("s f s")
b4.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.pitch_list("c b b f b b")
b4.reach("BB")
b4.advance(4, "28 HR")

# 4. BOS #28 J.D. Martinez (X - X - 13)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(4, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b b c")
b4.hit(1)
b4.advance(2, "11 1B")

# 6. BOS #11 Rafael Devers (X - X - 2)
b4.new_ab()
b4.hit(1)

# 7. BOS #36 Eduardo Núñez (X - 2 - 11)
b4.new_ab()
b4.out("L8")

# 8. BOS #3  Sandy León (X - 2 - 11)
b4.new_ab()
b4.pitch_list("d c f f f")
b4.out("G5-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #31 Drew Pomeranz
t5 = game.new_inning()

# 2. KCR #12 Jorge Soler (X - X - X)
t5.new_ab()
t5.pitch_list("b b")
t5.out("F9")

# 3. KCR #8  Mike Moustakas (X - X - X)
t5.new_ab()
t5.pitch_list("b b f b c f f")
t5.out("F7")

# 4. KCR #13 Salvador Perez (X - X - X)
t5.new_ab()
t5.pitch_list("b s b f")
t5.out("G5-3")


# Bot 5th
# Pitching: KCR #41 Danny Duffy
b5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b f s")
b5.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.hit(4, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("b b b")
b5.out("F9")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b")
b5.hit(2)
b5.advance(3, "28 1B")

# 4. BOS #28 J.D. Martinez (X - 13 - X)
b5.new_ab()
b5.pitch_list("s s b f d b")
b5.hit(1)

# 5. BOS #2  Xander Bogaerts (13 - X - 28)
b5.new_ab()
b5.pitch_list("f 1 b b")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #31 Drew Pomeranz
t6 = game.new_inning()

# 5. KCR #19 Cheslor Cuthbert (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.thrown_out(2, "25 DP4-6-3", 1, 31)

# 6. KCR #25 Jon Jay (X - X - 19)
t6.new_ab()
t6.out("DP4-6-3")

# 7. KCR #2  Alcides Escobar (X - X - X)
t6.new_ab()
t6.pitch_list("b f b f c")
t6.out("!K")


# Bot 6th
# Pitching: KCR #41 Danny Duffy
b6 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.out("P6")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(1, "3 PO", 2, 41)

# 8. BOS #3  Sandy León (X - X - 36)
b6.new_ab()
b6.pitch_list("b b 1 s t b f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #31 Drew Pomeranz
t7.pitching_substitution(56)

# 8. KCR #4  Alex Gordon (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(1)
t7.thrown_out(2, "12 FC5-4", 3, 56)

# 9. KCR #9  Drew Butera (X - X - 4)
t7.new_ab()
t7.pitch_list("d 1 c s f c")
t7.out("!K")

# 1. KCR #15 Whit Merrifield (X - X - 4)
t7.new_ab()
t7.pitch_list("c d f f f b s")
t7.out("K")

# 2. KCR #12 Jorge Soler (X - X - 4)
t7.new_ab()
t7.reach("FC5-4")


# Bot 7th
# Pitching: KCR #41 Danny Duffy
b7 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b b f c s")
b7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c s b")
b7.hit(4, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c c f f b b s")
b7.out("K")

# Pitching change (KCR): #56 Brad Keller replaces #41 Danny Duffy
b7.pitching_substitution(56)

# 3. BOS #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("b s b")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t8.pitching_substitution(32)

# 3. KCR #8  Mike Moustakas (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.out("G6-3")

# 4. KCR #13 Salvador Perez (X - X - X)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K2-3")

# 5. KCR #19 Cheslor Cuthbert (X - X - X)
t8.new_ab()
t8.hit(4, rbis=1)

# 6. KCR #25 Jon Jay (X - X - X)
t8.new_ab()
t8.pitch_list("f b c f f")
t8.reach("HBP")

# 7. KCR #2  Alcides Escobar (X - X - 25)
t8.new_ab()
t8.pitch_list("c b 1 s s")
t8.out("K2-3")


# Bot 8th
# Pitching: KCR #56 Brad Keller
b8 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b b s f f")
b8.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G1-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("s b b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# 8. KCR #4  Alex Gordon (X - X - X)
t9.new_ab()
t9.pitch_list("b c f b c")
t9.out("!K")

# Offensive change (KCR): Pinch-hitter #21 Lucas Duda replaces #9 Drew Butera, batting 9th
t9.offensive_substitution(9, 21, "PH")

# 9. KCR #21 Lucas Duda (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b f b f s")
t9.out("K")

# 1. KCR #15 Whit Merrifield (X - X - X)
t9.new_ab()
t9.pitch_list("c c b s")
t9.out("K")

# Winning team: BOS
# WP: BOS #31 Drew Pomeranz
game.winning_pitcher(31)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: KCR
# LP: KCR #41 Danny Duffy
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
