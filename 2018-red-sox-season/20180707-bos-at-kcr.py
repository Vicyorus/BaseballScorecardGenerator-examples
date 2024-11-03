import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KCR, 2018-07-07
# https://www.baseball-reference.com/boxes/KCA/KCA201807070.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2018/07/07/530733/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-07 19:15-23:18",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "30,347",
        "temp": "87F, Clear",
        "wind": "9mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                22: "Rick Porcello",
                41: "Chris Sale",
                56: "Joe Kelly",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [24, 57, 41],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [12, "4"],
                [11, "5"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [47, 57, 44, 46, 76, 22, 41, 56, 32, 37],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 56,
            "roster": {
                # Lineup
                15: "Whit Merrifield",
                38: "Jorge Bonifacio",
                8: "Mike Moustakas",
                13: "Salvador Perez",
                17: "Hunter Dozier",
                21: "Lucas Duda",
                2: "Alcides Escobar",
                4: "Alex Gordon",
                27: "Adalberto Mondesi",
                # Starting pitcher
                56: "Brad Keller",
                # Bench
                7: "Rosell Herrera",
                9: "Drew Butera",
                45: "Abraham Almonte",
                # Bullpen
                41: "Danny Duffy",
                50: "Jason Adam",
                61: "Kevin McCarthy",
                43: "Wily Peralta",
                64: "Burch Smith",
                33: "Brian Flynn",
                54: "Tim Hill",
                49: "Heath Fillmyer",
                37: "Brandon Maurer",
                39: "Jason Hammel",
                72: "Enny Romero",
                65: "Jakob Junis",
            },
            "lefties": [41, 33, 54, 72],
            "lineup": [
                [15, "4"],
                [38, "9"],
                [8, "3"],
                [13, "2"],
                [17, "5"],
                [21, "0"],
                [2, "8"],
                [4, "7"],
                [27, "6"],
            ],
            "bench": [
                [7, "2B"],
                [9, "C"],
                [45, "OF"],
            ],
            "bullpen": [41, 50, 61, 43, 64, 33, 54, 49, 37, 39, 72, 65],
        },
        "umpires": {
            "HP": "Sam Holbrook",
            "1B": "Jim Wolf",
            "2B": "D.J. Reyburn",
            "3B": "Ryan Blakney",
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
# Pitching: KCR #56 Brad Keller
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(2)
t1.advance(3, "18 F8")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c f b b b b")
t1.reach("BB")
t1.thrown_out(2, "2 2-4", 3, 56)

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("f")
t1.out("F9")

# 4. BOS #18 Mitch Moreland (X - 50 - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("b")
t1.out("F8")

# 5. BOS #2  Xander Bogaerts (50 - X - 16)
t1.new_ab(is_risp=True)
t1.pitch_list("b c d")
t1.no_ab("2-4")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G5-3")

# 2. KCR #38 Jorge Bonifacio (X - X - X)
b1.new_ab()
b1.pitch_list("b f b b f b")
b1.reach("BB")

# 3. KCR #8  Mike Moustakas (X - X - 38)
b1.new_ab()
b1.pitch_list("b f f c")
b1.out("!K")

# 4. KCR #13 Salvador Perez (X - X - 38)
b1.new_ab()
b1.pitch_list("c b f")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #56 Brad Keller
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b f b")
t2.out("L6")

# 6. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c c b b b")
t2.hit(1)

# 7. BOS #11 Rafael Devers (X - X - 12)
t2.new_ab()
t2.out("P6")

# 8. BOS #7  Christian Vázquez (X - X - 12)
t2.new_ab()
t2.pitch_list("b b f")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 5. KCR #17 Hunter Dozier (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f s")
b2.out("K")

# 6. KCR #21 Lucas Duda (X - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.hit(4)

# 7. KCR #2  Alcides Escobar (X - X - X)
b2.new_ab()
b2.pitch_list("t f b b f")
b2.out("G6-3")

# 8. KCR #4  Alex Gordon (X - X - X)
b2.new_ab()
b2.pitch_list("c b s f b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #56 Brad Keller
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("s")
t3.out("L4")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b c b")
t3.hit(1)
t3.advance(2, "16 SB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab(is_risp=True)
t3.pitch_list("f b b d c b")
t3.reach("BB")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t3.new_ab(is_risp=True)
t3.pitch_list("c b b b f f s")
t3.out("K")

# 4. BOS #18 Mitch Moreland (X - 50 - 16)
t3.new_ab(is_risp=True)
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 9. KCR #27 Adalberto Mondesi (X - X - X)
b3.new_ab()
b3.pitch_list("l t b f t")
b3.out("KT")

# 1. KCR #15 Whit Merrifield (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(3, "38 2B")
b3.advance(4, "8 1B")

# 2. KCR #38 Jorge Bonifacio (X - X - 15)
b3.new_ab()
b3.pitch_list("b s b f f f b 1 f")
b3.hit(2)
b3.advance(3, "8 1B")
b3.advance(4, "13 SF9")

# 3. KCR #8  Mike Moustakas (15 - 38 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f b f")
b3.hit(1, rbis=1)

# 4. KCR #13 Salvador Perez (38 - X - 8)
b3.new_ab(is_risp=True)
b3.pitch_list("s b b")
b3.out("SF9", rbis=1)

# 5. KCR #17 Hunter Dozier (X - X - 8)
b3.new_ab()
b3.pitch_list("c b b b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #56 Brad Keller
t4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b c b")
t4.reach("BB")
t4.thrown_out(2, "12 FC6", 1, 56)

# 6. BOS #12 Brock Holt (X - X - 2)
t4.new_ab()
t4.pitch_list("c")
t4.reach("FC6")
t4.thrown_out(2, "11 DP1-6-3", 2, 56)

# 7. BOS #11 Rafael Devers (X - X - 12)
t4.new_ab()
t4.pitch_list("b")
t4.out("DP1-6-3")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 6. KCR #21 Lucas Duda (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b s")
b4.out("K")

# 7. KCR #2  Alcides Escobar (X - X - X)
b4.new_ab()
b4.hit(2)

# 8. KCR #4  Alex Gordon (X - 2 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c f f f s")
b4.out("K")

# 9. KCR #27 Adalberto Mondesi (X - 2 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("f f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #56 Brad Keller
t5 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("P4")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b t c b f c")
t5.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.hit(1)
t5.advance(2, "16 BB")
t5.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("1 b b b b")
t5.reach("BB")
t5.advance(3, "28 1B")
t5.advance(4, "2 2B")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("f c d")
t5.hit(1, rbis=1)
t5.advance(2, "18 BB")
t5.advance(4, "2 2B")

# 4. BOS #18 Mitch Moreland (16 - X - 28)
t5.new_ab(is_risp=True)
t5.pitch_list("b d b b")
t5.reach("BB")
t5.advance(4, "2 2B")

# 5. BOS #2  Xander Bogaerts (16 - 28 - 18)
t5.new_ab(is_risp=True)
t5.pitch_list("b b c")
t5.hit(2, rbis=3)
t5.advance(3, "T")

# Pitching change (KCR): #54 Tim Hill replaces #56 Brad Keller
t5.pitching_substitution(54)

# 6. BOS #12 Brock Holt (2 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f b b b")
t5.reach("BB")
t5.advance(2, "11 SB")

# 7. BOS #11 Rafael Devers (2 - X - 12)
t5.new_ab(is_risp=True)
t5.pitch_list("c b c b f f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1)
b5.advance(2, "8 HBP")
b5.advance(3, "13 HBP")
b5.advance(4, "21 HBP")

# 2. KCR #38 Jorge Bonifacio (X - X - 15)
b5.new_ab()
b5.pitch_list("c s f f c")
b5.out("!K")

# 3. KCR #8  Mike Moustakas (X - X - 15)
b5.new_ab()
b5.reach("HBP")
b5.advance(2, "13 HBP")
b5.advance(3, "21 HBP")

# 4. KCR #13 Salvador Perez (X - 15 - 8)
b5.new_ab(is_risp=True)
b5.pitch_list("s f b f")
b5.reach("HBP")
b5.advance(2, "21 HBP")

# 5. KCR #17 Hunter Dozier (15 - 8 - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("s f c")
b5.out("!K")

# 6. KCR #21 Lucas Duda (15 - 8 - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("c b f b")
b5.reach("HBP", rbis=1)

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
b5.pitching_substitution(37)

# 7. KCR #2  Alcides Escobar (8 - 13 - 21)
b5.new_ab(is_risp=True)
b5.pitch_list("s")
b5.out("(F)F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #50 Jason Adam
t6 = game.new_inning()

# Pitching change (KCR): #50 Jason Adam replaces #54 Tim Hill
t6.pitching_substitution(50)

# 8. BOS #7  Christian Vázquez (X - X - X)
t6.new_ab()
t6.pitch_list("f f s")
t6.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("f c b s")
t6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #37 Heath Hembree
b6 = game.new_inning()

# 8. KCR #4  Alex Gordon (X - X - X)
b6.new_ab()
b6.out("P6")

# 9. KCR #27 Adalberto Mondesi (X - X - X)
b6.new_ab()
b6.pitch_list("c s b b b f s")
b6.out("K")

# 1. KCR #15 Whit Merrifield (X - X - X)
b6.new_ab()
b6.pitch_list("b c b s f b b")
b6.reach("BB")
b6.advance(2, "38 E5")

# 2. KCR #38 Jorge Bonifacio (X - X - 15)
b6.new_ab()
b6.pitch_list("1 b b")
b6.error(5)
b6.reach("E5")

# 3. KCR #8  Mike Moustakas (X - 15 - 38)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #50 Jason Adam
t7 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("f b b b b")
t7.reach("BB")
t7.advance(3, "28 2B")
t7.advance(4, "18 SF7")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t7.new_ab()
t7.pitch_list("c f b b")
t7.hit(2)
t7.advance(3, "11 BB")
t7.advance(4, "7 1B")

# Pitching change (KCR): #72 Enny Romero replaces #50 Jason Adam
t7.pitching_substitution(72)

# 4. BOS #18 Mitch Moreland (16 - 28 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b d f")
t7.out("SF7", rbis=1)

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("v v v v")
t7.reach("IBB")
t7.advance(2, "11 BB")
t7.advance(4, "7 1B")

# 6. BOS #12 Brock Holt (X - 28 - 2)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.out("F8")

# 7. BOS #11 Rafael Devers (X - 28 - 2)
t7.new_ab(is_risp=True)
t7.pitch_list("b f b b b")
t7.reach("BB")
t7.advance(3, "7 1B")

# 8. BOS #7  Christian Vázquez (28 - 2 - 11)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.hit(1, rbis=2)
t7.advance(2, "19 SB")

# 9. BOS #19 Jackie Bradley Jr. (11 - X - 7)
t7.new_ab(is_risp=True)
t7.pitch_list("b s")
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree
b7.pitching_substitution(32)

# 4. KCR #13 Salvador Perez (X - X - X)
b7.new_ab()
b7.pitch_list("b c f b b s")
b7.out("K")

# 5. KCR #17 Hunter Dozier (X - X - X)
b7.new_ab()
b7.pitch_list("c s b")
b7.out("G6-3")

# 6. KCR #21 Lucas Duda (X - X - X)
b7.new_ab()
b7.pitch_list("c b c s")
b7.wp()
b7.reach("K")

# 7. KCR #2  Alcides Escobar (X - X - 21)
b7.new_ab()
b7.pitch_list("b c f b")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #61 Kevin McCarthy
t8 = game.new_inning()

# Pitching change (KCR): #61 Kevin McCarthy replaces #72 Enny Romero
t8.pitching_substitution(61)

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c f s")
t8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("f b b f f")
t8.hit(4)

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("f f t")
t8.out("KT")

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b s s b b b")
t8.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t8.new_ab()
t8.out("G4-3")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b8.pitching_substitution(56)

# Defensive change (BOS): #3 Sandy León replaces #7 Christian Vázquez (C), playing C, batting 8th
b8.defensive_substitution(8, 3, "2")

# 8. KCR #4  Alex Gordon (X - X - X)
b8.new_ab()
b8.pitch_list("c f b s")
b8.out("K")

# 9. KCR #27 Adalberto Mondesi (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G3-1")

# Pitching change (BOS): #44 Brandon Workman replaces #56 Joe Kelly
b8.pitching_substitution(44)

# 1. KCR #15 Whit Merrifield (X - X - X)
b8.new_ab()
b8.pitch_list("c b s b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #37 Brandon Maurer
t9 = game.new_inning()

# Pitching change (KCR): #37 Brandon Maurer replaces #61 Kevin McCarthy
t9.pitching_substitution(37)

# 6. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b")
t9.out("G3-1")

# 7. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c c")
t9.hit(1)
t9.advance(3, "3 1B")
t9.advance(4, "19 FC3-6")

# 8. BOS #3  Sandy León (X - X - 11)
t9.new_ab()
t9.pitch_list("c c")
t9.hit(1)
t9.thrown_out(2, "19 FC3-6", 2, 37)

# 9. BOS #19 Jackie Bradley Jr. (11 - X - 3)
t9.new_ab(is_risp=True)
t9.pitch_list("b b t b c")
t9.reach("FC3-6", rbis=1)
t9.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (X - X - 19)
t9.new_ab()
t9.pitch_list("b s")
t9.hit(2, rbis=1)
t9.advance(3, "T")
t9.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (50 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("f b b f")
t9.hit(2, rbis=1)
t9.advance(4, "23 1B")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #28 J.D. Martinez, batting 3rd
t9.offensive_substitution(3, 23, "PH")

# 3. BOS #23 Blake Swihart (X - 16 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b")
t9.hit(1, rbis=1)
t9.advance(3, "18 1B")
t9.advance(4, "12 BB")

# Pitching change (KCR): #9  Drew Butera replaces #37 Brandon Maurer
t9.pitching_substitution(9)

# 4. BOS #18 Mitch Moreland (X - X - 23)
t9.new_ab()
t9.hit(1)
t9.advance(2, "2 BB")
t9.advance(3, "12 BB")
t9.advance(4, "11 BB")

# 5. BOS #2  Xander Bogaerts (23 - X - 18)
t9.new_ab(is_risp=True)
t9.pitch_list("b c b b b")
t9.reach("BB")
t9.advance(2, "12 BB")
t9.advance(3, "11 BB")
t9.advance(4, "3 1B")

# 6. BOS #12 Brock Holt (23 - 18 - 2)
t9.new_ab(is_risp=True)
t9.pitch_list("s d b b c f b")
t9.reach("BB", rbis=1)
t9.advance(2, "11 BB")
t9.advance(3, "3 1B")

# 7. BOS #11 Rafael Devers (18 - 2 - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b b b c b")
t9.reach("BB", rbis=1)
t9.advance(2, "3 1B")

# 8. BOS #3  Sandy León (2 - 12 - 11)
t9.new_ab(is_risp=True)
t9.pitch_list("f")
t9.hit(1, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (12 - 11 - 3)
t9.new_ab(is_risp=True)
t9.pitch_list("s d b")
t9.out("L4")


# Bot 9th
# Pitching: BOS #76 Hector Velázquez
b9 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #44 Brandon Workman
b9.pitching_substitution(76)

# Defensive switch (BOS): #23 Blake Swihart moves to DH
b9.defensive_switch(23, "0")

# Offensive change (KCR): Pinch-hitter #45 Abraham Almonte replaces #38 Jorge Bonifacio, batting 2nd
b9.offensive_substitution(2, 45, "PH")

# 2. KCR #45 Abraham Almonte (X - X - X)
b9.new_ab()
b9.pitch_list("f b t")
b9.out("(F)P5")

# 3. KCR #8  Mike Moustakas (X - X - X)
b9.new_ab()
b9.pitch_list("b f f b f")
b9.out("G1-3")

# 4. KCR #13 Salvador Perez (X - X - X)
b9.new_ab()
b9.pitch_list("s")
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #37 Heath Hembree
game.winning_pitcher(37, is_away_team=True)

# Loser team: KCR
# LP: KCR #50 Jason Adam
game.losing_pitcher(50)

# print(game)
game.generate_scorecard()
