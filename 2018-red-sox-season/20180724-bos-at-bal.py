import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ BAL, 2018-07-24
# https://www.baseball-reference.com/boxes/BAL/BAL201807240.shtml
# https://www.mlb.com/gameday/red-sox-vs-orioles/2018/07/24/530918/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-24 19:08-22:15",
        "at": "Oriole Park at Camden Yards, Baltimore, MD",
        "att": "13,342",
        "temp": "79F, Overcast",
        "wind": "6mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                19: "Jackie Bradley Jr.",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                23: "Blake Swihart",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
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
            "lefties": [31, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [19, "8"],
                [36, "4"],
                [11, "5"],
                [23, "2"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 41, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Baltimore Orioles",
            "starter": 32,
            "roster": {
                # Lineup
                1: "Tim Beckham",
                6: "Jonathan Schoop",
                10: "Adam Jones",
                45: "Mark Trumbo",
                2: "Danny Valencia",
                16: "Trey Mancini",
                19: "Chris Davis",
                39: "Renato Núñez",
                36: "Caleb Joseph",
                # Starting pitcher
                32: "Yefry Ramírez",
                # Bench
                29: "Jace Peterson",
                61: "Austin Wynns",
                23: "Joey Rickard",
                # Bullpen
                17: "Alex Cobb",
                54: "Andrew Cashner",
                51: "Paul Fry",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                59: "Jhan Mariñez",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                34: "Kevin Gausman",
                35: "Brad Brach",
                66: "Tanner Scott",
            },
            "lefties": [51, 66],
            "lineup": [
                [1, "6"],
                [6, "4"],
                [10, "8"],
                [45, "9"],
                [2, "0"],
                [16, "7"],
                [19, "3"],
                [39, "5"],
                [36, "2"],
            ],
            "bench": [
                [29, "SS"],
                [61, "C"],
                [23, "RF"],
            ],
            "bullpen": [17, 54, 51, 60, 37, 59, 43, 50, 34, 35, 66],
        },
        "umpires": {
            "HP": "Brian O'Nora",
            "1B": "Fieldin Culbreth",
            "2B": "CB Bucknor",
            "3B": "Chris Conroy",
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
# Pitching: BAL #32 Yefry Ramírez
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c f b b")
t1.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f f b b f f s")
t1.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.hit(4, rbis=1)

# 4. BOS #18 Mitch Moreland (X - X - X)
t1.new_ab()
t1.pitch_list("c f")
t1.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 18)
t1.new_ab()
t1.pitch_list("b s b f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #31 Drew Pomeranz
b1 = game.new_inning()

# 1. BAL #1  Tim Beckham (X - X - X)
b1.new_ab()
b1.out("L8")

# 2. BAL #6  Jonathan Schoop (X - X - X)
b1.new_ab()
b1.pitch_list("b f c s")
b1.out("K")

# 3. BAL #10 Adam Jones (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b b")
b1.reach("BB")

# 4. BAL #45 Mark Trumbo (X - X - 10)
b1.new_ab()
b1.pitch_list("c f d s")
b1.out("K2-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BAL #32 Yefry Ramírez
t2 = game.new_inning()

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t2.new_ab()
t2.pitch_list("f b s b f s")
t2.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G4-3")

# 8. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.out("F8")


# Bot 2nd
# Pitching: BOS #31 Drew Pomeranz
b2 = game.new_inning()

# 5. BAL #2  Danny Valencia (X - X - X)
b2.new_ab()
b2.pitch_list("b c")
b2.hit(1)
b2.advance(2, "16 G5-3")
b2.advance(3, "19 F9")

# 6. BAL #16 Trey Mancini (X - X - 2)
b2.new_ab()
b2.pitch_list("1 b f 1 b")
b2.out("G5-3")

# 7. BAL #19 Chris Davis (X - 2 - X)
b2.new_ab()
b2.pitch_list("b b c f b")
b2.out("F9")

# 8. BAL #39 Renato Núñez (2 - X - X)
b2.new_ab()
b2.pitch_list("f s f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BAL #32 Yefry Ramírez
t3 = game.new_inning()

# 9. BOS #23 Blake Swihart (X - X - X)
t3.new_ab()
t3.pitch_list("c f b s")
t3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("f b b b c f f f s")
t3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f b f b")
t3.reach("BB")

# 3. BOS #28 J.D. Martinez (X - X - 16)
t3.new_ab()
t3.pitch_list("b")
t3.out("P6")


# Bot 3rd
# Pitching: BOS #31 Drew Pomeranz
b3 = game.new_inning()

# 9. BAL #36 Caleb Joseph (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.hit(1)
b3.advance(4, "6 HR")

# 1. BAL #1  Tim Beckham (X - X - 36)
b3.new_ab()
b3.pitch_list("b c f b f f f")
b3.out("L8")

# 2. BAL #6  Jonathan Schoop (X - X - 36)
b3.new_ab()
b3.hit(4, rbis=2)

# 3. BAL #10 Adam Jones (X - X - X)
b3.new_ab()
b3.pitch_list("b b c")
b3.out("G6-3")

# 4. BAL #45 Mark Trumbo (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BAL #32 Yefry Ramírez
t4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b b t s s")
t4.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("b b c")
t4.out("F9")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.pitch_list("b c b s b")
t4.out("L8")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 5. BAL #2  Danny Valencia (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.thrown_out(2, "16 FC5-4", 1, 31)

# 6. BAL #16 Trey Mancini (X - X - 2)
b4.new_ab()
b4.pitch_list("f")
b4.reach("FC5-4")

# 7. BAL #19 Chris Davis (X - X - 16)
b4.new_ab()
b4.pitch_list("d c")
b4.out("F7")

# 8. BAL #39 Renato Núñez (X - X - 16)
b4.new_ab()
b4.pitch_list("b f s f b")
b4.out("P3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BAL #32 Yefry Ramírez
t5 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("c b b b c")
t5.out("L7")

# 8. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.pitch_list("c f b")
t5.out("G3-1")

# 9. BOS #23 Blake Swihart (X - X - X)
t5.new_ab()
t5.pitch_list("b f b")
t5.hit(4, rbis=1)

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("b f b")
t5.hit(4, rbis=1)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("s")
t5.out("F8")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# 9. BAL #36 Caleb Joseph (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c f f b")
b5.reach("BB")
b5.advance(2, "1 WP")
b5.advance(4, "1 HR")

# 1. BAL #1  Tim Beckham (X - X - 36)
b5.new_ab()
b5.pitch_list("c f b f b b")
b5.wp()
b5.hit(4, rbis=2)

# 2. BAL #6  Jonathan Schoop (X - X - X)
b5.new_ab()
b5.pitch_list("f b f s")
b5.out("K")

# 3. BAL #10 Adam Jones (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.out("G6-3")

# 4. BAL #45 Mark Trumbo (X - X - X)
b5.new_ab()
b5.pitch_list("f")
b5.hit(1)

# Pitching change (BOS): #47 Tyler Thornburg replaces #31 Drew Pomeranz
b5.pitching_substitution(47)

# 5. BAL #2  Danny Valencia (X - X - 45)
b5.new_ab()
b5.pitch_list("b c s b b f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BAL #43 Mike Wright Jr.
t6 = game.new_inning()

# Pitching change (BAL): #43 Mike Wright Jr. replaces #32 Yefry Ramírez
t6.pitching_substitution(43)

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("f b c s")
t6.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F7")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c c f b t")
t6.out("KT")


# Bot 6th
# Pitching: BOS #56 Joe Kelly
b6 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #47 Tyler Thornburg
b6.pitching_substitution(56)

# 6. BAL #16 Trey Mancini (X - X - X)
b6.new_ab()
b6.out("G5-3")

# 7. BAL #19 Chris Davis (X - X - X)
b6.new_ab()
b6.pitch_list("b t b b f b")
b6.reach("BB")
b6.advance(2, "39 SB")
b6.advance(3, "36 1B")
b6.advance(4, "1 SF9")

# 8. BAL #39 Renato Núñez (X - X - 19)
b6.new_ab()
b6.pitch_list("b b f b s f b")
b6.reach("BB")
b6.advance(2, "36 1B")
b6.advance(3, "1 SF9")
b6.advance(4, "6 1B")

# 9. BAL #36 Caleb Joseph (X - 19 - 39)
b6.new_ab()
b6.pitch_list("b s c f")
b6.hit(1)
b6.advance(2, "6 1B")
b6.advance(4, "10 1B")

# 1. BAL #1  Tim Beckham (19 - 39 - 36)
b6.new_ab()
b6.pitch_list("b f s f f f f d f b")
b6.out("SF9", rbis=1)

# 2. BAL #6  Jonathan Schoop (39 - X - 36)
b6.new_ab()
b6.pitch_list("b")
b6.hit(1, rbis=1)
b6.advance(3, "10 1B")

# Pitching change (BOS): #76 Hector Velázquez replaces #56 Joe Kelly
b6.pitching_substitution(76)

# 3. BAL #10 Adam Jones (X - 36 - 6)
b6.new_ab()
b6.hit(1, rbis=1)

# 4. BAL #45 Mark Trumbo (6 - X - 10)
b6.new_ab()
b6.pitch_list("c")
b6.out("L8")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BAL #51 Paul Fry
t7 = game.new_inning()

# Pitching change (BAL): #51 Paul Fry replaces #43 Mike Wright Jr.
t7.pitching_substitution(51)

# Defensive change (BAL): #23 Joey Rickard replaces #45 Mark Trumbo (RF), playing RF, batting 4th
t7.defensive_substitution(4, 23, "9")

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b f b f s")
t7.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.out("G1-3")

# 8. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("b b c b f f")
t7.hit(1)

# 9. BOS #23 Blake Swihart (X - X - 11)
t7.new_ab()
t7.pitch_list("b 1 c")
t7.out("G5-3")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# 5. BAL #2  Danny Valencia (X - X - X)
b7.new_ab()
b7.out("P6")

# 6. BAL #16 Trey Mancini (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c f b")
b7.reach("BB")
# Offensive change (BAL): Pinch-runner #29 Jace Peterson replaces #16 Trey Mancini
b7.offensive_substitution(6, 29, "PR")
b7.atbase("PR")
b7.thrown_out(2, "39 CS", 3, 76)

# 7. BAL #19 Chris Davis (X - X - 16)
b7.new_ab()
b7.out("F7")

# 8. BAL #39 Renato Núñez (X - X - 29)
b7.new_ab()
b7.pitch_list("1 b c")
b7.no_ab("CS")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BAL #51 Paul Fry
t8 = game.new_inning()

# Defensive switch (BAL): #29 Jace Peterson moves to LF
t8.defensive_switch(29, "7")

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)
t8.thrown_out(2, "16 FC6-5", 1, 51)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t8.new_ab()
t8.pitch_list("c c b f b")
t8.reach("FC6-5")
t8.advance(4, "28 HR")

# Pitching change (BAL): #60 Mychal Givens replaces #51 Paul Fry
t8.pitching_substitution(60)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t8.new_ab()
t8.pitch_list("c f")
t8.hit(4, rbis=2)

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b b f b f s")
t8.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t8.new_ab()
t8.out("F8")


# Bot 8th
# Pitching: BOS #76 Hector Velázquez
b8 = game.new_inning()

# 8. BAL #39 Renato Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("(F)P3")

# 9. BAL #36 Caleb Joseph (X - X - X)
b8.new_ab()
b8.pitch_list("c b b c")
b8.out("G5-3")

# 1. BAL #1  Tim Beckham (X - X - X)
b8.new_ab()
b8.pitch_list("c c b b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BAL #35 Brad Brach
t9 = game.new_inning()

# Pitching change (BAL): #35 Brad Brach replaces #60 Mychal Givens
t9.pitching_substitution(35)

# 6. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("s b b b c")
t9.hit(1)
t9.error(6)
t9.advance(2, "E6")
t9.advance(3, "12 G3")
t9.advance("U", "11 1B")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #36 Eduardo Núñez, batting 7th
t9.offensive_substitution(7, 12, "PH")

# 7. BOS #12 Brock Holt (X - 19 - X)
t9.new_ab()
t9.pitch_list("c d f b")
t9.out("G3")

# 8. BOS #11 Rafael Devers (19 - X - X)
t9.new_ab()
t9.pitch_list("c t f f")
t9.hit(1, rbis=1)
t9.advance(2, "23 BB")

# 9. BOS #23 Blake Swihart (X - X - 11)
t9.new_ab()
t9.pitch_list("b b b b")
t9.reach("BB")
t9.thrown_out(2, "50 DP4-6-3", 2, 35)

# 1. BOS #50 Mookie Betts (X - 11 - 23)
t9.new_ab()
t9.pitch_list("b")
t9.out("DP4-6-3")

# Winning team: BAL
# WP: BAL #32 Yefry Ramírez
game.winning_pitcher(32)
# SV: BAL #35 Brad Brach
game.save_pitcher(35)

# Loser team: BOS
# LP: BOS #31 Drew Pomeranz
game.losing_pitcher(31, is_away_team=True)

# print(game)
game.generate_scorecard()
