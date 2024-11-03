import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIA @ BOS, 2018-08-28
# https://www.baseball-reference.com/boxes/BOS/BOS201808280.shtml
# https://www.mlb.com/gameday/marlins-vs-red-sox/2018/08/28/531384/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-28 19:12-22:41",
        "at": "Fenway Park, Boston, MA",
        "att": "36,708",
        "temp": "92F, Partly Cloudy",
        "wind": "14mph, Out To CF",
        "away": {
            "team": "Miami Marlins",
            "starter": 62,
            "roster": {
                # Lineup
                52: "Rafael Ortega",
                15: "Brian Anderson",
                11: "J.T. Realmuto",
                13: "Starlin Castro",
                32: "Derek Dietrich",
                44: "Austin Dean",
                19: "Miguel Rojas",
                79: "Isaac Galloway",
                28: "Bryan Holaday",
                # Starting pitcher
                62: "José Ureña",
                # Bench
                34: "Magneuris Sierra",
                10: "JT Riddle",
                2: "Yadiel Rivera",
                # Bullpen
                51: "Ben Meyer",
                56: "Tayron Guerrero",
                53: "Brett Graves",
                46: "Kyle Barraclough",
                61: "Adam Conley",
                36: "Trevor Richards",
                49: "Pablo López",
                58: "Dan Straily",
                54: "Wei-Yin Chen",
                55: "Drew Rucinski",
                71: "Drew Steckenrider",
                40: "Javy Guerra",
            },
            "lefties": [61, 54],
            "lineup": [
                [52, "9"],
                [15, "5"],
                [11, "3"],
                [13, "4"],
                [32, "0"],
                [44, "7"],
                [19, "6"],
                [79, "8"],
                [28, "2"],
            ],
            "bench": [
                [34, "CF"],
                [10, "SS"],
                [2, "3B"],
            ],
            "bullpen": [51, 56, 53, 46, 61, 36, 49, 58, 54, 55, 71, 40],
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
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
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
                [36, "5"],
                [5, "4"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Paul Nauert",
            "1B": "Scott Barry",
            "2B": "Carlos Torres",
            "3B": "Nic Lentz",
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

# 1. MIA #52 Rafael Ortega (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.out("F8")

# 2. MIA #15 Brian Anderson (X - X - X)
t1.new_ab()
t1.pitch_list("c b b f")
t1.out("G4-3")

# 3. MIA #11 J.T. Realmuto (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("G5-3")


# Bot 1st
# Pitching: MIA #62 José Ureña
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b 1 b")
b1.out("F7")

# 3. BOS #18 Mitch Moreland (X - X - 50)
b1.new_ab()
b1.pitch_list("1 b")
b1.out("L9")

# 4. BOS #28 J.D. Martinez (X - X - 50)
b1.new_ab()
b1.pitch_list("c 1 1 s f")
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 4. MIA #13 Starlin Castro (X - X - X)
t2.new_ab()
t2.pitch_list("c b f f b")
t2.out("G6-3")

# 5. MIA #32 Derek Dietrich (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b f f f c")
t2.out("!K")

# 6. MIA #44 Austin Dean (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b c")
t2.out("F8")


# Bot 2nd
# Pitching: MIA #62 José Ureña
b2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b b f b c")
b2.hit(2)
b2.advance(3, "36 G4-3")
b2.advance(4, "5 1B")

# 6. BOS #36 Eduardo Núñez (X - 2 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b f")
b2.out("G4-3")

# 7. BOS #5  Ian Kinsler (2 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b")
b2.hit(1, rbis=1)
b2.thrown_out(2, "23 DP4-6-3", 2, 62)

# 8. BOS #23 Blake Swihart (X - X - 5)
b2.new_ab()
b2.pitch_list("b s b 1 b f f")
b2.out("DP4-6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 7. MIA #19 Miguel Rojas (X - X - X)
t3.new_ab()
t3.out("G5-3")

# 8. MIA #79 Isaac Galloway (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(4)

# 9. MIA #28 Bryan Holaday (X - X - X)
t3.new_ab()
t3.pitch_list("b c c")
t3.hit(1)
t3.advance(3, "15 2B")

# 1. MIA #52 Rafael Ortega (X - X - 28)
t3.new_ab()
t3.pitch_list("s b f c")
t3.out("!K")

# 2. MIA #15 Brian Anderson (X - X - 28)
t3.new_ab()
t3.pitch_list("f")
t3.hit(2)

# 3. MIA #11 J.T. Realmuto (28 - 15 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("d b")
t3.out("L4")


# Bot 3rd
# Pitching: MIA #62 José Ureña
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("f b s")
b3.hit(1)
b3.advance(2, "50 BB")
b3.advance(4, "16 2B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b3.new_ab()
b3.pitch_list("c c b b f b b")
b3.reach("BB")
b3.advance(3, "16 2B")
b3.advance(4, "2 SF7")

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b3.new_ab(is_risp=True)
b3.pitch_list("s f b")
b3.hit(2, rbis=1)

# 3. BOS #18 Mitch Moreland (50 - 16 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b s b s s")
b3.out("K")

# 4. BOS #28 J.D. Martinez (50 - 16 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("v v v v")
b3.reach("IBB")

# 5. BOS #2  Xander Bogaerts (50 - 16 - 28)
b3.new_ab(is_risp=True)
b3.out("SF7", rbis=1)

# 6. BOS #36 Eduardo Núñez (X - 16 - 28)
b3.new_ab(is_risp=True)
b3.pitch_list("c b d")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 4. MIA #13 Starlin Castro (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(3)

# 5. MIA #32 Derek Dietrich (13 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c s b c")
t4.out("!K")

# 6. MIA #44 Austin Dean (13 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("d b c b b")
t4.reach("BB")

# 7. MIA #19 Miguel Rojas (13 - X - 44)
t4.new_ab(is_risp=True)
t4.pitch_list("b b")
t4.out("P3")

# 8. MIA #79 Isaac Galloway (13 - X - 44)
t4.new_ab(is_risp=True)
t4.pitch_list("1 b f d b")
t4.out("P4")


# Bot 4th
# Pitching: MIA #62 José Ureña
b4 = game.new_inning()

# 7. BOS #5  Ian Kinsler (X - X - X)
b4.new_ab()
b4.out("G6-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b b c s s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 9. MIA #28 Bryan Holaday (X - X - X)
t5.new_ab()
t5.pitch_list("f c b")
t5.out("F9")

# 1. MIA #52 Rafael Ortega (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.thrown_out(2, "15 CS", 2, 44)

# Pitching change (BOS): #44 Brandon Workman replaces #61 Brian Johnson
t5.pitching_substitution(44)

# 2. MIA #15 Brian Anderson (X - X - 52)
t5.new_ab()
t5.pitch_list("1 c s b b b b")
t5.reach("BB")
t5.advance(2, "11 1B")
t5.thrown_out(3, "13 FC5", 3, 44)

# 3. MIA #11 J.T. Realmuto (X - X - 15)
t5.new_ab()
t5.pitch_list("b f s")
t5.hit(1)
t5.advance(2, "13 FC5")

# 4. MIA #13 Starlin Castro (X - 15 - 11)
t5.new_ab(is_risp=True)
t5.reach("FC5")


# Bot 5th
# Pitching: MIA #62 José Ureña
b5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b f b b")
b5.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.out("G1-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("b b b b")
b5.reach("BB")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b5.new_ab()
b5.pitch_list("f f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #44 Brandon Workman
t6 = game.new_inning()

# 5. MIA #32 Derek Dietrich (X - X - X)
t6.new_ab()
t6.pitch_list("b b c c")
t6.out("P6")

# 6. MIA #44 Austin Dean (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("L8")

# 7. MIA #19 Miguel Rojas (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G5-3")


# Bot 6th
# Pitching: MIA #62 José Ureña
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("b s")
b6.out("G5-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("f")
b6.hit(4)

# 7. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("c f")
b6.out("G6-3")

# 8. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("b b b f f")
b6.out("G3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #44 Brandon Workman
t7.pitching_substitution(56)

# 8. MIA #79 Isaac Galloway (X - X - X)
t7.new_ab()
t7.pitch_list("c b f f f c")
t7.out("!K")

# 9. MIA #28 Bryan Holaday (X - X - X)
t7.new_ab()
t7.out("P3")

# 1. MIA #52 Rafael Ortega (X - X - X)
t7.new_ab()
t7.pitch_list("c b b s b")
t7.out("L8")


# Bot 7th
# Pitching: MIA #46 Kyle Barraclough
b7 = game.new_inning()

# Pitching change (MIA): #46 Kyle Barraclough replaces #62 José Ureña
b7.pitching_substitution(46)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")
b7.advance(2, "50 SB")
b7.thrown_out(3, "16 DP5-3", 1, 46)

# 1. BOS #50 Mookie Betts (X - X - 19)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b b f f 2 b")
b7.reach("BB")
b7.advance(2, "16 DP5-3")

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b7.new_ab(is_risp=True)
b7.pitch_list("d")
b7.out("DP5-3")

# 3. BOS #18 Mitch Moreland (X - 50 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.out("F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t8.pitching_substitution(32)

# 2. MIA #15 Brian Anderson (X - X - X)
t8.new_ab()
t8.pitch_list("b c c b")
t8.hit(1)
t8.advance(4, "11 HR")

# 3. MIA #11 J.T. Realmuto (X - X - 15)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(4, rbis=2)

# 4. MIA #13 Starlin Castro (X - X - X)
t8.new_ab()
t8.pitch_list("b s")
t8.hit(4)

# 5. MIA #32 Derek Dietrich (X - X - X)
t8.new_ab()
t8.pitch_list("c f b s")
t8.out("K")

# 6. MIA #44 Austin Dean (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.hit(1)
# Offensive change (MIA): Pinch-runner #34 Magneuris Sierra replaces #44 Austin Dean
t8.offensive_substitution(6, 34, "PR")
t8.atbase("PR")
t8.advance(2, "19 1B")
t8.advance(3, "10 BB")
t8.advance(4, "52 1B")

# Pitching change (BOS): #37 Heath Hembree replaces #32 Matt Barnes
t8.pitching_substitution(37)

# 7. MIA #19 Miguel Rojas (X - X - 44)
t8.new_ab()
t8.pitch_list("c b 1 f f b")
t8.hit(1)
t8.advance(2, "10 BB")
t8.advance(4, "52 1B")

# 8. MIA #79 Isaac Galloway (X - 34 - 19)
t8.new_ab(is_risp=True)
t8.out("F8")

# Offensive change (MIA): Pinch-hitter #10 JT Riddle replaces #28 Bryan Holaday, batting 9th
t8.offensive_substitution(9, 10, "PH")

# 9. MIA #10 JT Riddle (X - 34 - 19)
t8.new_ab(is_risp=True)
t8.pitch_list("b b c b d")
t8.reach("BB")
t8.advance(2, "52 1B")

# 1. MIA #52 Rafael Ortega (34 - 19 - 10)
t8.new_ab(is_risp=True)
t8.hit(1, rbis=2)

# 2. MIA #15 Brian Anderson (X - 10 - 52)
t8.new_ab(is_risp=True)
t8.pitch_list("b f f")
t8.out("G1-3")


# Bot 8th
# Pitching: MIA #56 Tayron Guerrero
b8 = game.new_inning()

# Pitching change (MIA): #56 Tayron Guerrero replaces #46 Kyle Barraclough
b8.pitching_substitution(56)

# Defensive switch (MIA): #52 Rafael Ortega moves to LF
b8.defensive_switch(52, "7")

# Defensive switch (MIA): #11 J.T. Realmuto moves to C
b8.defensive_switch(11, "2")

# Defensive switch (MIA): #34 Magneuris Sierra moves to CF
b8.defensive_switch(34, "8")

# Defensive switch (MIA): #19 Miguel Rojas moves to 1B
b8.defensive_switch(19, "3")

# Defensive switch (MIA): #79 Isaac Galloway moves to RF
b8.defensive_switch(79, "9")

# Defensive switch (MIA): #10 JT Riddle moves to SS
b8.defensive_switch(10, "6")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b")
b8.hit(1)
b8.advance(2, "36 1B")
b8.advance(3, "5 1B")
b8.advance(4, "19 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b8.new_ab()
b8.pitch_list("b b b c c")
b8.out("L9")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
b8.new_ab()
b8.pitch_list("c s b d")
b8.hit(1)
b8.advance(2, "5 1B")
b8.advance(4, "19 1B")

# 7. BOS #5  Ian Kinsler (X - 28 - 36)
b8.new_ab(is_risp=True)
b8.pitch_list("c b")
b8.hit(1)
b8.advance(3, "19 1B")
b8.advance(4, "50 WP")

# 8. BOS #23 Blake Swihart (28 - 36 - 5)
b8.new_ab(is_risp=True)
b8.pitch_list("b c d b c s")
b8.out("K")

# 9. BOS #19 Jackie Bradley Jr. (28 - 36 - 5)
b8.new_ab(is_risp=True)
b8.pitch_list("b c b f b f")
b8.hit(1, rbis=2)
b8.advance(2, "50 WP")

# 1. BOS #50 Mookie Betts (5 - X - 19)
b8.new_ab(is_risp=True)
b8.pitch_list("c b b b b")
b8.wp()
b8.reach("BB")

# Pitching change (MIA): #61 Adam Conley replaces #56 Tayron Guerrero
b8.pitching_substitution(61)

# 2. BOS #16 Andrew Benintendi (X - 19 - 50)
b8.new_ab(is_risp=True)
b8.pitch_list("b f b b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree
t9.pitching_substitution(46)

# 3. MIA #11 J.T. Realmuto (X - X - X)
t9.new_ab()
t9.pitch_list("c b s")
t9.out("L6")

# 4. MIA #13 Starlin Castro (X - X - X)
t9.new_ab()
t9.pitch_list("b b c s b b")
t9.reach("BB")
# Offensive change (MIA): Pinch-runner #2 Yadiel Rivera replaces #13 Starlin Castro
t9.offensive_substitution(4, 2, "PR")
t9.atbase("PR")
t9.advance(2, "32 BB")
t9.advance(4, "34 1B")

# 5. MIA #32 Derek Dietrich (X - X - 13)
t9.new_ab()
t9.pitch_list("b 1 b b c 1 d")
t9.reach("BB")
t9.advance(2, "34 1B")
t9.advance(3, "79 WP")

# 6. MIA #34 Magneuris Sierra (X - 2 - 32)
t9.new_ab(is_risp=True)
t9.pitch_list("f b s f f")
t9.hit(1, rbis=1)
t9.advance(2, "79 WP")

# 7. MIA #19 Miguel Rojas (X - 32 - 34)
t9.new_ab(is_risp=True)
t9.out("L4")

# 8. MIA #79 Isaac Galloway (X - 32 - 34)
t9.new_ab(is_risp=True)
t9.pitch_list("d s b c b s")
t9.wp()
t9.out("K2-3")


# Bot 9th
# Pitching: MIA #71 Drew Steckenrider
b9 = game.new_inning()

# Pitching change (MIA): #71 Drew Steckenrider replaces #61 Adam Conley
b9.pitching_substitution(71)

# Defensive switch (MIA): #2 Yadiel Rivera moves to 2B
b9.defensive_switch(2, "4")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #18 Mitch Moreland, batting 3rd
b9.offensive_substitution(3, 25, "PH")

# 3. BOS #25 Steve Pearce (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.out("F9")

# 4. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("c b")
b9.hit(1)
b9.advance(2, "2 1B")
b9.error(6)
b9.advance("U", "36 E6")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b9.new_ab()
b9.pitch_list("c 1 s")
b9.hit(1)
b9.thrown_out(2, "36 FC6", 2, 71)

# 6. BOS #36 Eduardo Núñez (X - 28 - 2)
b9.new_ab(is_risp=True)
b9.pitch_list("f")
b9.reach("FC6")

# Winning team: BOS
# WP: BOS #46 Craig Kimbrel
game.winning_pitcher(46)

# Loser team: MIA
# LP: MIA #71 Drew Steckenrider
game.losing_pitcher(71, is_away_team=True)

# print(game)
game.generate_scorecard()
