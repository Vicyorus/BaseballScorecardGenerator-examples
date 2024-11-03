import os
from baseball_scorecard.baseball_scorecard import Scorecard

# KCR @ BOS, 2018-05-01
# https://www.baseball-reference.com/boxes/BOS/BOS201805010.shtml
# https://www.mlb.com/gameday/royals-vs-red-sox/2018/05/01/529845/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-01 19:10-23:35",
        "at": "Fenway Park, Boston, MA",
        "att": "34,466",
        "temp": "65F, Partly Cloudy",
        "wind": "7mph, L To R",
        "away": {
            "team": "Kansas City Royals",
            "starter": 65,
            "roster": {
                # Lineup
                15: "Whit Merrifield",
                12: "Jorge Soler",
                19: "Cheslor Cuthbert",
                13: "Salvador Perez",
                25: "Jon Jay",
                45: "Abraham Almonte",
                21: "Lucas Duda",
                2: "Alcides Escobar",
                4: "Alex Gordon",
                # Starting pitcher
                65: "Jakob Junis",
                # Bench
                1: "Ryan Goins",
                9: "Drew Butera",
                8: "Mike Moustakas",
                # Bullpen
                31: "Ian Kennedy",
                58: "Scott Barlow",
                41: "Danny Duffy",
                61: "Kevin McCarthy",
                53: "Eric Skoglund",
                64: "Burch Smith",
                33: "Brian Flynn",
                54: "Tim Hill",
                39: "Jason Hammel",
                51: "Blaine Boyer",
                40: "Kelvin Herrera",
                56: "Brad Keller",
            },
            "lefties": [41, 53, 33, 54],
            "lineup": [
                [15, "4"],
                [12, "0"],
                [19, "5"],
                [13, "2"],
                [25, "9"],
                [45, "8"],
                [21, "3"],
                [2, "6"],
                [4, "7"],
            ],
            "bench": [
                [1, "2B"],
                [9, "C"],
                [8, "1B"],
            ],
            "bullpen": [31, 58, 41, 61, 53, 64, 33, 54, 39, 51, 40, 56],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                50: "Mookie Betts",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                39: "Carson Smith",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [41, 57, 24, 31, 61],
            "lineup": [
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [19, "9"],
                [7, "2"],
                [5, "4"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [50, "SS"],
                [3, "C"],
            ],
            "bullpen": [57, 24, 46, 76, 39, 22, 31, 61, 32, 37],
        },
        "umpires": {
            "HP": "Chris Conroy",
            "1B": "Brian O'Nora",
            "2B": "Fieldin Culbreth",
            "3B": "CB Bucknor",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F8")

# 2. KCR #12 Jorge Soler (X - X - X)
t1.new_ab()
t1.hit(2)
t1.advance(3, "19 G5-3")

# 3. KCR #19 Cheslor Cuthbert (X - 12 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("G5-3")

# 4. KCR #13 Salvador Perez (12 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c b f f b s")
t1.out("K2-3")


# Bot 1st
# Pitching: KCR #65 Jakob Junis
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c s b")
b1.out("F7")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("G5-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(1)

# 4. BOS #18 Mitch Moreland (X - X - 28)
b1.new_ab()
b1.pitch_list("c f")
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 5. KCR #25 Jon Jay (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.thrown_out(2, "45 DP6-3", 1, 41)

# 6. KCR #45 Abraham Almonte (X - X - 25)
t2.new_ab()
t2.out("DP6-3")

# 7. KCR #21 Lucas Duda (X - X - X)
t2.new_ab()
t2.pitch_list("c c b")
t2.hit(1)

# 8. KCR #2  Alcides Escobar (X - X - 21)
t2.new_ab()
t2.pitch_list("f")
t2.out("G1-3")


# Bot 2nd
# Pitching: KCR #65 Jakob Junis
b2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b f c")
b2.out("!K")

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.hit(2)

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c b")
b2.out("F9")

# 8. BOS #7  Christian Vázquez (X - 11 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c s f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 9. KCR #4  Alex Gordon (X - X - X)
t3.new_ab()
t3.pitch_list("f f b f")
t3.out("G5-3")

# 1. KCR #15 Whit Merrifield (X - X - X)
t3.new_ab()
t3.pitch_list("s s")
t3.out("F8")

# 2. KCR #12 Jorge Soler (X - X - X)
t3.new_ab()
t3.pitch_list("b s")
t3.reach("HBP")
t3.thrown_out(2, "19 FC6-4", 3, 41)

# 3. KCR #19 Cheslor Cuthbert (X - X - 12)
t3.new_ab()
t3.pitch_list("s f")
t3.reach("FC6-4")


# Bot 3rd
# Pitching: KCR #65 Jakob Junis
b3 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b3.new_ab()
b3.pitch_list("f c b b")
b3.out("G3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("f b")
b3.hit(1)
b3.advance(2, "28 BB")
b3.advance(3, "18 1B")

# 2. BOS #13 Hanley Ramirez (X - X - 16)
b3.new_ab()
b3.out("(F)P3")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b3.new_ab()
b3.pitch_list("1 b c 1 b t f f b f f b")
b3.reach("BB")
b3.advance(2, "18 1B")

# 4. BOS #18 Mitch Moreland (X - 16 - 28)
b3.new_ab(is_risp=True)
b3.pitch_list("b c")
b3.hit(1)

# 5. BOS #2  Xander Bogaerts (16 - 28 - 18)
b3.new_ab(is_risp=True)
b3.pitch_list("s s b b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 4. KCR #13 Salvador Perez (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.error(5)
t4.reach("E5")
t4.advance(2, "45 BB")
t4.advance(3, "21 HBP")
t4.advance("U", "2 SF7")

# 5. KCR #25 Jon Jay (X - X - 13)
t4.new_ab()
t4.pitch_list("f s s")
t4.out("K")

# 6. KCR #45 Abraham Almonte (X - X - 13)
t4.new_ab()
t4.pitch_list("c d b s b b")
t4.reach("BB")
t4.advance(2, "21 HBP")
t4.error(2)
t4.advance(3, "2 E2")

# 7. KCR #21 Lucas Duda (X - 13 - 45)
t4.new_ab(is_risp=True)
t4.pitch_list("c")
t4.reach("HBP")
t4.advance(2, "2 E2")

# 8. KCR #2  Alcides Escobar (13 - 45 - 21)
t4.new_ab(is_risp=True)
t4.pitch_list("c t d")
t4.out("SF7", rbis=1)

# 9. KCR #4  Alex Gordon (45 - 21 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b c b")
t4.out("G6-3")


# Bot 4th
# Pitching: KCR #65 Jakob Junis
b4 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b b f f f b c")
b4.out("!K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b c f b t")
b4.out("KT")

# 8. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
t5.new_ab()
t5.pitch_list("c f s")
t5.out("K2-3")

# 2. KCR #12 Jorge Soler (X - X - X)
t5.new_ab()
t5.pitch_list("c s f b b c")
t5.out("!K")

# 3. KCR #19 Cheslor Cuthbert (X - X - X)
t5.new_ab()
t5.pitch_list("b s b s f b f f f b")
t5.reach("BB")

# 4. KCR #13 Salvador Perez (X - X - 19)
t5.new_ab()
t5.pitch_list("b")
t5.out("P6")


# Bot 5th
# Pitching: KCR #65 Jakob Junis
b5 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b5.new_ab()
b5.out("G3-1")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b f")
b5.out("F7")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b5.new_ab()
b5.pitch_list("b f b")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #41 Chris Sale
t6 = game.new_inning()

# 5. KCR #25 Jon Jay (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(2, "21 1B")
t6.advance(3, "2 FC6-4")
t6.advance(4, "4 CS")

# 6. KCR #45 Abraham Almonte (X - X - 25)
t6.new_ab()
t6.pitch_list("l b")
t6.out("L9")

# 7. KCR #21 Lucas Duda (X - X - 25)
t6.new_ab()
t6.pitch_list("1 c")
t6.hit(1)
t6.thrown_out(2, "2 FC6-4", 2, 41)

# 8. KCR #2  Alcides Escobar (X - 25 - 21)
t6.new_ab(is_risp=True)
t6.reach("FC6-4")
t6.thrown_out(2, "4 CS", 3, 41)

# 9. KCR #4  Alex Gordon (25 - X - 2)
t6.new_ab(is_risp=True)
t6.pitch_list("b c")
t6.no_ab("CS")


# Bot 6th
# Pitching: KCR #65 Jakob Junis
b6 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.out("L9")

# 4. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b f b")
b6.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b")
b6.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("f b b")
b6.hit(2)
b6.advance(4, "19 1B")

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b s b d")
b6.hit(1, rbis=1)

# 8. BOS #7  Christian Vázquez (X - X - 19)
b6.new_ab()
b6.pitch_list("1 s")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #41 Chris Sale
t7 = game.new_inning()

# 9. KCR #4  Alex Gordon (X - X - X)
t7.new_ab()
t7.pitch_list("c f s")
t7.out("K")

# 1. KCR #15 Whit Merrifield (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("G6-3")

# 2. KCR #12 Jorge Soler (X - X - X)
t7.new_ab()
t7.pitch_list("c b f c")
t7.out("!K")


# Bot 7th
# Pitching: KCR #54 Tim Hill
b7 = game.new_inning()

# Pitching change (KCR): #54 Tim Hill replaces #65 Jakob Junis
b7.pitching_substitution(54)

# Offensive change (BOS): Pinch-hitter #36 Eduardo Núñez replaces #5 Tzu-Wei Lin, batting 9th
b7.offensive_substitution(9, 36, "PH")

# 9. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("P4")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("b b f")
b7.hit(2)
b7.advance(3, "13 WP")
b7.advance(4, "28 WP")

# Pitching change (KCR): #56 Brad Keller replaces #54 Tim Hill
b7.pitching_substitution(56)

# 2. BOS #13 Hanley Ramirez (X - 16 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b s b s")
b7.wp()
b7.out("K")

# 3. BOS #28 J.D. Martinez (16 - X - X)
b7.new_ab()
b7.pitch_list("c b b b")
b7.wp()
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
t8.pitching_substitution(32)

# Defensive switch (BOS): #36 Eduardo Núñez moves to 2B
t8.defensive_switch(36, "4")

# 3. KCR #19 Cheslor Cuthbert (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c f f")
t8.out("G1-3")

# 4. KCR #13 Salvador Perez (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(2, "25 1B")
t8.advance(3, "21 SB")

# 5. KCR #25 Jon Jay (X - X - 13)
t8.new_ab()
t8.pitch_list("b b c")
t8.hit(1)
t8.error(6)
t8.advance(2, "21 E6")

# 6. KCR #45 Abraham Almonte (X - 13 - 25)
t8.new_ab(is_risp=True)
t8.pitch_list("d c b c f c")
t8.out("!K")

# 7. KCR #21 Lucas Duda (X - 13 - 25)
t8.new_ab(is_risp=True)
t8.pitch_list("f s")
t8.out("F9")


# Bot 8th
# Pitching: KCR #51 Blaine Boyer
b8 = game.new_inning()

# Pitching change (KCR): #51 Blaine Boyer replaces #56 Brad Keller
b8.pitching_substitution(51)

# 4. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b b f c f f f b f")
b8.out("F7")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c b c f")
b8.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("f b b b b")
b8.reach("BB")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 11)
b8.new_ab()
b8.pitch_list("s c f b b b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# Defensive switch (BOS): #16 Andrew Benintendi moves to LF
t9.defensive_switch(16, "7")

# Defensive change (BOS): #50 Mookie Betts replaces #28 J.D. Martinez (LF), playing RF, batting 3rd
t9.defensive_substitution(3, 50, "9")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to CF
t9.defensive_switch(19, "8")

# 8. KCR #2  Alcides Escobar (X - X - X)
t9.new_ab()
t9.pitch_list("b b c b f")
t9.out("(F)P3")

# 9. KCR #4  Alex Gordon (X - X - X)
t9.new_ab()
t9.pitch_list("b s b")
t9.hit(4)

# 1. KCR #15 Whit Merrifield (X - X - X)
t9.new_ab()
t9.pitch_list("c b b f b")
t9.out("G5-3")

# 2. KCR #12 Jorge Soler (X - X - X)
t9.new_ab()
t9.pitch_list("b s c s")
t9.out("K")


# Bot 9th
# Pitching: KCR #61 Kevin McCarthy
b9 = game.new_inning()

# Pitching change (KCR): #61 Kevin McCarthy replaces #51 Blaine Boyer
b9.pitching_substitution(61)

# 8. BOS #7  Christian Vázquez (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.out("G6-3")

# 9. BOS #36 Eduardo Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("c f s")
b9.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.out("G3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #39 Carson Smith
t10 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #46 Craig Kimbrel
t10.pitching_substitution(39)

# Offensive change (KCR): Pinch-hitter #8 Mike Moustakas replaces #19 Cheslor Cuthbert, batting 3rd
t10.offensive_substitution(3, 8, "PH")

# 3. KCR #8  Mike Moustakas (X - X - X)
t10.new_ab()
t10.pitch_list("b b")
t10.out("G4-3")

# 4. KCR #13 Salvador Perez (X - X - X)
t10.new_ab()
t10.hit(1)
t10.advance(2, "25 1B")
# Offensive change (KCR): Pinch-runner #1 Ryan Goins replaces #13 Salvador Perez
t10.offensive_substitution(4, 1, "PR")
t10.atbase("PR")
t10.error(2)
t10.advance(3, "21 E2")

# 5. KCR #25 Jon Jay (X - X - 13)
t10.new_ab()
t10.pitch_list("f f f f b")
t10.hit(1)
t10.advance(2, "21 E2")

# 6. KCR #45 Abraham Almonte (X - 13 - 25)
t10.new_ab(is_risp=True)
t10.pitch_list("s f s")
t10.out("K")

# 7. KCR #21 Lucas Duda (X - 1 - 25)
t10.new_ab(is_risp=True)
t10.pitch_list("c s d n d b")
t10.out("G3-1")


# Bot 10th
# Pitching: KCR #61 Kevin McCarthy
b10 = game.new_inning()

# Defensive change (KCR): #9 Drew Butera replaces #8 Mike Moustakas (PH), playing C, batting 3rd
b10.defensive_substitution(3, 9, "2")

# Defensive switch (KCR): #1 Ryan Goins moves to 3B
b10.defensive_switch(1, "5")

# 2. BOS #13 Hanley Ramirez (X - X - X)
b10.new_ab()
b10.pitch_list("f b b f f b")
b10.out("F8")

# 3. BOS #50 Mookie Betts (X - X - X)
b10.new_ab()
b10.pitch_list("c")
b10.out("G5-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
b10.new_ab()
b10.pitch_list("c s b s")
b10.out("K")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BOS #37 Heath Hembree
t11 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #39 Carson Smith
t11.pitching_substitution(37)

# 8. KCR #2  Alcides Escobar (X - X - X)
t11.new_ab()
t11.pitch_list("s b t t")
t11.out("KT")

# 9. KCR #4  Alex Gordon (X - X - X)
t11.new_ab()
t11.out("G3")

# 1. KCR #15 Whit Merrifield (X - X - X)
t11.new_ab()
t11.pitch_list("c b b f b b")
t11.reach("BB")

# 2. KCR #12 Jorge Soler (X - X - 15)
t11.new_ab()
t11.pitch_list("1 s f b b 1")
t11.out("G5-3")


# Bot 11th
# Pitching: KCR #61 Kevin McCarthy
b11 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b11.new_ab()
b11.pitch_list("b c")
b11.out("G5-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b11.new_ab()
b11.out("L9")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b11.new_ab()
b11.out("G4-3")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BOS #37 Heath Hembree
t12 = game.new_inning()

# 3. KCR #9  Drew Butera (X - X - X)
t12.new_ab()
t12.pitch_list("b b")
t12.hit(2)
t12.advance(3, "1 1B")
t12.advance(4, "25 SF7")

# 4. KCR #1  Ryan Goins (X - 9 - X)
t12.new_ab(is_risp=True)
t12.pitch_list("c")
t12.hit(1)
t12.advance(2, "25 SF7")
t12.advance(3, "45 G6-3")

# 5. KCR #25 Jon Jay (9 - X - 1)
t12.new_ab(is_risp=True)
t12.pitch_list("c b b")
t12.out("SF7", rbis=1)

# 6. KCR #45 Abraham Almonte (X - 1 - X)
t12.new_ab(is_risp=True)
t12.out("G6-3")

# 7. KCR #21 Lucas Duda (1 - X - X)
t12.new_ab(is_risp=True)
t12.pitch_list("b s f b")
t12.out("G4-3")


# Bot 12th
# Pitching: KCR #40 Kelvin Herrera
b12 = game.new_inning()

# Pitching change (KCR): #40 Kelvin Herrera replaces #61 Kevin McCarthy
b12.pitching_substitution(40)

# 8. BOS #7  Christian Vázquez (X - X - X)
b12.new_ab()
b12.pitch_list("c f b")
b12.out("P4")

# 9. BOS #36 Eduardo Núñez (X - X - X)
b12.new_ab()
b12.pitch_list("b")
b12.hit(4)

# 1. BOS #16 Andrew Benintendi (X - X - X)
b12.new_ab()
b12.pitch_list("s s f")
b12.hit(1)

# 2. BOS #13 Hanley Ramirez (X - X - 16)
b12.new_ab()
b12.out("(F)P5")

# 3. BOS #50 Mookie Betts (X - X - 16)
b12.new_ab()
b12.pitch_list("c 1 f d b s")
b12.out("K")


##########################################################
# 13th Inning
##########################################################
# Top 13th
# Pitching: BOS #61 Brian Johnson
t13 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #37 Heath Hembree
t13.pitching_substitution(61)

# 8. KCR #2  Alcides Escobar (X - X - X)
t13.new_ab()
t13.pitch_list("s b")
t13.out("G5-3")

# 9. KCR #4  Alex Gordon (X - X - X)
t13.new_ab()
t13.pitch_list("c b")
t13.hit(1)
t13.advance(2, "15 1B")
t13.advance(4, "12 HR")

# 1. KCR #15 Whit Merrifield (X - X - 4)
t13.new_ab()
t13.pitch_list("1 1")
t13.hit(1)
t13.advance(4, "12 HR")

# 2. KCR #12 Jorge Soler (X - 4 - 15)
t13.new_ab(is_risp=True)
t13.pitch_list("d")
t13.hit(4, rbis=3)

# 3. KCR #9  Drew Butera (X - X - X)
t13.new_ab()
t13.pitch_list("c")
t13.out("F9")

# 4. KCR #1  Ryan Goins (X - X - X)
t13.new_ab()
t13.pitch_list("c f b b s")
t13.out("K")


# Bot 13th
# Pitching: KCR #64 Burch Smith
b13 = game.new_inning()

# Pitching change (KCR): #64 Burch Smith replaces #40 Kelvin Herrera
b13.pitching_substitution(64)

# 4. BOS #18 Mitch Moreland (X - X - X)
b13.new_ab()
b13.hit(1)
b13.advance(2, "2 HBP")
b13.advance(3, "11 FC6-4")
b13.advance(4, "19 G3")

# 5. BOS #2  Xander Bogaerts (X - X - 18)
b13.new_ab()
b13.pitch_list("c")
b13.reach("HBP")
b13.thrown_out(2, "11 FC6-4", 1, 64)

# 6. BOS #11 Rafael Devers (X - 18 - 2)
b13.new_ab(is_risp=True)
b13.pitch_list("b b b c f f f f f f")
b13.reach("FC6-4")
b13.advance(2, "19 G3")
b13.advance(4, "7 1B")

# Pitching change (KCR): #33 Brian Flynn replaces #64 Burch Smith
b13.pitching_substitution(33)

# 7. BOS #19 Jackie Bradley Jr. (18 - X - 11)
b13.new_ab(is_risp=True)
b13.pitch_list("c f")
b13.out("G3", rbis=1)

# 8. BOS #7  Christian Vázquez (X - 11 - X)
b13.new_ab(is_risp=True)
b13.hit(1, rbis=1)

# 9. BOS #36 Eduardo Núñez (X - X - 7)
b13.new_ab()
b13.pitch_list("s f f")
b13.out("F8")

# Winning team: KCR
# WP: KCR #40 Kelvin Herrera
game.winning_pitcher(40, is_away_team=True)
# SV: KCR #33 Brian Flynn
game.save_pitcher(33, is_away_team=True)

# Loser team: BOS
# LP: BOS #61 Brian Johnson
game.losing_pitcher(61)

# print(game)
game.generate_scorecard()
