import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-06-11
# https://www.baseball-reference.com/boxes/BAL/BAL201806110.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/06/11/530388/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-06-11 19:06-22:51",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "15,934",
        "temp": "66F, Partly Cloudy",
        "wind": "2mph, In From RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 35,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                35: "Steven Wright",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
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
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 44, 22, 41, 61, 37, 24, 46, 76, 65, 56, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 37,
            "roster": {
                # Lineup
                23: "Joey Rickard",
                10: "Adam Jones",
                6: "Jonathan Schoop",
                2: "Danny Valencia",
                45: "Mark Trumbo",
                16: "Trey Mancini",
                19: "Chris Davis",
                15: "Chance Sisco",
                29: "Jace Peterson",
                # Starting pitcher
                37: "Dylan Bundy",
                # Bench
                13: "Manny Machado",
                24: "Pedro Alvarez",
                61: "Austin Wynns",
                14: "Craig Gentry",
                # Bullpen
                17: "Alex Cobb",
                48: "Richard Bleier",
                60: "Mychal Givens",
                41: "David Hess",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                34: "Kevin Gausman",
                56: "Darren O'Day",
                35: "Brad Brach",
                53: "Zack Britton",
            },
            "lefties": [48, 53],
            "lineup": [
                [23, "9"],
                [10, "8"],
                [6, "4"],
                [2, "5"],
                [45, "0"],
                [16, "7"],
                [19, "3"],
                [15, "2"],
                [29, "6"],
            ],
            "bench": [
                [13, "3B"],
                [24, "3B"],
                [61, "C"],
                [14, "CF"],
            ],
            "bullpen": [17, 48, 60, 41, 43, 50, 34, 56, 35, 53],
        },
        "umpires": {
            "HP": "Nic Lentz",
            "1B": "Mark Carlson",
            "2B": "Brian Knight",
            "3B": "Pat Hoberg",
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
# Pitching: BAL #37 Dylan Bundy
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.hit(1)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab()
t1.pitch_list("f 1 b c s")
t1.out("K")

# 4. BOS #18 Mitch Moreland (X - X - 16)
t1.new_ab()
t1.pitch_list("b b f f f 1 d f f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #35 Steven Wright
b1 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b1.new_ab()
b1.pitch_list("c b s b b")
b1.out("(F)P2")

# 2. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("f")
b1.hit(1)
b1.thrown_out(2, "6 FC4-6", 2, 35)

# 3. BAL #6  Jonathan Schoop (X - X - 10)
b1.new_ab()
b1.reach("FC4-6")

# 4. BAL #2  Danny Valencia (X - X - 6)
b1.new_ab()
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #37 Dylan Bundy
t2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.out("(F)P5")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b b c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #35 Steven Wright
b2 = game.new_inning()

# 5. BAL #45 Mark Trumbo (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G4-3")

# 6. BAL #16 Trey Mancini (X - X - X)
b2.new_ab()
b2.pitch_list("b f b b b")
b2.reach("BB")
b2.advance(2, "15 1B")

# 7. BAL #19 Chris Davis (X - X - 16)
b2.new_ab()
b2.pitch_list("s f s")
b2.out("K")

# 8. BAL #15 Chance Sisco (X - X - 16)
b2.new_ab()
b2.pitch_list("c b b b")
b2.hit(1)

# 9. BAL #29 Jace Peterson (X - 16 - 15)
b2.new_ab()
b2.pitch_list("b")
b2.out("F7")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #37 Dylan Bundy
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("L9")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("t c")
t3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c s b c")
t3.out("!K")


# Bot 3rd
# Pitching: BOS #35 Steven Wright
b3 = game.new_inning()

# 1. BAL #23 Joey Rickard (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.out("G5-3")

# 2. BAL #10 Adam Jones (X - X - X)
b3.new_ab()
b3.hit(1)
b3.advance(2, "6 PB")
b3.advance(3, "6 F9")

# 3. BAL #6  Jonathan Schoop (X - X - 10)
b3.new_ab()
b3.pitch_list("b b")
b3.pb()
b3.out("F9")

# 4. BAL #2  Danny Valencia (10 - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #37 Dylan Bundy
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.hit(1)
t4.thrown_out(2, "18 DP4-6-3", 2, 37)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t4.new_ab()
t4.pitch_list("f")
t4.out("P4")

# 4. BOS #18 Mitch Moreland (X - X - 16)
t4.new_ab()
t4.pitch_list("c")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: BOS #35 Steven Wright
b4 = game.new_inning()

# 5. BAL #45 Mark Trumbo (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")

# 6. BAL #16 Trey Mancini (X - X - X)
b4.new_ab()
b4.pitch_list("f b b")
b4.out("G5-3")

# 7. BAL #19 Chris Davis (X - X - X)
b4.new_ab()
b4.pitch_list("c c b b t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #37 Dylan Bundy
t5 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c b")
t5.reach("BB")
t5.advance(2, "36 G4-3")

# 6. BOS #11 Rafael Devers (X - X - 2)
t5.new_ab()
t5.pitch_list("f s")
t5.out("F9")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t5.new_ab()
t5.pitch_list("1 c")
t5.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - 2 - X)
t5.new_ab()
t5.pitch_list("s c f f c")
t5.out("!K")


# Bot 5th
# Pitching: BOS #35 Steven Wright
b5 = game.new_inning()

# 8. BAL #15 Chance Sisco (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G3")

# 9. BAL #29 Jace Peterson (X - X - X)
b5.new_ab()
b5.pitch_list("c b c s")
b5.out("K")

# 1. BAL #23 Joey Rickard (X - X - X)
b5.new_ab()
b5.pitch_list("s b c b f f f")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #37 Dylan Bundy
t6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("b t b b f")
t6.out("L8")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c b f f b b")
t6.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "28 SB")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t6.new_ab()
t6.pitch_list("b b f b 1 s t")
t6.out("KT")


# Bot 6th
# Pitching: BOS #35 Steven Wright
b6 = game.new_inning()

# 2. BAL #10 Adam Jones (X - X - X)
b6.new_ab()
b6.pitch_list("b b c f f b b")
b6.reach("BB")
b6.thrown_out(2, "45 FC6-4", 3, 35)

# 3. BAL #6  Jonathan Schoop (X - X - 10)
b6.new_ab()
b6.pitch_list("b b f")
b6.out("L8")

# 4. BAL #2  Danny Valencia (X - X - 10)
b6.new_ab()
b6.pitch_list("b f f")
b6.out("P6")

# 5. BAL #45 Mark Trumbo (X - X - 10)
b6.new_ab()
b6.pitch_list("b")
b6.reach("FC6-4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #37 Dylan Bundy
t7 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.out("F8")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("b s c b b")
t7.hit(1)

# 6. BOS #11 Rafael Devers (X - X - 2)
t7.new_ab()
t7.pitch_list("1 f f b f 1 s")
t7.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
t7.new_ab()
t7.pitch_list("b")
t7.out("G3")


# Bot 7th
# Pitching: BOS #35 Steven Wright
b7 = game.new_inning()

# 6. BAL #16 Trey Mancini (X - X - X)
b7.new_ab()
b7.pitch_list("c s b s")
b7.out("K")

# 7. BAL #19 Chris Davis (X - X - X)
b7.new_ab()
b7.out("G4-3")

# 8. BAL #15 Chance Sisco (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.reach("HBP")
b7.advance(2, "29 1B")
b7.advance(3, "23 BB")

# 9. BAL #29 Jace Peterson (X - X - 15)
b7.new_ab()
b7.hit(1)
b7.advance(2, "23 BB")

# 1. BAL #23 Joey Rickard (X - 15 - 29)
b7.new_ab()
b7.pitch_list("b f b b b")
b7.reach("BB")

# Pitching change (BOS): #56 Joe Kelly replaces #35 Steven Wright
b7.pitching_substitution(56)

# 2. BAL #10 Adam Jones (15 - 29 - 23)
b7.new_ab()
b7.pitch_list("b s s f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #37 Dylan Bundy
t8 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t8.new_ab()
t8.pitch_list("b b s f f s")
t8.out("K")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("F7")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# 3. BAL #6  Jonathan Schoop (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G1-3")

# 4. BAL #2  Danny Valencia (X - X - X)
b8.new_ab()
b8.pitch_list("b b c f b f f b")
b8.reach("BB")

# 5. BAL #45 Mark Trumbo (X - X - 2)
b8.new_ab()
b8.pitch_list("c f")
b8.out("(F)P2")

# 6. BAL #16 Trey Mancini (X - X - 2)
b8.new_ab()
b8.pitch_list("f 1")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #48 Richard Bleier
t9 = game.new_inning()

# Pitching change (BAL): #48 Richard Bleier replaces #37 Dylan Bundy
t9.pitching_substitution(48)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.out("L6")

# 3. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("s b c c")
t9.out("!K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t9.new_ab()
t9.pitch_list("c s c")
t9.out("!K")


# Bot 9th
# Pitching: BOS #61 Brian Johnson
b9 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #56 Joe Kelly
b9.pitching_substitution(61)

# 7. BAL #19 Chris Davis (X - X - X)
b9.new_ab()
b9.pitch_list("s b s b")
b9.out("P5")

# 8. BAL #15 Chance Sisco (X - X - X)
b9.new_ab()
b9.pitch_list("f b f f b f f b")
b9.out("G4-3")

# 9. BAL #29 Jace Peterson (X - X - X)
b9.new_ab()
b9.pitch_list("c b f f b b f b")
b9.reach("BB")
b9.advance(2, "24 SB")

# Pitching change (BOS): #44 Brandon Workman replaces #61 Brian Johnson
b9.pitching_substitution(44)

# Offensive change (BAL): Pinch-hitter #24 Pedro Alvarez replaces #23 Joey Rickard, batting 1st
b9.offensive_substitution(1, 24, "PH")

# 1. BAL #24 Pedro Alvarez (X - X - 29)
b9.new_ab()
b9.pitch_list("c s b t")
b9.out("KT")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BAL #35 Brad Brach
t10 = game.new_inning()

# Pitching change (BAL): #35 Brad Brach replaces #48 Richard Bleier
t10.pitching_substitution(35)

# Defensive change (BAL): #14 Craig Gentry replaces #24 Pedro Alvarez (PH), playing RF, batting 1st
t10.defensive_substitution(1, 14, "9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t10.new_ab()
t10.pitch_list("b s f")
t10.out("F9")

# 6. BOS #11 Rafael Devers (X - X - X)
t10.new_ab()
t10.pitch_list("t f")
t10.out("G4-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t10.new_ab()
t10.pitch_list("b f f s")
t10.out("K")


# Bot 10th
# Pitching: BOS #44 Brandon Workman
b10 = game.new_inning()

# 2. BAL #10 Adam Jones (X - X - X)
b10.new_ab()
b10.pitch_list("s b b")
b10.out("G5-3")

# 3. BAL #6  Jonathan Schoop (X - X - X)
b10.new_ab()
b10.pitch_list("b b")
b10.out("F8")

# 4. BAL #2  Danny Valencia (X - X - X)
b10.new_ab()
b10.pitch_list("b")
b10.hit(2)

# 5. BAL #45 Mark Trumbo (X - 2 - X)
b10.new_ab()
b10.pitch_list("b b f b b")
b10.reach("BB")

# 6. BAL #16 Trey Mancini (X - 2 - 45)
b10.new_ab()
b10.pitch_list("b f b c s")
b10.out("K")


##########################################################
# 11th Inning
##########################################################
# Top 11th
# Pitching: BAL #35 Brad Brach
t11 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #7 Christian Vázquez, batting 8th
t11.offensive_substitution(8, 12, "PH")

# 8. BOS #12 Brock Holt (X - X - X)
t11.new_ab()
t11.pitch_list("c b")
t11.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
t11.new_ab()
t11.pitch_list("c s f b b f s")
t11.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t11.new_ab()
t11.pitch_list("b c b b")
t11.hit(1)
t11.advance(2, "16 WP")
t11.advance(3, "28 BB")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t11.new_ab()
t11.pitch_list("1 1 b b b d")
t11.wp()
t11.reach("BB")
t11.advance(2, "28 BB")

# Pitching change (BAL): #60 Mychal Givens replaces #35 Brad Brach
t11.pitching_substitution(60)

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
t11.new_ab()
t11.pitch_list("b c c b b f b")
t11.reach("BB")

# 4. BOS #18 Mitch Moreland (50 - 16 - 28)
t11.new_ab()
t11.pitch_list("b b b c c s")
t11.out("K")


# Bot 11th
# Pitching: BOS #37 Heath Hembree
b11 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #44 Brandon Workman
b11.pitching_substitution(37)

# Defensive change (BOS): #3 Sandy León replaces #50 Mookie Betts (RF), playing C, batting 1st
b11.defensive_substitution(1, 3, "2")

# Defensive switch (BOS): #12 Brock Holt moves to RF
b11.defensive_switch(12, "9")

# 7. BAL #19 Chris Davis (X - X - X)
b11.new_ab()
b11.pitch_list("b f s f b s")
b11.out("K")

# 8. BAL #15 Chance Sisco (X - X - X)
b11.new_ab()
b11.pitch_list("c c f s")
b11.out("K")

# 9. BAL #29 Jace Peterson (X - X - X)
b11.new_ab()
b11.pitch_list("b c b c s")
b11.out("K")


##########################################################
# 12th Inning
##########################################################
# Top 12th
# Pitching: BAL #60 Mychal Givens
t12 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t12.new_ab()
t12.pitch_list("b c")
t12.hit(1)
t12.advance(3, "11 2B")
t12.advance(4, "12 SF8")

# 6. BOS #11 Rafael Devers (X - X - 2)
t12.new_ab()
t12.pitch_list("1 b")
t12.hit(2)
t12.advance(3, "12 SF8")
t12.advance(4, "19 SF7")

# 7. BOS #36 Eduardo Núñez (2 - 11 - X)
t12.new_ab()
t12.reach("HBP")
t12.advance(2, "12 SF8")

# 8. BOS #12 Brock Holt (2 - 11 - 36)
t12.new_ab()
t12.pitch_list("c f b")
t12.out("SF8", rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (11 - 36 - X)
t12.new_ab()
t12.pitch_list("b")
t12.out("SF7", rbis=1)

# 1. BOS #3  Sandy León (X - 36 - X)
t12.new_ab()
t12.pitch_list("b f")
t12.out("G6-3")


# Bot 12th
# Pitching: BOS #46 Craig Kimbrel
b12 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #37 Heath Hembree
b12.pitching_substitution(46)

# 1. BAL #14 Craig Gentry (X - X - X)
b12.new_ab()
b12.pitch_list("b b c f f b f b")
b12.reach("BB")
b12.advance(2, "6 SB")

# 2. BAL #10 Adam Jones (X - X - 14)
b12.new_ab()
b12.pitch_list("s s b b s")
b12.out("K")

# 3. BAL #6  Jonathan Schoop (X - X - 14)
b12.new_ab()
b12.pitch_list("s s b b s")
b12.out("K")

# 4. BAL #2  Danny Valencia (X - 14 - X)
b12.new_ab()
b12.pitch_list("c b s d s")
b12.out("K")

# Winning team: BOS
# WP: BOS #37 Heath Hembree
game.winning_pitcher(37, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: BAL
# LP: BAL #60 Mychal Givens
game.losing_pitcher(60)

# print(game)
game.generate_scorecard()
