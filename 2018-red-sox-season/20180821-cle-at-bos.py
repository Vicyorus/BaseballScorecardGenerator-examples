import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2018-08-21
# https://www.baseball-reference.com/boxes/BOS/BOS201808210.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2018/08/21/531292/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-21 19:12-22:09",
        "at": "Fenway Park, Boston, MA",
        "att": "37,188",
        "temp": "70F, Partly Cloudy",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Cleveland Indians",
            "starter": 57,
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
                57: "Shane Bieber",
                # Bench
                9: "Erik González",
                6: "Brandon Guyer",
                55: "Roberto Pérez",
                # Bullpen
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
                28: "Corey Kluber",
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
            "bullpen": [39, 37, 45, 52, 90, 24, 61, 59, 58, 33, 28],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [5, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Brian Knight",
            "1B": "Jeremie Rehak",
            "2B": "Gerry Davis",
            "3B": "Pat Hoberg",
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
# Pitching: BOS #17 Nathan Eovaldi
t1 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("(F)P5")

# 2. CLE #23 Michael Brantley (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.out("G1-3")

# 3. CLE #11 José Ramírez (X - X - X)
t1.new_ab()
t1.pitch_list("c c")
t1.out("G1-3")


# Bot 1st
# Pitching: CLE #57 Shane Bieber
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c s b f b b f c")
b1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b c f")
b1.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c b b s f b f c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #17 Nathan Eovaldi
t2 = game.new_inning()

# 4. CLE #36 Yandy Díaz (X - X - X)
t2.new_ab()
t2.pitch_list("c f")
t2.hit(1)
t2.advance(3, "53 2B")
t2.thrown_out(4, "22 FC3-2", 2, 17)

# 5. CLE #17 Yonder Alonso (X - X - 36)
t2.new_ab()
t2.pitch_list("c b s 1 f f s")
t2.out("K")

# 6. CLE #53 Melky Cabrera (X - X - 36)
t2.new_ab()
t2.pitch_list("c b f b b")
t2.hit(2)
t2.advance(3, "22 FC3-2")

# 7. CLE #22 Jason Kipnis (36 - 53 - X)
t2.new_ab()
t2.pitch_list("c")
t2.reach("FC3-2")

# 8. CLE #7  Yan Gomes (53 - X - 22)
t2.new_ab()
t2.pitch_list("f b")
t2.out("F8")


# Bot 2nd
# Pitching: CLE #57 Shane Bieber
b2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("P3")

# 5. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c c s")
b2.out("K")

# 6. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.pitch_list("b b f f")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #17 Nathan Eovaldi
t3 = game.new_inning()

# 9. CLE #1  Greg Allen (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("G2-3")

# 1. CLE #12 Francisco Lindor (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G6-3")

# 2. CLE #23 Michael Brantley (X - X - X)
t3.new_ab()
t3.pitch_list("b b c b b")
t3.reach("BB")

# 3. CLE #11 José Ramírez (X - X - 23)
t3.new_ab()
t3.pitch_list("f c b")
t3.out("G3")


# Bot 3rd
# Pitching: CLE #57 Shane Bieber
b3 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G6-3")

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("b s c c")
b3.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #17 Nathan Eovaldi
t4 = game.new_inning()

# 4. CLE #36 Yandy Díaz (X - X - X)
t4.new_ab()
t4.out("L9")

# 5. CLE #17 Yonder Alonso (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G3-1")

# 6. CLE #53 Melky Cabrera (X - X - X)
t4.new_ab()
t4.pitch_list("c c")
t4.hit(1)
t4.advance(3, "22 1B")
t4.advance(4, "7 1B")

# 7. CLE #22 Jason Kipnis (X - X - 53)
t4.new_ab()
t4.hit(1)
t4.advance(2, "7 1B")
t4.advance(4, "1 2B")

# 8. CLE #7  Yan Gomes (53 - X - 22)
t4.new_ab()
t4.pitch_list("f b")
t4.hit(1, rbis=1)
t4.advance(3, "1 2B")

# 9. CLE #1  Greg Allen (X - 22 - 7)
t4.new_ab()
t4.hit(2, rbis=1)

# 1. CLE #12 Francisco Lindor (7 - 1 - X)
t4.new_ab()
t4.pitch_list("f")
t4.out("F7")


# Bot 4th
# Pitching: CLE #57 Shane Bieber
b4 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b b f")
b4.hit(1)
b4.thrown_out(2, "28 DP6-4-3", 2, 57)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b4.new_ab()
b4.pitch_list("b b")
b4.out("DP6-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #17 Nathan Eovaldi
t5 = game.new_inning()

# 2. CLE #23 Michael Brantley (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(2)
t5.advance(3, "36 G4-3")

# 3. CLE #11 José Ramírez (X - 23 - X)
t5.new_ab()
t5.pitch_list("c b f b f s")
t5.out("K")

# 4. CLE #36 Yandy Díaz (X - 23 - X)
t5.new_ab()
t5.pitch_list("d b b")
t5.out("G4-3")

# 5. CLE #17 Yonder Alonso (23 - X - X)
t5.new_ab()
t5.out("G3")


# Bot 5th
# Pitching: CLE #57 Shane Bieber
b5 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.out("F8")

# 5. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("F8")

# 6. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #17 Nathan Eovaldi
t6 = game.new_inning()

# 6. CLE #53 Melky Cabrera (X - X - X)
t6.new_ab()
t6.pitch_list("f f b f")
t6.hit(4)

# 7. CLE #22 Jason Kipnis (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("F7")

# 8. CLE #7  Yan Gomes (X - X - X)
t6.new_ab()
t6.pitch_list("b s b s")
t6.hit(1)
t6.advance(2, "1 1B")
t6.advance(4, "23 1B")

# 9. CLE #1  Greg Allen (X - X - 7)
t6.new_ab()
t6.pitch_list("c c")
t6.hit(1)
t6.advance(3, "23 1B")

# Pitching change (BOS): #56 Joe Kelly replaces #17 Nathan Eovaldi
t6.pitching_substitution(56)

# 1. CLE #12 Francisco Lindor (X - 7 - 1)
t6.new_ab()
t6.pitch_list("c s b f f f f s")
t6.out("K")

# 2. CLE #23 Michael Brantley (X - 7 - 1)
t6.new_ab()
t6.pitch_list("b f c b")
t6.hit(1, rbis=1)
t6.thrown_out(2, "8-2-6", 3, 56)


# Bot 6th
# Pitching: CLE #57 Shane Bieber
b6 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(2)

# 8. BOS #3  Sandy León (X - 36 - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - 36 - X)
b6.new_ab()
b6.pitch_list("b c c f b f b")
b6.out("L9")

# 1. BOS #50 Mookie Betts (X - 36 - X)
b6.new_ab()
b6.pitch_list("b c c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #44 Brandon Workman
t7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #56 Joe Kelly
t7.pitching_substitution(44)

# 3. CLE #11 José Ramírez (X - X - X)
t7.new_ab()
t7.pitch_list("b c c b f b d")
t7.reach("BB")
t7.advance(2, "36 SB")
t7.advance(3, "36 G6-3")
t7.advance(4, "17 SF9")

# 4. CLE #36 Yandy Díaz (X - X - 11)
t7.new_ab()
t7.pitch_list("1 c")
t7.out("G6-3")

# 5. CLE #17 Yonder Alonso (11 - X - X)
t7.new_ab()
t7.pitch_list("c c d")
t7.out("SF9", rbis=1)

# 6. CLE #53 Melky Cabrera (X - X - X)
t7.new_ab()
t7.pitch_list("c b s c")
t7.out("!K")


# Bot 7th
# Pitching: CLE #57 Shane Bieber
b7 = game.new_inning()

# Defensive change (CLE): #6 Brandon Guyer replaces #53 Melky Cabrera (RF), playing RF, batting 6th
b7.defensive_substitution(6, 6, "9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.hit(2)
b7.advance(3, "28 1B")
b7.advance(4, "2 2B")

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b7.new_ab()
b7.hit(1)
b7.advance(3, "2 2B")
b7.advance(4, "18 SF8")

# 4. BOS #2  Xander Bogaerts (16 - X - 28)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2, rbis=1)
b7.advance(3, "18 SF8")
b7.advance(4, "5 G4-3")

# 5. BOS #18 Mitch Moreland (28 - 2 - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.out("SF8", rbis=1)

# Pitching change (CLE): #90 Adam Cimber replaces #57 Shane Bieber
b7.pitching_substitution(90)

# 6. BOS #5  Ian Kinsler (2 - X - X)
b7.new_ab()
b7.pitch_list("b f b b")
b7.out("G4-3", rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #47 Tyler Thornburg
t8 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #44 Brandon Workman
t8.pitching_substitution(47)

# 7. CLE #22 Jason Kipnis (X - X - X)
t8.new_ab()
t8.pitch_list("b c s s")
t8.out("K")

# 8. CLE #7  Yan Gomes (X - X - X)
t8.new_ab()
t8.pitch_list("b c c b")
t8.hit(4)

# 9. CLE #1  Greg Allen (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.reach("HBP")

# 1. CLE #12 Francisco Lindor (X - X - 1)
t8.new_ab()
t8.pitch_list("b c 1")
t8.out("P5")

# 2. CLE #23 Michael Brantley (X - X - 1)
t8.new_ab()
t8.pitch_list("b f 1 b c f f f")
t8.out("L4")


# Bot 8th
# Pitching: CLE #24 Andrew Miller
b8 = game.new_inning()

# Pitching change (CLE): #24 Andrew Miller replaces #90 Adam Cimber
b8.pitching_substitution(24)

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #3 Sandy León, batting 8th
b8.offensive_substitution(8, 25, "PH")

# 8. BOS #25 Steve Pearce (X - X - X)
b8.new_ab()
b8.pitch_list("b c s f b s")
b8.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("s s b b s")
b8.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #31 Drew Pomeranz
t9 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #47 Tyler Thornburg
t9.pitching_substitution(31)

# Defensive change (BOS): #23 Blake Swihart replaces #25 Steve Pearce (PH), playing C, batting 8th
t9.defensive_substitution(8, 23, "2")

# 3. CLE #11 José Ramírez (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b b b")
t9.reach("BB")
t9.thrown_out(2, "36 DP6-3", 1, 31)

# 4. CLE #36 Yandy Díaz (X - X - 11)
t9.new_ab()
t9.pitch_list("b c f f 1 1 b")
t9.out("DP6-3")

# 5. CLE #17 Yonder Alonso (X - X - X)
t9.new_ab()
t9.pitch_list("f s")
t9.hit(1)

# 6. CLE #6  Brandon Guyer (X - X - 17)
t9.new_ab()
t9.pitch_list("c b t f f f")
t9.out("L5")


# Bot 9th
# Pitching: CLE #33 Brad Hand
b9 = game.new_inning()

# Pitching change (CLE): #33 Brad Hand replaces #24 Andrew Miller
b9.pitching_substitution(33)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("c b c b s")
b9.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.out("L6")

# 4. BOS #2  Xander Bogaerts (X - X - X)
b9.new_ab()
b9.pitch_list("c s b b")
b9.error(4)
b9.reach("E4")
b9.advance(2, "18 DI")

# 5. BOS #18 Mitch Moreland (X - X - 2)
b9.new_ab()
b9.pitch_list("c s f b s")
b9.out("K")

# Winning team: CLE
# WP: CLE #57 Shane Bieber
game.winning_pitcher(57, is_away_team=True)
# SV: CLE #33 Brad Hand
game.save_pitcher(33, is_away_team=True)

# Loser team: BOS
# LP: BOS #17 Nathan Eovaldi
game.losing_pitcher(17)

# print(game)
game.generate_scorecard()
