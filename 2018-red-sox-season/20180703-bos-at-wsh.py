import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ WSH, 2018-07-03
# https://www.baseball-reference.com/boxes/WAS/WAS201807030.shtml
# https://www.mlb.com/gameday/red-sox-vs-nationals/2018/07/03/530680/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-03 18:06-21:01",
        "at": "Nationals Park, Washington, DC",
        "att": "42,531",
        "temp": "94F, Cloudy",
        "wind": "5mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                61: "Brian Johnson",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [61, 57, 41, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "9"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [61, "1"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
                [7, "C"],
            ],
            "bullpen": [57, 44, 67, 22, 41, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Washington Nationals",
            "starter": 57,
            "roster": {
                # Lineup
                7: "Trea Turner",
                22: "Juan Soto",
                6: "Anthony Rendon",
                34: "Bryce Harper",
                20: "Daniel Murphy",
                14: "Mark Reynolds",
                3: "Michael A. Taylor",
                29: "Pedro Severino",
                57: "Tanner Roark",
                # Starting pitcher
                57: "Tanner Roark",
                # Bench
                2: "Adam Eaton",
                1: "Wilmer Difo",
                8: "Brian Goodwin",
                64: "Spencer Kieboom",
                # Bullpen
                58: "Jeremy Hellickson",
                27: "Shawn Kelley",
                21: "Brandon Kintzler",
                62: "Sean Doolittle",
                47: "Gio González",
                44: "Ryan Madson",
                31: "Max Scherzer",
                40: "Kelvin Herrera",
                23: "Erick Fedde",
                60: "Justin Miller",
                33: "Matt Grace",
                55: "Tim Collins",
            },
            "lefties": [62, 47, 33, 55],
            "lineup": [
                [7, "6"],
                [22, "7"],
                [6, "5"],
                [34, "9"],
                [20, "4"],
                [14, "3"],
                [3, "8"],
                [29, "2"],
                [57, "1"],
            ],
            "bench": [
                [2, "CF"],
                [1, "SS"],
                [8, "CF"],
                [64, "C"],
            ],
            "bullpen": [58, 27, 21, 62, 47, 44, 31, 40, 23, 60, 33, 55],
        },
        "umpires": {
            "HP": "Vic Carapazza",
            "1B": "Jordan Baker",
            "2B": "Jeremie Rehak",
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
# Pitching: WSH #57 Tanner Roark
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b")
t1.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("t")
t1.out("L8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")


# Bot 1st
# Pitching: BOS #61 Brian Johnson
b1 = game.new_inning()

# 1. WSH #7  Trea Turner (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "22 1B")

# 2. WSH #22 Juan Soto (X - X - 7)
b1.new_ab()
b1.pitch_list("s")
b1.hit(1)

# 3. WSH #6  Anthony Rendon (X - 7 - 22)
b1.new_ab()
b1.out("IF4")

# 4. WSH #34 Bryce Harper (X - 7 - 22)
b1.new_ab()
b1.pitch_list("c f b t")
b1.out("KT")

# 5. WSH #20 Daniel Murphy (X - 7 - 22)
b1.new_ab()
b1.pitch_list("f")
b1.out("(F)P5")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: WSH #57 Tanner Roark
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.advance(2, "2 1B")
t2.advance(3, "11 FC1-6")
t2.advance(4, "36 HR")

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t2.new_ab()
t2.hit(1)
t2.thrown_out(2, "11 FC1-6", 1, 57)

# 6. BOS #11 Rafael Devers (X - 18 - 2)
t2.new_ab()
t2.pitch_list("c d")
t2.reach("FC1-6")
t2.advance(4, "36 HR")

# 7. BOS #36 Eduardo Núñez (18 - X - 11)
t2.new_ab()
t2.pitch_list("1 c")
t2.hit(4, rbis=3)

# 8. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("L7")

# 9. BOS #61 Brian Johnson (X - X - X)
t2.new_ab()
t2.pitch_list("f s f b b")
t2.out("G5-3")


# Bot 2nd
# Pitching: BOS #61 Brian Johnson
b2 = game.new_inning()

# 6. WSH #14 Mark Reynolds (X - X - X)
b2.new_ab()
b2.pitch_list("c f b s")
b2.out("K")

# 7. WSH #3  Michael A. Taylor (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f")
b2.hit(1)
b2.thrown_out(2, "29 CS", 2, 61)

# 8. WSH #29 Pedro Severino (X - X - 3)
b2.new_ab()
b2.pitch_list("1 1 b f b b f f b")
b2.reach("BB")

# 9. WSH #57 Tanner Roark (X - X - 29)
b2.new_ab()
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: WSH #57 Tanner Roark
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f")
t3.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("f f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #61 Brian Johnson
b3 = game.new_inning()

# Defensive change (BOS): #25 Steve Pearce replaces #18 Mitch Moreland (1B), playing 1B, batting 4th
b3.defensive_substitution(4, 25, "3")

# 1. WSH #7  Trea Turner (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("(F)P5")

# 2. WSH #22 Juan Soto (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("G4-3")

# 3. WSH #6  Anthony Rendon (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f b f f")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: WSH #57 Tanner Roark
t4 = game.new_inning()

# 4. BOS #25 Steve Pearce (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.hit(2)
t4.advance(3, "2 WP")

# 5. BOS #2  Xander Bogaerts (X - 25 - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.wp()
t4.reach("BB")
t4.thrown_out(2, "36 DP4-6-3", 2, 57)

# 6. BOS #11 Rafael Devers (25 - X - 2)
t4.new_ab()
t4.pitch_list("c f c")
t4.out("!K")

# 7. BOS #36 Eduardo Núñez (25 - X - 2)
t4.new_ab()
t4.pitch_list("1 c")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: BOS #61 Brian Johnson
b4 = game.new_inning()

# 4. WSH #34 Bryce Harper (X - X - X)
b4.new_ab()
b4.hit(2)
b4.advance(3, "20 G3")
b4.advance(4, "14 1B")

# 5. WSH #20 Daniel Murphy (X - 34 - X)
b4.new_ab()
b4.pitch_list("c b")
b4.out("G3")

# 6. WSH #14 Mark Reynolds (34 - X - X)
b4.new_ab()
b4.pitch_list("d")
b4.hit(1, rbis=1)
b4.advance(2, "3 1B")
b4.advance(3, "29 L8")
b4.advance(4, "57 1B")

# 7. WSH #3  Michael A. Taylor (X - X - 14)
b4.new_ab()
b4.pitch_list("s")
b4.hit(1)
b4.advance(2, "57 1B")

# 8. WSH #29 Pedro Severino (X - 14 - 3)
b4.new_ab()
b4.pitch_list("c f f b")
b4.out("L8")

# 9. WSH #57 Tanner Roark (14 - X - 3)
b4.new_ab()
b4.pitch_list("c")
b4.hit(1, rbis=1)

# 1. WSH #7  Trea Turner (X - 3 - 57)
b4.new_ab()
b4.pitch_list("c")
b4.out("F7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: WSH #57 Tanner Roark
t5 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("f b f t")
t5.out("KT")

# 9. BOS #61 Brian Johnson (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "50 1B")
t5.advance(3, "16 1B")
t5.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (X - X - 61)
t5.new_ab()
t5.pitch_list("f b b f")
t5.hit(1)
t5.advance(2, "16 1B")
t5.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - 61 - 50)
t5.new_ab()
t5.pitch_list("s b f")
t5.hit(1)
t5.advance(2, "28 1B")
t5.advance(4, "25 1B")

# 3. BOS #28 J.D. Martinez (61 - 50 - 16)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1, rbis=2)
t5.advance(3, "25 1B")
t5.advance(4, "2 HR")

# 4. BOS #25 Steve Pearce (X - 16 - 28)
t5.new_ab()
t5.pitch_list("d c")
t5.hit(1, rbis=1)
t5.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (28 - X - 25)
t5.new_ab()
t5.pitch_list("b d c s")
t5.hit(4, rbis=3)

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("f f b b f b b")
t5.reach("BB")
t5.thrown_out(2, "36 DP5-4-3", 2, 57)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
t5.new_ab()
t5.pitch_list("f")
t5.out("DP5-4-3")


# Bot 5th
# Pitching: BOS #61 Brian Johnson
b5 = game.new_inning()

# 2. WSH #22 Juan Soto (X - X - X)
b5.new_ab()
b5.pitch_list("b b c c f")
b5.out("G5-3")

# 3. WSH #6  Anthony Rendon (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)
b5.advance(2, "34 BB")
b5.advance(3, "14 1B")

# 4. WSH #34 Bryce Harper (X - X - 6)
b5.new_ab()
b5.pitch_list("c d b c b b")
b5.reach("BB")
b5.advance(2, "14 1B")

# 5. WSH #20 Daniel Murphy (X - 6 - 34)
b5.new_ab()
b5.pitch_list("c d")
b5.out("L9")

# Pitching change (BOS): #37 Heath Hembree replaces #61 Brian Johnson, batting 9th
b5.pitching_substitution(37)
b5.defensive_substitution(9, 37, "1")

# 6. WSH #14 Mark Reynolds (X - 6 - 34)
b5.new_ab()
b5.pitch_list("f s b b")
b5.hit(1)

# 7. WSH #3  Michael A. Taylor (6 - 34 - 14)
b5.new_ab()
b5.pitch_list("c s b b b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: WSH #57 Tanner Roark
t6 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t6.new_ab()
t6.pitch_list("c b f")
t6.out("L9")

# 9. BOS #61 Brian Johnson (X - X - X)
t6.new_ab()
t6.pitch_list("b f s f s")
t6.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b b")
t6.out("F9")


# Bot 6th
# Pitching: BOS #37 Heath Hembree
b6 = game.new_inning()

# 8. WSH #29 Pedro Severino (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4)

# 9. WSH #57 Tanner Roark (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")

# 1. WSH #7  Trea Turner (X - X - X)
b6.new_ab()
b6.pitch_list("c f b f f s")
b6.out("K")

# 2. WSH #22 Juan Soto (X - X - X)
b6.new_ab()
b6.pitch_list("f b c f f b c")
b6.out("!K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: WSH #57 Tanner Roark
t7 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.out("L8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.out("F9")

# 4. BOS #25 Steve Pearce (X - X - X)
t7.new_ab()
t7.pitch_list("b f b c f b")
t7.out("L8")


# Bot 7th
# Pitching: BOS #44 Brandon Workman
b7 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree, batting 9th
b7.pitching_substitution(44)
b7.defensive_substitution(9, 44, "1")

# 3. WSH #6  Anthony Rendon (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("G6-3")

# 4. WSH #34 Bryce Harper (X - X - X)
b7.new_ab()
b7.pitch_list("s f b b c")
b7.out("!K")

# 5. WSH #20 Daniel Murphy (X - X - X)
b7.new_ab()
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: WSH #55 Tim Collins
t8 = game.new_inning()

# Pitching change (WSH): #55 Tim Collins replaces #57 Tanner Roark, batting 5th
t8.pitching_substitution(55)
t8.defensive_substitution(5, 55, "1")

# Defensive change (WSH): #8 Brian Goodwin replaces #57 Tanner Roark (P), playing RF, batting 9th
t8.defensive_substitution(9, 8, "9")

# Defensive change (WSH): #1 Wilmer Difo replaces #34 Bryce Harper (RF), playing 2B, batting 4th
t8.defensive_substitution(4, 1, "4")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.thrown_out(2, "11 DP6-4-3", 1, 55)

# 6. BOS #11 Rafael Devers (X - X - 2)
t8.new_ab()
t8.out("DP6-4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b f s")
t8.hit(2)

# 8. BOS #3  Sandy León (X - 36 - X)
t8.new_ab()
t8.pitch_list("d s b f d d")
t8.reach("BB")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #44 Brandon Workman, batting 9th
t8.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - 36 - 3)
t8.new_ab()
t8.pitch_list("b d s c c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #67 William Cuevas
b8 = game.new_inning()

# Pitching change (BOS): #67 William Cuevas replaces #44 Brandon Workman, batting 9th
b8.pitching_substitution(67)
b8.defensive_substitution(9, 67, "1")

# 6. WSH #14 Mark Reynolds (X - X - X)
b8.new_ab()
b8.pitch_list("f b b f")
b8.out("G6-3")

# 7. WSH #3  Michael A. Taylor (X - X - X)
b8.new_ab()
b8.pitch_list("b s f b b")
b8.out("G6-3")

# 8. WSH #29 Pedro Severino (X - X - X)
b8.new_ab()
b8.pitch_list("s b")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: WSH #33 Matt Grace
t9 = game.new_inning()

# Pitching change (WSH): #33 Matt Grace replaces #55 Tim Collins, batting 5th
t9.pitching_substitution(33)
t9.defensive_substitution(5, 33, "1")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b b")
t9.reach("BB")
t9.thrown_out(2, "16 FC3-6", 1, 33)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t9.new_ab()
t9.pitch_list("c b s b")
t9.reach("FC3-6")
t9.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t9.new_ab()
t9.pitch_list("b f")
t9.hit(4, rbis=2)

# 4. BOS #25 Steve Pearce (X - X - X)
t9.new_ab()
t9.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("b c f b")
t9.out("G4-3")


# Bot 9th
# Pitching: BOS #67 William Cuevas
b9 = game.new_inning()

# 9. WSH #8  Brian Goodwin (X - X - X)
b9.new_ab()
b9.pitch_list("c")
b9.hit(4)

# 1. WSH #7  Trea Turner (X - X - X)
b9.new_ab()
b9.pitch_list("s s b")
b9.hit(1)
b9.advance(2, "22 G3-1")

# 2. WSH #22 Juan Soto (X - X - 7)
b9.new_ab()
b9.pitch_list("b")
b9.out("G3-1")

# 3. WSH #6  Anthony Rendon (X - 7 - X)
b9.new_ab()
b9.pitch_list("f s")
b9.out("F9")

# 4. WSH #1  Wilmer Difo (X - 7 - X)
b9.new_ab()
b9.pitch_list("c b s b f")
b9.out("G4-3")

# Winning team: BOS
# WP: BOS #44 Brandon Workman
game.winning_pitcher(44, is_away_team=True)

# Loser team: WSH
# LP: WSH #57 Tanner Roark
game.losing_pitcher(57)

# print(game)
game.generate_scorecard()
