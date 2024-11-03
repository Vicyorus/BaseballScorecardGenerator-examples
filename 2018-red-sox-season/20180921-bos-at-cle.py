import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CLE, 2018-09-21
# https://www.baseball-reference.com/boxes/CLE/CLE201809210.shtml
# https://www.mlb.com/gameday/red-sox-vs-indians/2018/09/21/531699/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-21 19:11-22:45",
        "at": "Progressive Field, Cleveland, OH",
        "att": "27,892",
        "temp": "78F, Partly Cloudy",
        "wind": "9mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                30: "Tzu-Wei Lin",
                0: "Brandon Phillips",
                11: "Rafael Devers",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                12: "Brock Holt",
                23: "Blake Swihart",
                59: "Sam Travis",
                3: "Sandy León",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                16: "Andrew Benintendi",
                50: "Mookie Betts",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 66, 63, 24],
            "lineup": [
                [30, "8"],
                [0, "4"],
                [11, "5"],
                [28, "0"],
                [25, "3"],
                [12, "6"],
                [23, "9"],
                [59, "7"],
                [3, "2"],
            ],
            "bench": [
                [36, "SS"],
                [18, "1B"],
                [5, "2B"],
                [16, "LF"],
                [50, "SS"],
                [2, "2B"],
                [19, "CF"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Cleveland Indians",
            "starter": 47,
            "roster": {
                # Lineup
                12: "Francisco Lindor",
                23: "Michael Brantley",
                11: "José Ramírez",
                10: "Edwin Encarnación",
                27: "Josh Donaldson",
                36: "Yandy Díaz",
                6: "Brandon Guyer",
                7: "Yan Gomes",
                22: "Jason Kipnis",
                # Starting pitcher
                47: "Trevor Bauer",
                # Bench
                1: "Greg Allen",
                9: "Erik González",
                0: "Brandon Barnes",
                17: "Yonder Alonso",
                38: "Eric Haase",
                32: "Adam Rosales",
                53: "Melky Cabrera",
                55: "Roberto Pérez",
                26: "Rajai Davis",
                # Bullpen
                57: "Shane Bieber",
                46: "Jon Edwards",
                37: "Cody Allen",
                45: "Adam Plutko",
                49: "Tyler Olson",
                24: "Andrew Miller",
                59: "Carlos Carrasco",
                58: "Neil Ramírez",
                39: "Oliver Pérez",
                52: "Mike Clevinger",
                90: "Adam Cimber",
                61: "Dan Otero",
                33: "Brad Hand",
                28: "Corey Kluber",
                43: "Josh Tomlin",
            },
            "lefties": [49, 24, 39, 33],
            "lineup": [
                [12, "6"],
                [23, "7"],
                [11, "4"],
                [10, "3"],
                [27, "0"],
                [36, "5"],
                [6, "9"],
                [7, "2"],
                [22, "8"],
            ],
            "bench": [
                [1, "CF"],
                [9, "SS"],
                [0, "CF"],
                [17, "1B"],
                [38, "C"],
                [32, "SS"],
                [53, "LF"],
                [55, "C"],
                [26, "CF"],
            ],
            "bullpen": [57, 46, 37, 45, 49, 24, 59, 58, 39, 52, 90, 61, 33, 28, 43],
        },
        "umpires": {
            "HP": "Jordan Baker",
            "1B": "Greg Gibson",
            "2B": "Vic Carapazza",
            "3B": "Jerry Layne",
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
# Pitching: CLE #47 Trevor Bauer
t1 = game.new_inning()

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
t1.new_ab()
t1.pitch_list("t b b b")
t1.out("L8")

# 2. BOS #0  Brandon Phillips (X - X - X)
t1.new_ab()
t1.pitch_list("s f b f b b b")
t1.reach("BB")
t1.thrown_out(2, "28 2-4", 3, 47)

# 3. BOS #11 Rafael Devers (X - X - 0)
t1.new_ab()
t1.pitch_list("b d b s")
t1.out("F7")

# 4. BOS #28 J.D. Martinez (X - X - 0)
t1.new_ab()
t1.pitch_list("b c b s d")
t1.no_ab("2-4")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c")
b1.out("P6")

# 2. CLE #23 Michael Brantley (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G4-3")

# 3. CLE #11 José Ramírez (X - X - X)
b1.new_ab()
b1.pitch_list("c c b b f b f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CLE #47 Trevor Bauer
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c s s")
t2.out("K")

# 5. BOS #25 Steve Pearce (X - X - X)
t2.new_ab()
t2.pitch_list("b b s")
t2.hit(1)
t2.advance(2, "12 1B")

# 6. BOS #12 Brock Holt (X - X - 25)
t2.new_ab()
t2.pitch_list("b b c c")
t2.hit(1)
t2.thrown_out(2, "23 DP6-4-3", 2, 49)

# Pitching change (CLE): #49 Tyler Olson replaces #47 Trevor Bauer
t2.pitching_substitution(49)

# 7. BOS #23 Blake Swihart (X - 25 - 12)
t2.new_ab(is_risp=True)
t2.out("DP6-4-3")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. CLE #10 Edwin Encarnación (X - X - X)
b2.new_ab()
b2.pitch_list("c c b b s")
b2.out("K")

# 5. CLE #27 Josh Donaldson (X - X - X)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(1)

# 6. CLE #36 Yandy Díaz (X - X - 27)
b2.new_ab()
b2.pitch_list("b s c b f f f c")
b2.out("!K")

# 7. CLE #6  Brandon Guyer (X - X - 27)
b2.new_ab()
b2.pitch_list("c b b f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CLE #57 Shane Bieber
t3 = game.new_inning()

# Pitching change (CLE): #57 Shane Bieber replaces #49 Tyler Olson
t3.pitching_substitution(57)

# 8. BOS #59 Sam Travis (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(4)

# 9. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("b f s f c")
t3.out("!K")

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
t3.new_ab()
t3.pitch_list("f b b b")
t3.out("F7")

# 2. BOS #0  Brandon Phillips (X - X - X)
t3.new_ab()
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 8. CLE #7  Yan Gomes (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.advance(3, "23 1B")

# 9. CLE #22 Jason Kipnis (X - X - 7)
b3.new_ab()
b3.pitch_list("c s f s")
b3.out("K")

# 1. CLE #12 Francisco Lindor (X - X - 7)
b3.new_ab()
b3.pitch_list("b f c b c")
b3.out("!K")

# 2. CLE #23 Michael Brantley (X - X - 7)
b3.new_ab()
b3.hit(1)

# 3. CLE #11 José Ramírez (7 - X - 23)
b3.new_ab(is_risp=True)
b3.pitch_list("c 1 1 f f b f b b f f")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CLE #57 Shane Bieber
t4 = game.new_inning()

# 3. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b b")
t4.reach("BB")
t4.thrown_out(2, "25 DP5-4-3", 2, 57)

# 5. BOS #25 Steve Pearce (X - X - 28)
t4.new_ab()
t4.pitch_list("c f b f")
t4.out("DP5-4-3")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 4. CLE #10 Edwin Encarnación (X - X - X)
b4.new_ab()
b4.pitch_list("s b s t")
b4.out("KT")

# 5. CLE #27 Josh Donaldson (X - X - X)
b4.new_ab()
b4.pitch_list("c b f")
b4.hit(4)

# 6. CLE #36 Yandy Díaz (X - X - X)
b4.new_ab()
b4.pitch_list("b s s f")
b4.hit(1)
b4.advance(2, "6 G6-3")
b4.advance(4, "7 HR")

# Pitching change (BOS): #37 Heath Hembree replaces #41 Chris Sale
b4.pitching_substitution(37)

# 7. CLE #6  Brandon Guyer (X - X - 36)
b4.new_ab()
b4.pitch_list("b f 1 b b f")
b4.out("G6-3")

# 8. CLE #7  Yan Gomes (X - 36 - X)
b4.new_ab(is_risp=True)
b4.hit(4, rbis=2)

# 9. CLE #22 Jason Kipnis (X - X - X)
b4.new_ab()
b4.pitch_list("c f b t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CLE #57 Shane Bieber
t5 = game.new_inning()

# Defensive change (CLE): #1 Greg Allen replaces #6 Brandon Guyer (RF), playing RF, batting 7th
t5.defensive_substitution(7, 1, "9")

# 6. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(1)
t5.advance(2, "23 BB")
t5.advance(3, "59 DP6-4-3")

# 7. BOS #23 Blake Swihart (X - X - 12)
t5.new_ab()
t5.pitch_list("d c b 1 b f f b")
t5.reach("BB")
t5.thrown_out(2, "59 DP6-4-3", 1, 57)

# 8. BOS #59 Sam Travis (X - 12 - 23)
t5.new_ab(is_risp=True)
t5.pitch_list("c f")
t5.out("DP6-4-3")

# 9. BOS #3  Sandy León (12 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("d f b d")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #66 Bobby Poyner
b5 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #37 Heath Hembree
b5.pitching_substitution(66)

# 1. CLE #12 Francisco Lindor (X - X - X)
b5.new_ab()
b5.pitch_list("c c b f f b f")
b5.hit(2)
b5.advance(3, "23 1B")
b5.advance(4, "11 SF9")

# 2. CLE #23 Michael Brantley (X - 12 - X)
b5.new_ab(is_risp=True)
b5.hit(1)
b5.advance(2, "11 SF9")

# 3. CLE #11 José Ramírez (12 - X - 23)
b5.new_ab(is_risp=True)
b5.pitch_list("b f")
b5.out("SF9", rbis=1)

# 4. CLE #10 Edwin Encarnación (X - 23 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("c f b s")
b5.out("K")

# 5. CLE #27 Josh Donaldson (X - 23 - X)
b5.new_ab(is_risp=True)
b5.out("(F)F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CLE #57 Shane Bieber
t6 = game.new_inning()

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G6-3")

# 2. BOS #0  Brandon Phillips (X - X - X)
t6.new_ab()
t6.pitch_list("c f f b f")
t6.out("G6-3")

# 3. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b f")
t6.hit(4)

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("s s b b")
t6.out("L4-3")


# Bot 6th
# Pitching: BOS #32 Matt Barnes
b6 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #66 Bobby Poyner
b6.pitching_substitution(32)

# 6. CLE #36 Yandy Díaz (X - X - X)
b6.new_ab()
b6.pitch_list("c b c b b f f d")
b6.reach("BB")
# Offensive change (CLE): Pinch-runner #26 Rajai Davis replaces #36 Yandy Díaz
b6.offensive_substitution(6, 26, "PR")
b6.atbase("PR")
b6.thrown_out(2, "1 CS", 1, 32)

# 7. CLE #1  Greg Allen (X - X - 36)
b6.new_ab()
b6.pitch_list("c 1 1 b b b")
b6.out("G5-3")

# 8. CLE #7  Yan Gomes (X - X - X)
b6.new_ab()
b6.pitch_list("b b s f b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CLE #57 Shane Bieber
t7 = game.new_inning()

# Defensive change (CLE): #9 Erik González replaces #26 Rajai Davis (PR), playing 3B, batting 6th
t7.defensive_substitution(6, 9, "5")

# 5. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.out("G6-3")

# 6. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.hit(1)
t7.advance(2, "23 1B")
t7.advance(3, "59 WP")
t7.advance(4, "59 2B")

# 7. BOS #23 Blake Swihart (X - X - 12)
t7.new_ab()
t7.pitch_list("1 b c")
t7.hit(1)
t7.advance(2, "59 WP")
t7.advance(4, "59 2B")

# 8. BOS #59 Sam Travis (X - 12 - 23)
t7.new_ab(is_risp=True)
t7.pitch_list("c b d")
t7.wp()
t7.hit(2, rbis=2)
t7.advance(3, "3 G4-3")
t7.advance(4, "30 1B")

# 9. BOS #3  Sandy León (X - 59 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c s")
t7.out("G4-3")

# 1. BOS #30 Tzu-Wei Lin (59 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.hit(1, rbis=1)
t7.advance(3, "0 1B")
t7.advance(4, "11 1B")

# 2. BOS #0  Brandon Phillips (X - X - 30)
t7.new_ab()
t7.pitch_list("1 c f b 1")
t7.hit(1)
t7.advance(2, "11 1B")
t7.advance(3, "28 BB")

# Pitching change (CLE): #58 Neil Ramírez replaces #57 Shane Bieber
t7.pitching_substitution(58)

# 3. BOS #11 Rafael Devers (30 - X - 0)
t7.new_ab(is_risp=True)
t7.pitch_list("b f 1 c d")
t7.hit(1, rbis=1)
t7.advance(2, "28 BB")
t7.thrown_out(3, "25 FC5", 3, 58)

# 4. BOS #28 J.D. Martinez (X - 0 - 11)
t7.new_ab(is_risp=True)
t7.pitch_list("f b b b b")
t7.reach("BB")
t7.advance(2, "25 FC5")

# 5. BOS #25 Steve Pearce (0 - 11 - 28)
t7.new_ab(is_risp=True)
t7.pitch_list("b c b c")
t7.reach("FC5")


# Bot 7th
# Pitching: BOS #31 Drew Pomeranz
b7 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #32 Matt Barnes
b7.pitching_substitution(31)

# 9. CLE #22 Jason Kipnis (X - X - X)
b7.new_ab()
b7.pitch_list("b b c f c")
b7.out("!K")

# 1. CLE #12 Francisco Lindor (X - X - X)
b7.new_ab()
b7.pitch_list("f b c s")
b7.out("K")

# 2. CLE #23 Michael Brantley (X - X - X)
b7.new_ab()
b7.reach("HBP")
b7.advance("U", "11 E7")

# 3. CLE #11 José Ramírez (X - X - 23)
b7.new_ab()
b7.pitch_list("c d b")
b7.error(7)
b7.reach("E7", end_base=2)

# 4. CLE #10 Edwin Encarnación (X - 11 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c d c b b f b")
b7.reach("BB")

# Pitching change (BOS): #44 Brandon Workman replaces #31 Drew Pomeranz
b7.pitching_substitution(44)

# 5. CLE #27 Josh Donaldson (X - 11 - 10)
b7.new_ab(is_risp=True)
b7.pitch_list("c b c b f d")
b7.out("L8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CLE #58 Neil Ramírez
t8 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("L7")

# 7. BOS #23 Blake Swihart (X - X - X)
t8.new_ab()
t8.pitch_list("s s")
t8.out("G3-1")

# 8. BOS #59 Sam Travis (X - X - X)
t8.new_ab()
t8.pitch_list("t b f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #44 Brandon Workman
b8.pitching_substitution(76)

# 6. CLE #9  Erik González (X - X - X)
b8.new_ab()
b8.pitch_list("f b b b")
b8.error(5)
b8.reach("E5")
b8.advance(3, "7 2B")

# 7. CLE #1  Greg Allen (X - X - 9)
b8.new_ab()
b8.pitch_list("c b 1 c")
b8.out("L7")

# 8. CLE #7  Yan Gomes (X - X - 9)
b8.new_ab()
b8.hit(2)

# Pitching change (BOS): #63 Robby Scott replaces #76 Hector Velázquez
b8.pitching_substitution(63)

# 9. CLE #22 Jason Kipnis (9 - 7 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("s b s")
b8.out("(F)P2")

# 1. CLE #12 Francisco Lindor (9 - 7 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("v v v v")
b8.reach("IBB")

# 2. CLE #23 Michael Brantley (9 - 7 - 12)
b8.new_ab(is_risp=True)
b8.pitch_list("c b")
b8.out("(F)F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CLE #61 Dan Otero
t9 = game.new_inning()

# Pitching change (CLE): #61 Dan Otero replaces #58 Neil Ramírez
t9.pitching_substitution(61)

# 9. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G3")

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(4)

# 2. BOS #0  Brandon Phillips (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.hit(1)
t9.thrown_out(2, "11 DP4-6-3", 2, 61)

# 3. BOS #11 Rafael Devers (X - X - 0)
t9.new_ab()
t9.pitch_list("c")
t9.out("DP4-6-3")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #63 Robby Scott
b9.pitching_substitution(46)

# Defensive switch (BOS): #23 Blake Swihart moves to LF
b9.defensive_switch(23, "7")

# Defensive change (BOS): #19 Jackie Bradley Jr. replaces #59 Sam Travis (LF), playing RF, batting 8th
b9.defensive_substitution(8, 19, "9")

# 3. CLE #11 José Ramírez (X - X - X)
b9.new_ab()
b9.out("G6-3")

# 4. CLE #10 Edwin Encarnación (X - X - X)
b9.new_ab()
b9.pitch_list("b c s s")
b9.out("K2-3")

# 5. CLE #27 Josh Donaldson (X - X - X)
b9.new_ab()
b9.pitch_list("c b b f")
b9.out("G6-3")

# Winning team: BOS
# WP: BOS #32 Matt Barnes
game.winning_pitcher(32, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: CLE
# LP: CLE #57 Shane Bieber
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
