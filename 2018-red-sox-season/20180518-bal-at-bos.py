import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-05-18
# https://www.baseball-reference.com/boxes/BOS/BOS201805180.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/05/18/530063/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-18 19:11-22:29",
        "at": "Fenway Park, Boston, MA",
        "att": "34,935",
        "temp": "52F, Partly Cloudy",
        "wind": "10mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 17,
            "roster": {
                # Lineup
                16: "Trey Mancini",
                10: "Adam Jones",
                13: "Manny Machado",
                6: "Jonathan Schoop",
                45: "Mark Trumbo",
                19: "Chris Davis",
                2: "Danny Valencia",
                23: "Joey Rickard",
                27: "Andrew Susac",
                # Starting pitcher
                17: "Alex Cobb",
                # Bench
                29: "Jace Peterson",
                24: "Pedro Alvarez",
                15: "Chance Sisco",
                14: "Craig Gentry",
                # Bullpen
                48: "Richard Bleier",
                34: "Kevin Gausman",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                57: "Donnie Hart",
                43: "Mike Wright Jr.",
                38: "Pedro Araújo",
                50: "Miguel Castro",
                35: "Brad Brach",
            },
            "lefties": [48, 66, 57],
            "lineup": [
                [16, "7"],
                [10, "8"],
                [13, "6"],
                [6, "4"],
                [45, "0"],
                [19, "3"],
                [2, "5"],
                [23, "9"],
                [27, "2"],
            ],
            "bench": [
                [29, "SS"],
                [24, "3B"],
                [15, "C"],
                [14, "CF"],
            ],
            "bullpen": [48, 34, 66, 54, 60, 37, 57, 43, 38, 50, 35],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 57, 41, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 22, 41, 61, 66, 37, 24, 46, 56, 32],
        },
        "umpires": {
            "HP": "Lance Barrett",
            "1B": "Bill Welke",
            "2B": "Nic Lentz",
            "3B": "Alfonso Márquez",
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
# Pitching: BOS #31 Drew Pomeranz
t1 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.thrown_out(2, "10 FC5-4", 1, 31)

# 2. BAL #10 Adam Jones (X - X - 16)
t1.new_ab()
t1.pitch_list("c s b")
t1.reach("FC5-4")
t1.advance(3, "13 2B")
t1.advance(4, "45 G5-3")

# 3. BAL #13 Manny Machado (X - X - 10)
t1.new_ab()
t1.pitch_list("s f b")
t1.hit(2)
t1.advance(3, "45 G5-3")

# 4. BAL #6  Jonathan Schoop (10 - 13 - X)
t1.new_ab()
t1.pitch_list("b b f b s b")
t1.reach("BB")
t1.advance(2, "45 G5-3")

# 5. BAL #45 Mark Trumbo (10 - 13 - 6)
t1.new_ab()
t1.pitch_list("c f")
t1.out("G5-3", rbis=1)

# 6. BAL #19 Chris Davis (13 - 6 - X)
t1.new_ab()
t1.pitch_list("b c 3")
t1.out("F7")


# Bot 1st
# Pitching: BAL #17 Alex Cobb
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("f c")
b1.hit(2)
b1.thrown_out(3, "16 DP4-6", 2, 17)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b1.new_ab()
b1.pitch_list("c f")
b1.out("DP4-6")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Drew Pomeranz
t2 = game.new_inning()

# 7. BAL #2  Danny Valencia (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G5-3")

# 8. BAL #23 Joey Rickard (X - X - X)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")

# 9. BAL #27 Andrew Susac (X - X - X)
t2.new_ab()
t2.pitch_list("s c b f")
t2.out("L8")


# Bot 2nd
# Pitching: BAL #17 Alex Cobb
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.pitch_list("b b c f b")
b2.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.thrown_out(2, "11 CS", 2, 17)

# 6. BOS #11 Rafael Devers (X - X - 2)
b2.new_ab()
b2.pitch_list("c 1 d b b c d")
b2.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - X - 11)
b2.new_ab()
b2.pitch_list("b b b c")
b2.out("P6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Drew Pomeranz
t3 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("c b b")
t3.out("G5-3")

# 2. BAL #10 Adam Jones (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.advance(3, "13 2B")

# 3. BAL #13 Manny Machado (X - X - 10)
t3.new_ab()
t3.hit(2)

# 4. BAL #6  Jonathan Schoop (10 - 13 - X)
t3.new_ab()
t3.pitch_list("b s s")
t3.out("(F)P5")

# 5. BAL #45 Mark Trumbo (10 - 13 - X)
t3.new_ab()
t3.pitch_list("s d b d")
t3.out("G6-3")


# Bot 3rd
# Pitching: BAL #17 Alex Cobb
b3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("s s s")
b3.out("K")

# 9. BOS #7  Christian Vázquez (X - X - X)
b3.new_ab()
b3.pitch_list("b c c")
b3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b b f")
b3.hit(4, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("G3-1")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Drew Pomeranz
t4 = game.new_inning()

# 6. BAL #19 Chris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.hit(2)
t4.advance(3, "2 1B")
t4.advance(4, "10 1B")

# 7. BAL #2  Danny Valencia (X - 19 - X)
t4.new_ab()
t4.pitch_list("c b f b")
t4.hit(1)
t4.advance(2, "T")
t4.advance(4, "10 1B")

# 8. BAL #23 Joey Rickard (19 - 2 - X)
t4.new_ab()
t4.out("F7")

# 9. BAL #27 Andrew Susac (19 - 2 - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("P3")

# 1. BAL #16 Trey Mancini (19 - 2 - X)
t4.new_ab()
t4.pitch_list("b c d c b d")
t4.reach("BB")
t4.advance(2, "10 1B")
t4.advance(3, "10 E7")
t4.advance(4, "13 1B")

# 2. BAL #10 Adam Jones (19 - 2 - 16)
t4.new_ab()
t4.pitch_list("b b c")
t4.hit(1, rbis=2)
t4.error(7)
t4.advance(2, "E7")
t4.advance("U", "13 1B")

# 3. BAL #13 Manny Machado (16 - 10 - X)
t4.new_ab()
t4.hit(1, rbis=2)

# 4. BAL #6  Jonathan Schoop (X - X - 13)
t4.new_ab()
t4.pitch_list("b s d s d c")
t4.out("!K")


# Bot 4th
# Pitching: BAL #17 Alex Cobb
b4 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("P6")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(2)
b4.advance(3, "2 F9")

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("F9")

# 6. BOS #11 Rafael Devers (28 - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #35 Steven Wright
t5 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #31 Drew Pomeranz
t5.pitching_substitution(35)

# 5. BAL #45 Mark Trumbo (X - X - X)
t5.new_ab()
t5.out("P6")

# 6. BAL #19 Chris Davis (X - X - X)
t5.new_ab()
t5.pitch_list("c b b f")
t5.out("G4-3")

# 7. BAL #2  Danny Valencia (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c s b")
t5.reach("BB")
t5.advance(2, "23 PB")

# 8. BAL #23 Joey Rickard (X - X - 2)
t5.new_ab()
t5.pitch_list("b c f")
t5.pb()
t5.out("G1-3")


# Bot 5th
# Pitching: BAL #17 Alex Cobb
b5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.hit(1)
b5.advance(3, "7 1B")
b5.advance(4, "50 2B")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 36)
b5.new_ab()
b5.pitch_list("b s t t")
b5.out("KT")

# 9. BOS #7  Christian Vázquez (X - X - 36)
b5.new_ab()
b5.pitch_list("c b 1 f")
b5.hit(1)
b5.advance(3, "50 2B")
b5.advance(4, "16 1B")

# 1. BOS #50 Mookie Betts (36 - X - 7)
b5.new_ab()
b5.pitch_list("b")
b5.hit(2, rbis=1)
b5.advance(3, "16 1B")

# 2. BOS #16 Andrew Benintendi (7 - 50 - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1, rbis=1)
b5.thrown_out(2, "13 DP4-6-3", 2, 17)

# 3. BOS #13 Hanley Ramirez (50 - X - 16)
b5.new_ab()
b5.pitch_list("f 1 b f")
b5.out("DP4-6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #35 Steven Wright
t6 = game.new_inning()

# 9. BAL #27 Andrew Susac (X - X - X)
t6.new_ab()
t6.pitch_list("c f t")
t6.out("KT")

# 1. BAL #16 Trey Mancini (X - X - X)
t6.new_ab()
t6.pitch_list("c s s")
t6.out("K")

# 2. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("c s")
t6.out("G4-3")


# Bot 6th
# Pitching: BAL #17 Alex Cobb
b6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("L9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G4-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("f b c b")
b6.hit(1)

# 7. BOS #36 Eduardo Núñez (X - X - 11)
b6.new_ab()
b6.pitch_list("b d f s f")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# 3. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.pitch_list("b f f t")
t7.out("KT")

# 4. BAL #6  Jonathan Schoop (X - X - X)
t7.new_ab()
t7.hit(4, rbis=1)

# 5. BAL #45 Mark Trumbo (X - X - X)
t7.new_ab()
t7.pitch_list("c s f f")
t7.out("G1-3")

# 6. BAL #19 Chris Davis (X - X - X)
t7.new_ab()
t7.pitch_list("b f f t")
t7.out("KT")


# Bot 7th
# Pitching: BAL #17 Alex Cobb
b7 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #19 Jackie Bradley Jr., batting 8th
b7.offensive_substitution(8, 12, "PH")

# 8. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("s s f c")
b7.out("!K")

# 9. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2)

# Pitching change (BAL): #60 Mychal Givens replaces #17 Alex Cobb
b7.pitching_substitution(60)

# 1. BOS #50 Mookie Betts (X - 7 - X)
b7.new_ab()
b7.pitch_list("c f b b f f b f")
b7.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - 7 - X)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")

# 3. BOS #13 Hanley Ramirez (X - 7 - 16)
b7.new_ab()
b7.pitch_list("s")
b7.out("L9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #35 Steven Wright
t8 = game.new_inning()

# Defensive switch (BOS): #16 Andrew Benintendi moves to CF
t8.defensive_switch(16, "8")

# Defensive switch (BOS): #12 Brock Holt moves to LF
t8.defensive_switch(12, "7")

# 7. BAL #2  Danny Valencia (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("P4")

# 8. BAL #23 Joey Rickard (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f b f")
t8.hit(2)
t8.advance(3, "27 G4-3")

# 9. BAL #27 Andrew Susac (X - 23 - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G4-3")

# 1. BAL #16 Trey Mancini (23 - X - X)
t8.new_ab()
t8.out("G4-3")


# Bot 8th
# Pitching: BAL #60 Mychal Givens
b8 = game.new_inning()

# Defensive change (BAL): #29 Jace Peterson replaces #2 Danny Valencia (3B), playing 3B, batting 7th
b8.defensive_substitution(7, 29, "5")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c c b f f f f f")
b8.error(7)
b8.reach("E7", end_base=2)
b8.advance(3, "11 G4-3")
b8.advance("U", "36 2B")

# Pitching change (BAL): #48 Richard Bleier replaces #60 Mychal Givens
b8.pitching_substitution(48)

# 6. BOS #11 Rafael Devers (X - 2 - X)
b8.new_ab()
b8.pitch_list("c b s")
b8.out("G4-3")

# 7. BOS #36 Eduardo Núñez (2 - X - X)
b8.new_ab()
b8.pitch_list("f")
b8.hit(2, rbis=1)
b8.advance(3, "12 1B")

# 8. BOS #12 Brock Holt (X - 36 - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.hit(1)
b8.advance(2, "18 BB")

# Pitching change (BAL): #35 Brad Brach replaces #48 Richard Bleier
b8.pitching_substitution(35)

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #7 Christian Vázquez, batting 9th
b8.offensive_substitution(9, 18, "PH")

# 9. BOS #18 Mitch Moreland (36 - X - 12)
b8.new_ab()
b8.pitch_list("b b f d c f f d")
b8.reach("BB")
# Offensive change (BOS): Pinch-runner #23 Blake Swihart replaces #18 Mitch Moreland
b8.offensive_substitution(9, 23, "PR")
b8.atbase("PR")

# 1. BOS #50 Mookie Betts (36 - 12 - 18)
b8.new_ab()
b8.pitch_list("c s b")
b8.out("P3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #35 Steven Wright
t9 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to C
t9.defensive_switch(23, "2")

# 2. BAL #10 Adam Jones (X - X - X)
t9.new_ab()
t9.pitch_list("b f f f b")
t9.out("F9")

# 3. BAL #13 Manny Machado (X - X - X)
t9.new_ab()
t9.pitch_list("c s s")
t9.out("K")

# 4. BAL #6  Jonathan Schoop (X - X - X)
t9.new_ab()
t9.pitch_list("b c b b f b")
t9.reach("BB")
t9.advance(4, "45 2B")

# 5. BAL #45 Mark Trumbo (X - X - 6)
t9.new_ab()
t9.pitch_list("b")
t9.hit(2, rbis=1)

# Pitching change (BOS): #37 Heath Hembree replaces #35 Steven Wright
t9.pitching_substitution(37)

# 6. BAL #19 Chris Davis (X - 45 - X)
t9.new_ab()
t9.pitch_list("c d f c")
t9.out("!K")


# Bot 9th
# Pitching: BAL #35 Brad Brach
b9 = game.new_inning()

# Defensive change (BAL): #14 Craig Gentry replaces #16 Trey Mancini (LF), playing LF, batting 1st
b9.defensive_substitution(1, 14, "7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b9.new_ab()
b9.pitch_list("b s f")
b9.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b9.new_ab()
b9.pitch_list("f f")
b9.out("F7")

# 4. BOS #28 J.D. Martinez (X - X - X)
b9.new_ab()
b9.pitch_list("b c t b b")
b9.hit(2)

# 5. BOS #2  Xander Bogaerts (X - 28 - X)
b9.new_ab()
b9.pitch_list("c s b")
b9.out("G6-3")

# Winning team: BAL
# WP: BAL #17 Alex Cobb
game.winning_pitcher(17, is_away_team=True)
# SV: BAL #35 Brad Brach
game.save_pitcher(35, is_away_team=True)

# Loser team: BOS
# LP: BOS #31 Drew Pomeranz
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
