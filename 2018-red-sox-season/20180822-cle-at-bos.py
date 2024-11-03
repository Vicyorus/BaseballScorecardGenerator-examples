import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2018-08-22
# https://www.baseball-reference.com/boxes/BOS/BOS201808220.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2018/08/22/531307/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-22 19:10-22:34",
        "at": "Fenway Park, Boston, MA",
        "att": "37,107",
        "temp": "80F, Partly Cloudy",
        "wind": "7mph, Out To RF",
        "away": {
            "team": "Cleveland Indians",
            "starter": 59,
            "roster": {
                # Lineup
                12: "Francisco Lindor",
                23: "Michael Brantley",
                11: "José Ramírez",
                10: "Edwin Encarnación",
                36: "Yandy Díaz",
                6: "Brandon Guyer",
                7: "Yan Gomes",
                1: "Greg Allen",
                9: "Erik González",
                # Starting pitcher
                59: "Carlos Carrasco",
                # Bench
                22: "Jason Kipnis",
                17: "Yonder Alonso",
                53: "Melky Cabrera",
                55: "Roberto Pérez",
                # Bullpen
                57: "Shane Bieber",
                37: "Cody Allen",
                45: "Adam Plutko",
                24: "Andrew Miller",
                58: "Neil Ramírez",
                39: "Oliver Pérez",
                52: "Mike Clevinger",
                90: "Adam Cimber",
                61: "Dan Otero",
                33: "Brad Hand",
                28: "Corey Kluber",
            },
            "lefties": [24, 39, 33],
            "lineup": [
                [12, "6"],
                [23, "7"],
                [11, "5"],
                [10, "3"],
                [36, "0"],
                [6, "9"],
                [7, "2"],
                [1, "8"],
                [9, "4"],
            ],
            "bench": [
                [22, "2B"],
                [17, "1B"],
                [53, "LF"],
                [55, "C"],
            ],
            "bullpen": [57, 37, 45, 24, 58, 39, 52, 90, 61, 33, 28],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                5: "Ian Kinsler",
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                3: "Sandy León",
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
                [5, "4"],
                [12, "5"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Jeremie Rehak",
            "1B": "Gerry Davis",
            "2B": "Pat Hoberg",
            "3B": "Brian Knight",
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

# 1. CLE #12 Francisco Lindor (X - X - X)
t1.new_ab()
t1.pitch_list("b c b c f")
t1.hit(2)
t1.advance(4, "10 HR")

# 2. CLE #23 Michael Brantley (X - 12 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.out("L7")

# 3. CLE #11 José Ramírez (X - 12 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b f")
t1.out("P4")

# 4. CLE #10 Edwin Encarnación (X - 12 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b")
t1.hit(4, rbis=2)

# 5. CLE #36 Yandy Díaz (X - X - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(1)

# 6. CLE #6  Brandon Guyer (X - X - 36)
t1.new_ab()
t1.pitch_list("f f b f f s")
t1.out("K")


# Bot 1st
# Pitching: CLE #59 Carlos Carrasco
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b f c s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b c c f")
b1.error(4)
b1.reach("E4")
b1.advance(2, "18 G4-3")
b1.advance(3, "28 WP")
b1.advance("U", "28 1B")

# 3. BOS #18 Mitch Moreland (X - X - 16)
b1.new_ab()
b1.pitch_list("1 b f f")
b1.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("s f b b")
b1.wp()
b1.hit(1, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b1.new_ab()
b1.pitch_list("c f f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 7. CLE #7  Yan Gomes (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.out("F7")

# 8. CLE #1  Greg Allen (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G6-3")

# 9. CLE #9  Erik González (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G6-3")


# Bot 2nd
# Pitching: CLE #59 Carlos Carrasco
b2 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.thrown_out(2, "12 CS", 2, 59)

# 7. BOS #12 Brock Holt (X - X - 5)
b2.new_ab()
b2.pitch_list("b f 1 1 c s")
b2.out("KDP2-6")

# 8. BOS #23 Blake Swihart (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
t3.new_ab()
t3.pitch_list("c f f b b f f f")
t3.out("L9")

# 2. CLE #23 Michael Brantley (X - X - X)
t3.new_ab()
t3.pitch_list("c f")
t3.out("G4-3")

# 3. CLE #11 José Ramírez (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f b")
t3.hit(2)

# 4. CLE #10 Edwin Encarnación (X - 11 - X)
t3.new_ab(is_risp=True)
t3.out("G5-3")


# Bot 3rd
# Pitching: CLE #59 Carlos Carrasco
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b b f f f f")
b3.out("G6-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c t")
b3.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("c b f f 1")
b3.out("F9")

# 3. BOS #18 Mitch Moreland (X - X - 50)
b3.new_ab()
b3.pitch_list("1 b c")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 5. CLE #36 Yandy Díaz (X - X - X)
t4.new_ab()
t4.pitch_list("b b f b")
t4.out("L6")

# 6. CLE #6  Brandon Guyer (X - X - X)
t4.new_ab()
t4.pitch_list("c c f b")
t4.reach("HBP")
t4.advance(2, "7 1B")

# 7. CLE #7  Yan Gomes (X - X - 6)
t4.new_ab()
t4.pitch_list("c f")
t4.hit(1)

# 8. CLE #1  Greg Allen (X - 6 - 7)
t4.new_ab(is_risp=True)
t4.pitch_list("b b c f s")
t4.out("K")

# 9. CLE #9  Erik González (X - 6 - 7)
t4.new_ab(is_risp=True)
t4.pitch_list("c b s b c")
t4.out("!K")


# Bot 4th
# Pitching: CLE #59 Carlos Carrasco
b4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("s f c")
b4.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.hit(4)

# 6. BOS #5  Ian Kinsler (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b c f")
b4.hit(1)
b4.advance(3, "12 1B")
b4.advance(4, "23 1B")

# 7. BOS #12 Brock Holt (X - X - 5)
b4.new_ab()
b4.hit(1)
b4.advance(2, "23 1B")
b4.advance(3, "50 BB")
b4.advance(4, "16 2B")

# 8. BOS #23 Blake Swihart (5 - X - 12)
b4.new_ab(is_risp=True)
b4.hit(1, rbis=1)
b4.advance(2, "50 BB")
b4.advance(4, "16 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - 23)
b4.new_ab(is_risp=True)
b4.pitch_list("f b s s")
b4.out("K")

# 1. BOS #50 Mookie Betts (X - 12 - 23)
b4.new_ab(is_risp=True)
b4.pitch_list("b b b b")
b4.reach("BB")
b4.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (12 - 23 - 50)
b4.new_ab(is_risp=True)
b4.pitch_list("b c f")
b4.hit(2, rbis=3)
b4.advance(3, "18 1B")

# Pitching change (CLE): #39 Oliver Pérez replaces #59 Carlos Carrasco
b4.pitching_substitution(39)

# 3. BOS #18 Mitch Moreland (X - 16 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("s b")
b4.hit(1)
b4.advance(2, "28 BB")
b4.thrown_out(3, "2 FC5", 3, 58)

# Pitching change (CLE): #58 Neil Ramírez replaces #39 Oliver Pérez
b4.pitching_substitution(58)

# 4. BOS #28 J.D. Martinez (16 - X - 18)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b d c b")
b4.reach("BB")
b4.advance(2, "2 FC5")

# 5. BOS #2  Xander Bogaerts (16 - 18 - 28)
b4.new_ab(is_risp=True)
b4.pitch_list("b c c")
b4.reach("FC5")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.advance(4, "10 HR")

# 2. CLE #23 Michael Brantley (X - X - 12)
t5.new_ab()
t5.pitch_list("b b c")
t5.out("L7")

# Pitching change (BOS): #37 Heath Hembree replaces #61 Brian Johnson
t5.pitching_substitution(37)

# 3. CLE #11 José Ramírez (X - X - 12)
t5.new_ab()
t5.pitch_list("c")
t5.out("F8")

# 4. CLE #10 Edwin Encarnación (X - X - 12)
t5.new_ab()
t5.pitch_list("b b 1 b c")
t5.hit(4, rbis=2)

# 5. CLE #36 Yandy Díaz (X - X - X)
t5.new_ab()
t5.pitch_list("c b f c")
t5.out("!K")


# Bot 5th
# Pitching: CLE #58 Neil Ramírez
b5 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c f b s")
b5.out("K")

# 7. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("c s f b b")
b5.out("G3")

# 8. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("s c f f f f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Brandon Workman
t6 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree
t6.pitching_substitution(44)

# 6. CLE #6  Brandon Guyer (X - X - X)
t6.new_ab()
t6.pitch_list("c c s")
t6.out("K")

# 7. CLE #7  Yan Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("c f")
t6.hit(1)
t6.thrown_out(2, "8-4", 2, 44)

# 8. CLE #1  Greg Allen (X - X - X)
t6.new_ab()
t6.pitch_list("b f c")
t6.out("F8")


# Bot 6th
# Pitching: CLE #58 Neil Ramírez
b6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.hit(2)
b6.advance(3, "16 G4-3")
b6.advance(4, "18 HR")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b d f c")
b6.out("F8")

# Pitching change (CLE): #61 Dan Otero replaces #58 Neil Ramírez
b6.pitching_substitution(61)

# 2. BOS #16 Andrew Benintendi (X - 19 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("t c b")
b6.out("G4-3")

# 3. BOS #18 Mitch Moreland (19 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b b s s f")
b6.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b c s b f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Matt Barnes
t7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #44 Brandon Workman
t7.pitching_substitution(32)

# 9. CLE #9  Erik González (X - X - X)
t7.new_ab()
t7.pitch_list("b b f")
t7.out("G3-1")

# 1. CLE #12 Francisco Lindor (X - X - X)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("G1-3")

# 2. CLE #23 Michael Brantley (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("F9")


# Bot 7th
# Pitching: CLE #61 Dan Otero
b7 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.hit(4)

# 6. BOS #5  Ian Kinsler (X - X - X)
b7.new_ab()
b7.pitch_list("f b s b f")
b7.out("G5-3")

# 7. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G6-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("b s")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
t8.pitching_substitution(56)

# 3. CLE #11 José Ramírez (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b")
t8.hit(1)
t8.advance(2, "10 G5-4-3")
t8.advance(3, "53 WP")

# 4. CLE #10 Edwin Encarnación (X - X - 11)
t8.new_ab()
t8.pitch_list("c s d f b f b")
t8.out("G5-4-3")

# 5. CLE #36 Yandy Díaz (X - 11 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b c")
t8.out("L3")

# Offensive change (CLE): Pinch-hitter #53 Melky Cabrera replaces #6 Brandon Guyer, batting 6th
t8.offensive_substitution(6, 53, "PH")

# 6. CLE #53 Melky Cabrera (X - 11 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("s t f b b b b")
t8.wp()
t8.reach("BB")

# 7. CLE #7  Yan Gomes (11 - X - 53)
t8.new_ab(is_risp=True)
t8.pitch_list("c s f s")
t8.out("K")


# Bot 8th
# Pitching: CLE #37 Cody Allen
b8 = game.new_inning()

# Pitching change (CLE): #37 Cody Allen replaces #61 Dan Otero
b8.pitching_substitution(37)

# Defensive switch (CLE): #53 Melky Cabrera moves to RF
b8.defensive_switch(53, "9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.hit(1)
b8.advance(2, "18 BB")
b8.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b8.new_ab()
b8.pitch_list("b f")
b8.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - 19)
b8.new_ab()
b8.pitch_list("c b s f s")
b8.out("K")

# 3. BOS #18 Mitch Moreland (X - X - 19)
b8.new_ab()
b8.pitch_list("f b b b f b")
b8.reach("BB")
b8.advance(2, "28 1B")

# 4. BOS #28 J.D. Martinez (X - 19 - 18)
b8.new_ab(is_risp=True)
b8.pitch_list("b b")
b8.hit(1, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - 18 - 28)
b8.new_ab(is_risp=True)
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #70 Ryan Brasier
t9 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly
t9.pitching_substitution(70)

# 8. CLE #1  Greg Allen (X - X - X)
t9.new_ab()
t9.pitch_list("c f b f b f f")
t9.out("L7")

# 9. CLE #9  Erik González (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G3")

# 1. CLE #12 Francisco Lindor (X - X - X)
t9.new_ab()
t9.pitch_list("b f b f")
t9.out("L3")

# Winning team: BOS
# WP: BOS #32 Matt Barnes
game.winning_pitcher(32)

# Loser team: CLE
# LP: CLE #59 Carlos Carrasco
game.losing_pitcher(59, is_away_team=True)

# print(game)
game.generate_scorecard()
