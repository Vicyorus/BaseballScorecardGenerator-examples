import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-12
# https://www.baseball-reference.com/boxes/BAL/BAL201806120.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/06/12/530396/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-12 19:08-23:06",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "21,837",
        "temp": "75F, Partly Cloudy",
        "wind": "8mph, Out To LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                36: "Eduardo Núñez",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                23: "Blake Swihart",
                50: "Mookie Betts",
                3: "Sandy León",
                # Bullpen
                35: "Steven Wright",
                44: "Brandon Workman",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                65: "Justin Haley",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [36, "0"],
                [16, "7"],
                [28, "9"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [23, "C"],
                [50, "SS"],
                [3, "C"],
            ],
            "bullpen": [35, 44, 22, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 41,
            "roster": {
                # Lineup
                23: "Joey Rickard",
                10: "Adam Jones",
                13: "Manny Machado",
                2: "Danny Valencia",
                16: "Trey Mancini",
                6: "Jonathan Schoop",
                45: "Mark Trumbo",
                14: "Craig Gentry",
                61: "Austin Wynns",
                # Starting pitcher
                41: "David Hess",
                # Bench
                19: "Chris Davis",
                29: "Jace Peterson",
                24: "Pedro Alvarez",
                15: "Chance Sisco",
                # Bullpen
                17: "Alex Cobb",
                48: "Richard Bleier",
                34: "Kevin Gausman",
                56: "Darren O'Day",
                53: "Zack Britton",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                57: "Donnie Hart",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                35: "Brad Brach",
            },
            "lefties": [48, 53, 57],
            "lineup": [
                [23, "7"],
                [10, "8"],
                [13, "6"],
                [2, "5"],
                [16, "3"],
                [6, "4"],
                [45, "0"],
                [14, "9"],
                [61, "2"],
            ],
            "bench": [
                [19, "1B"],
                [29, "SS"],
                [24, "3B"],
                [15, "C"],
            ],
            "bullpen": [17, 48, 34, 56, 53, 60, 37, 57, 43, 50, 35],
        },
        "umpires": {
            "HP": "Mark Carlson",
            "1B": "Brian Knight",
            "2B": "Pat Hoberg",
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
# Pitching: BAL #41 David Hess
t1 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
t1.new_ab()
t1.pitch_list("f f f")
t1.out("P6")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t1.new_ab()
t1.pitch_list("c b s s")
t1.out("K")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b f")
b1.hit(4)

# 2. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("s b")
b1.hit(1)
b1.thrown_out(2, "13 FC6-4", 1, 57)

# 3. BAL #13 Manny Machado (X - X - 10)
b1.new_ab()
b1.pitch_list("b c f f")
b1.reach("FC6-4")
b1.thrown_out(2, "2 DP4-6-3", 2, 57)

# 4. BAL #2  Danny Valencia (X - X - 13)
b1.new_ab()
b1.pitch_list("c b s")
b1.out("DP4-6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #41 David Hess
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b b")
t2.reach("BB")
t2.advance(4, "11 HR")

# 6. BOS #11 Rafael Devers (X - X - 2)
t2.new_ab()
t2.pitch_list("f b b 1")
t2.hit(4, rbis=2)

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.out("L8")

# 8. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b")
t2.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("b b f b")
t2.out("F7")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 5. BAL #16 Trey Mancini (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f")
b2.hit(1)
b2.error(7)
b2.advance(2, "6 1B")
b2.advance(3, "6 E7")

# 6. BAL #6  Jonathan Schoop (X - X - 16)
b2.new_ab()
b2.pitch_list("b f")
b2.hit(1)

# 7. BAL #45 Mark Trumbo (16 - X - 6)
b2.new_ab()
b2.pitch_list("s b s f d s")
b2.out("K")

# 8. BAL #14 Craig Gentry (16 - X - 6)
b2.new_ab()
b2.pitch_list("f b s s")
b2.out("K")

# 9. BAL #61 Austin Wynns (16 - X - 6)
b2.new_ab()
b2.pitch_list("b s")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #41 David Hess
t3 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
t3.new_ab()
t3.out("(F)P2")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(4)

# 3. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.reach("HBP")
t3.advance(2, "18 BB")
t3.advance(3, "2 F9")

# 4. BOS #18 Mitch Moreland (X - X - 28)
t3.new_ab()
t3.pitch_list("b b b b")
t3.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - 28 - 18)
t3.new_ab()
t3.pitch_list("c b")
t3.out("F9")

# 6. BOS #11 Rafael Devers (28 - X - 18)
t3.new_ab()
t3.pitch_list("s f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b b")
b3.reach("BB")
b3.advance(2, "10 G6-3")
b3.advance(4, "2 1B")

# 2. BAL #10 Adam Jones (X - X - 23)
b3.new_ab()
b3.pitch_list("c f b b f")
b3.out("G6-3")

# 3. BAL #13 Manny Machado (X - 23 - X)
b3.new_ab()
b3.pitch_list("d c f t")
b3.out("KT")

# 4. BAL #2  Danny Valencia (X - 23 - X)
b3.new_ab()
b3.pitch_list("b f d")
b3.hit(1, rbis=1)

# 5. BAL #16 Trey Mancini (X - X - 2)
b3.new_ab()
b3.pitch_list("s s s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #41 David Hess
t4 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("c b c")
t4.hit(1)
t4.advance(2, "7 1B")
t4.advance(3, "36 1B")
t4.advance(4, "16 BB")

# 8. BOS #7  Christian Vázquez (X - X - 12)
t4.new_ab()
t4.pitch_list("1")
t4.hit(1)
t4.advance(2, "36 1B")
t4.advance(3, "16 BB")
t4.advance(4, "28 BLK")

# 9. BOS #19 Jackie Bradley Jr. (X - 12 - 7)
t4.new_ab()
t4.pitch_list("d b c b f f")
t4.out("L9")

# 1. BOS #36 Eduardo Núñez (X - 12 - 7)
t4.new_ab()
t4.pitch_list("s d f f f")
t4.hit(1)
t4.advance(2, "16 BB")
t4.advance(3, "28 BLK")
t4.thrown_out(4, "18 DP3-2", 3, 50)

# 2. BOS #16 Andrew Benintendi (12 - 7 - 36)
t4.new_ab()
t4.pitch_list("f b b b b")
t4.reach("BB", rbis=1)
t4.advance(2, "28 BLK")

# Pitching change (BAL): #50 Miguel Castro replaces #41 David Hess
t4.pitching_substitution(50)

# 3. BOS #28 J.D. Martinez (7 - 36 - 16)
t4.new_ab()
t4.pitch_list("c d n f b b b")
t4.balk()
t4.reach("BB")

# 4. BOS #18 Mitch Moreland (36 - 16 - 28)
t4.new_ab()
t4.pitch_list("f")
t4.out("DP3-2")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 6. BAL #6  Jonathan Schoop (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G4-3")

# 7. BAL #45 Mark Trumbo (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b b")
b4.out("P4")

# 8. BAL #14 Craig Gentry (X - X - X)
b4.new_ab()
b4.hit(1)
b4.advance(2, "61 1B")

# 9. BAL #61 Austin Wynns (X - X - 14)
b4.new_ab()
b4.pitch_list("1 c b b t b")
b4.hit(1)

# 1. BAL #23 Joey Rickard (X - 14 - 61)
b4.new_ab()
b4.out("F8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #50 Miguel Castro
t5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "12 WP")
t5.advance(4, "7 1B")

# 6. BOS #11 Rafael Devers (X - X - 2)
t5.new_ab()
t5.pitch_list("b")
t5.out("F9")

# 7. BOS #12 Brock Holt (X - X - 2)
t5.new_ab()
t5.pitch_list("b b b v")
t5.wp()
t5.reach("IBB")
t5.advance(3, "7 1B")

# 8. BOS #7  Christian Vázquez (X - 2 - 12)
t5.new_ab()
t5.pitch_list("c f")
t5.hit(1, rbis=1)
t5.thrown_out(2, "19 DP4-6-3", 2, 50)

# 9. BOS #19 Jackie Bradley Jr. (12 - X - 7)
t5.new_ab()
t5.out("DP4-6-3")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 2. BAL #10 Adam Jones (X - X - X)
b5.new_ab()
b5.out("F7")

# 3. BAL #13 Manny Machado (X - X - X)
b5.new_ab()
b5.pitch_list("b b s c b b")
b5.reach("BB")

# 4. BAL #2  Danny Valencia (X - X - 13)
b5.new_ab()
b5.pitch_list("b c b f")
b5.out("P4")

# 5. BAL #16 Trey Mancini (X - X - 13)
b5.new_ab()
b5.pitch_list("b b c f f b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #50 Miguel Castro
t6 = game.new_inning()

# 1. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.out("L8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c b s b s")
t6.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("f b s f")
t6.out("L5")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 6. BAL #6  Jonathan Schoop (X - X - X)
b6.new_ab()
b6.pitch_list("b f s b")
b6.out("G6-3")

# 7. BAL #45 Mark Trumbo (X - X - X)
b6.new_ab()
b6.pitch_list("f c b b")
b6.out("G4-3")

# 8. BAL #14 Craig Gentry (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.hit(1)

# Pitching change (BOS): #76 Hector Velázquez replaces #57 Eduardo Rodriguez
b6.pitching_substitution(76)

# 9. BAL #61 Austin Wynns (X - X - 14)
b6.new_ab()
b6.pitch_list("c c b s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #53 Zack Britton
t7 = game.new_inning()

# Pitching change (BAL): #53 Zack Britton replaces #50 Miguel Castro
t7.pitching_substitution(53)

# 4. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("c b b b s b")
t7.reach("BB")
t7.thrown_out(2, "2 2-4", 1, 53)

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t7.new_ab()
t7.pitch_list("d d c t b b")
t7.reach("BB")
t7.advance(2, "12 BB")

# 6. BOS #11 Rafael Devers (X - X - 2)
t7.new_ab()
t7.pitch_list("s f d s")
t7.out("K")

# 7. BOS #12 Brock Holt (X - X - 2)
t7.new_ab()
t7.pitch_list("b b b b")
t7.reach("BB")

# 8. BOS #7  Christian Vázquez (X - 2 - 12)
t7.new_ab()
t7.pitch_list("d c f f b")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b7.new_ab()
b7.pitch_list("b c b s")
b7.out("F9")

# 2. BAL #10 Adam Jones (X - X - X)
b7.new_ab()
b7.pitch_list("c b s f f")
b7.hit(1)
b7.advance(2, "13 1B")
b7.advance(3, "2 BB")
b7.thrown_out(4, "6 FC1-2", 3, 56)

# 3. BAL #13 Manny Machado (X - X - 10)
b7.new_ab()
b7.hit(1)
b7.advance(2, "2 BB")
b7.advance(3, "6 FC1-2")

# 4. BAL #2  Danny Valencia (X - 10 - 13)
b7.new_ab()
b7.pitch_list("c t d b b f b")
b7.reach("BB")
b7.advance(2, "6 FC1-2")

# 5. BAL #16 Trey Mancini (10 - 13 - 2)
b7.new_ab()
b7.pitch_list("s t b f s")
b7.out("K")

# Pitching change (BOS): #56 Joe Kelly replaces #76 Hector Velázquez
b7.pitching_substitution(56)

# 6. BAL #6  Jonathan Schoop (10 - 13 - 2)
b7.new_ab()
b7.pitch_list("f s b")
b7.reach("FC1-2")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #57 Donnie Hart
t8 = game.new_inning()

# Pitching change (BAL): #57 Donnie Hart replaces #53 Zack Britton
t8.pitching_substitution(57)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.out("G5-3")

# 1. BOS #36 Eduardo Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("c s b f b b b")
t8.reach("BB")
t8.advance(2, "28 1B")
t8.thrown_out(4, "18 9-2", 3, 57)
t8.advance(3, "18 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 36)
t8.new_ab()
t8.pitch_list("b c f c")
t8.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - 36)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.advance(2, "18 9-2")

# 4. BOS #18 Mitch Moreland (X - 36 - 28)
t8.new_ab()
t8.pitch_list("b b c c f")
t8.hit(1)


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
b8.pitching_substitution(32)

# 7. BAL #45 Mark Trumbo (X - X - X)
b8.new_ab()
b8.pitch_list("b b b c s b")
b8.reach("BB")
b8.advance(2, "14 E5")

# 8. BAL #14 Craig Gentry (X - X - 45)
b8.new_ab()
b8.pitch_list("b c b")
b8.error(5)
b8.reach("E5")

# Offensive change (BAL): Pinch-hitter #15 Chance Sisco replaces #61 Austin Wynns, batting 9th
b8.offensive_substitution(9, 15, "PH")

# 9. BAL #15 Chance Sisco (X - 45 - 14)
b8.new_ab()
b8.pitch_list("c c b b b f f s")
b8.out("K")

# 1. BAL #23 Joey Rickard (X - 45 - 14)
b8.new_ab()
b8.pitch_list("d")
b8.out("L9")

# 2. BAL #10 Adam Jones (X - 45 - 14)
b8.new_ab()
b8.pitch_list("b c b c")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #56 Darren O'Day
t9 = game.new_inning()

# Pitching change (BAL): #56 Darren O'Day replaces #57 Donnie Hart
t9.pitching_substitution(56)

# Defensive switch (BAL): #15 Chance Sisco moves to C
t9.defensive_switch(15, "2")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t9.new_ab()
t9.pitch_list("c f b f")
t9.out("F8")

# 6. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("f b b f c")
t9.out("!K")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c b b c t")
t9.out("KT")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b9.pitching_substitution(46)

# 3. BAL #13 Manny Machado (X - X - X)
b9.new_ab()
b9.pitch_list("b b f b f f f")
b9.out("L8")

# 4. BAL #2  Danny Valencia (X - X - X)
b9.new_ab()
b9.pitch_list("b b b b")
b9.reach("BB")
b9.advance(2, "6 BB")
b9.advance(4, "45 2B")

# 5. BAL #16 Trey Mancini (X - X - 2)
b9.new_ab()
b9.pitch_list("b f b f f")
b9.out("(F)P3")

# 6. BAL #6  Jonathan Schoop (X - X - 2)
b9.new_ab()
b9.pitch_list("b f s b b f b")
b9.reach("BB")
b9.advance(4, "45 2B")

# 7. BAL #45 Mark Trumbo (X - 2 - 6)
b9.new_ab()
b9.pitch_list("s s d")
b9.hit(2, rbis=2)

# Offensive change (BAL): Pinch-hitter #24 Pedro Alvarez replaces #14 Craig Gentry, batting 8th
b9.offensive_substitution(8, 24, "PH")

# 8. BAL #24 Pedro Alvarez (X - 45 - X)
b9.new_ab()
b9.pitch_list("c s b s")
b9.out("K2-3")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57, is_away_team=True)

# Loser team: BAL
# LP: BAL #41 David Hess
game.losing_pitcher(41)

# print(game)
game.generate_scorecard()
