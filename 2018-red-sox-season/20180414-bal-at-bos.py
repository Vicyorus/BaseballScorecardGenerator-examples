import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-04-14
# https://www.baseball-reference.com/boxes/BOS/BOS201804140.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/04/14/529614/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-14 13:05-16:10",
        "at": "Fenway Park, Boston, MA",
        "att": "33,584",
        "temp": "48F, Cloudy",
        "wind": "15mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 17,
            "roster": {
                # Lineup
                16: "Trey Mancini",
                24: "Pedro Alvarez",
                13: "Manny Machado",
                10: "Adam Jones",
                19: "Chris Davis",
                1: "Tim Beckham",
                15: "Chance Sisco",
                2: "Danny Valencia",
                25: "Anthony Santander",
                # Starting pitcher
                17: "Alex Cobb",
                # Bench
                12: "Engelb Vielma",
                14: "Craig Gentry",
                36: "Caleb Joseph",
                # Bullpen
                48: "Richard Bleier",
                30: "Chris Tillman",
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
                [24, "0"],
                [13, "6"],
                [10, "8"],
                [19, "3"],
                [1, "4"],
                [15, "2"],
                [2, "5"],
                [25, "9"],
            ],
            "bench": [
                [12, "SS"],
                [14, "CF"],
                [36, "C"],
            ],
            "bullpen": [48, 30, 34, 56, 54, 60, 37, 42, 43, 38, 50, 35],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                11: "Rafael Devers",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                12: "Brock Holt",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                64: "Marcus Walden",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [11, "5"],
                [19, "8"],
                [3, "2"],
                [12, "4"],
                [5, "6"],
            ],
            "bench": [
                [36, "SS"],
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 22, 41, 61, 37, 24, 46, 64, 56, 32],
        },
        "umpires": {
            "HP": "Stu Scheurwater",
            "1B": "Gary Cederstrom",
            "2B": "Eric Cooper",
            "3B": "Cory Blaser",
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
# Pitching: BOS #76 Hector Velázquez
t1 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.hit(1)

# 2. BAL #24 Pedro Alvarez (X - X - 16)
t1.new_ab()
t1.pitch_list("c f b")
t1.out("L8")

# 3. BAL #13 Manny Machado (X - X - 16)
t1.new_ab()
t1.pitch_list("c b s b c")
t1.out("!K")

# 4. BAL #10 Adam Jones (X - X - 16)
t1.new_ab()
t1.pitch_list("f f d")
t1.out("F8")


# Bot 1st
# Pitching: BAL #17 Alex Cobb
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b f b f b b")
b1.reach("BB")
b1.advance(4, "16 E6")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b b 1 t 1")
b1.hit(2, rbis=1)
b1.error(6)
b1.advance(3, "E6")
b1.advance(4, "13 HR")

# 3. BOS #13 Hanley Ramirez (16 - X - X)
b1.new_ab()
b1.pitch_list("d b c f f")
b1.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("b b c")
b1.hit(1)
b1.thrown_out(2, "11 DP4-3", 1, 17)

# 5. BOS #11 Rafael Devers (X - X - 28)
b1.new_ab()
b1.pitch_list("c b")
b1.out("DP4-3")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.hit(1)

# 7. BOS #3  Sandy León (X - X - 19)
b1.new_ab()
b1.out("F8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #76 Hector Velázquez
t2 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f s")
t2.out("K")

# 6. BAL #1  Tim Beckham (X - X - X)
t2.new_ab()
t2.pitch_list("c b b s s")
t2.out("K")

# 7. BAL #15 Chance Sisco (X - X - X)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")


# Bot 2nd
# Pitching: BAL #17 Alex Cobb
b2 = game.new_inning()

# 8. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c f")
b2.out("G4-3")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f b")
b2.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 5)
b2.new_ab()
b2.pitch_list("b c b")
b2.out("(F)P3")

# 2. BOS #16 Andrew Benintendi (X - X - 5)
b2.new_ab()
b2.pitch_list("1 c b f 1")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #76 Hector Velázquez
t3 = game.new_inning()

# 8. BAL #2  Danny Valencia (X - X - X)
t3.new_ab()
t3.pitch_list("b b b c f f f")
t3.out("G5-3")

# 9. BAL #25 Anthony Santander (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("(F)P5")

# 1. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("b b c c")
t3.hit(2)

# 2. BAL #24 Pedro Alvarez (X - 16 - X)
t3.new_ab()
t3.pitch_list("s d d b b")
t3.reach("BB")

# 3. BAL #13 Manny Machado (X - 16 - 24)
t3.new_ab()
t3.pitch_list("b f")
t3.out("L8")


# Bot 3rd
# Pitching: BAL #17 Alex Cobb
b3 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b3.new_ab()
b3.pitch_list("b c b")
b3.out("F8")

# 4. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.hit(4, rbis=1)

# 5. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.out("F7")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b b c")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #76 Hector Velázquez
t4 = game.new_inning()

# Defensive change (BOS): #23 Blake Swihart replaces #50 Mookie Betts (RF), playing LF, batting 1st
t4.defensive_substitution(1, 23, "7")

# Defensive switch (BOS): #16 Andrew Benintendi moves to CF
t4.defensive_switch(16, "8")

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to RF
t4.defensive_switch(19, "9")

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("b c")
t4.hit(1)
t4.advance(2, "19 1B")
t4.advance(3, "1 DP6-4-3")

# 5. BAL #19 Chris Davis (X - X - 10)
t4.new_ab()
t4.pitch_list("b f")
t4.hit(1)
t4.thrown_out(2, "1 DP6-4-3", 1, 76)

# 6. BAL #1  Tim Beckham (X - 10 - 19)
t4.new_ab()
t4.pitch_list("f")
t4.out("DP6-4-3")

# 7. BAL #15 Chance Sisco (10 - X - X)
t4.new_ab()
t4.pitch_list("s d f b s")
t4.out("K")


# Bot 4th
# Pitching: BAL #17 Alex Cobb
b4 = game.new_inning()

# 7. BOS #3  Sandy León (X - X - X)
b4.new_ab()
b4.pitch_list("f b")
b4.hit(1)
b4.advance(2, "5 1B")
b4.advance(3, "23 G3")
b4.advance(4, "16 1B")

# 8. BOS #12 Brock Holt (X - X - 3)
b4.new_ab()
b4.pitch_list("b c f")
b4.out("L5")

# 9. BOS #5  Tzu-Wei Lin (X - X - 3)
b4.new_ab()
b4.pitch_list("b s 1 f")
b4.hit(1)
b4.advance(2, "23 G3")
b4.advance(4, "16 1B")

# 1. BOS #23 Blake Swihart (X - 3 - 5)
b4.new_ab()
b4.pitch_list("f f b")
b4.out("G3")

# 2. BOS #16 Andrew Benintendi (3 - 5 - X)
b4.new_ab()
b4.hit(1, rbis=2)
b4.advance(2, "T")
b4.advance(4, "13 2B")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
b4.new_ab()
b4.pitch_list("b s b")
b4.hit(2, rbis=1)
b4.advance("U", "28 E6")

# Pitching change (BAL): #50 Miguel Castro replaces #17 Alex Cobb
b4.pitching_substitution(50)

# 4. BOS #28 J.D. Martinez (X - 13 - X)
b4.new_ab()
b4.pitch_list("s c f b f b")
b4.error(6)
b4.reach("E6", 2)

# 5. BOS #11 Rafael Devers (X - 28 - X)
b4.new_ab()
b4.pitch_list("b b")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #76 Hector Velázquez
t5 = game.new_inning()

# 8. BAL #2  Danny Valencia (X - X - X)
t5.new_ab()
t5.out("F9")

# 9. BAL #25 Anthony Santander (X - X - X)
t5.new_ab()
t5.pitch_list("c b l b f f f")
t5.hit(2)
t5.advance(4, "24 HR")

# 1. BAL #16 Trey Mancini (X - 25 - X)
t5.new_ab()
t5.pitch_list("s")
t5.out("L7")

# 2. BAL #24 Pedro Alvarez (X - 25 - X)
t5.new_ab()
t5.pitch_list("d b")
t5.hit(4, rbis=2)

# 3. BAL #13 Manny Machado (X - X - X)
t5.new_ab()
t5.pitch_list("s f f f b")
t5.out("P6")


# Bot 5th
# Pitching: BAL #50 Miguel Castro
b5 = game.new_inning()

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f f b b")
b5.reach("BB")
b5.advance(3, "12 2B")
b5.thrown_out(4, "5 DP6-5", 3, 50)

# 7. BOS #3  Sandy León (X - X - 19)
b5.new_ab()
b5.pitch_list("b c b f")
b5.out("L7")

# 8. BOS #12 Brock Holt (X - X - 19)
b5.new_ab()
b5.pitch_list("f")
b5.hit(2)

# 9. BOS #5  Tzu-Wei Lin (19 - 12 - X)
b5.new_ab()
b5.pitch_list("c f b d f")
b5.out("DP6-5")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #56 Joe Kelly
t6 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #76 Hector Velázquez
t6.pitching_substitution(56)

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("b s")
t6.out("L9")

# 5. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c")
t6.out("F7")

# 6. BAL #1  Tim Beckham (X - X - X)
t6.new_ab()
t6.pitch_list("b c f s")
t6.out("K")


# Bot 6th
# Pitching: BAL #50 Miguel Castro
b6 = game.new_inning()

# 1. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.hit(2)
b6.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - 23 - X)
b6.new_ab()
b6.pitch_list("b b b f s f c")
b6.out("!K")

# 3. BOS #13 Hanley Ramirez (X - 23 - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - 23 - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1, rbis=1)

# Pitching change (BAL): #42 Donnie Hart replaces #50 Miguel Castro
b6.pitching_substitution(42)

# 5. BOS #11 Rafael Devers (X - X - 28)
b6.new_ab()
b6.pitch_list("f b b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #64 Marcus Walden
t7 = game.new_inning()

# Pitching change (BOS): #64 Marcus Walden replaces #56 Joe Kelly
t7.pitching_substitution(64)

# 7. BAL #15 Chance Sisco (X - X - X)
t7.new_ab()
t7.pitch_list("c f")
t7.out("G6-3")

# 8. BAL #2  Danny Valencia (X - X - X)
t7.new_ab()
t7.pitch_list("c b c s")
t7.out("K")

# 9. BAL #25 Anthony Santander (X - X - X)
t7.new_ab()
t7.pitch_list("c b f f b b f f c")
t7.out("!K")


# Bot 7th
# Pitching: BAL #42 Donnie Hart
b7 = game.new_inning()

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.out("F8")

# 7. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c")
b7.out("F8")

# 8. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(1)
b7.error(5)
b7.advance(2, "5 E5")
b7.advance(3, "23 1B")
b7.advance("U", "23 1B")

# 9. BOS #5  Tzu-Wei Lin (X - X - 12)
b7.new_ab()
b7.pitch_list("c f b")
b7.reach("FC5")
b7.advance(3, "23 1B")

# 1. BOS #23 Blake Swihart (X - 12 - 5)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1, rbis=1)

# 2. BOS #16 Andrew Benintendi (5 - X - 23)
b7.new_ab()
b7.pitch_list("s c s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #64 Marcus Walden
t8 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t8.new_ab()
t8.pitch_list("b b s f")
t8.out("G4-3")

# 2. BAL #24 Pedro Alvarez (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(2, "13 1B")

# 3. BAL #13 Manny Machado (X - X - 24)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(1)
t8.thrown_out(2, "10 DP6-4-3", 2, 64)

# 4. BAL #10 Adam Jones (X - 24 - 13)
t8.new_ab()
t8.pitch_list("b b b c c f")
t8.out("DP6-4-3")


# Bot 8th
# Pitching: BAL #60 Mychal Givens
b8 = game.new_inning()

# Pitching change (BAL): #60 Mychal Givens replaces #42 Donnie Hart
b8.pitching_substitution(60)

# Defensive change (BAL): #12 Engelb Vielma replaces #13 Manny Machado (SS), playing SS, batting 3rd
b8.defensive_substitution(3, 12, "6")

# Defensive change (BAL): #14 Craig Gentry replaces #10 Adam Jones (CF), playing CF, batting 4th
b8.defensive_substitution(4, 14, "8")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("F8")

# 5. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #64 Marcus Walden
t9 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
t9.new_ab()
t9.pitch_list("c b t b b")
t9.hit(2)
t9.advance(3, "1 G6-3")
t9.advance(4, "15 G6-3")

# 6. BAL #1  Tim Beckham (X - 19 - X)
t9.new_ab()
t9.out("G6-3")

# 7. BAL #15 Chance Sisco (19 - X - X)
t9.new_ab()
t9.out("G6-3", rbis=1)

# 8. BAL #2  Danny Valencia (X - X - X)
t9.new_ab()
t9.pitch_list("b b s b f f f s")
t9.out("K")

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76)
# SV: BOS #64 Marcus Walden
game.save_pitcher(64)

# Loser team: BAL
# LP: BAL #17 Alex Cobb
game.losing_pitcher(17, is_away_team=True)

# print(game)
game.generate_scorecard()
