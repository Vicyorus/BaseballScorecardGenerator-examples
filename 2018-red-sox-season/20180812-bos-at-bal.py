import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-08-12
# https://www.baseball-reference.com/boxes/BAL/BAL201808120.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/08/12/531173/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-12 13:07-16:11",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "25,303",
        "temp": "85F, Cloudy",
        "wind": "1mph, In From CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                68: "Dan Butler",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                # Bullpen
                47: "Tyler Thornburg",
                22: "Rick Porcello",
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
            "lefties": [41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [12, "6"],
                [25, "0"],
                [28, "7"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [68, "C"],
                [16, "LF"],
                [2, "2B"],
            ],
            "bullpen": [47, 22, 31, 61, 37, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 17,
            "roster": {
                # Lineup
                23: "Joey Rickard",
                34: "Jonathan Villar",
                10: "Adam Jones",
                16: "Trey Mancini",
                1: "Tim Beckham",
                19: "Chris Davis",
                39: "Renato Núñez",
                61: "Austin Wynns",
                3: "Cedric Mullins",
                # Starting pitcher
                17: "Alex Cobb",
                # Bench
                29: "Jace Peterson",
                45: "Mark Trumbo",
                36: "Caleb Joseph",
                # Bullpen
                63: "Sean Gilmartin",
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
                [23, "7"],
                [34, "4"],
                [10, "9"],
                [16, "0"],
                [1, "6"],
                [19, "3"],
                [39, "5"],
                [61, "2"],
                [3, "8"],
            ],
            "bench": [
                [29, "SS"],
                [45, "1B"],
                [36, "C"],
            ],
            "bullpen": [63, 32, 41, 49, 66, 54, 51, 58, 60, 37, 43, 50],
        },
        "umpires": {
            "HP": "Adrian Johnson",
            "1B": "Marvin Hudson",
            "2B": "Tripp Gibson",
            "3B": "Hunter Wendelstedt",
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
# Pitching: BAL #17 Alex Cobb
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c f b f f s")
t1.out("K")

# 2. BOS #12 Brock Holt (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.out("G5-3")

# 3. BOS #25 Steve Pearce (X - X - X)
t1.new_ab()
t1.pitch_list("b c f f")
t1.hit(4, rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b s f b s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b1.new_ab()
b1.pitch_list("f b c f b")
b1.out("F8")

# 2. BAL #34 Jonathan Villar (X - X - X)
b1.new_ab()
b1.pitch_list("b f s s")
b1.out("K")

# 3. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("c c c")
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #17 Alex Cobb
t2 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G1-5-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("F8")

# 7. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b")
t2.out("L7")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 4. BAL #16 Trey Mancini (X - X - X)
b2.new_ab()
b2.out("G5-3")

# 5. BAL #1  Tim Beckham (X - X - X)
b2.new_ab()
b2.pitch_list("c f c")
b2.out("!K")

# 6. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #17 Alex Cobb
t3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f f")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 7. BAL #39 Renato Núñez (X - X - X)
b3.new_ab()
b3.pitch_list("c c b")
b3.hit(1)

# 8. BAL #61 Austin Wynns (X - X - 39)
b3.new_ab()
b3.pitch_list("b c b s b c")
b3.out("!K")

# 9. BAL #3  Cedric Mullins (X - X - 39)
b3.new_ab()
b3.pitch_list("b s c s")
b3.out("K")

# 1. BAL #23 Joey Rickard (X - X - 39)
b3.new_ab()
b3.pitch_list("c c b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #17 Alex Cobb
t4 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.hit(1)
t4.error(9)
t4.advance(3, "28 2B")
t4.advance("U", "28 E9")

# 3. BOS #25 Steve Pearce (X - X - 12)
t4.new_ab()
t4.pitch_list("b b f b")
t4.out("(F)P2")

# 4. BOS #28 J.D. Martinez (X - X - 12)
t4.new_ab()
t4.hit(2)

# 5. BOS #18 Mitch Moreland (X - 28 - X)
t4.new_ab()
t4.pitch_list("b b f")
t4.out("G1-3")

# 6. BOS #36 Eduardo Núñez (X - 28 - X)
t4.new_ab()
t4.pitch_list("c b")
t4.out("G6-3")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 2. BAL #34 Jonathan Villar (X - X - X)
b4.new_ab()
b4.pitch_list("f t b b t")
b4.out("KT")

# 3. BAL #10 Adam Jones (X - X - X)
b4.new_ab()
b4.out("G6-3")

# 4. BAL #16 Trey Mancini (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #17 Alex Cobb
t5 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("f s b b s")
t5.out("K")

# 8. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c c s")
t5.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f")
t5.hit(1)
t5.thrown_out(2, "50 FC5-4", 3, 17)

# 1. BOS #50 Mookie Betts (X - X - 19)
t5.new_ab()
t5.pitch_list("b 1")
t5.reach("FC5-4")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 5. BAL #1  Tim Beckham (X - X - X)
b5.new_ab()
b5.pitch_list("f c f s")
b5.out("K")

# 6. BAL #19 Chris Davis (X - X - X)
b5.new_ab()
b5.pitch_list("c f b s")
b5.out("K")

# 7. BAL #39 Renato Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b b s s s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #17 Alex Cobb
t6 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("b c b c s")
t6.out("K")

# 3. BOS #25 Steve Pearce (X - X - X)
t6.new_ab()
t6.pitch_list("b c b c b b")
t6.reach("BB")
t6.advance(3, "28 2B")

# 4. BOS #28 J.D. Martinez (X - X - 25)
t6.new_ab()
t6.pitch_list("f")
t6.hit(2)

# 5. BOS #18 Mitch Moreland (25 - 28 - X)
t6.new_ab()
t6.pitch_list("c b f s")
t6.out("K")

# 6. BOS #36 Eduardo Núñez (25 - 28 - X)
t6.new_ab()
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #47 Tyler Thornburg
b6 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #41 Chris Sale
b6.pitching_substitution(47)

# 8. BAL #61 Austin Wynns (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G5-3")

# 9. BAL #3  Cedric Mullins (X - X - X)
b6.new_ab()
b6.pitch_list("c f b b b f")
b6.out("L8")

# 1. BAL #23 Joey Rickard (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c")
b6.hit(1)
b6.advance(2, "34 BB")
b6.advance(3, "10 PB")

# 2. BAL #34 Jonathan Villar (X - X - 23)
b6.new_ab()
b6.pitch_list("b c b 1 b b")
b6.reach("BB")
b6.advance(2, "10 PB")

# 3. BAL #10 Adam Jones (X - 23 - 34)
b6.new_ab()
b6.pitch_list("b d s b b")
b6.pb()
b6.reach("BB")

# Pitching change (BOS): #70 Ryan Brasier replaces #47 Tyler Thornburg
b6.pitching_substitution(70)

# 4. BAL #16 Trey Mancini (23 - 34 - 10)
b6.new_ab()
b6.pitch_list("b b c s f d f f t")
b6.out("KT")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #17 Alex Cobb
t7 = game.new_inning()

# 7. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.advance(2, "3 SAC1-3")

# 8. BOS #3  Sandy León (X - X - 11)
t7.new_ab()
t7.out("SAC1-3")

# 9. BOS #19 Jackie Bradley Jr. (X - 11 - X)
t7.new_ab()
t7.pitch_list("b d c b s s")
t7.out("K")

# 1. BOS #50 Mookie Betts (X - 11 - X)
t7.new_ab()
t7.pitch_list("d c b d v")
t7.reach("IBB")

# 2. BOS #12 Brock Holt (X - 11 - 50)
t7.new_ab()
t7.pitch_list("c")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #61 Brian Johnson
b7 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #70 Ryan Brasier
b7.pitching_substitution(61)

# 5. BAL #1  Tim Beckham (X - X - X)
b7.new_ab()
b7.pitch_list("b c s b")
b7.out("L6")

# 6. BAL #19 Chris Davis (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# 7. BAL #39 Renato Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b b c s b b")
b7.reach("BB")
b7.thrown_out(2, "61 FC6-4", 3, 61)

# 8. BAL #61 Austin Wynns (X - X - 39)
b7.new_ab()
b7.pitch_list("c")
b7.reach("FC6-4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #60 Mychal Givens
t8 = game.new_inning()

# Pitching change (BAL): #60 Mychal Givens replaces #17 Alex Cobb
t8.pitching_substitution(60)

# 3. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("c b s f f b f f")
t8.out("L7")

# 4. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("s")
t8.out("L8")

# 5. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b f s s")
t8.out("K")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #61 Brian Johnson
b8.pitching_substitution(32)

# 9. BAL #3  Cedric Mullins (X - X - X)
b8.new_ab()
b8.hit(1)
b8.advance(2, "34 1B")
b8.advance(3, "10 WP")
b8.advance(4, "16 SF8")

# 1. BAL #23 Joey Rickard (X - X - 3)
b8.new_ab()
b8.pitch_list("b b c f 1")
b8.out("F8")

# 2. BAL #34 Jonathan Villar (X - X - 3)
b8.new_ab()
b8.pitch_list("1")
b8.hit(1)
b8.advance(2, "10 WP")
b8.advance(3, "16 SF8")

# 3. BAL #10 Adam Jones (X - 3 - 34)
b8.new_ab()
b8.pitch_list("b b b b")
b8.wp()
b8.reach("BB")

# 4. BAL #16 Trey Mancini (3 - 34 - 10)
b8.new_ab()
b8.pitch_list("c b b f")
b8.out("SF8", rbis=1)

# 5. BAL #1  Tim Beckham (34 - X - 10)
b8.new_ab()
b8.pitch_list("f c b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #60 Mychal Givens
t9 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("s b f")
t9.hit(1)
t9.advance(2, "3 SB")
t9.advance(4, "19 1B")

# 7. BOS #11 Rafael Devers (X - X - 36)
t9.new_ab()
t9.pitch_list("1 c t s")
t9.out("K")

# 8. BOS #3  Sandy León (X - X - 36)
t9.new_ab()
t9.pitch_list("c 1 s f 1 f d d f")
t9.out("P6")

# 9. BOS #19 Jackie Bradley Jr. (X - 36 - X)
t9.new_ab()
t9.pitch_list("b f")
t9.hit(1, rbis=1)
t9.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (X - X - 19)
t9.new_ab()
t9.pitch_list("b 1 b")
t9.hit(2, rbis=1)

# Pitching change (BAL): #66 Tanner Scott replaces #60 Mychal Givens
t9.pitching_substitution(66)

# 2. BOS #12 Brock Holt (X - 50 - X)
t9.new_ab()
t9.pitch_list("c s b")
t9.out("F7")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b9.pitching_substitution(46)

# 6. BAL #19 Chris Davis (X - X - X)
b9.new_ab()
b9.pitch_list("f b b s c")
b9.out("!K")

# 7. BAL #39 Renato Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b c b")
b9.reach("BB")
b9.advance(2, "61 1B")

# 8. BAL #61 Austin Wynns (X - X - 39)
b9.new_ab()
b9.pitch_list("b b c f")
b9.hit(1)

# 9. BAL #3  Cedric Mullins (X - 39 - 61)
b9.new_ab()
b9.pitch_list("b b c c s")
b9.out("K")

# Offensive change (BAL): Pinch-hitter #45 Mark Trumbo replaces #23 Joey Rickard, batting 1st
b9.offensive_substitution(1, 45, "PH")

# 1. BAL #45 Mark Trumbo (X - 39 - 61)
b9.new_ab()
b9.pitch_list("c b s s")
b9.out("K")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: BAL
# LP: BAL #17 Alex Cobb
game.losing_pitcher(17)

# print(game)
game.generate_scorecard()
