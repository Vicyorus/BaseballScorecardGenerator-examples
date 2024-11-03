import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-09-26, game 1 of 2
# https://www.baseball-reference.com/boxes/BOS/BOS201809261.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/09/26/531756/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-26 13:06-16:16",
        "at": "Fenway Park, Boston, MA",
        "att": "33,577",
        "temp": "83F, Partly Cloudy",
        "wind": "20mph, Out To LF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 52,
            "roster": {
                # Lineup
                3: "Cedric Mullins",
                2: "Jonathan Villar",
                10: "Adam Jones",
                16: "Trey Mancini",
                1: "Tim Beckham",
                39: "Renato Núñez",
                23: "Joey Rickard",
                61: "Austin Wynns",
                12: "Stevie Wilkerson",
                # Starting pitcher
                52: "Ryan Meisinger",
                # Bench
                28: "Breyvic Valera",
                19: "Chris Davis",
                29: "Jace Peterson",
                34: "John Andreoli",
                62: "DJ Stewart",
                15: "Chance Sisco",
                64: "Corban Joseph",
                36: "Caleb Joseph",
                # Bullpen
                31: "Jimmy Yacabonis",
                63: "Sean Gilmartin",
                17: "Alex Cobb",
                32: "Yefry Ramírez",
                41: "David Hess",
                49: "Cody Carroll",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                51: "Paul Fry",
                65: "Josh Rogers",
                58: "Evan Phillips",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                57: "Donnie Hart",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                67: "John Means",
                59: "Luis F. Ortiz",
            },
            "lefties": [63, 66, 51, 65, 57, 67],
            "lineup": [
                [3, "8"],
                [2, "6"],
                [10, "7"],
                [16, "3"],
                [1, "0"],
                [39, "5"],
                [23, "9"],
                [61, "2"],
                [12, "4"],
            ],
            "bench": [
                [28, "LF"],
                [19, "1B"],
                [29, "SS"],
                [34, "OF"],
                [62, "RF"],
                [15, "C"],
                [64, "1B"],
                [36, "C"],
            ],
            "bullpen": [31, 63, 17, 32, 41, 49, 66, 54, 51, 65, 58, 60, 37, 57, 43, 50, 67, 59],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                11: "Rafael Devers",
                23: "Blake Swihart",
                3: "Sandy León",
                # Starting pitcher
                24: "David Price",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                59: "Sam Travis",
                19: "Jackie Bradley Jr.",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61, 66, 63],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [18, "3"],
                [5, "4"],
                [11, "5"],
                [23, "9"],
                [3, "2"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [12, "2B"],
                [59, "1B"],
                [19, "CF"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Ryan Blakney",
            "1B": "Sean Barber",
            "2B": "Mike Winters",
            "3B": "Tim Timmons",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. BAL #3  Cedric Mullins (X - X - X)
t1.new_ab()
t1.pitch_list("f b f s")
t1.out("K")

# 2. BAL #2  Jonathan Villar (X - X - X)
t1.new_ab()
t1.pitch_list("c")
t1.out("F7")

# 3. BAL #10 Adam Jones (X - X - X)
t1.new_ab()
t1.pitch_list("c s b b b")
t1.out("G6-3")


# Bot 1st
# Pitching: BAL #52 Ryan Meisinger
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(1)
b1.thrown_out(2, "16 FC1-6", 1, 52)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("f f f 1 1 b f 1")
b1.reach("FC1-6")
b1.advance(3, "28 2B")
b1.advance(4, "2 2B")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.hit(2)
b1.advance(4, "2 2B")

# 4. BOS #2  Xander Bogaerts (16 - 28 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b")
b1.hit(2, rbis=2)
b1.advance(3, "5 1B")
b1.advance(4, "11 2B")

# 5. BOS #18 Mitch Moreland (X - 2 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b b")
b1.reach("BB")
b1.advance(2, "5 1B")
b1.advance(4, "11 2B")

# 6. BOS #5  Ian Kinsler (X - 2 - 18)
b1.new_ab(is_risp=True)
b1.pitch_list("c c")
b1.hit(1)
b1.advance(4, "11 2B")

# Pitching change (BAL): #57 Donnie Hart replaces #52 Ryan Meisinger
b1.pitching_substitution(57)

# 7. BOS #11 Rafael Devers (2 - 18 - 5)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.hit(2, rbis=3)

# 8. BOS #23 Blake Swihart (X - 11 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c c")
b1.out("P4")

# 9. BOS #3  Sandy León (X - 11 - X)
b1.new_ab(is_risp=True)
b1.out("P4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 4. BAL #16 Trey Mancini (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(4)

# 5. BAL #1  Tim Beckham (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b b")
t2.reach("BB")
t2.advance(4, "39 HR")

# 6. BAL #39 Renato Núñez (X - X - 1)
t2.new_ab()
t2.pitch_list("c s f b b")
t2.hit(4, rbis=2)

# 7. BAL #23 Joey Rickard (X - X - X)
t2.new_ab()
t2.pitch_list("b s b")
t2.hit(1)
t2.advance(2, "61 BB")
t2.advance(3, "3 BB")

# 8. BAL #61 Austin Wynns (X - X - 23)
t2.new_ab()
t2.pitch_list("b t b b b")
t2.reach("BB")
t2.advance(2, "3 BB")

# 9. BAL #12 Stevie Wilkerson (X - 23 - 61)
t2.new_ab(is_risp=True)
t2.pitch_list("c c c")
t2.out("!K")

# 1. BAL #3  Cedric Mullins (X - 23 - 61)
t2.new_ab(is_risp=True)
t2.pitch_list("s c b b f f b f b")
t2.reach("BB")
t2.thrown_out(2, "10 FC5-4", 3, 24)

# 2. BAL #2  Jonathan Villar (23 - 61 - 3)
t2.new_ab(is_risp=True)
t2.pitch_list("c f c")
t2.out("!K")

# 3. BAL #10 Adam Jones (23 - 61 - 3)
t2.new_ab(is_risp=True)
t2.reach("FC5-4")


# Bot 2nd
# Pitching: BAL #57 Donnie Hart
b2 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("c b b b c b")
b2.reach("BB")
b2.advance(2, "16 SB")
b2.advance(3, "28 F9")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b2.new_ab(is_risp=True)
b2.pitch_list("1 1 c f b b f b f")
b2.out("L7")

# 3. BOS #28 J.D. Martinez (X - 50 - X)
b2.new_ab(is_risp=True)
b2.pitch_list("f b")
b2.out("F9")

# 4. BOS #2  Xander Bogaerts (50 - X - X)
b2.new_ab(is_risp=True)
b2.pitch_list("c")
b2.out("F8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 4. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("c f b f")
t3.out("G6-3")

# 5. BAL #1  Tim Beckham (X - X - X)
t3.new_ab()
t3.hit(1)
t3.advance(3, "23 2B")
t3.thrown_out(4, "23 8-6-2", 3, 24)

# 6. BAL #39 Renato Núñez (X - X - 1)
t3.new_ab()
t3.pitch_list("b s f d f c")
t3.out("!K")

# 7. BAL #23 Joey Rickard (X - X - 1)
t3.new_ab()
t3.hit(2)


# Bot 3rd
# Pitching: BAL #67 John Means
b3 = game.new_inning()

# Pitching change (BAL): #67 John Means replaces #57 Donnie Hart
b3.pitching_substitution(67)

# 5. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("b c b f f f s")
b3.out("K")

# 6. BOS #5  Ian Kinsler (X - X - X)
b3.new_ab()
b3.out("G3")

# 7. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("b f b b")
b3.out("P5")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 8. BAL #61 Austin Wynns (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("P4")

# 9. BAL #12 Stevie Wilkerson (X - X - X)
t4.new_ab()
t4.out("G3-1")

# 1. BAL #3  Cedric Mullins (X - X - X)
t4.new_ab()
t4.pitch_list("b f c b s")
t4.out("K")


# Bot 4th
# Pitching: BAL #67 John Means
b4 = game.new_inning()

# 8. BOS #23 Blake Swihart (X - X - X)
b4.new_ab()
b4.pitch_list("f")
b4.out("F9")

# 9. BOS #3  Sandy León (X - X - X)
b4.new_ab()
b4.pitch_list("b b f f c")
b4.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(2)
b4.advance(3, "16 1B")
b4.advance(4, "28 HR")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b4.new_ab(is_risp=True)
b4.pitch_list("b c b f")
b4.hit(1)
b4.advance(4, "28 HR")

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b4.new_ab(is_risp=True)
b4.pitch_list("b b")
b4.hit(4, rbis=3)

# 4. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c b f f f b b s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 2. BAL #2  Jonathan Villar (X - X - X)
t5.new_ab()
t5.pitch_list("b t s b f f b")
t5.hit(1)
t5.advance(2, "10 G1-3")
t5.advance(3, "1 SB")

# 3. BAL #10 Adam Jones (X - X - 2)
t5.new_ab()
t5.pitch_list("c")
t5.out("G1-3")

# 4. BAL #16 Trey Mancini (X - 2 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b c c s")
t5.out("K")

# 5. BAL #1  Tim Beckham (X - 2 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.out("G4-3")


# Bot 5th
# Pitching: BAL #67 John Means
b5 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.hit(2)
b5.advance(4, "5 2B")

# 6. BOS #5  Ian Kinsler (X - 18 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f")
b5.hit(2, rbis=1)
b5.advance(4, "11 1B")

# 7. BOS #11 Rafael Devers (X - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s b d b s f")
b5.hit(1, rbis=1)

# 8. BOS #23 Blake Swihart (X - X - 11)
b5.new_ab()
b5.pitch_list("d f c s")
b5.out("K")

# 9. BOS #3  Sandy León (X - X - 11)
b5.new_ab()
b5.pitch_list("s b")
b5.out("F7")

# Offensive change (BOS): Pinch-hitter #30 Tzu-Wei Lin replaces #50 Mookie Betts, batting 1st
b5.offensive_substitution(1, 30, "PH")

# 1. BOS #30 Tzu-Wei Lin (X - X - 11)
b5.new_ab()
b5.pitch_list("b s s b")
b5.out("G6-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #35 Steven Wright
t6 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #24 David Price
t6.pitching_substitution(35)

# Defensive switch (BOS): #30 Tzu-Wei Lin moves to CF
t6.defensive_switch(30, "8")

# 6. BAL #39 Renato Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b c b b c c")
t6.out("!K")

# 7. BAL #23 Joey Rickard (X - X - X)
t6.new_ab()
t6.pitch_list("c c f b c")
t6.out("!K")

# 8. BAL #61 Austin Wynns (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(2, "12 PB")

# 9. BAL #12 Stevie Wilkerson (X - X - 61)
t6.new_ab(is_risp=True)
t6.pitch_list("c")
t6.pb()
t6.out("G3-1")


# Bot 6th
# Pitching: BAL #67 John Means
b6 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("f c f")
b6.out("L4")

# Pitching change (BAL): #49 Cody Carroll replaces #67 John Means
b6.pitching_substitution(49)

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b b c c")
b6.hit(1)
b6.advance(4, "2 HR")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b6.new_ab()
b6.pitch_list("c b b b f")
b6.hit(4, rbis=2)

# 5. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("c s")
b6.out("F7")

# 6. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("(F)P3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# Defensive switch (BOS): #30 Tzu-Wei Lin moves to SS
t7.defensive_switch(30, "6")

# Defensive switch (BOS): #16 Andrew Benintendi moves to CF
t7.defensive_switch(16, "8")

# Defensive change (BOS): #59 Sam Travis replaces #2 Xander Bogaerts (SS), playing LF, batting 4th
t7.defensive_substitution(4, 59, "7")

# 1. BAL #3  Cedric Mullins (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.out("G5-3")

# 2. BAL #2  Jonathan Villar (X - X - X)
t7.new_ab()
t7.pitch_list("b c")
t7.out("G1-3")

# 3. BAL #10 Adam Jones (X - X - X)
t7.new_ab()
t7.pitch_list("s f f")
t7.out("G6-3")


# Bot 7th
# Pitching: BAL #49 Cody Carroll
b7 = game.new_inning()

# Defensive change (BAL): #29 Jace Peterson replaces #2 Jonathan Villar (SS), playing 2B, batting 2nd
b7.defensive_substitution(2, 29, "4/1")

# Defensive change (BAL): #34 John Andreoli replaces #10 Adam Jones (LF), playing RF, batting 3rd
b7.defensive_substitution(3, 34, "9")

# Defensive switch (BAL): #23 Joey Rickard moves to LF
b7.defensive_switch(23, "7")

# Defensive switch (BAL): #12 Stevie Wilkerson moves to SS
b7.defensive_switch(12, "6")

# 7. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c f b")
b7.hit(4)

# 8. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.hit(4)

# 9. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# 1. BOS #30 Tzu-Wei Lin (X - X - X)
b7.new_ab()
b7.pitch_list("c f b b f f b f b")
b7.reach("BB")
b7.advance(4, "16 2B")

# 2. BOS #16 Andrew Benintendi (X - X - 30)
b7.new_ab()
b7.hit(2, rbis=1)

# 3. BOS #28 J.D. Martinez (X - 16 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s f d")
b7.out("L3")

# 4. BOS #59 Sam Travis (X - 16 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b f b c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #37 Heath Hembree
t8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #35 Steven Wright
t8.pitching_substitution(37)

# 4. BAL #16 Trey Mancini (X - X - X)
t8.new_ab()
t8.pitch_list("c b s f f s")
t8.out("K")

# 5. BAL #1  Tim Beckham (X - X - X)
t8.new_ab()
t8.out("F8")

# 6. BAL #39 Renato Núñez (X - X - X)
t8.new_ab()
t8.pitch_list("b b c")
t8.out("F7")


# Bot 8th
# Pitching: BAL #29 Jace Peterson
b8 = game.new_inning()

# Pitching change (BAL): #29 Jace Peterson replaces #49 Cody Carroll, batting 2nd
b8.pitching_substitution(29)
b8.defensive_substitution(2, 29, "1")

# Defensive change (BAL): #36 Caleb Joseph replaces #16 Trey Mancini (1B), playing 1B, batting 4th
b8.defensive_substitution(4, 36, "3")

# Defensive change (BAL): #64 Corban Joseph replaces #1 Tim Beckham (DH), playing 2B, batting 5th
b8.defensive_substitution(5, 64, "4")

# 5. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c f b f")
b8.hit(1)
b8.thrown_out(2, "5 DP1-6-3", 1, 29)

# 6. BOS #5  Ian Kinsler (X - X - 18)
b8.new_ab()
b8.pitch_list("b c f")
b8.out("DP1-6-3")

# 7. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(4)

# 8. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b b s f")
b8.hit(1)
b8.advance(3, "3 2B")
b8.advance(4, "30 2B")

# 9. BOS #3  Sandy León (X - X - 23)
b8.new_ab()
b8.pitch_list("b")
b8.hit(2)
b8.advance(4, "30 2B")

# 1. BOS #30 Tzu-Wei Lin (23 - 3 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b f s")
b8.hit(2, rbis=2)
b8.advance(4, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - 30 - X)
b8.new_ab(is_risp=True)
b8.pitch_list("b")
b8.hit(1, rbis=1)

# Offensive change (BOS): Pinch-hitter #7 Christian Vázquez replaces #28 J.D. Martinez, batting 3rd
b8.offensive_substitution(3, 7, "PH")

# 3. BOS #7  Christian Vázquez (X - X - 16)
b8.new_ab()
b8.pitch_list("b c b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #44 Brandon Workman
t9 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #37 Heath Hembree, batting 7th
t9.pitching_substitution(44)
t9.defensive_substitution(7, 44, "1")

# Defensive switch (BOS): #7 Christian Vázquez moves to 3B
t9.defensive_switch(7, "5")

# Offensive change (BAL): Pinch-hitter #62 DJ Stewart replaces #23 Joey Rickard, batting 7th
t9.offensive_substitution(7, 62, "PH")

# 7. BAL #62 DJ Stewart (X - X - X)
t9.new_ab()
t9.out("G3-1")

# 8. BAL #61 Austin Wynns (X - X - X)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("G4-3")

# 9. BAL #12 Stevie Wilkerson (X - X - X)
t9.new_ab()
t9.pitch_list("b s")
t9.hit(2)

# 1. BAL #3  Cedric Mullins (X - 12 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("c d c")
t9.out("F7")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)

# Loser team: BAL
# LP: BAL #52 Ryan Meisinger
game.losing_pitcher(52, is_away_team=True)

# print(game)
game.generate_scorecard()
