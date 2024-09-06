import os
from baseball_scorecard.baseball_scorecard import Scorecard

# OAK @ BOS, 2018-05-15
# https://www.baseball-reference.com/boxes/BOS/BOS201805150.shtml
# https://www.mlb.com/gameday/athletics-vs-red-sox/2018/05/15/530033/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-15 20:52-01:50 +1 (1:42 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "34,906",
        "temp": "59F, Cloudy",
        "wind": "9mph, In From CF",
        "away": {
            "team": "Oakland Athletics",
            "starter": 33,
            "roster": {
                # Lineup
                10: "Marcus Semien",
                18: "Chad Pinder",
                8: "Jed Lowrie",
                2: "Khris Davis",
                26: "Matt Chapman",
                28: "Matt Olson",
                20: "Mark Canha",
                25: "Stephen Piscotty",
                21: "Jonathan Lucroy",
                # Starting pitcher
                33: "Daniel Mengden",
                # Bench
                11: "Dustin Fowler",
                23: "Matt Joyce",
                13: "Bruce Maxwell",
                5: "Jake Smolinski",
                # Bullpen
                62: "Lou Trivino",
                55: "Sean Manaea",
                66: "Ryan Dull",
                44: "Chris Hatcher",
                57: "Wilmer Font",
                30: "Brett Anderson",
                60: "Andrew Triggs",
                39: "Blake Treinen",
                46: "Santiago Casilla",
                35: "Danny Coulombe",
                36: "Yusmeiro Petit",
            },
            "lefties": [55, 30, 35],
            "lineup": [
                [10, "6"],
                [18, "7"],
                [8, "4"],
                [2, "0"],
                [26, "5"],
                [28, "3"],
                [20, "8"],
                [25, "9"],
                [21, "2"],
            ],
            "bench": [
                [11, "CF"],
                [23, "RF"],
                [13, "1B"],
                [5, "CF"],
            ],
            "bullpen": [62, 55, 66, 44, 57, 30, 60, 39, 46, 35, 36],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [35, 22, 41, 31, 61, 66, 37, 24, 46, 56, 32],
        },
        "umpires": {
            "HP": "Mark Wegner",
            "1B": "John Tumpane",
            "2B": "Jim Reynolds",
            "3B": "Ben May",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.hit(1)
t1.advance(2, "18 1B")
t1.advance(4, "26 E4")

# 2. OAK #18 Chad Pinder (X - X - 10)
t1.new_ab()
t1.hit(1)
t1.advance(4, "26 E4")

# 3. OAK #8  Jed Lowrie (X - 10 - 18)
t1.new_ab()
t1.pitch_list("c b")
t1.out("F7")

# 4. OAK #2  Khris Davis (X - 10 - 18)
t1.new_ab()
t1.pitch_list("s b s s")
t1.out("K")

# 5. OAK #26 Matt Chapman (X - 10 - 18)
t1.new_ab()
t1.pitch_list("f b f")
t1.hit(2, rbis=2)
t1.error(4)
t1.advance(3, "E4")

# 6. OAK #28 Matt Olson (26 - X - X)
t1.new_ab()
t1.pitch_list("b b b c f f")
t1.out("L9")


# Bot 1st
# Pitching: OAK #33 Daniel Mengden
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("s b f")
b1.hit(1)
b1.advance(2, "28 1B")
b1.thrown_out(4, "2 5-2-6", 3, 33)
b1.advance(3, "2 1B")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
b1.new_ab()
b1.pitch_list("b 1")
b1.out("P4")

# 4. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.pitch_list("1")
b1.hit(1)
b1.advance(2, "2 5-2-6")

# 5. BOS #2  Xander Bogaerts (X - 16 - 28)
b1.new_ab()
b1.pitch_list("b c")
b1.hit(1)


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 7. OAK #20 Mark Canha (X - X - X)
t2.new_ab()
t2.pitch_list("f b f b b f")
t2.out("F9")

# 8. OAK #25 Stephen Piscotty (X - X - X)
t2.new_ab()
t2.pitch_list("c s")
t2.hit(4, rbis=1)

# 9. OAK #21 Jonathan Lucroy (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.hit(1)

# 1. OAK #10 Marcus Semien (X - X - 21)
t2.new_ab()
t2.pitch_list("b b s t f")
t2.out("F9")

# 2. OAK #18 Chad Pinder (X - X - 21)
t2.new_ab()
t2.pitch_list("s b f b f f b s")
t2.out("K")


# Bot 2nd
# Pitching: OAK #33 Daniel Mengden
b2 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("c f f")
b2.hit(2)

# 7. BOS #36 Eduardo Núñez (X - 18 - X)
b2.new_ab()
b2.out("(F)P3")

# 8. BOS #11 Rafael Devers (X - 18 - X)
b2.new_ab()
b2.pitch_list("c b b f s")
b2.out("K")

# 9. BOS #7  Christian Vázquez (X - 18 - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G6-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 3. OAK #8  Jed Lowrie (X - X - X)
t3.new_ab()
t3.hit(1)
t3.thrown_out(2, "26 DP6-3", 2, 57)

# 4. OAK #2  Khris Davis (X - X - 8)
t3.new_ab()
t3.pitch_list("s b b f f b c")
t3.out("!K")

# 5. OAK #26 Matt Chapman (X - X - 8)
t3.new_ab()
t3.pitch_list("b b")
t3.out("DP6-3")


# Bot 3rd
# Pitching: OAK #33 Daniel Mengden
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b b")
b3.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F7")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b3.new_ab()
b3.pitch_list("b b c s b")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 6. OAK #28 Matt Olson (X - X - X)
t4.new_ab()
t4.pitch_list("b b s f b f f")
t4.reach("HBP")
t4.thrown_out(2, "21 FC6-4", 3, 57)

# 7. OAK #20 Mark Canha (X - X - 28)
t4.new_ab()
t4.pitch_list("f f f t")
t4.out("KT")

# 8. OAK #25 Stephen Piscotty (X - X - 28)
t4.new_ab()
t4.pitch_list("f f b b f f")
t4.out("F7")

# 9. OAK #21 Jonathan Lucroy (X - X - 28)
t4.new_ab()
t4.pitch_list("f f")
t4.reach("FC6-4")


# Bot 4th
# Pitching: OAK #33 Daniel Mengden
b4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("s b")
b4.error(5)
b4.reach("E5", end_base=2)
b4.advance(3, "2 1B")
b4.advance("U", "18 FC3-6")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
b4.new_ab()
b4.pitch_list("b f f")
b4.hit(1)
b4.thrown_out(2, "18 FC3-6", 1, 33)

# 6. BOS #18 Mitch Moreland (28 - X - 2)
b4.new_ab()
b4.pitch_list("b b")
b4.reach("FC3-6", rbis=1)
b4.thrown_out(2, "36 FC6-4", 2, 33)

# 7. BOS #36 Eduardo Núñez (X - X - 18)
b4.new_ab()
b4.pitch_list("c")
b4.reach("FC6-4")

# 8. BOS #11 Rafael Devers (X - X - 36)
b4.new_ab()
b4.pitch_list("1 1 c f f f 1 b")
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
t5.new_ab()
t5.pitch_list("b f c f f f b f f f")
t5.out("G5-3")

# 2. OAK #18 Chad Pinder (X - X - X)
t5.new_ab()
t5.out("F9")

# 3. OAK #8  Jed Lowrie (X - X - X)
t5.new_ab()
t5.pitch_list("f b f")
t5.out("F9")


# Bot 5th
# Pitching: OAK #33 Daniel Mengden
b5 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.out("L6")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("c c b b s")
b5.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(4, rbis=1)

# 3. BOS #13 Hanley Ramirez (X - X - X)
b5.new_ab()
b5.pitch_list("f f b")
b5.hit(1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
b5.new_ab()
b5.pitch_list("1 s d 1 b d c f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #35 Steven Wright
t6 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #57 Eduardo Rodriguez
t6.pitching_substitution(35)

# 4. OAK #2  Khris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("c s b")
t6.out("F8")

# 5. OAK #26 Matt Chapman (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b b b")
t6.reach("BB")
t6.advance(2, "28 BB")

# 6. OAK #28 Matt Olson (X - X - 26)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.thrown_out(2, "25 FC6-4", 3, 35)

# 7. OAK #20 Mark Canha (X - 26 - 28)
t6.new_ab()
t6.pitch_list("c b s f")
t6.out("L7")

# 8. OAK #25 Stephen Piscotty (X - 26 - 28)
t6.new_ab()
t6.pitch_list("b s b")
t6.reach("FC6-4")


# Bot 6th
# Pitching: OAK #33 Daniel Mengden
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("s b b c f")
b6.out("G5-3")

# 6. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b c b b")
b6.hit(2)

# 7. BOS #36 Eduardo Núñez (X - 18 - X)
b6.new_ab()
b6.pitch_list("f d f f s")
b6.out("K2-3")

# 8. BOS #11 Rafael Devers (X - 18 - X)
b6.new_ab()
b6.pitch_list("s d f f")
b6.out("F7")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# 9. OAK #21 Jonathan Lucroy (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")
t7.thrown_out(2, "18 DP5-4-3", 2, 35)

# 1. OAK #10 Marcus Semien (X - X - 21)
t7.new_ab()
t7.pitch_list("c b b s s")
t7.out("K")

# 2. OAK #18 Chad Pinder (X - X - 21)
t7.new_ab()
t7.out("DP5-4-3")


# Bot 7th
# Pitching: OAK #62 Lou Trivino
b7 = game.new_inning()

# Pitching change (OAK): #62 Lou Trivino replaces #33 Daniel Mengden
b7.pitching_substitution(62)

# 9. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.pitch_list("b s b b")
b7.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("f b f")
b7.hit(2)

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
b7.new_ab()
b7.out("P3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #35 Steven Wright
t8 = game.new_inning()

# 3. OAK #8  Jed Lowrie (X - X - X)
t8.new_ab()
t8.pitch_list("c b b f b f")
t8.out("G5-3")

# 4. OAK #2  Khris Davis (X - X - X)
t8.new_ab()
t8.pitch_list("s s b b f")
t8.hit(1)
t8.advance(2, "26 1B")
t8.advance(4, "20 2B")

# 5. OAK #26 Matt Chapman (X - X - 2)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.advance(4, "20 2B")

# Pitching change (BOS): #66 Bobby Poyner replaces #35 Steven Wright
t8.pitching_substitution(66)

# 6. OAK #28 Matt Olson (X - 2 - 26)
t8.new_ab()
t8.pitch_list("b b")
t8.out("F9")

# 7. OAK #20 Mark Canha (X - 2 - 26)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(2, rbis=2)

# 8. OAK #25 Stephen Piscotty (X - 20 - X)
t8.new_ab()
t8.pitch_list("b s s f b f")
t8.out("F8")


# Bot 8th
# Pitching: OAK #62 Lou Trivino
b8 = game.new_inning()

# Defensive change (OAK): #11 Dustin Fowler replaces #20 Mark Canha (CF), playing CF, batting 7th
b8.defensive_substitution(7, 11, "8")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("c b s s")
b8.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c s b f s")
b8.out("K")

# 6. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c b b c b b")
b8.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - X - 18)
b8.new_ab()
b8.out("G2-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #66 Bobby Poyner
t9.pitching_substitution(61)

# 9. OAK #21 Jonathan Lucroy (X - X - X)
t9.new_ab()
t9.pitch_list("c f f f b b b")
t9.out("L6")

# 1. OAK #10 Marcus Semien (X - X - X)
t9.new_ab()
t9.pitch_list("s b b")
t9.out("P3")

# 2. OAK #18 Chad Pinder (X - X - X)
t9.new_ab()
t9.pitch_list("b f b f f")
t9.out("F7")


# Bot 9th
# Pitching: OAK #39 Blake Treinen
b9 = game.new_inning()

# Pitching change (OAK): #39 Blake Treinen replaces #62 Lou Trivino
b9.pitching_substitution(39)

# 8. BOS #11 Rafael Devers (X - X - X)
b9.new_ab()
b9.pitch_list("s c s")
b9.wp()
b9.reach("K")
b9.advance(3, "12 2B")
b9.advance(4, "50 G5-3")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #7 Christian Vázquez, batting 9th
b9.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Brock Holt (X - X - 11)
b9.new_ab()
b9.pitch_list("b")
b9.hit(2)

# 1. BOS #50 Mookie Betts (11 - 12 - X)
b9.new_ab()
b9.pitch_list("c f f f")
b9.out("G5-3", rbis=1)

# 2. BOS #16 Andrew Benintendi (X - 12 - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("F7")

# 3. BOS #13 Hanley Ramirez (X - 12 - X)
b9.new_ab()
b9.pitch_list("b f b d f")
b9.out("G6-3")

# Winning team: OAK
# WP: OAK #33 Daniel Mengden
game.winning_pitcher(33, is_away_team=True)
# SV: OAK #39 Blake Treinen
game.save_pitcher(39, is_away_team=True)

# Loser team: BOS
# LP: BOS #57 Eduardo Rodriguez
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
