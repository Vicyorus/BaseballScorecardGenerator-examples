import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-08-11, game 1 of 2
# https://www.baseball-reference.com/boxes/BAL/BAL201808111.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/08/11/530932/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-11 13:07-15:55",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "18,003",
        "temp": "87F, Partly Cloudy",
        "wind": "8mph, Out To CF",
        "away": {
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
                68: "Dan Butler",
                11: "Rafael Devers",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                67: "William Cuevas",
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
                [68, "C"],
                [11, "3B"],
            ],
            "bullpen": [47, 44, 67, 22, 31, 61, 37, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 31,
            "roster": {
                # Lineup
                34: "Jonathan Villar",
                1: "Tim Beckham",
                10: "Adam Jones",
                45: "Mark Trumbo",
                16: "Trey Mancini",
                19: "Chris Davis",
                39: "Renato Núñez",
                3: "Cedric Mullins",
                61: "Austin Wynns",
                # Starting pitcher
                31: "Jimmy Yacabonis",
                # Bench
                29: "Jace Peterson",
                36: "Caleb Joseph",
                23: "Joey Rickard",
                # Bullpen
                63: "Sean Gilmartin",
                17: "Alex Cobb",
                32: "Yefry Ramírez",
                41: "David Hess",
                49: "Cody Carroll",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                51: "Paul Fry",
                58: "Evan Phillips",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
            },
            "lefties": [63, 66, 51],
            "lineup": [
                [34, "4"],
                [1, "6"],
                [10, "9"],
                [45, "0"],
                [16, "7"],
                [19, "3"],
                [39, "5"],
                [3, "8"],
                [61, "2"],
            ],
            "bench": [
                [29, "SS"],
                [36, "C"],
                [23, "RF"],
            ],
            "bullpen": [63, 17, 32, 41, 49, 66, 54, 51, 58, 60, 37, 43, 50],
        },
        "umpires": {
            "HP": "Tripp Gibson",
            "1B": "Andy Fletcher",
            "2B": "Adrian Johnson",
            "3B": "Marvin Hudson",
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
# Pitching: BAL #31 Jimmy Yacabonis
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f f b")
t1.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b f")
t1.out("L7")

# 3. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F7")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. BAL #34 Jonathan Villar (X - X - X)
b1.new_ab()
b1.pitch_list("c b f b")
b1.out("F8")

# 2. BAL #1  Tim Beckham (X - X - X)
b1.new_ab()
b1.out("P3")

# 3. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #31 Jimmy Yacabonis
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)

# 6. BOS #12 Brock Holt (X - X - 2)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t2.new_ab()
t2.pitch_list("b f")
t2.out("F9")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 4. BAL #45 Mark Trumbo (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("P4")

# 5. BAL #16 Trey Mancini (X - X - X)
b2.new_ab()
b2.pitch_list("b s b s")
b2.hit(1)

# 6. BAL #19 Chris Davis (X - X - 16)
b2.new_ab()
b2.pitch_list("c c b s")
b2.out("K")

# 7. BAL #39 Renato Núñez (X - X - 16)
b2.new_ab()
b2.pitch_list("b b b s c")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #31 Jimmy Yacabonis
t3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.out("P5")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c b s f")
t3.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c s b b f t")
t3.out("KT")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 8. BAL #3  Cedric Mullins (X - X - X)
b3.new_ab()
b3.pitch_list("b f c b f c")
b3.out("!K")

# 9. BAL #61 Austin Wynns (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.hit(1)
b3.advance(2, "34 G6-3")

# 1. BAL #34 Jonathan Villar (X - X - 61)
b3.new_ab()
b3.pitch_list("f f")
b3.out("G6-3")

# 2. BAL #1  Tim Beckham (X - 61 - X)
b3.new_ab()
b3.pitch_list("c b b s b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #31 Jimmy Yacabonis
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("F7")

# 3. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("f f b")
t4.out("G5-3")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 3. BAL #10 Adam Jones (X - X - X)
b4.new_ab()
b4.pitch_list("c f b f")
b4.hit(1)

# 4. BAL #45 Mark Trumbo (X - X - 10)
b4.new_ab()
b4.pitch_list("b c s c")
b4.out("!K")

# 5. BAL #16 Trey Mancini (X - X - 10)
b4.new_ab()
b4.pitch_list("b c f c")
b4.out("!K")

# 6. BAL #19 Chris Davis (X - X - 10)
b4.new_ab()
b4.pitch_list("s s b f b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #31 Jimmy Yacabonis
t5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(4, "36 HR")

# 6. BOS #12 Brock Holt (X - X - 2)
t5.new_ab()
t5.pitch_list("b 1 b")
t5.out("L8")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t5.new_ab()
t5.pitch_list("b b b")
t5.hit(4, rbis=2)

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(4, rbis=1)

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.hit(1)
t5.advance(3, "16 1B")

# Pitching change (BAL): #63 Sean Gilmartin replaces #31 Jimmy Yacabonis
t5.pitching_substitution(63)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("1 b b 1 b c")
t5.hit(1)
t5.thrown_out(2, "18 FC4-6", 3, 63)

# 3. BOS #18 Mitch Moreland (50 - X - 16)
t5.new_ab()
t5.pitch_list("b c f 1")
t5.reach("FC4-6")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 7. BAL #39 Renato Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b c s")
b5.out("F7")

# 8. BAL #3  Cedric Mullins (X - X - X)
b5.new_ab()
b5.pitch_list("l")
b5.hit(1)

# 9. BAL #61 Austin Wynns (X - X - 3)
b5.new_ab()
b5.pitch_list("b c f s")
b5.out("K")

# 1. BAL #34 Jonathan Villar (X - X - 3)
b5.new_ab()
b5.pitch_list("1 s b s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #63 Sean Gilmartin
t6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L8")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("b c b")
t6.hit(2)
t6.error(5)
t6.advance(3, "12 SB")
t6.advance(4, "12 E5")

# 6. BOS #12 Brock Holt (X - 2 - X)
t6.new_ab()
t6.pitch_list("c b")
t6.hit(1)
t6.thrown_out(2, "36 DP6-4-3", 2, 63)

# 7. BOS #36 Eduardo Núñez (X - X - 12)
t6.new_ab()
t6.pitch_list("b f")
t6.out("DP6-4-3")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 2. BAL #1  Tim Beckham (X - X - X)
b6.new_ab()
b6.pitch_list("b s t")
b6.out("L4")

# 3. BAL #10 Adam Jones (X - X - X)
b6.new_ab()
b6.pitch_list("s f")
b6.hit(2)

# 4. BAL #45 Mark Trumbo (X - 10 - X)
b6.new_ab()
b6.pitch_list("b f s s")
b6.out("K")

# 5. BAL #16 Trey Mancini (X - 10 - X)
b6.new_ab()
b6.pitch_list("c c")
b6.out("G1-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #63 Sean Gilmartin
t7 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")
t7.advance(2, "19 G1-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
t7.new_ab()
t7.pitch_list("c f b")
t7.out("G1-3")

# 1. BOS #50 Mookie Betts (X - 3 - X)
t7.new_ab()
t7.pitch_list("b c d d b")
t7.reach("BB")
t7.thrown_out(2, "18 FC4-6", 3, 63)

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
t7.new_ab()
t7.out("F7")

# 3. BOS #18 Mitch Moreland (X - 3 - 50)
t7.new_ab()
t7.pitch_list("c b b f")
t7.reach("FC4-6")


# Bot 7th
# Pitching: BOS #47 Tyler Thornburg
b7 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #24 David Price
b7.pitching_substitution(47)

# 6. BAL #19 Chris Davis (X - X - X)
b7.new_ab()
b7.pitch_list("c b b c b t")
b7.out("KT")

# 7. BAL #39 Renato Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b b f f")
b7.out("F8")

# 8. BAL #3  Cedric Mullins (X - X - X)
b7.new_ab()
b7.out("F7")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #50 Miguel Castro
t8 = game.new_inning()

# Pitching change (BAL): #50 Miguel Castro replaces #63 Sean Gilmartin
t8.pitching_substitution(50)

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("s s s")
t8.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.pitch_list("c f t")
t8.out("KT")

# 6. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b f b b b")
t8.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - X - 12)
t8.new_ab()
t8.pitch_list("b 1 b c b f")
t8.out("G5-3")


# Bot 8th
# Pitching: BOS #70 Ryan Brasier
b8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
b8.pitching_substitution(70)

# 9. BAL #61 Austin Wynns (X - X - X)
b8.new_ab()
b8.out("P4")

# 1. BAL #34 Jonathan Villar (X - X - X)
b8.new_ab()
b8.pitch_list("c b b s f b s")
b8.out("K")

# 2. BAL #1  Tim Beckham (X - X - X)
b8.new_ab()
b8.pitch_list("f b t b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #50 Miguel Castro
t9 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("t b b s")
t9.hit(4, rbis=1)

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.pitch_list("c b b b f")
t9.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b f f")
t9.out("L6")


# Bot 9th
# Pitching: BOS #32 Matt Barnes
b9 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #70 Ryan Brasier
b9.pitching_substitution(32)

# 3. BAL #10 Adam Jones (X - X - X)
b9.new_ab()
b9.pitch_list("f s b s")
b9.out("K2-3")

# 4. BAL #45 Mark Trumbo (X - X - X)
b9.new_ab()
b9.pitch_list("b f s s")
b9.out("K")

# 5. BAL #16 Trey Mancini (X - X - X)
b9.new_ab()
b9.pitch_list("s c b f")
b9.out("F8")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24, is_away_team=True)

# Loser team: BAL
# LP: BAL #31 Jimmy Yacabonis
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
