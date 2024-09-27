import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ CLE, 2018-09-22
# https://www.baseball-reference.com/boxes/CLE/CLE201809220.shtml
# https://www.mlb.com/gameday/red-sox-vs-indians/2018/09/22/531714/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-22 19:10-22:56",
        "at": "Progressive Field, Cleveland, OH",
        "att": "35,095",
        "temp": "62F, Cloudy",
        "wind": "8mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                5: "Ian Kinsler",
                11: "Rafael Devers",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                50: "Mookie Betts",
                3: "Sandy León",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                41: "Chris Sale",
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
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [16, "7"],
                [5, "4"],
                [11, "5"],
                [28, "9"],
                [2, "6"],
                [18, "0"],
                [12, "3"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [59, "1B"],
                [50, "SS"],
                [3, "C"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Cleveland Indians",
            "starter": 52,
            "roster": {
                # Lineup
                12: "Francisco Lindor",
                23: "Michael Brantley",
                11: "José Ramírez",
                10: "Edwin Encarnación",
                27: "Josh Donaldson",
                17: "Yonder Alonso",
                53: "Melky Cabrera",
                7: "Yan Gomes",
                22: "Jason Kipnis",
                # Starting pitcher
                52: "Mike Clevinger",
                # Bench
                1: "Greg Allen",
                9: "Erik González",
                6: "Brandon Guyer",
                0: "Brandon Barnes",
                38: "Eric Haase",
                32: "Adam Rosales",
                36: "Yandy Díaz",
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
                90: "Adam Cimber",
                61: "Dan Otero",
                33: "Brad Hand",
                47: "Trevor Bauer",
                28: "Corey Kluber",
                43: "Josh Tomlin",
            },
            "lefties": [49, 24, 39, 33],
            "lineup": [
                [12, "6"],
                [23, "7"],
                [11, "4"],
                [10, "0"],
                [27, "5"],
                [17, "3"],
                [53, "9"],
                [7, "2"],
                [22, "8"],
            ],
            "bench": [
                [1, "CF"],
                [9, "SS"],
                [6, "LF"],
                [0, "CF"],
                [38, "C"],
                [32, "SS"],
                [36, "1B"],
                [55, "C"],
                [26, "CF"],
            ],
            "bullpen": [57, 46, 37, 45, 49, 24, 59, 58, 39, 90, 61, 33, 47, 28, 43],
        },
        "umpires": {
            "HP": "Greg Gibson",
            "1B": "Vic Carapazza",
            "2B": "Jerry Layne",
            "3B": "Jordan Baker",
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
# Pitching: CLE #52 Mike Clevinger
t1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.advance(2, "11 WP")

# 2. BOS #5  Ian Kinsler (X - X - 16)
t1.new_ab()
t1.pitch_list("c s f s")
t1.out("K")

# 3. BOS #11 Rafael Devers (X - X - 16)
t1.new_ab()
t1.pitch_list("b b 1 c c s")
t1.wp()
t1.out("K")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
t1.new_ab()
t1.pitch_list("b b c b b")
t1.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - 16 - 28)
t1.new_ab()
t1.pitch_list("b c s b b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. CLE #12 Francisco Lindor (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b")
b1.out("F8")

# 2. CLE #23 Michael Brantley (X - X - X)
b1.new_ab()
b1.pitch_list("f b b f")
b1.hit(1)

# 3. CLE #11 José Ramírez (X - X - 23)
b1.new_ab()
b1.pitch_list("c c d b f b")
b1.out("F8")

# 4. CLE #10 Edwin Encarnación (X - X - 23)
b1.new_ab()
b1.out("G4-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: CLE #52 Mike Clevinger
t2 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c b f b b b")
t2.reach("BB")
t2.advance(2, "12 HBP")

# 7. BOS #12 Brock Holt (X - X - 18)
t2.new_ab()
t2.pitch_list("c b f f")
t2.reach("HBP")

# 8. BOS #23 Blake Swihart (X - 18 - 12)
t2.new_ab()
t2.pitch_list("s b")
t2.out("IF6")

# 9. BOS #19 Jackie Bradley Jr. (X - 18 - 12)
t2.new_ab()
t2.pitch_list("c b b 2 f b c")
t2.out("!K")

# 1. BOS #16 Andrew Benintendi (X - 18 - 12)
t2.new_ab()
t2.pitch_list("s b")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. CLE #27 Josh Donaldson (X - X - X)
b2.new_ab()
b2.pitch_list("b f s")
b2.hit(1)
b2.advance(3, "53 1B")
b2.advance(4, "7 2B")

# 6. CLE #17 Yonder Alonso (X - X - 27)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 7. CLE #53 Melky Cabrera (X - X - 27)
b2.new_ab()
b2.pitch_list("c b b")
b2.hit(1)
b2.advance(3, "7 2B")
b2.advance(4, "12 1B")

# 8. CLE #7  Yan Gomes (27 - X - 53)
b2.new_ab()
b2.hit(2, rbis=1)
b2.thrown_out(4, "12 9-2", 3, 22)

# 9. CLE #22 Jason Kipnis (53 - 7 - X)
b2.new_ab()
b2.out("L3")

# 1. CLE #12 Francisco Lindor (53 - 7 - X)
b2.new_ab()
b2.pitch_list("f f b")
b2.hit(1, rbis=1)


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: CLE #52 Mike Clevinger
t3 = game.new_inning()

# 2. BOS #5  Ian Kinsler (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G6-3")

# 3. BOS #11 Rafael Devers (X - X - X)
t3.new_ab()
t3.pitch_list("c b b s b f")
t3.hit(4)

# 4. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.out("L9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b b")
t3.reach("BB")
t3.advance(2, "18 BB")

# 6. BOS #18 Mitch Moreland (X - X - 2)
t3.new_ab()
t3.pitch_list("b b s b c b")
t3.reach("BB")

# 7. BOS #12 Brock Holt (X - 2 - 18)
t3.new_ab()
t3.pitch_list("f b f b s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 2. CLE #23 Michael Brantley (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1)
b3.advance(2, "11 BB")
b3.thrown_out(3, "10 DP5-3", 1, 22)

# 3. CLE #11 José Ramírez (X - X - 23)
b3.new_ab()
b3.pitch_list("1 1 c b b b f b")
b3.reach("BB")
b3.advance(2, "10 DP5-3")
b3.advance(4, "27 1B")

# 4. CLE #10 Edwin Encarnación (X - 23 - 11)
b3.new_ab()
b3.out("DP5-3")

# 5. CLE #27 Josh Donaldson (X - 11 - X)
b3.new_ab()
b3.pitch_list("c")
b3.hit(1, rbis=1)

# 6. CLE #17 Yonder Alonso (X - X - 27)
b3.new_ab()
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: CLE #52 Mike Clevinger
t4 = game.new_inning()

# 8. BOS #23 Blake Swihart (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(4)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("b c c b b f f t")
t4.out("KT")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("f b")
t4.out("F7")

# 2. BOS #5  Ian Kinsler (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.out("G3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 7. CLE #53 Melky Cabrera (X - X - X)
b4.new_ab()
b4.pitch_list("b f b f")
b4.out("G4-3")

# 8. CLE #7  Yan Gomes (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.error(6)
b4.reach("E6")
b4.advance(2, "22 BB")
b4.advance("U", "12 1B")

# 9. CLE #22 Jason Kipnis (X - X - 7)
b4.new_ab()
b4.pitch_list("b b b c c f f f b")
b4.reach("BB")
b4.advance(2, "12 1B")
b4.thrown_out(2, "23 DP7-4", 3, 22)

# 1. CLE #12 Francisco Lindor (X - 7 - 22)
b4.new_ab()
b4.pitch_list("s f")
b4.hit(1, rbis=1)

# 2. CLE #23 Michael Brantley (X - 22 - 12)
b4.new_ab()
b4.pitch_list("b f f")
b4.out("DP7-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: CLE #52 Mike Clevinger
t5 = game.new_inning()

# 3. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("c b f b")
t5.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("f b b s")
t5.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.hit(1)

# 6. BOS #18 Mitch Moreland (X - X - 2)
t5.new_ab()
t5.out("F7")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 3. CLE #11 José Ramírez (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.out("F8")

# 4. CLE #10 Edwin Encarnación (X - X - X)
b5.new_ab()
b5.pitch_list("c s f b b s")
b5.out("K")

# 5. CLE #27 Josh Donaldson (X - X - X)
b5.new_ab()
b5.pitch_list("c f b b f")
b5.out("G5-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: CLE #39 Oliver Pérez
t6 = game.new_inning()

# Pitching change (CLE): #39 Oliver Pérez replaces #52 Mike Clevinger
t6.pitching_substitution(39)

# 7. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("b c b f b")
t6.hit(1)
t6.thrown_out(2, "23 POCS", 1, 39)

# 8. BOS #23 Blake Swihart (X - X - 12)
t6.new_ab()
t6.pitch_list("s b b s f f f 1 f c")
t6.out("!K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("s b c f f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #63 Robby Scott
b6 = game.new_inning()

# Pitching change (BOS): #63 Robby Scott replaces #22 Rick Porcello
b6.pitching_substitution(63)

# 6. CLE #17 Yonder Alonso (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F8")

# 7. CLE #53 Melky Cabrera (X - X - X)
b6.new_ab()
b6.pitch_list("s b")
b6.out("G6-3")

# 8. CLE #7  Yan Gomes (X - X - X)
b6.new_ab()
b6.pitch_list("b b c s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: CLE #24 Andrew Miller
t7 = game.new_inning()

# Pitching change (CLE): #24 Andrew Miller replaces #39 Oliver Pérez
t7.pitching_substitution(24)

# Defensive change (CLE): #0 Brandon Barnes replaces #53 Melky Cabrera (RF), playing RF, batting 7th
t7.defensive_substitution(7, 0, "9")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("b b f b b")
t7.reach("BB")
t7.error(4)
t7.advance(2, "11 E4")

# 2. BOS #5  Ian Kinsler (X - X - 16)
t7.new_ab()
t7.pitch_list("s b s f b f")
t7.out("F7")

# 3. BOS #11 Rafael Devers (X - X - 16)
t7.new_ab()
t7.reach("FC4")

# 4. BOS #28 J.D. Martinez (X - 16 - 11)
t7.new_ab()
t7.pitch_list("f")
t7.out("F9")

# 5. BOS #2  Xander Bogaerts (X - 16 - 11)
t7.new_ab()
t7.pitch_list("b c")
t7.out("L4")


# Bot 7th
# Pitching: BOS #63 Robby Scott
b7 = game.new_inning()

# 9. CLE #22 Jason Kipnis (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)
# Offensive change (CLE): Pinch-runner #1 Greg Allen replaces #22 Jason Kipnis
b7.offensive_substitution(9, 1, "PR")
b7.atbase("PR")
b7.advance(2, "12 SB")
b7.advance(3, "10 BB")

# Pitching change (BOS): #61 Brian Johnson replaces #63 Robby Scott
b7.pitching_substitution(61)

# 1. CLE #12 Francisco Lindor (X - X - 22)
b7.new_ab()
b7.pitch_list("d f b 1 b")
b7.out("G6-3")

# 2. CLE #23 Michael Brantley (X - 1 - X)
b7.new_ab()
b7.pitch_list("b c b b")
b7.out("F7")

# 3. CLE #11 José Ramírez (X - 1 - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "10 BB")

# 4. CLE #10 Edwin Encarnación (X - 1 - 11)
b7.new_ab()
b7.pitch_list("s b d b b")
b7.reach("BB")

# 5. CLE #27 Josh Donaldson (1 - 11 - 10)
b7.new_ab()
b7.pitch_list("d c d")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: CLE #24 Andrew Miller
t8 = game.new_inning()

# Defensive switch (CLE): #1 Greg Allen moves to CF
t8.defensive_switch(1, "8")

# 6. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)
# Offensive change (BOS): Pinch-runner #30 Tzu-Wei Lin replaces #18 Mitch Moreland
t8.offensive_substitution(6, 30, "PR")
t8.atbase("PR")
t8.advance(3, "19 2B")
t8.advance(4, "16 1B")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #12 Brock Holt, batting 7th
t8.offensive_substitution(7, 25, "PH")

# 7. BOS #25 Steve Pearce (X - X - 18)
t8.new_ab()
t8.pitch_list("c b")
t8.out("F8")

# 8. BOS #23 Blake Swihart (X - X - 18)
t8.new_ab()
t8.pitch_list("b s c f b f c")
t8.out("!K")

# Pitching change (CLE): #33 Brad Hand replaces #24 Andrew Miller
t8.pitching_substitution(33)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 18)
t8.new_ab()
t8.hit(2)
t8.advance(4, "16 1B")

# 1. BOS #16 Andrew Benintendi (30 - 19 - X)
t8.new_ab()
t8.pitch_list("b c f")
t8.hit(1, rbis=2)
t8.thrown_out(2, "7-4", 3, 33)


# Bot 8th
# Pitching: BOS #61 Brian Johnson
b8 = game.new_inning()

# Defensive switch (BOS): #25 Steve Pearce moves to 1B
b8.defensive_switch(25, "3")

# Defensive switch (BOS): #30 Tzu-Wei Lin moves to DH
b8.defensive_switch(30, "0")

# 6. CLE #17 Yonder Alonso (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b c f f")
b8.out("P3")

# 7. CLE #0  Brandon Barnes (X - X - X)
b8.new_ab()
b8.pitch_list("b b s s b")
b8.out("F9")

# 8. CLE #7  Yan Gomes (X - X - X)
b8.new_ab()
b8.pitch_list("s s b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: CLE #46 Jon Edwards
t9 = game.new_inning()

# Pitching change (CLE): #46 Jon Edwards replaces #33 Brad Hand
t9.pitching_substitution(46)

# 2. BOS #5  Ian Kinsler (X - X - X)
t9.new_ab()
t9.out("G5-3")

# 3. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("s c")
t9.hit(1)
t9.thrown_out(2, "2 FC6-4", 3, 46)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t9.new_ab()
t9.pitch_list("s s f f b f 1")
t9.reach("FC6-4")


# Bot 9th
# Pitching: BOS #61 Brian Johnson
b9 = game.new_inning()

# 9. CLE #1  Greg Allen (X - X - X)
b9.new_ab()
b9.pitch_list("c b f")
b9.out("G5-3")

# 1. CLE #12 Francisco Lindor (X - X - X)
b9.new_ab()
b9.pitch_list("f")
b9.out("F9")

# 2. CLE #23 Michael Brantley (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c")
b9.out("G4-3")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: CLE #49 Tyler Olson
t10 = game.new_inning()

# Pitching change (CLE): #49 Tyler Olson replaces #46 Jon Edwards
t10.pitching_substitution(49)

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #30 Tzu-Wei Lin, batting 6th
t10.offensive_substitution(6, 59, "PH")

# 6. BOS #59 Sam Travis (X - X - X)
t10.new_ab()
t10.out("F8")

# 7. BOS #25 Steve Pearce (X - X - X)
t10.new_ab()
t10.pitch_list("c s f")
t10.out("G5-3")

# 8. BOS #23 Blake Swihart (X - X - X)
t10.new_ab()
t10.out("G6-3")


# Bot 10th
# Pitching: BOS #61 Brian Johnson
b10 = game.new_inning()

# Defensive switch (BOS): #59 Sam Travis moves to DH
b10.defensive_switch(59, "0")

# 3. CLE #11 José Ramírez (X - X - X)
b10.new_ab()
b10.pitch_list("b b b b")
b10.reach("BB")
b10.advance(2, "10 BB")

# 4. CLE #10 Edwin Encarnación (X - X - 11)
b10.new_ab()
b10.pitch_list("b c b b b")
b10.reach("BB")

# Pitching change (BOS): #56 Joe Kelly replaces #61 Brian Johnson
b10.pitching_substitution(56)

# 5. CLE #27 Josh Donaldson (X - 11 - 10)
b10.new_ab()
b10.pitch_list("b f b b f s")
b10.out("K")

# 6. CLE #17 Yonder Alonso (X - 11 - 10)
b10.new_ab()
b10.pitch_list("c s s")
b10.out("K")

# Offensive change (CLE): Pinch-hitter #36 Yandy Díaz replaces #0 Brandon Barnes, batting 7th
b10.offensive_substitution(7, 36, "PH")

# 7. CLE #36 Yandy Díaz (X - 11 - 10)
b10.new_ab()
b10.pitch_list("b b c b c")
b10.out("G6-3")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: CLE #49 Tyler Olson
t11 = game.new_inning()

# Defensive change (CLE): #9 Erik González replaces #27 Josh Donaldson (3B), playing 3B, batting 5th
t11.defensive_substitution(5, 9, "5")

# Defensive change (CLE): #6 Brandon Guyer replaces #36 Yandy Díaz (PH), playing RF, batting 7th
t11.defensive_substitution(7, 6, "9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t11.new_ab()
t11.pitch_list("b c b c b s")
t11.out("K")

# 1. BOS #16 Andrew Benintendi (X - X - X)
t11.new_ab()
t11.pitch_list("c f b s")
t11.out("K")

# 2. BOS #5  Ian Kinsler (X - X - X)
t11.new_ab()
t11.pitch_list("c")
t11.out("G6-3")


# Bot 11th
# Pitching: BOS #31 Drew Pomeranz
b11 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #56 Joe Kelly
b11.pitching_substitution(31)

# 8. CLE #7  Yan Gomes (X - X - X)
b11.new_ab()
b11.pitch_list("b b c f f f f f f")
b11.hit(1)
# Offensive change (CLE): Pinch-runner #26 Rajai Davis replaces #7 Yan Gomes
b11.offensive_substitution(8, 26, "PR")
b11.atbase("PR")
b11.advance(2, "1 1B")
b11.advance(3, "12 SB")
b11.advance(4, "23 1B")

# 9. CLE #1  Greg Allen (X - X - 7)
b11.new_ab()
b11.pitch_list("b b l c")
b11.hit(1)
b11.advance(2, "12 SB")
b11.advance(3, "23 1B")

# 1. CLE #12 Francisco Lindor (X - 26 - 1)
b11.new_ab()
b11.pitch_list("b b v v")
b11.reach("IBB")
b11.advance(2, "23 1B")

# 2. CLE #23 Michael Brantley (26 - 1 - 12)
b11.new_ab()
b11.pitch_list("b f")
b11.hit(1, rbis=1)

# Winning team: CLE
# WP: CLE #49 Tyler Olson
game.winning_pitcher(49)

# Loser team: BOS
# LP: BOS #31 Drew Pomeranz
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
