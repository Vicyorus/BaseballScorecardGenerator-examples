import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-05-20
# https://www.baseball-reference.com/boxes/BOS/BOS201805200.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/05/20/530093/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-20 13:06-16:31",
        "at": "Fenway Park, Boston, MA",
        "att": "35,550",
        "temp": "78F, Cloudy",
        "wind": "18mph, Out To CF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 41,
            "roster": {
                # Lineup
                16: "Trey Mancini",
                10: "Adam Jones",
                13: "Manny Machado",
                6: "Jonathan Schoop",
                45: "Mark Trumbo",
                2: "Danny Valencia",
                23: "Joey Rickard",
                27: "Andrew Susac",
                14: "Craig Gentry",
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
                66: "Tanner Scott",
                54: "Andrew Cashner",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                43: "Mike Wright Jr.",
                38: "Pedro Araújo",
                50: "Miguel Castro",
                35: "Brad Brach",
            },
            "lefties": [48, 66],
            "lineup": [
                [16, "3"],
                [10, "8"],
                [13, "6"],
                [6, "4"],
                [45, "0"],
                [2, "5"],
                [23, "9"],
                [27, "2"],
                [14, "7"],
            ],
            "bench": [
                [19, "1B"],
                [29, "SS"],
                [24, "3B"],
                [15, "C"],
            ],
            "bullpen": [17, 48, 34, 66, 54, 60, 37, 43, 38, 50, 35],
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
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                23: "Blake Swihart",
                2: "Xander Bogaerts",
                3: "Sandy León",
                13: "Hanley Ramirez",
                # Bullpen
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [11, "5"],
                [36, "4"],
                [12, "6"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [23, "C"],
                [2, "2B"],
                [3, "C"],
                [13, "SS"],
            ],
            "bullpen": [35, 22, 41, 31, 61, 66, 37, 24, 46, 56, 32],
        },
        "umpires": {
            "HP": "Nic Lentz",
            "1B": "Alfonso Márquez",
            "2B": "Lance Barrett",
            "3B": "Bill Welke",
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
t1.pitch_list("b b c f")
t1.out("G4-3")

# 2. BAL #10 Adam Jones (X - X - X)
t1.new_ab()
t1.pitch_list("b c b b")
t1.hit(1)

# 3. BAL #13 Manny Machado (X - X - 10)
t1.new_ab()
t1.pitch_list("c c f b b b")
t1.out("F9")

# 4. BAL #6  Jonathan Schoop (X - X - 10)
t1.new_ab()
t1.pitch_list("c b")
t1.out("L8")


# Bot 1st
# Pitching: BAL #41 David Hess
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("f b")
b1.out("(F)P2")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b c b")
b1.out("G4-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 5. BAL #45 Mark Trumbo (X - X - X)
t2.new_ab()
t2.pitch_list("b f")
t2.hit(1)

# 6. BAL #2  Danny Valencia (X - X - 45)
t2.new_ab()
t2.out("F8")

# 7. BAL #23 Joey Rickard (X - X - 45)
t2.new_ab()
t2.pitch_list("b c f b b f f f")
t2.out("L7")

# 8. BAL #27 Andrew Susac (X - X - 45)
t2.new_ab()
t2.pitch_list("b f b s c")
t2.out("!K")


# Bot 2nd
# Pitching: BAL #41 David Hess
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.hit(4, rbis=1)

# 5. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("s b b f f b b")
b2.reach("BB")
b2.advance(2, "12 1B")
b2.advance(3, "7 FC5-4")

# 6. BOS #36 Eduardo Núñez (X - X - 11)
b2.new_ab()
b2.pitch_list("c t s")
b2.out("K")

# 7. BOS #12 Brock Holt (X - X - 11)
b2.new_ab()
b2.pitch_list("c b f f f")
b2.hit(1)
b2.thrown_out(2, "7 FC5-4", 2, 41)

# 8. BOS #7  Christian Vázquez (X - 11 - 12)
b2.new_ab()
b2.pitch_list("b b f c")
b2.reach("FC5-4")

# 9. BOS #19 Jackie Bradley Jr. (11 - X - 7)
b2.new_ab()
b2.pitch_list("c s b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 9. BAL #14 Craig Gentry (X - X - X)
t3.new_ab()
t3.pitch_list("c f s")
t3.out("K")

# 1. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.hit(1)
t3.advance(2, "10 1B")

# 2. BAL #10 Adam Jones (X - X - 16)
t3.new_ab()
t3.pitch_list("c f")
t3.hit(1)

# 3. BAL #13 Manny Machado (X - 16 - 10)
t3.new_ab()
t3.pitch_list("s b 2 b")
t3.out("IF5")

# 4. BAL #6  Jonathan Schoop (X - 16 - 10)
t3.new_ab()
t3.pitch_list("b b s b")
t3.out("G5-3")


# Bot 3rd
# Pitching: BAL #41 David Hess
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b c f f b b")
b3.hit(2)

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b3.new_ab()
b3.pitch_list("c b b t f d")
b3.out("P4")

# 3. BOS #18 Mitch Moreland (X - 50 - X)
b3.new_ab()
b3.pitch_list("f f t")
b3.out("KT")

# 4. BOS #28 J.D. Martinez (X - 50 - X)
b3.new_ab()
b3.pitch_list("d b b v")
b3.reach("IBB")

# 5. BOS #11 Rafael Devers (X - 50 - 28)
b3.new_ab()
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 5. BAL #45 Mark Trumbo (X - X - X)
t4.new_ab()
t4.pitch_list("b f b c f")
t4.out("G1-3")

# 6. BAL #2  Danny Valencia (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f")
t4.error(5)
t4.reach("E5")
t4.thrown_out(2, "23 FC4-6", 2, 57)

# 7. BAL #23 Joey Rickard (X - X - 2)
t4.new_ab()
t4.pitch_list("c f b")
t4.reach("FC4-6")
t4.advance(2, "27 1B")

# 8. BAL #27 Andrew Susac (X - X - 23)
t4.new_ab()
t4.pitch_list("b")
t4.hit(1)

# 9. BAL #14 Craig Gentry (X - 23 - 27)
t4.new_ab()
t4.out("F8")


# Bot 4th
# Pitching: BAL #41 David Hess
b4 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("f s s")
b4.out("K")

# 7. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G3-1")

# 8. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t5.new_ab()
t5.pitch_list("c b s s")
t5.out("K")

# 2. BAL #10 Adam Jones (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)

# 3. BAL #13 Manny Machado (X - X - 10)
t5.new_ab()
t5.pitch_list("b c s b c")
t5.out("!K")

# 4. BAL #6  Jonathan Schoop (X - X - 10)
t5.new_ab()
t5.pitch_list("b c s b s")
t5.out("K")


# Bot 5th
# Pitching: BAL #41 David Hess
b5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("f s")
b5.hit(2)
b5.advance(3, "50 F8")
b5.advance(4, "16 HR")

# 1. BOS #50 Mookie Betts (X - 19 - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("F8")

# 2. BOS #16 Andrew Benintendi (19 - X - X)
b5.new_ab()
b5.pitch_list("c f b b b")
b5.hit(4, rbis=2)

# 3. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.hit(2)
b5.advance(4, "28 HR")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(4, rbis=2)

# 5. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("c b f")
b5.out("G5-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c s f")
b5.hit(1)
b5.advance(2, "12 1B")

# Pitching change (BAL): #43 Mike Wright Jr. replaces #41 David Hess
b5.pitching_substitution(43)

# 7. BOS #12 Brock Holt (X - X - 36)
b5.new_ab()
b5.pitch_list("c")
b5.hit(1)

# 8. BOS #7  Christian Vázquez (X - 36 - 12)
b5.new_ab()
b5.pitch_list("c d c b f f f b f")
b5.out("F8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 5. BAL #45 Mark Trumbo (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b s")
t6.out("K")

# 6. BAL #2  Danny Valencia (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.hit(1)
t6.advance(2, "23 1B")
t6.advance(3, "14 1B")

# 7. BAL #23 Joey Rickard (X - X - 2)
t6.new_ab()
t6.pitch_list("f b s f b f")
t6.hit(1)
t6.advance(2, "14 1B")

# 8. BAL #27 Andrew Susac (X - 2 - 23)
t6.new_ab()
t6.pitch_list("c f s")
t6.out("K")

# 9. BAL #14 Craig Gentry (X - 2 - 23)
t6.new_ab()
t6.pitch_list("b c c")
t6.hit(1)

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
t6.pitching_substitution(37)

# 1. BAL #16 Trey Mancini (2 - 23 - 14)
t6.new_ab()
t6.pitch_list("s")
t6.out("F9")


# Bot 6th
# Pitching: BAL #43 Mike Wright Jr.
b6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("b b b c b")
b6.reach("BB")
b6.advance(3, "16 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b6.new_ab()
b6.pitch_list("s")
b6.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - 19)
b6.new_ab()
b6.pitch_list("b 1")
b6.hit(1)

# 3. BOS #18 Mitch Moreland (19 - X - 16)
b6.new_ab()
b6.pitch_list("c")
b6.out("P5")

# 4. BOS #28 J.D. Martinez (19 - X - 16)
b6.new_ab()
b6.pitch_list("c")
b6.out("L5")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# 2. BAL #10 Adam Jones (X - X - X)
t7.new_ab()
t7.pitch_list("s b f f s")
t7.out("K")

# 3. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.pitch_list("b f f")
t7.hit(1)

# 4. BAL #6  Jonathan Schoop (X - X - 13)
t7.new_ab()
t7.pitch_list("f s s")
t7.out("K")

# 5. BAL #45 Mark Trumbo (X - X - 13)
t7.new_ab()
t7.pitch_list("s b s b")
t7.out("P3")


# Bot 7th
# Pitching: BAL #43 Mike Wright Jr.
b7 = game.new_inning()

# Defensive change (BAL): #29 Jace Peterson replaces #10 Adam Jones (CF), playing LF, batting 2nd
b7.defensive_substitution(2, 29, "7")

# Defensive switch (BAL): #14 Craig Gentry moves to CF
b7.defensive_switch(14, "8")

# 5. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("c b f f f")
b7.out("P5")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.out("L9")

# 7. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")
b7.advance(3, "7 1B")

# 8. BOS #7  Christian Vázquez (X - X - 12)
b7.new_ab()
b7.hit(1)

# 9. BOS #19 Jackie Bradley Jr. (12 - X - 7)
b7.new_ab()
b7.pitch_list("t b f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #66 Bobby Poyner
t8 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #37 Heath Hembree
t8.pitching_substitution(66)

# 6. BAL #2  Danny Valencia (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b b")
t8.out("G5-3")

# 7. BAL #23 Joey Rickard (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(1)
t8.advance(2, "14 1B")

# 8. BAL #27 Andrew Susac (X - X - 23)
t8.new_ab()
t8.pitch_list("f f b b")
t8.out("(F)P5")

# 9. BAL #14 Craig Gentry (X - X - 23)
t8.new_ab()
t8.hit(1)

# 1. BAL #16 Trey Mancini (X - 23 - 14)
t8.new_ab()
t8.pitch_list("b f")
t8.out("G1-3")


# Bot 8th
# Pitching: BAL #43 Mike Wright Jr.
b8 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b b")
b8.reach("BB")
b8.advance(2, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b8.new_ab()
b8.pitch_list("c 1 f b")
b8.hit(1)

# Pitching change (BAL): #38 Pedro Araújo replaces #43 Mike Wright Jr.
b8.pitching_substitution(38)

# 3. BOS #18 Mitch Moreland (X - 50 - 16)
b8.new_ab()
b8.pitch_list("s f s")
b8.out("K")

# 4. BOS #28 J.D. Martinez (X - 50 - 16)
b8.new_ab()
b8.pitch_list("f c f b s")
b8.out("K")

# 5. BOS #11 Rafael Devers (X - 50 - 16)
b8.new_ab()
b8.pitch_list("b f d b s s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #66 Bobby Poyner
t9.pitching_substitution(61)

# 2. BAL #29 Jace Peterson (X - X - X)
t9.new_ab()
t9.pitch_list("b f c f")
t9.hit(2)
t9.advance(3, "13 G3")

# 3. BAL #13 Manny Machado (X - 29 - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G3")

# 4. BAL #6  Jonathan Schoop (29 - X - X)
t9.new_ab()
t9.pitch_list("b f c f b d f f f")
t9.out("F8")

# 5. BAL #45 Mark Trumbo (29 - X - X)
t9.new_ab()
t9.pitch_list("b c f f b c")
t9.out("!K")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)

# Loser team: BAL
# LP: BAL #41 David Hess
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
