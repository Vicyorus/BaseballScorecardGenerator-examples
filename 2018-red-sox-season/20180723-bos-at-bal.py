import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-07-23
# https://www.baseball-reference.com/boxes/BAL/BAL201807230.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/07/23/530905/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-23 19:08-23:02 (1:00 delay)",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "16,885",
        "temp": "81F, Rain",
        "wind": "5mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                12: "Brock Holt",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                5: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [12, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [5, "OF"],
                [25, "1B"],
                [36, "SS"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 41, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 34,
            "roster": {
                # Lineup
                1: "Tim Beckham",
                6: "Jonathan Schoop",
                10: "Adam Jones",
                45: "Mark Trumbo",
                19: "Chris Davis",
                16: "Trey Mancini",
                39: "Renato Núñez",
                36: "Caleb Joseph",
                29: "Jace Peterson",
                # Starting pitcher
                34: "Kevin Gausman",
                # Bench
                61: "Austin Wynns",
                23: "Joey Rickard",
                2: "Danny Valencia",
                # Bullpen
                17: "Alex Cobb",
                32: "Yefry Ramírez",
                66: "Tanner Scott",
                53: "Zack Britton",
                54: "Andrew Cashner",
                51: "Paul Fry",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                59: "Jhan Mariñez",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                35: "Brad Brach",
            },
            "lefties": [66, 53, 51],
            "lineup": [
                [1, "6"],
                [6, "4"],
                [10, "8"],
                [45, "0"],
                [19, "3"],
                [16, "7"],
                [39, "5"],
                [36, "2"],
                [29, "9"],
            ],
            "bench": [
                [61, "C"],
                [23, "RF"],
                [2, "3B"],
            ],
            "bullpen": [17, 32, 66, 53, 54, 51, 60, 37, 59, 43, 50, 35],
        },
        "umpires": {
            "HP": "Chris Conroy",
            "1B": "Brian O'Nora",
            "2B": "Fieldin Culbreth",
            "3B": "CB Bucknor",
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
# Pitching: BAL #34 Kevin Gausman
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b s")
t1.out("G1-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. BAL #1  Tim Beckham (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.hit(1)
b1.thrown_out(2, "45 2-3-4", 3, 22)

# 2. BAL #6  Jonathan Schoop (X - X - 1)
b1.new_ab()
b1.pitch_list("c b s")
b1.out("P4")

# 3. BAL #10 Adam Jones (X - X - 1)
b1.new_ab()
b1.out("L7")

# 4. BAL #45 Mark Trumbo (X - X - 1)
b1.new_ab()
b1.pitch_list("c d")
b1.no_ab("2-3-4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #34 Kevin Gausman
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(4, rbis=1)

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b")
t2.out("G6-3")

# 6. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b")
t2.out("G4-3")

# 7. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b s f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 4. BAL #45 Mark Trumbo (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("F8")

# 5. BAL #19 Chris Davis (X - X - X)
b2.new_ab()
b2.pitch_list("b f f f b")
b2.out("G4-3")

# 6. BAL #16 Trey Mancini (X - X - X)
b2.new_ab()
b2.hit(2)

# 7. BAL #39 Renato Núñez (X - 16 - X)
b2.new_ab()
b2.pitch_list("c c b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #34 Kevin Gausman
t3 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("f b s b")
t3.out("L7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c c b b")
t3.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c b b b f f")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 8. BAL #36 Caleb Joseph (X - X - X)
b3.new_ab()
b3.pitch_list("f c b b c")
b3.out("!K")

# 9. BAL #29 Jace Peterson (X - X - X)
b3.new_ab()
b3.pitch_list("c s b b f f b b")
b3.reach("BB")
b3.thrown_out(4, "6 7-6-2", 3, 22)
b3.advance(3, "6 2B")

# 1. BAL #1  Tim Beckham (X - X - 29)
b3.new_ab()
b3.pitch_list("c 1 l b b")
b3.out("F8")

# 2. BAL #6  Jonathan Schoop (X - X - 29)
b3.new_ab()
b3.pitch_list("d f")
b3.hit(2)


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #34 Kevin Gausman
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b f")
t4.out("F9")

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.out("F7")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 3. BAL #10 Adam Jones (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(1)
b4.advance(2, "45 G5-3")
b4.advance(3, "19 BLK")

# 4. BAL #45 Mark Trumbo (X - X - 10)
b4.new_ab()
b4.pitch_list("c")
b4.out("G5-3")

# 5. BAL #19 Chris Davis (X - 10 - X)
b4.new_ab()
b4.pitch_list("b b n b f f s")
b4.balk()
b4.out("K")

# 6. BAL #16 Trey Mancini (10 - X - X)
b4.new_ab()
b4.pitch_list("s b d b c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #34 Kevin Gausman
t5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.hit(2)
t5.advance(3, "12 G4-3")
t5.advance(4, "19 BB")

# 6. BOS #12 Brock Holt (X - 2 - X)
t5.new_ab()
t5.out("G4-3")

# 7. BOS #11 Rafael Devers (2 - X - X)
t5.new_ab()
t5.pitch_list("f b b f f b f b")
t5.reach("BB")
t5.advance(2, "3 BB")
t5.advance(3, "19 BB")
t5.advance(4, "16 2B")

# 8. BOS #3  Sandy León (2 - X - 11)
t5.new_ab()
t5.pitch_list("b b b b")
t5.reach("BB")
t5.advance(2, "19 BB")
t5.advance(4, "16 2B")

# 9. BOS #19 Jackie Bradley Jr. (2 - 11 - 3)
t5.new_ab()
t5.pitch_list("f b b b b")
t5.reach("BB", rbis=1)
t5.advance(3, "16 2B")
t5.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (11 - 3 - 19)
t5.new_ab()
t5.pitch_list("c b f s")
t5.out("K")

# 2. BOS #16 Andrew Benintendi (11 - 3 - 19)
t5.new_ab()
t5.pitch_list("d b t b")
t5.hit(2, rbis=2)
t5.advance(3, "28 1B")

# Pitching change (BAL): #50 Miguel Castro replaces #34 Kevin Gausman
t5.pitching_substitution(50)

# 3. BOS #28 J.D. Martinez (19 - 16 - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1, rbis=1)
t5.advance(2, "18 SB")

# 4. BOS #18 Mitch Moreland (16 - X - 28)
t5.new_ab()
t5.pitch_list("f f f b")
t5.out("G3")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 7. BAL #39 Renato Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("f b f t")
b5.out("KT")

# 8. BAL #36 Caleb Joseph (X - X - X)
b5.new_ab()
b5.out("G6-3")

# 9. BAL #29 Jace Peterson (X - X - X)
b5.new_ab()
b5.pitch_list("b c b")
b5.hit(1)

# 1. BAL #1  Tim Beckham (X - X - 29)
b5.new_ab()
b5.pitch_list("d")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #50 Miguel Castro
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")

# 6. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.pitch_list("b c f b f b f f")
t6.out("G4-3")

# 7. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 2. BAL #6  Jonathan Schoop (X - X - X)
b6.new_ab()
b6.pitch_list("b s")
b6.out("F7")

# 3. BAL #10 Adam Jones (X - X - X)
b6.new_ab()
b6.pitch_list("b b s f f s")
b6.out("K")

# 4. BAL #45 Mark Trumbo (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f")
b6.hit(1)

# 5. BAL #19 Chris Davis (X - X - 45)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #50 Miguel Castro
t7 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b f f")
t7.out("G1-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("s b")
t7.out("G6-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c s b b b f f")
t7.hit(1)
t7.thrown_out(2, "16 CS", 3, 50)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t7.new_ab()
t7.pitch_list("f b f b")
t7.no_ab("CS")


# Bot 7th
# Pitching: BOS #70 Ryan Brasier
b7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #22 Rick Porcello
b7.pitching_substitution(70)

# 6. BAL #16 Trey Mancini (X - X - X)
b7.new_ab()
b7.pitch_list("s s b b")
b7.out("L8")

# 7. BAL #39 Renato Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("b b s f t")
b7.out("KT")

# 8. BAL #36 Caleb Joseph (X - X - X)
b7.new_ab()
b7.pitch_list("b f")
b7.hit(1)

# 9. BAL #29 Jace Peterson (X - X - 36)
b7.new_ab()
b7.pitch_list("c s d f f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #50 Miguel Castro
t8 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.thrown_out(2, "28 DP6-4-3", 1, 50)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t8.new_ab()
t8.pitch_list("b s b")
t8.out("DP6-4-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b b b b")
t8.reach("BB")
t8.thrown_out(2, "2 FC5-4", 3, 59)

# Pitching change (BAL): #59 Jhan Mariñez replaces #50 Miguel Castro
t8.pitching_substitution(59)

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t8.new_ab()
t8.pitch_list("b f")
t8.reach("FC5-4")


# Bot 8th
# Pitching: BOS #44 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #70 Ryan Brasier
b8.pitching_substitution(44)

# 1. BAL #1  Tim Beckham (X - X - X)
b8.new_ab()
b8.pitch_list("b s c b")
b8.hit(1)
b8.advance(4, "6 HR")

# 2. BAL #6  Jonathan Schoop (X - X - 1)
b8.new_ab()
b8.hit(4, rbis=2)

# 3. BAL #10 Adam Jones (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F9")

# 4. BAL #45 Mark Trumbo (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b s")
b8.out("K")

# 5. BAL #19 Chris Davis (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #59 Jhan Mariñez
t9 = game.new_inning()

# 6. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("b b b c b")
t9.reach("BB")
t9.advance(2, "11 1B")
t9.advance(3, "3 SAC2-3")

# 7. BOS #11 Rafael Devers (X - X - 12)
t9.new_ab()
t9.pitch_list("b")
t9.hit(1)
t9.advance(2, "3 SAC2-3")
t9.thrown_out(3, "50 DP8-4", 3, 59)

# 8. BOS #3  Sandy León (X - 12 - 11)
t9.new_ab()
t9.pitch_list("l")
t9.out("SAC2-3")

# 9. BOS #19 Jackie Bradley Jr. (12 - 11 - X)
t9.new_ab()
t9.pitch_list("b f b b b")
t9.reach("BB")

# 1. BOS #50 Mookie Betts (12 - 11 - 19)
t9.new_ab()
t9.pitch_list("c c b f b")
t9.out("DP8-4")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #44 Brandon Workman
b9.pitching_substitution(46)

# 6. BAL #16 Trey Mancini (X - X - X)
b9.new_ab()
b9.out("L9")

# 7. BAL #39 Renato Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("s t")
b9.hit(2)
b9.advance(4, "36 1B")

# 8. BAL #36 Caleb Joseph (X - 39 - X)
b9.new_ab()
b9.hit(1, rbis=1)
b9.thrown_out(2, "29 DP3-6", 3, 46)

# 9. BAL #29 Jace Peterson (X - X - 36)
b9.new_ab()
b9.pitch_list("b b f f f b f f")
b9.out("DP3-6")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: BAL
# LP: BAL #34 Kevin Gausman
game.losing_pitcher(34)

# print(game)
game.generate_scorecard()
