import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-04-13
# https://www.baseball-reference.com/boxes/BOS/BOS201804130.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/04/13/529599/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-13 19:10-22:32",
        "at": "Fenway Park, Boston, MA",
        "att": "32,610",
        "temp": "53F, Partly Cloudy",
        "wind": "7mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 30,
            "roster": {
                # Lineup
                16: "Trey Mancini",
                13: "Manny Machado",
                6: "Jonathan Schoop",
                10: "Adam Jones",
                2: "Danny Valencia",
                19: "Chris Davis",
                1: "Tim Beckham",
                14: "Craig Gentry",
                36: "Caleb Joseph",
                # Starting pitcher
                30: "Chris Tillman",
                # Bench
                25: "Anthony Santander",
                24: "Pedro Alvarez",
                12: "Engelb Vielma",
                15: "Chance Sisco",
                # Bullpen
                48: "Richard Bleier",
                34: "Kevin Gausman",
                56: "Darren O'Day",
                54: "Andrew Cashner",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                42: "Donnie Hart",
                43: "Mike Wright Jr.",
                38: "Pedro Araújo",
                50: "Miguel Castro",
                35: "Brad Brach",
            },
            "lefties": [48, 42],
            "lineup": [
                [16, "7"],
                [13, "6"],
                [6, "4"],
                [10, "8"],
                [2, "0"],
                [19, "3"],
                [1, "5"],
                [14, "9"],
                [36, "2"],
            ],
            "bench": [
                [25, "RF"],
                [24, "3B"],
                [12, "SS"],
                [15, "C"],
            ],
            "bullpen": [48, 34, 56, 54, 60, 37, 42, 43, 38, 50, 35],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                3: "Sandy León",
                13: "Hanley Ramirez",
                # Bullpen
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
                [5, "6"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [3, "C"],
                [13, "SS"],
            ],
            "bullpen": [39, 22, 41, 61, 37, 24, 46, 76, 64, 56, 32],
        },
        "umpires": {
            "HP": "Cory Blaser",
            "1B": "Stu Scheurwater",
            "2B": "Gary Cederstrom",
            "3B": "Eric Cooper",
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

# 1. BAL #16 Trey Mancini (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.hit(1)
t1.advance(3, "6 1B")
t1.advance(4, "10 SF7")

# 2. BAL #13 Manny Machado (X - X - 16)
t1.new_ab()
t1.pitch_list("c b b d")
t1.out("F9")

# 3. BAL #6  Jonathan Schoop (X - X - 16)
t1.new_ab()
t1.pitch_list("b 1")
t1.hit(1)

# 4. BAL #10 Adam Jones (16 - X - 6)
t1.new_ab(is_risp=True)
t1.pitch_list("b f f f")
t1.out("SF7", rbis=1)

# 5. BAL #2  Danny Valencia (X - X - 6)
t1.new_ab()
t1.pitch_list("1 b c s")
t1.out("F9")


# Bot 1st
# Pitching: BAL #30 Chris Tillman
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c b")
b1.reach("BB")
b1.advance(2, "16 G1-3")
b1.advance(3, "18 1B")
b1.advance(4, "28 SF8")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b")
b1.out("G1-3")

# 3. BOS #18 Mitch Moreland (X - 50 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b")
b1.hit(1)
b1.advance(3, "11 2B")
b1.advance(4, "36 HR")

# 4. BOS #28 J.D. Martinez (50 - X - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("f s b f b b")
b1.out("SF8", rbis=1)

# 5. BOS #11 Rafael Devers (X - X - 18)
b1.new_ab()
b1.pitch_list("c b")
b1.hit(2)
b1.advance(4, "36 HR")

# 6. BOS #36 Eduardo Núñez (18 - 11 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b f")
b1.hit(4, rbis=3)

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b1.new_ab()
b1.pitch_list("f b f b")
b1.out("P6")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 6. BAL #19 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("b f s s")
t2.out("K")

# 7. BAL #1  Tim Beckham (X - X - X)
t2.new_ab()
t2.pitch_list("c s f b s")
t2.out("K")

# 8. BAL #14 Craig Gentry (X - X - X)
t2.new_ab()
t2.pitch_list("c c b c")
t2.out("!K")


# Bot 2nd
# Pitching: BAL #30 Chris Tillman
b2 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("c b f f")
b2.out("F8")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b2.new_ab()
b2.pitch_list("c c")
b2.hit(2)
b2.advance(4, "50 2B")

# 1. BOS #50 Mookie Betts (X - 5 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b c b")
b2.hit(2, rbis=1)
b2.advance(3, "16 G3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b2.new_ab(is_risp=True)
b2.out("G3")

# 3. BOS #18 Mitch Moreland (50 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c b b")
b2.reach("BB")

# 4. BOS #28 J.D. Martinez (50 - X - 18)
b2.new_ab(is_risp=True)
b2.pitch_list("s")
b2.out("L9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 9. BAL #36 Caleb Joseph (X - X - X)
t3.new_ab()
t3.pitch_list("b c b f")
t3.out("L9")

# 1. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c b")
t3.reach("BB")

# 2. BAL #13 Manny Machado (X - X - 16)
t3.new_ab()
t3.out("L7")

# 3. BAL #6  Jonathan Schoop (X - X - 16)
t3.new_ab()
t3.pitch_list("d b c c b")
t3.out("G6-3")


# Bot 3rd
# Pitching: BAL #30 Chris Tillman
b3 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(1)
b3.advance(2, "36 1B")
b3.advance(3, "19 HBP")
b3.advance(4, "7 PB")

# 6. BOS #36 Eduardo Núñez (X - X - 11)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(1)
b3.advance(2, "19 HBP")
b3.advance(3, "7 PB")

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
b3.new_ab(is_risp=True)
b3.pitch_list("d b c")
b3.reach("HBP")
b3.advance(2, "7 PB")

# Pitching change (BAL): #38 Pedro Araújo replaces #30 Chris Tillman
b3.pitching_substitution(38)

# 8. BOS #7  Christian Vázquez (11 - 36 - 19)
b3.new_ab(is_risp=True)
b3.pitch_list("b f t b f f f f d b")
b3.pb()
b3.reach("BB")

# 9. BOS #5  Tzu-Wei Lin (36 - 19 - 7)
b3.new_ab(is_risp=True)
b3.pitch_list("b s s s")
b3.out("K")

# 1. BOS #50 Mookie Betts (36 - 19 - 7)
b3.new_ab(is_risp=True)
b3.pitch_list("s c d")
b3.out("F8")

# 2. BOS #16 Andrew Benintendi (36 - 19 - 7)
b3.new_ab(is_risp=True)
b3.pitch_list("b c s f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("b s s f")
t4.hit(1)
t4.thrown_out(2, "9-6", 1, 57)

# 5. BAL #2  Danny Valencia (X - X - X)
t4.new_ab()
t4.hit(1)

# 6. BAL #19 Chris Davis (X - X - 2)
t4.new_ab()
t4.pitch_list("f f b s")
t4.out("K")

# 7. BAL #1  Tim Beckham (X - X - 2)
t4.new_ab()
t4.pitch_list("f c t")
t4.out("KT")


# Bot 4th
# Pitching: BAL #38 Pedro Araújo
b4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b f f s")
b4.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("F9")

# 5. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.hit(1)

# 6. BOS #36 Eduardo Núñez (X - X - 11)
b4.new_ab()
b4.out("L8")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 8. BAL #14 Craig Gentry (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K")

# 9. BAL #36 Caleb Joseph (X - X - X)
t5.new_ab()
t5.pitch_list("b s b b")
t5.out("F8")

# 1. BAL #16 Trey Mancini (X - X - X)
t5.new_ab()
t5.pitch_list("f b f b b s")
t5.out("K")


# Bot 5th
# Pitching: BAL #43 Mike Wright Jr.
b5 = game.new_inning()

# Pitching change (BAL): #43 Mike Wright Jr. replaces #38 Pedro Araújo
b5.pitching_substitution(43)

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c f f c")
b5.out("!K")

# 8. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("c b c f b b")
b5.out("P4")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b5.new_ab()
b5.pitch_list("b c b b b")
b5.reach("BB")

# 1. BOS #50 Mookie Betts (X - X - 5)
b5.new_ab()
b5.pitch_list("c b f")
b5.out("F7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 2. BAL #13 Manny Machado (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f f")
t6.out("P3")

# 3. BAL #6  Jonathan Schoop (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b f")
t6.hit(1)
t6.advance(2, "2 BB")

# 4. BAL #10 Adam Jones (X - X - 6)
t6.new_ab()
t6.pitch_list("b s b")
t6.out("L7")

# 5. BAL #2  Danny Valencia (X - X - 6)
t6.new_ab()
t6.pitch_list("b b c b f b")
t6.reach("BB")

# 6. BAL #19 Chris Davis (X - 6 - 2)
t6.new_ab(is_risp=True)
t6.pitch_list("b f b b c c")
t6.out("!K")


# Bot 6th
# Pitching: BAL #43 Mike Wright Jr.
b6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b b b")
b6.reach("BB")
b6.thrown_out(2, "18 FC4-6", 1, 43)

# 3. BOS #18 Mitch Moreland (X - X - 16)
b6.new_ab()
b6.reach("FC4-6")
b6.advance(3, "28 2B")
b6.advance(4, "36 WP")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b6.new_ab()
b6.hit(2)
b6.advance(3, "36 WP")

# 5. BOS #11 Rafael Devers (18 - 28 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b s s s")
b6.out("K")

# 6. BOS #36 Eduardo Núñez (18 - 28 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c c f d b b b")
b6.wp()
b6.reach("BB")

# 7. BOS #19 Jackie Bradley Jr. (28 - X - 36)
b6.new_ab(is_risp=True)
b6.pitch_list("b s b")
b6.out("P5")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
t7.pitching_substitution(37)

# 7. BAL #1  Tim Beckham (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G4-3")

# 8. BAL #14 Craig Gentry (X - X - X)
t7.new_ab()
t7.pitch_list("c b f f")
t7.hit(1)
t7.advance(2, "16 1B")
t7.advance(4, "13 2B")

# 9. BAL #36 Caleb Joseph (X - X - 14)
t7.new_ab()
t7.pitch_list("c f b s")
t7.out("K")

# 1. BAL #16 Trey Mancini (X - X - 14)
t7.new_ab()
t7.pitch_list("f b")
t7.hit(1)
t7.advance(4, "13 2B")

# 2. BAL #13 Manny Machado (X - 14 - 16)
t7.new_ab(is_risp=True)
t7.pitch_list("c f b d")
t7.hit(2, rbis=2)

# 3. BAL #6  Jonathan Schoop (X - 13 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("t s s")
t7.out("K")


# Bot 7th
# Pitching: BAL #43 Mike Wright Jr.
b7 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.pitch_list("f b f")
b7.out("F9")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 5)
b7.new_ab()
b7.pitch_list("b s f d s")
b7.out("K")

# Pitching change (BAL): #42 Donnie Hart replaces #43 Mike Wright Jr.
b7.pitching_substitution(42)

# 2. BOS #16 Andrew Benintendi (X - X - 5)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t8.pitching_substitution(56)

# 4. BAL #10 Adam Jones (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b b s")
t8.out("K")

# Offensive change (BAL): Pinch-hitter #24 Pedro Alvarez replaces #2 Danny Valencia, batting 5th
t8.offensive_substitution(5, 24, "PH")

# 5. BAL #24 Pedro Alvarez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G4-3")

# 6. BAL #19 Chris Davis (X - X - X)
t8.new_ab()
t8.out("G3")


# Bot 8th
# Pitching: BAL #42 Donnie Hart
b8 = game.new_inning()

# Defensive change (BAL): #12 Engelb Vielma replaces #6 Jonathan Schoop (2B), playing 2B, batting 3rd
b8.defensive_substitution(3, 12, "4")

# Defensive switch (BAL): #24 Pedro Alvarez moves to DH
b8.defensive_switch(24, "0")

# 3. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b b s")
b8.out("G1-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(1)

# 5. BOS #11 Rafael Devers (X - X - 28)
b8.new_ab()
b8.pitch_list("s s")
b8.out("F8")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
b8.new_ab()
b8.pitch_list("b b f t b")
b8.out("G1-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Matt Barnes
t9 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t9.pitching_substitution(32)

# 7. BAL #1  Tim Beckham (X - X - X)
t9.new_ab()
t9.pitch_list("c s b")
t9.out("G5-3")

# 8. BAL #14 Craig Gentry (X - X - X)
t9.new_ab()
t9.pitch_list("b b c f c")
t9.out("!K")

# Offensive change (BAL): Pinch-hitter #15 Chance Sisco replaces #36 Caleb Joseph, batting 9th
t9.offensive_substitution(9, 15, "PH")

# 9. BAL #15 Chance Sisco (X - X - X)
t9.new_ab()
t9.pitch_list("c b s b")
t9.hit(1)
t9.thrown_out(2, "16 FC6-4", 3, 32)

# 1. BAL #16 Trey Mancini (X - X - 15)
t9.new_ab()
t9.pitch_list("b")
t9.reach("FC6-4")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)

# Loser team: BAL
# LP: BAL #30 Chris Tillman
game.losing_pitcher(30, is_away_team=True)

# print(game)
game.generate_scorecard()
