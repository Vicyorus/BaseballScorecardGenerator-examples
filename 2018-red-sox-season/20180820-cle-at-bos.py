import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2018-08-20
# https://www.baseball-reference.com/boxes/BOS/BOS201808200.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2018/08/20/531282/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-20 19:10-22:11",
        "at": "Fenway Park, Boston, MA",
        "att": "37,274",
        "temp": "70F, Partly Cloudy",
        "wind": "13mph, In From RF",
        "away": {
            "team": "Cleveland Indians",
            "starter": 28,
            "roster": {
                # Lineup
                12: "Francisco Lindor",
                23: "Michael Brantley",
                11: "José Ramírez",
                36: "Yandy Díaz",
                17: "Yonder Alonso",
                53: "Melky Cabrera",
                22: "Jason Kipnis",
                7: "Yan Gomes",
                1: "Greg Allen",
                # Starting pitcher
                28: "Corey Kluber",
                # Bench
                9: "Erik González",
                6: "Brandon Guyer",
                55: "Roberto Pérez",
                # Bullpen
                57: "Shane Bieber",
                39: "Oliver Pérez",
                37: "Cody Allen",
                45: "Adam Plutko",
                52: "Mike Clevinger",
                90: "Adam Cimber",
                24: "Andrew Miller",
                61: "Dan Otero",
                59: "Carlos Carrasco",
                58: "Neil Ramírez",
                33: "Brad Hand",
            },
            "lefties": [39, 24, 33],
            "lineup": [
                [12, "6"],
                [23, "7"],
                [11, "5"],
                [36, "0"],
                [17, "3"],
                [53, "9"],
                [22, "4"],
                [7, "2"],
                [1, "8"],
            ],
            "bench": [
                [9, "SS"],
                [6, "LF"],
                [55, "C"],
            ],
            "bullpen": [57, 39, 37, 45, 52, 90, 24, 61, 59, 58, 33],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                5: "Ian Kinsler",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
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
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [5, "4"],
                [12, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Pat Hoberg",
            "1B": "Brian Knight",
            "2B": "Jeremie Rehak",
            "3B": "Gerry Davis",
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

# 1. CLE #12 Francisco Lindor (X - X - X)
t1.new_ab()
t1.pitch_list("c f c")
t1.out("!K")

# 2. CLE #23 Michael Brantley (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("G4-3")

# 3. CLE #11 José Ramírez (X - X - X)
t1.new_ab()
t1.pitch_list("c c c")
t1.out("!K")


# Bot 1st
# Pitching: CLE #28 Corey Kluber
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b s f s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b s c f f c")
b1.out("!K")

# 3. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("c s f f b")
b1.hit(1)
b1.advance(3, "28 2B")
b1.advance(4, "2 1B")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b1.new_ab()
b1.pitch_list("b d")
b1.hit(2)
b1.advance(4, "2 1B")

# 5. BOS #2  Xander Bogaerts (18 - 28 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c t f")
b1.hit(1, rbis=2)

# 6. BOS #5  Ian Kinsler (X - X - 2)
b1.new_ab()
b1.pitch_list("b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. CLE #36 Yandy Díaz (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G6-3")

# 5. CLE #17 Yonder Alonso (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.hit(1)
t2.advance(2, "53 1B")
t2.advance(3, "7 WP")

# 6. CLE #53 Melky Cabrera (X - X - 17)
t2.new_ab()
t2.hit(1)
t2.advance(2, "7 WP")

# 7. CLE #22 Jason Kipnis (X - 17 - 53)
t2.new_ab(is_risp=True)
t2.pitch_list("c b d f b f t")
t2.out("KT")

# 8. CLE #7  Yan Gomes (X - 17 - 53)
t2.new_ab(is_risp=True)
t2.pitch_list("b f c b t")
t2.wp()
t2.out("KT")


# Bot 2nd
# Pitching: CLE #28 Corey Kluber
b2 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("b b f")
b2.out("L8")

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.hit(2)
b2.advance(3, "50 1B")
b2.advance(4, "16 1B")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "16 1B")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b2.new_ab(is_risp=True)
b2.pitch_list("s b b")
b2.hit(1, rbis=1)

# 3. BOS #18 Mitch Moreland (X - 50 - 16)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.out("G3-1")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 9. CLE #1  Greg Allen (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b")
t3.out("L9")

# 1. CLE #12 Francisco Lindor (X - X - X)
t3.new_ab()
t3.pitch_list("b f b b c f")
t3.out("(F)P5")

# 2. CLE #23 Michael Brantley (X - X - X)
t3.new_ab()
t3.pitch_list("c b f")
t3.out("G3")


# Bot 3rd
# Pitching: CLE #28 Corey Kluber
b3 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("f b s")
b3.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("c b s")
b3.out("G6-3")

# 6. BOS #5  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 3. CLE #11 José Ramírez (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("(F)P3")

# 4. CLE #36 Yandy Díaz (X - X - X)
t4.new_ab()
t4.pitch_list("b c s s")
t4.out("K")

# 5. CLE #17 Yonder Alonso (X - X - X)
t4.new_ab()
t4.pitch_list("c f f f s")
t4.out("K")


# Bot 4th
# Pitching: CLE #28 Corey Kluber
b4 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "3 CS", 1, 28)

# 8. BOS #3  Sandy León (X - X - 12)
b4.new_ab()
b4.pitch_list("1 s b c f f s")
b4.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b s s")
b4.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 19)
b4.new_ab()
b4.pitch_list("c 1 1 b s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 6. CLE #53 Melky Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(4)

# 7. CLE #22 Jason Kipnis (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G3-1")

# 8. CLE #7  Yan Gomes (X - X - X)
t5.new_ab()
t5.pitch_list("b f b f f f b")
t5.out("F9")

# 9. CLE #1  Greg Allen (X - X - X)
t5.new_ab()
t5.pitch_list("c c b b")
t5.out("L7")


# Bot 5th
# Pitching: CLE #28 Corey Kluber
b5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("b b c b s c")
b5.out("!K")

# 3. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("b f b b b")
b5.reach("BB")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b5.new_ab()
b5.pitch_list("f b b b f s")
b5.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - 18)
b5.new_ab()
b5.pitch_list("b b b c f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(4, "23 HR")

# 2. CLE #23 Michael Brantley (X - X - 12)
t6.new_ab()
t6.pitch_list("1 1 b")
t6.hit(4, rbis=2)

# 3. CLE #11 José Ramírez (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.out("P5")

# 4. CLE #36 Yandy Díaz (X - X - X)
t6.new_ab()
t6.out("G1-3")

# 5. CLE #17 Yonder Alonso (X - X - X)
t6.new_ab()
t6.pitch_list("c b s f f b")
t6.out("F9")


# Bot 6th
# Pitching: CLE #28 Corey Kluber
b6 = game.new_inning()

# 6. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1)

# 7. BOS #12 Brock Holt (X - X - 5)
b6.new_ab()
b6.pitch_list("c b 1 b")
b6.out("L7")

# 8. BOS #3  Sandy León (X - X - 5)
b6.new_ab()
b6.pitch_list("c 1 b")
b6.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 5)
b6.new_ab()
b6.pitch_list("1 b 1 1 b")
b6.out("(F)P2")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #22 Rick Porcello
t7 = game.new_inning()

# 6. CLE #53 Melky Cabrera (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G3-1")

# 7. CLE #22 Jason Kipnis (X - X - X)
t7.new_ab()
t7.pitch_list("b b f f b b")
t7.reach("BB")
t7.thrown_out(2, "7 FC1-4", 2, 22)

# 8. CLE #7  Yan Gomes (X - X - 22)
t7.new_ab()
t7.pitch_list("b")
t7.reach("FC1-4")
t7.advance(4, "1 HR")

# 9. CLE #1  Greg Allen (X - X - 7)
t7.new_ab()
t7.pitch_list("d")
t7.hit(4, rbis=2)

# 1. CLE #12 Francisco Lindor (X - X - X)
t7.new_ab()
t7.pitch_list("b c t f b f")
t7.out("F8")


# Bot 7th
# Pitching: CLE #28 Corey Kluber
b7 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G6-3")

# Pitching change (CLE): #39 Oliver Pérez replaces #28 Corey Kluber
b7.pitching_substitution(39)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.out("G3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("f b b f b b")
b7.reach("BB")
b7.advance(3, "28 1B")

# Pitching change (CLE): #90 Adam Cimber replaces #39 Oliver Pérez
b7.pitching_substitution(90)

# 4. BOS #28 J.D. Martinez (X - X - 18)
b7.new_ab()
b7.pitch_list("c c")
b7.hit(1)

# 5. BOS #2  Xander Bogaerts (18 - X - 28)
b7.new_ab(is_risp=True)
b7.pitch_list("b c")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #47 Tyler Thornburg
t8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #22 Rick Porcello
t8.pitching_substitution(47)

# 2. CLE #23 Michael Brantley (X - X - X)
t8.new_ab()
t8.pitch_list("c f")
t8.hit(1)

# 3. CLE #11 José Ramírez (X - X - 23)
t8.new_ab()
t8.pitch_list("b b f 1 b")
t8.out("P5")

# 4. CLE #36 Yandy Díaz (X - X - 23)
t8.new_ab()
t8.pitch_list("c f b s")
t8.out("K")

# 5. CLE #17 Yonder Alonso (X - X - 23)
t8.new_ab()
t8.out("L9")


# Bot 8th
# Pitching: CLE #90 Adam Cimber
b8 = game.new_inning()

# Defensive change (CLE): #6 Brandon Guyer replaces #53 Melky Cabrera (RF), playing RF, batting 6th
b8.defensive_substitution(6, 6, "9")

# 6. BOS #5  Ian Kinsler (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b f f f s")
b8.out("K")

# Pitching change (CLE): #33 Brad Hand replaces #90 Adam Cimber
b8.pitching_substitution(33)

# Offensive change (BOS): Pinch-hitter #36 Eduardo Núñez replaces #12 Brock Holt, batting 7th
b8.offensive_substitution(7, 36, "PH")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F9")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #3 Sandy León, batting 8th
b8.offensive_substitution(8, 25, "PH")

# 8. BOS #25 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)

# 9. BOS #19 Jackie Bradley Jr. (X - 25 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b c b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #31 Drew Pomeranz
t9 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #47 Tyler Thornburg
t9.pitching_substitution(31)

# Defensive switch (BOS): #36 Eduardo Núñez moves to 3B
t9.defensive_switch(36, "5")

# Defensive change (BOS): #23 Blake Swihart replaces #25 Steve Pearce (PH), playing C, batting 8th
t9.defensive_substitution(8, 23, "2")

# 6. CLE #6  Brandon Guyer (X - X - X)
t9.new_ab()
t9.pitch_list("b f c f b")
t9.out("L8")

# 7. CLE #22 Jason Kipnis (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b s")
t9.out("K")

# 8. CLE #7  Yan Gomes (X - X - X)
t9.new_ab()
t9.out("G5-3")


# Bot 9th
# Pitching: CLE #37 Cody Allen
b9 = game.new_inning()

# Pitching change (CLE): #37 Cody Allen replaces #33 Brad Hand
b9.pitching_substitution(37)

# 1. BOS #50 Mookie Betts (X - X - X)
b9.new_ab()
b9.pitch_list("b c")
b9.hit(2)
b9.advance(3, "18 FC4-6")
b9.advance(4, "2 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b9.new_ab(is_risp=True)
b9.pitch_list("b s b f b f b")
b9.reach("BB")
b9.thrown_out(2, "18 FC4-6", 1, 37)

# 3. BOS #18 Mitch Moreland (X - 50 - 16)
b9.new_ab(is_risp=True)
b9.pitch_list("b b")
b9.reach("FC4-6")
b9.advance(2, "2 1B")

# 4. BOS #28 J.D. Martinez (50 - X - 18)
b9.new_ab(is_risp=True)
b9.pitch_list("b f f")
b9.out("P3")

# 5. BOS #2  Xander Bogaerts (50 - X - 18)
b9.new_ab(is_risp=True)
b9.pitch_list("c c")
b9.hit(1, rbis=1)

# 6. BOS #5  Ian Kinsler (X - 18 - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("b f b f f f b")
b9.out("F7")

# Winning team: CLE
# WP: CLE #28 Corey Kluber
game.winning_pitcher(28, is_away_team=True)
# SV: CLE #37 Cody Allen
game.save_pitcher(37, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
