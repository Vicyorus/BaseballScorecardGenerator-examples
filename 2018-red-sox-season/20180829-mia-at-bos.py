import os
from baseball_scorecard.baseball_scorecard import Scorecard

# MIA @ BOS, 2018-08-29
# https://www.baseball-reference.com/boxes/BOS/BOS201808290.shtml
# https://www.mlb.com/gameday/marlins-vs-red-sox/2018/08/29/531398/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-29 18:36-21:46",
        "at": "Fenway Park, Boston, MA",
        "att": "36,628",
        "temp": "94F, Partly Cloudy",
        "wind": "14mph, Out To CF",
        "away": {
            "team": "Miami Marlins",
            "starter": 36,
            "roster": {
                # Lineup
                52: "Rafael Ortega",
                15: "Brian Anderson",
                11: "J.T. Realmuto",
                13: "Starlin Castro",
                32: "Derek Dietrich",
                44: "Austin Dean",
                19: "Miguel Rojas",
                10: "JT Riddle",
                79: "Isaac Galloway",
                # Starting pitcher
                36: "Trevor Richards",
                # Bench
                28: "Bryan Holaday",
                34: "Magneuris Sierra",
                2: "Yadiel Rivera",
                # Bullpen
                51: "Ben Meyer",
                56: "Tayron Guerrero",
                62: "José Ureña",
                53: "Brett Graves",
                46: "Kyle Barraclough",
                61: "Adam Conley",
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
                [11, "2"],
                [13, "4"],
                [32, "0"],
                [44, "7"],
                [19, "3"],
                [10, "6"],
                [79, "8"],
            ],
            "bench": [
                [28, "C"],
                [34, "CF"],
                [2, "3B"],
            ],
            "bullpen": [51, 56, 62, 53, 46, 61, 49, 58, 54, 55, 71, 40],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
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
                [25, "3"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [5, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Scott Barry",
            "1B": "Carlos Torres",
            "2B": "Nic Lentz",
            "3B": "Paul Nauert",
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

# 1. MIA #52 Rafael Ortega (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("G4-3")

# 2. MIA #15 Brian Anderson (X - X - X)
t1.new_ab()
t1.pitch_list("f s c")
t1.out("!K")

# 3. MIA #11 J.T. Realmuto (X - X - X)
t1.new_ab()
t1.pitch_list("c b s")
t1.hit(1)

# 4. MIA #13 Starlin Castro (X - X - 11)
t1.new_ab()
t1.pitch_list("c")
t1.out("F9")


# Bot 1st
# Pitching: MIA #36 Trevor Richards
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.out("L9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b f c s")
b1.out("K")

# 3. BOS #25 Steve Pearce (X - X - X)
b1.new_ab()
b1.pitch_list("c s c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 5. MIA #32 Derek Dietrich (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(4)

# 6. MIA #44 Austin Dean (X - X - X)
t2.new_ab()
t2.pitch_list("c c b s")
t2.out("K")

# 7. MIA #19 Miguel Rojas (X - X - X)
t2.new_ab()
t2.pitch_list("b c s f b")
t2.out("G3")

# 8. MIA #10 JT Riddle (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("P6")


# Bot 2nd
# Pitching: MIA #36 Trevor Richards
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f b s")
b2.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.out("L4")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f b f f b f f f")
b2.hit(4)

# 7. BOS #5  Ian Kinsler (X - X - X)
b2.new_ab()
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 9. MIA #79 Isaac Galloway (X - X - X)
t3.new_ab()
t3.pitch_list("b s c c")
t3.out("!K")

# 1. MIA #52 Rafael Ortega (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.thrown_out(2, "15 FC3-6", 2, 24)

# 2. MIA #15 Brian Anderson (X - X - 52)
t3.new_ab()
t3.pitch_list("c s")
t3.reach("FC3-6")
t3.advance(4, "11 2B")

# 3. MIA #11 J.T. Realmuto (X - X - 15)
t3.new_ab()
t3.pitch_list("c")
t3.hit(2, rbis=1)
t3.advance(4, "13 1B")

# 4. MIA #13 Starlin Castro (X - 11 - X)
t3.new_ab()
t3.pitch_list("b c b")
t3.hit(1, rbis=1)
t3.advance(2, "32 HBP")

# 5. MIA #32 Derek Dietrich (X - X - 13)
t3.new_ab()
t3.pitch_list("c")
t3.reach("HBP")

# 6. MIA #44 Austin Dean (X - 13 - 32)
t3.new_ab()
t3.pitch_list("c f f")
t3.out("L1-3-1")


# Bot 3rd
# Pitching: MIA #36 Trevor Richards
b3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b f b")
b3.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b")
b3.out("G3-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #76 Hector Velázquez
t4 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #24 David Price
t4.pitching_substitution(76)

# 7. MIA #19 Miguel Rojas (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G6-3")

# 8. MIA #10 JT Riddle (X - X - X)
t4.new_ab()
t4.hit(1)
t4.thrown_out(2, "79 CS", 2, 76)

# 9. MIA #79 Isaac Galloway (X - X - 10)
t4.new_ab()
t4.pitch_list("b s b b c s")
t4.out("K")


# Bot 4th
# Pitching: MIA #36 Trevor Richards
b4 = game.new_inning()

# 3. BOS #25 Steve Pearce (X - X - X)
b4.new_ab()
b4.pitch_list("b b s b c s")
b4.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("s")
b4.out("L4")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #76 Hector Velázquez
t5 = game.new_inning()

# 1. MIA #52 Rafael Ortega (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("G3-1")

# 2. MIA #15 Brian Anderson (X - X - X)
t5.new_ab()
t5.pitch_list("b f")
t5.reach("HBP")
t5.advance(2, "13 WP")
t5.advance(4, "13 1B")

# 3. MIA #11 J.T. Realmuto (X - X - 15)
t5.new_ab()
t5.pitch_list("c f d d 1 s")
t5.out("K")

# 4. MIA #13 Starlin Castro (X - X - 15)
t5.new_ab()
t5.pitch_list("f c f b b b")
t5.wp()
t5.hit(1, rbis=1)

# 5. MIA #32 Derek Dietrich (X - X - 13)
t5.new_ab()
t5.pitch_list("b f b 1 b f f")
t5.out("F8")


# Bot 5th
# Pitching: MIA #36 Trevor Richards
b5 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b c")
b5.out("G6-3")

# 7. BOS #5  Ian Kinsler (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("L6")

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.out("P6")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #76 Hector Velázquez
t6 = game.new_inning()

# 6. MIA #44 Austin Dean (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G5-3")

# 7. MIA #19 Miguel Rojas (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G6-3")

# 8. MIA #10 JT Riddle (X - X - X)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")


# Bot 6th
# Pitching: MIA #36 Trevor Richards
b6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("f b")
b6.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.advance(2, "16 BB")
b6.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b6.new_ab()
b6.pitch_list("b 1 b 1 c b b")
b6.reach("BB")
b6.advance(2, "28 1B")

# 3. BOS #25 Steve Pearce (X - 50 - 16)
b6.new_ab()
b6.pitch_list("s b f b f c")
b6.out("!K")

# 4. BOS #28 J.D. Martinez (X - 50 - 16)
b6.new_ab()
b6.pitch_list("f")
b6.hit(1, rbis=1)
b6.thrown_out(2, "2 FC6-4", 3, 55)

# Pitching change (MIA): #55 Drew Rucinski replaces #36 Trevor Richards
b6.pitching_substitution(55)

# 5. BOS #2  Xander Bogaerts (X - 16 - 28)
b6.new_ab()
b6.pitch_list("f")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #76 Hector Velázquez
t7 = game.new_inning()

# 9. MIA #79 Isaac Galloway (X - X - X)
t7.new_ab()
t7.pitch_list("b b s f b b")
t7.reach("BB")
t7.advance(2, "52 1B")
t7.advance(3, "15 F9")
t7.advance(4, "11 G6-3")

# 1. MIA #52 Rafael Ortega (X - X - 79)
t7.new_ab()
t7.pitch_list("b 1 1 f b 1 1 b")
t7.hit(1)
t7.advance(2, "11 G6-3")

# Pitching change (BOS): #47 Tyler Thornburg replaces #76 Hector Velázquez
t7.pitching_substitution(47)

# 2. MIA #15 Brian Anderson (X - 79 - 52)
t7.new_ab()
t7.out("F9")

# 3. MIA #11 J.T. Realmuto (79 - X - 52)
t7.new_ab()
t7.pitch_list("c b b")
t7.out("G6-3", rbis=1)

# 4. MIA #13 Starlin Castro (X - 52 - X)
t7.new_ab()
t7.pitch_list("d c b")
t7.out("L8")


# Bot 7th
# Pitching: MIA #55 Drew Rucinski
b7 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(3, "5 2B")
b7.advance(4, "23 1B")

# 7. BOS #5  Ian Kinsler (X - X - 36)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(2)
b7.advance(3, "23 1B")
b7.advance(4, "19 2B")

# Pitching change (MIA): #61 Adam Conley replaces #55 Drew Rucinski
b7.pitching_substitution(61)

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #3 Sandy León, batting 8th
b7.offensive_substitution(8, 23, "PH")

# 8. BOS #23 Blake Swihart (36 - 5 - X)
b7.new_ab()
b7.pitch_list("c c")
b7.hit(1, rbis=1)
b7.advance(3, "19 2B")
b7.advance(4, "50 2B")

# 9. BOS #19 Jackie Bradley Jr. (5 - X - 23)
b7.new_ab()
b7.pitch_list("s")
b7.hit(2, rbis=1)
b7.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (23 - 19 - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2, rbis=2)
b7.advance(3, "16 SAC1-3")
b7.advance(4, "12 3B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b7.new_ab()
b7.out("SAC1-3")

# Pitching change (MIA): #71 Drew Steckenrider replaces #61 Adam Conley
b7.pitching_substitution(71)

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #25 Steve Pearce, batting 3rd
b7.offensive_substitution(3, 12, "PH")

# 3. BOS #12 Brock Holt (50 - X - X)
b7.new_ab()
b7.pitch_list("3 s b f b f b f")
b7.hit(3, rbis=1)
b7.advance(4, "2 1B")

# 4. BOS #28 J.D. Martinez (12 - X - X)
b7.new_ab()
b7.pitch_list("v v v v")
b7.reach("IBB")
b7.advance(2, "2 1B")
b7.advance(4, "36 1B")

# 5. BOS #2  Xander Bogaerts (12 - X - 28)
b7.new_ab()
b7.pitch_list("b d b")
b7.hit(1, rbis=1)
b7.advance(2, "36 1B")
b7.advance(4, "5 1B")

# Pitching change (MIA): #40 Javy Guerra replaces #71 Drew Steckenrider
b7.pitching_substitution(40)

# 6. BOS #36 Eduardo Núñez (X - 28 - 2)
b7.new_ab()
b7.pitch_list("d s f d")
b7.hit(1, rbis=1)
b7.advance(2, "5 1B")
b7.advance(4, "23 2B")

# 7. BOS #5  Ian Kinsler (X - 2 - 36)
b7.new_ab()
b7.pitch_list("f")
b7.hit(1, rbis=1)
b7.error(9)
b7.advance(3, "23 2B")
b7.advance(4, "23 E9")

# 8. BOS #23 Blake Swihart (X - 36 - 5)
b7.new_ab()
b7.hit(2, rbis=1)
b7.advance(3, "E9")
b7.advance(4, "19 1B")

# 9. BOS #19 Jackie Bradley Jr. (23 - X - X)
b7.new_ab()
b7.pitch_list("c f b b f b f")
b7.hit(1, rbis=1)
b7.advance(3, "50 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(1)
b7.thrown_out(2, "16 DP6-3", 2, 40)

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b7.new_ab()
b7.pitch_list("d")
b7.out("DP6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #70 Ryan Brasier
t8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
t8.pitching_substitution(70)

# Defensive switch (BOS): #12 Brock Holt moves to 1B
t8.defensive_switch(12, "3")

# Defensive switch (BOS): #23 Blake Swihart moves to C
t8.defensive_switch(23, "2")

# 5. MIA #32 Derek Dietrich (X - X - X)
t8.new_ab()
t8.out("F9")

# 6. MIA #44 Austin Dean (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b b f f f")
t8.hit(4)

# 7. MIA #19 Miguel Rojas (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("(F)P3")

# 8. MIA #10 JT Riddle (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F8")


# Bot 8th
# Pitching: MIA #53 Brett Graves
b8 = game.new_inning()

# Pitching change (MIA): #53 Brett Graves replaces #40 Javy Guerra
b8.pitching_substitution(53)

# Defensive change (MIA): #28 Bryan Holaday replaces #11 J.T. Realmuto (C), playing C, batting 3rd
b8.defensive_substitution(3, 28, "2")

# 3. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.hit(1)
b8.thrown_out(2, "28 DP4-6-3", 1, 53)

# 4. BOS #28 J.D. Martinez (X - X - 12)
b8.new_ab()
b8.pitch_list("b c f d b")
b8.out("DP4-6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f")
b8.out("L4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #31 Drew Pomeranz
t9 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #70 Ryan Brasier
t9.pitching_substitution(31)

# 9. MIA #79 Isaac Galloway (X - X - X)
t9.new_ab()
t9.pitch_list("b c s b f b f f f d")
t9.reach("BB")
t9.thrown_out(2, "15 DP6-4-3", 2, 31)

# 1. MIA #52 Rafael Ortega (X - X - 79)
t9.new_ab()
t9.pitch_list("b c s s")
t9.out("K")

# 2. MIA #15 Brian Anderson (X - X - 79)
t9.new_ab()
t9.pitch_list("c")
t9.out("DP6-4-3")

# Winning team: BOS
# WP: BOS #47 Tyler Thornburg
game.winning_pitcher(47)

# Loser team: MIA
# LP: MIA #61 Adam Conley
game.losing_pitcher(61, is_away_team=True)

# print(game)
game.generate_scorecard()
