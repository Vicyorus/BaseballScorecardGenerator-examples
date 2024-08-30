import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ KCR, 2018-07-08
# https://www.baseball-reference.com/boxes/KCA/KCA201807080.shtml
# https://www.mlb.com/gameday/red-sox-vs-royals/2018/07/08/530748/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-08 14:16-17:41",
        "at": "Kauffman Stadium, Kansas City, MO",
        "att": "28,443",
        "temp": "88F, Sunny",
        "wind": "6mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                12: "Brock Holt",
                28: "J.D. Martinez",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                67: "William Cuevas",
                41: "Chris Sale",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [25, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [12, "2B"],
                [28, "DH"],
                [23, "C"],
            ],
            "bullpen": [47, 57, 44, 67, 41, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Kansas City Royals",
            "starter": 49,
            "roster": {
                # Lineup
                15: "Whit Merrifield",
                38: "Jorge Bonifacio",
                8: "Mike Moustakas",
                21: "Lucas Duda",
                4: "Alex Gordon",
                17: "Hunter Dozier",
                45: "Abraham Almonte",
                27: "Adalberto Mondesi",
                9: "Drew Butera",
                # Starting pitcher
                49: "Heath Fillmyer",
                # Bench
                13: "Salvador Perez",
                7: "Rosell Herrera",
                2: "Alcides Escobar",
                # Bullpen
                57: "Glenn Sparkman",
                41: "Danny Duffy",
                50: "Jason Adam",
                61: "Kevin McCarthy",
                43: "Wily Peralta",
                64: "Burch Smith",
                33: "Brian Flynn",
                54: "Tim Hill",
                37: "Brandon Maurer",
                39: "Jason Hammel",
                72: "Enny Romero",
                56: "Brad Keller",
            },
            "lefties": [41, 33, 54, 72],
            "lineup": [
                [15, "4"],
                [38, "9"],
                [8, "3"],
                [21, "0"],
                [4, "7"],
                [17, "5"],
                [45, "8"],
                [27, "6"],
                [9, "2"],
            ],
            "bench": [
                [13, "C"],
                [7, "2B"],
                [2, "SS"],
            ],
            "bullpen": [57, 41, 50, 61, 43, 64, 33, 54, 37, 39, 72, 56],
        },
        "umpires": {
            "HP": "Jim Wolf",
            "1B": "D.J. Reyburn",
            "2B": "Ryan Blakney",
            "3B": "Sam Holbrook",
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
# Pitching: KCR #49 Heath Fillmyer
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c f b f b")
t1.hit(1)
t1.advance(2, "25 BB")

# 3. BOS #25 Steve Pearce (X - X - 16)
t1.new_ab()
t1.pitch_list("d b d b")
t1.reach("BB")
t1.thrown_out(2, "18 DP4-6-3", 2, 49)

# 4. BOS #18 Mitch Moreland (X - 16 - 25)
t1.new_ab()
t1.out("DP4-6-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
b1.new_ab()
b1.hit(1)

# 2. KCR #38 Jorge Bonifacio (X - X - 15)
b1.new_ab()
b1.pitch_list("b 1 c")
b1.out("F8")

# 3. KCR #8  Mike Moustakas (X - X - 15)
b1.new_ab()
b1.pitch_list("f")
b1.out("F9")

# 4. KCR #21 Lucas Duda (X - X - 15)
b1.new_ab()
b1.pitch_list("c")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: KCR #49 Heath Fillmyer
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(2, "11 1B")
t2.advance(3, "36 DP6-4-3")

# 6. BOS #11 Rafael Devers (X - X - 2)
t2.new_ab()
t2.pitch_list("1 1")
t2.hit(1)
t2.thrown_out(2, "36 DP6-4-3", 1, 49)

# 7. BOS #36 Eduardo Núñez (X - 2 - 11)
t2.new_ab()
t2.out("DP6-4-3")

# 8. BOS #3  Sandy León (2 - X - X)
t2.new_ab()
t2.pitch_list("d b f")
t2.out("G1-3")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. KCR #4  Alex Gordon (X - X - X)
b2.new_ab()
b2.pitch_list("c b f c")
b2.out("!K")

# 6. KCR #17 Hunter Dozier (X - X - X)
b2.new_ab()
b2.pitch_list("c b f s")
b2.out("K")

# 7. KCR #45 Abraham Almonte (X - X - X)
b2.new_ab()
b2.pitch_list("f")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: KCR #49 Heath Fillmyer
t3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b b")
t3.reach("BB")
t3.advance(3, "16 1B")
t3.advance(4, "25 SF7")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t3.new_ab()
t3.pitch_list("s b b f")
t3.hit(1)

# 3. BOS #25 Steve Pearce (50 - X - 16)
t3.new_ab()
t3.pitch_list("c b 1 f 1 b b")
t3.out("SF7", rbis=1)

# 4. BOS #18 Mitch Moreland (X - X - 16)
t3.new_ab()
t3.pitch_list("c s f b")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 8. KCR #27 Adalberto Mondesi (X - X - X)
b3.new_ab()
b3.pitch_list("b s l b s")
b3.out("K")

# 9. KCR #9  Drew Butera (X - X - X)
b3.new_ab()
b3.pitch_list("c b c b b f")
b3.hit(1)
b3.advance(2, "15 1B")
b3.advance(4, "38 2B")

# 1. KCR #15 Whit Merrifield (X - X - 9)
b3.new_ab()
b3.pitch_list("b c f b f")
b3.hit(1)
b3.advance(4, "38 2B")

# 2. KCR #38 Jorge Bonifacio (X - 9 - 15)
b3.new_ab()
b3.pitch_list("f")
b3.hit(2, rbis=2)

# 3. KCR #8  Mike Moustakas (X - 38 - X)
b3.new_ab()
b3.pitch_list("f b f d")
b3.out("P5")

# 4. KCR #21 Lucas Duda (X - 38 - X)
b3.new_ab()
b3.pitch_list("c f f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: KCR #49 Heath Fillmyer
t4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("b c b b")
t4.error(6)
t4.reach("E6", 2)
t4.advance("U", "36 1B")

# 6. BOS #11 Rafael Devers (X - 2 - X)
t4.new_ab()
t4.pitch_list("b f f")
t4.out("(F)P5")

# 7. BOS #36 Eduardo Núñez (X - 2 - X)
t4.new_ab()
t4.hit(1, rbis=1)
t4.thrown_out(2, "3 DP3-6-3", 2, 49)

# 8. BOS #3  Sandy León (X - X - 36)
t4.new_ab()
t4.pitch_list("b c")
t4.out("DP3-6-3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 5. KCR #4  Alex Gordon (X - X - X)
b4.new_ab()
b4.pitch_list("b f")
b4.hit(1)
b4.advance(2, "17 G4-3")
b4.advance(3, "27 WP")
b4.advance(4, "27 1B")

# 6. KCR #17 Hunter Dozier (X - X - 4)
b4.new_ab()
b4.out("G4-3")

# 7. KCR #45 Abraham Almonte (X - 4 - X)
b4.new_ab()
b4.pitch_list("b d f b s s")
b4.out("K")

# 8. KCR #27 Adalberto Mondesi (X - 4 - X)
b4.new_ab()
b4.pitch_list("f f b b b f f")
b4.wp()
b4.hit(1, rbis=1)

# 9. KCR #9  Drew Butera (X - X - 27)
b4.new_ab()
b4.pitch_list("d")
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: KCR #49 Heath Fillmyer
t5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.advance(2, "16 1B")
t5.advance(3, "25 1B")
t5.advance(4, "18 BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("1")
t5.hit(1)
t5.advance(2, "25 1B")
t5.advance(3, "18 BB")
t5.advance(4, "2 SF8")

# 3. BOS #25 Steve Pearce (X - 50 - 16)
t5.new_ab()
t5.pitch_list("b c b s")
t5.hit(1)
t5.advance(2, "18 BB")
t5.advance(3, "2 SF8")

# 4. BOS #18 Mitch Moreland (50 - 16 - 25)
t5.new_ab()
t5.pitch_list("b c b b b")
t5.reach("BB", rbis=1)

# Pitching change (KCR): #57 Glenn Sparkman replaces #49 Heath Fillmyer
t5.pitching_substitution(57)

# 5. BOS #2  Xander Bogaerts (16 - 25 - 18)
t5.new_ab()
t5.pitch_list("b c c f")
t5.out("SF8", rbis=1)

# 6. BOS #11 Rafael Devers (25 - X - 18)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 1. KCR #15 Whit Merrifield (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.hit(2)

# 2. KCR #38 Jorge Bonifacio (X - 15 - X)
b5.new_ab()
b5.pitch_list("f c b b")
b5.out("L9")

# 3. KCR #8  Mike Moustakas (X - 15 - X)
b5.new_ab()
b5.pitch_list("s")
b5.out("L7")

# 4. KCR #21 Lucas Duda (X - 15 - X)
b5.new_ab()
b5.pitch_list("c f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: KCR #57 Glenn Sparkman
t6 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.out("G6-3")

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f f b f c")
t6.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("c s b f b b b")
t6.reach("BB")

# 1. BOS #50 Mookie Betts (X - X - 19)
t6.new_ab()
t6.pitch_list("c 1 b b f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 5. KCR #4  Alex Gordon (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.out("G6-3")

# 6. KCR #17 Hunter Dozier (X - X - X)
b6.new_ab()
b6.pitch_list("b b s f")
b6.out("G1-3")

# 7. KCR #45 Abraham Almonte (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b b")
b6.reach("BB")

# 8. KCR #27 Adalberto Mondesi (X - X - 45)
b6.new_ab()
b6.pitch_list("b f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: KCR #57 Glenn Sparkman
t7 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.hit(2)
t7.advance(3, "25 1B")
t7.advance(4, "18 1B")

# 3. BOS #25 Steve Pearce (X - 16 - X)
t7.new_ab()
t7.pitch_list("b b s")
t7.hit(1)
t7.advance(2, "18 1B")
t7.advance(4, "2 2B")

# 4. BOS #18 Mitch Moreland (16 - X - 25)
t7.new_ab()
t7.pitch_list("d f")
t7.hit(1, rbis=1)
t7.advance(3, "2 2B")
t7.advance(4, "36 1B")

# 5. BOS #2  Xander Bogaerts (X - 25 - 18)
t7.new_ab()
t7.pitch_list("b b c f f f")
t7.hit(2, rbis=1)
t7.advance(3, "36 1B")

# Pitching change (KCR): #72 Enny Romero replaces #57 Glenn Sparkman
t7.pitching_substitution(72)

# 6. BOS #11 Rafael Devers (18 - 2 - X)
t7.new_ab()
t7.pitch_list("b b f f t")
t7.out("KT")

# 7. BOS #36 Eduardo Núñez (18 - 2 - X)
t7.new_ab()
t7.pitch_list("f d f d f")
t7.hit(1, rbis=1)
t7.thrown_out(2, "3 DP4-6-3", 2, 72)

# 8. BOS #3  Sandy León (2 - X - 36)
t7.new_ab()
t7.pitch_list("d")
t7.out("DP4-6-3")


# Bot 7th
# Pitching: BOS #22 Rick Porcello
b7 = game.new_inning()

# 9. KCR #9  Drew Butera (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.hit(1)
b7.advance(3, "15 2B")

# 1. KCR #15 Whit Merrifield (X - X - 9)
b7.new_ab()
b7.hit(2)

# 2. KCR #38 Jorge Bonifacio (9 - 15 - X)
b7.new_ab()
b7.pitch_list("b f f t")
b7.out("KT")

# 3. KCR #8  Mike Moustakas (9 - 15 - X)
b7.new_ab()
b7.pitch_list("f f s")
b7.out("K")

# 4. KCR #21 Lucas Duda (9 - 15 - X)
b7.new_ab()
b7.pitch_list("t b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: KCR #50 Jason Adam
t8 = game.new_inning()

# Pitching change (KCR): #50 Jason Adam replaces #72 Enny Romero
t8.pitching_substitution(50)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b b c b f")
t8.hit(1)
t8.advance(2, "16 SB")

# 1. BOS #50 Mookie Betts (X - X - 19)
t8.new_ab()
t8.pitch_list("c d 1 b")
t8.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - 19)
t8.new_ab()
t8.pitch_list("c f b 1 b s")
t8.out("K")

# 3. BOS #25 Steve Pearce (X - 19 - X)
t8.new_ab()
t8.pitch_list("b b d b")
t8.reach("BB")

# 4. BOS #18 Mitch Moreland (X - 19 - 25)
t8.new_ab()
t8.pitch_list("b")
t8.out("G3")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #22 Rick Porcello
b8.pitching_substitution(32)

# 5. KCR #4  Alex Gordon (X - X - X)
b8.new_ab()
b8.pitch_list("s b f b")
b8.out("G6-3")

# 6. KCR #17 Hunter Dozier (X - X - X)
b8.new_ab()
b8.pitch_list("c t b f b s")
b8.out("K")

# 7. KCR #45 Abraham Almonte (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: KCR #43 Wily Peralta
t9 = game.new_inning()

# Pitching change (KCR): #43 Wily Peralta replaces #50 Jason Adam
t9.pitching_substitution(43)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("b b f b b")
t9.reach("BB")
t9.advance(2, "11 BB")
t9.advance(3, "36 DP6-4-3")

# 6. BOS #11 Rafael Devers (X - X - 2)
t9.new_ab()
t9.pitch_list("c d b b b")
t9.reach("BB")
t9.thrown_out(2, "36 DP6-4-3", 1, 43)

# 7. BOS #36 Eduardo Núñez (X - 2 - 11)
t9.new_ab()
t9.pitch_list("b c")
t9.out("DP6-4-3")

# 8. BOS #3  Sandy León (2 - X - X)
t9.new_ab()
t9.pitch_list("c f b s")
t9.out("K")


# Bot 9th
# Pitching: BOS #47 Tyler Thornburg
b9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #32 Matt Barnes
b9.pitching_substitution(47)

# 8. KCR #27 Adalberto Mondesi (X - X - X)
b9.new_ab()
b9.pitch_list("c f b")
b9.hit(2)
b9.advance(3, "15 WP")
b9.advance(4, "15 1B")

# 9. KCR #9  Drew Butera (X - 27 - X)
b9.new_ab()
b9.out("F7")

# 1. KCR #15 Whit Merrifield (X - 27 - X)
b9.new_ab()
b9.pitch_list("d c b b f f")
b9.wp()
b9.hit(1, rbis=1)
b9.advance(2, "38 1B")

# Pitching change (BOS): #46 Craig Kimbrel replaces #47 Tyler Thornburg
b9.pitching_substitution(46)

# 2. KCR #38 Jorge Bonifacio (X - X - 15)
b9.new_ab()
b9.pitch_list("s f f")
b9.hit(1)

# 3. KCR #8  Mike Moustakas (X - 15 - 38)
b9.new_ab()
b9.pitch_list("c c s")
b9.out("K")

# 4. KCR #21 Lucas Duda (X - 15 - 38)
b9.new_ab()
b9.pitch_list("b c s b f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: KCR
# LP: KCR #49 Heath Fillmyer
game.losing_pitcher(49)

# print(game)
game.generate_scorecard()
