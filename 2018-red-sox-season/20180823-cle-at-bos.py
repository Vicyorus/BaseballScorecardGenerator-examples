import os
from baseball_scorecard.baseball_scorecard import Scorecard

# CLE @ BOS, 2018-08-23
# https://www.baseball-reference.com/boxes/BOS/BOS201808230.shtml
# https://www.mlb.com/gameday/indians-vs-red-sox/2018/08/23/531321/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-23 13:05-15:52",
        "at": "Fenway Park, Boston, MA",
        "att": "37,396",
        "temp": "72F, Cloudy",
        "wind": "14mph, L To R",
        "away": {
            "team": "Cleveland Indians",
            "starter": 45,
            "roster": {
                # Lineup
                12: "Francisco Lindor",
                36: "Yandy Díaz",
                11: "José Ramírez",
                10: "Edwin Encarnación",
                53: "Melky Cabrera",
                6: "Brandon Guyer",
                22: "Jason Kipnis",
                55: "Roberto Pérez",
                1: "Greg Allen",
                # Starting pitcher
                45: "Adam Plutko",
                # Bench
                9: "Erik González",
                7: "Yan Gomes",
                23: "Michael Brantley",
                17: "Yonder Alonso",
                # Bullpen
                57: "Shane Bieber",
                37: "Cody Allen",
                24: "Andrew Miller",
                59: "Carlos Carrasco",
                39: "Oliver Pérez",
                52: "Mike Clevinger",
                90: "Adam Cimber",
                61: "Dan Otero",
                33: "Brad Hand",
                28: "Corey Kluber",
                43: "Josh Tomlin",
            },
            "lefties": [24, 39, 33],
            "lineup": [
                [12, "6"],
                [36, "0"],
                [11, "5"],
                [10, "3"],
                [53, "7"],
                [6, "9"],
                [22, "4"],
                [55, "2"],
                [1, "8"],
            ],
            "bench": [
                [9, "SS"],
                [7, "C"],
                [23, "DH"],
                [17, "1B"],
            ],
            "bullpen": [57, 37, 24, 59, 39, 52, 90, 61, 33, 28, 43],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                25: "Steve Pearce",
                5: "Ian Kinsler",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [24, 31, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [12, "4"],
                [36, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [5, "2B"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Gerry Davis",
            "1B": "Pat Hoberg",
            "2B": "Brian Knight",
            "3B": "Jeremie Rehak",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
t1.new_ab()
t1.pitch_list("c b s f b")
t1.out("L9")

# 2. CLE #36 Yandy Díaz (X - X - X)
t1.new_ab()
t1.pitch_list("c f f f f b b")
t1.out("G6-3")

# 3. CLE #11 José Ramírez (X - X - X)
t1.new_ab()
t1.pitch_list("s b c b b c")
t1.out("!K")


# Bot 1st
# Pitching: CLE #45 Adam Plutko
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c c s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b b s b")
b1.reach("BB")
b1.advance(2, "18 1B")

# 3. BOS #18 Mitch Moreland (X - X - 16)
b1.new_ab()
b1.pitch_list("b b t 1 s")
b1.hit(1)
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #18 Mitch Moreland
b1.offensive_substitution(3, 23, "PR")
b1.atbase("PR")

# 4. BOS #28 J.D. Martinez (X - 16 - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("d b c f f c")
b1.out("!K")

# 5. BOS #2  Xander Bogaerts (X - 16 - 23)
b1.new_ab(is_risp=True)
b1.pitch_list("c c f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to 1B
t2.defensive_switch(23, "3")

# 4. CLE #10 Edwin Encarnación (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c b")
t2.out("G5-3")

# 5. CLE #53 Melky Cabrera (X - X - X)
t2.new_ab()
t2.pitch_list("c b b c c")
t2.out("!K")

# 6. CLE #6  Brandon Guyer (X - X - X)
t2.new_ab()
t2.pitch_list("s c b")
t2.out("G5-3")


# Bot 2nd
# Pitching: CLE #45 Adam Plutko
b2 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.out("F9")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c b c f b b s")
b2.out("K")

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f f f f b f")
b2.out("P5")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 7. CLE #22 Jason Kipnis (X - X - X)
t3.new_ab()
t3.out("G4-3")

# 8. CLE #55 Roberto Pérez (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b s")
t3.out("K")

# 9. CLE #1  Greg Allen (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(1)
t3.advance(2, "12 SB")

# 1. CLE #12 Francisco Lindor (X - X - 1)
t3.new_ab(is_risp=True)
t3.pitch_list("c b f n 1 t")
t3.out("KT")


# Bot 3rd
# Pitching: CLE #45 Adam Plutko
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f f")
b3.hit(1)
b3.thrown_out(2, "50 FC6-4", 1, 45)

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab()
b3.pitch_list("s f b b f 1")
b3.reach("FC6-4")
b3.thrown_out(2, "16 CS", 2, 45)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("1 b c b")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 2. CLE #36 Yandy Díaz (X - X - X)
t4.new_ab()
t4.pitch_list("b c f f")
t4.out("F9")

# 3. CLE #11 José Ramírez (X - X - X)
t4.new_ab()
t4.pitch_list("f s f")
t4.out("L6")

# 4. CLE #10 Edwin Encarnación (X - X - X)
t4.new_ab()
t4.out("F9")


# Bot 4th
# Pitching: CLE #45 Adam Plutko
b4 = game.new_inning()

# 3. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.pitch_list("b f f")
b4.out("G3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b b")
b4.reach("BB")
b4.advance(2, "12 BB")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b4.new_ab()
b4.out("F9")

# 6. BOS #12 Brock Holt (X - X - 28)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - 28 - 12)
b4.new_ab(is_risp=True)
b4.pitch_list("b s f")
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 5. CLE #53 Melky Cabrera (X - X - X)
t5.new_ab()
t5.pitch_list("l b b f s")
t5.out("K")

# 6. CLE #6  Brandon Guyer (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("P4")

# 7. CLE #22 Jason Kipnis (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G3-1")


# Bot 5th
# Pitching: CLE #45 Adam Plutko
b5 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b f f f f f")
b5.hit(2)
b5.advance(3, "19 1B")
b5.advance(4, "23 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - 3 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f")
b5.hit(1)
b5.advance(2, "16 BB")
b5.advance(4, "23 2B")

# 1. BOS #50 Mookie Betts (3 - X - 19)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.out("F7")

# 2. BOS #16 Andrew Benintendi (3 - X - 19)
b5.new_ab(is_risp=True)
b5.pitch_list("c b b b f b")
b5.reach("BB")
b5.advance(3, "23 2B")
b5.advance(4, "2 2B")

# 3. BOS #23 Blake Swihart (3 - 19 - 16)
b5.new_ab(is_risp=True)
b5.pitch_list("f b c b f f")
b5.hit(2, rbis=2)
b5.advance(4, "2 2B")

# 4. BOS #28 J.D. Martinez (16 - 23 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("v v v v")
b5.reach("IBB")
b5.advance(3, "2 2B")
b5.advance(4, "36 2B")

# Pitching change (CLE): #90 Adam Cimber replaces #45 Adam Plutko
b5.pitching_substitution(90)

# 5. BOS #2  Xander Bogaerts (16 - 23 - 28)
b5.new_ab(is_risp=True)
b5.pitch_list("b f s")
b5.hit(2, rbis=2)
b5.advance(4, "36 2B")

# 6. BOS #12 Brock Holt (28 - 2 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("v v v v")
b5.reach("IBB")
b5.advance(3, "36 2B")

# 7. BOS #36 Eduardo Núñez (28 - 2 - 12)
b5.new_ab(is_risp=True)
b5.hit(2, rbis=2)

# Pitching change (CLE): #39 Oliver Pérez replaces #90 Adam Cimber
b5.pitching_substitution(39)

# 8. BOS #3  Sandy León (12 - 36 - X)
b5.new_ab(is_risp=True)
b5.out("P6")

# 9. BOS #19 Jackie Bradley Jr. (12 - 36 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b s s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 8. CLE #55 Roberto Pérez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G1-3")

# 9. CLE #1  Greg Allen (X - X - X)
t6.new_ab()
t6.pitch_list("c c f f b s")
t6.out("K")

# 1. CLE #12 Francisco Lindor (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F9")


# Bot 6th
# Pitching: CLE #43 Josh Tomlin
b6 = game.new_inning()

# Pitching change (CLE): #43 Josh Tomlin replaces #39 Oliver Pérez
b6.pitching_substitution(43)

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.hit(1)
b6.advance(3, "23 1B")
b6.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b6.new_ab()
b6.out("F8")

# 3. BOS #23 Blake Swihart (X - X - 50)
b6.new_ab()
b6.pitch_list("1 c 1 b")
b6.hit(1)
b6.advance(2, "28 1B")
b6.advance(3, "12 1B")

# 4. BOS #28 J.D. Martinez (50 - X - 23)
b6.new_ab(is_risp=True)
b6.pitch_list("b")
b6.hit(1, rbis=1)
b6.advance(2, "12 1B")

# 5. BOS #2  Xander Bogaerts (X - 23 - 28)
b6.new_ab(is_risp=True)
b6.pitch_list("b c b b c s")
b6.out("K")

# 6. BOS #12 Brock Holt (X - 23 - 28)
b6.new_ab(is_risp=True)
b6.hit(1)

# 7. BOS #36 Eduardo Núñez (23 - 28 - 12)
b6.new_ab(is_risp=True)
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 2. CLE #36 Yandy Díaz (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.hit(1)
t7.advance(2, "10 1B")
t7.thrown_out(2, "53 DP6", 3, 24)

# 3. CLE #11 José Ramírez (X - X - 36)
t7.new_ab()
t7.out("L5")

# 4. CLE #10 Edwin Encarnación (X - X - 36)
t7.new_ab()
t7.pitch_list("c f f")
t7.hit(1)

# 5. CLE #53 Melky Cabrera (X - 36 - 10)
t7.new_ab(is_risp=True)
t7.out("DP6")


# Bot 7th
# Pitching: CLE #43 Josh Tomlin
b7 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("c c b")
b7.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c s b s")
b7.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("f b c b")
b7.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b7.new_ab()
b7.pitch_list("c 1 f")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #24 David Price
t8 = game.new_inning()

# 6. CLE #6  Brandon Guyer (X - X - X)
t8.new_ab()
t8.pitch_list("c b b s")
t8.reach("HBP")
t8.thrown_out(2, "22 DP3-6", 2, 24)

# 7. CLE #22 Jason Kipnis (X - X - 6)
t8.new_ab()
t8.pitch_list("b")
t8.out("DP3-6")

# 8. CLE #55 Roberto Pérez (X - X - X)
t8.new_ab()
t8.pitch_list("b s b f f s")
t8.out("K")


# Bot 8th
# Pitching: CLE #43 Josh Tomlin
b8 = game.new_inning()

# Pitching change (CLE): #43 Josh Tomlin replaces #43 Josh Tomlin, batting 4th
b8.pitching_substitution(43)
b8.defensive_substitution(4, 43, "1")

# Defensive switch (CLE): #36 Yandy Díaz moves to 1B
b8.defensive_switch(36, "3")

# Defensive change (CLE): #9 Erik González replaces #11 José Ramírez (3B), playing 3B, batting 3rd
b8.defensive_substitution(3, 9, "5")

# 3. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f")
b8.out("G3-1")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c b b b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #47 Tyler Thornburg
t9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #24 David Price
t9.pitching_substitution(47)

# 9. CLE #1  Greg Allen (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(1)
t9.advance(2, "12 1B")
t9.advance(3, "36 DP6-4-3")

# 1. CLE #12 Francisco Lindor (X - X - 1)
t9.new_ab()
t9.pitch_list("c b b c f b f")
t9.hit(1)
t9.thrown_out(2, "36 DP6-4-3", 1, 47)

# 2. CLE #36 Yandy Díaz (X - 1 - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b d c f f d f f f f")
t9.out("DP6-4-3")

# 3. CLE #9  Erik González (1 - X - X)
t9.new_ab(is_risp=True)
t9.out("F7")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)

# Loser team: CLE
# LP: CLE #45 Adam Plutko
game.losing_pitcher(45, is_away_team=True)

# print(game)
game.generate_scorecard()
