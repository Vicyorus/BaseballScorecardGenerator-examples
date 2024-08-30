import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-05-19
# https://www.baseball-reference.com/boxes/BOS/BOS201805190.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/05/19/530078/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-19 19:11-22:05",
        "at": "Fenway Park, Boston, MA",
        "att": "34,195",
        "temp": "50F, Cloudy",
        "wind": "12mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 37,
            "roster": {
                # Lineup
                16: "Trey Mancini",
                10: "Adam Jones",
                13: "Manny Machado",
                6: "Jonathan Schoop",
                19: "Chris Davis",
                45: "Mark Trumbo",
                24: "Pedro Alvarez",
                29: "Jace Peterson",
                15: "Chance Sisco",
                # Starting pitcher
                37: "Dylan Bundy",
                # Bench
                27: "Andrew Susac",
                14: "Craig Gentry",
                23: "Joey Rickard",
                2: "Danny Valencia",
                # Bullpen
                17: "Alex Cobb",
                48: "Richard Bleier",
                34: "Kevin Gausman",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                60: "Mychal Givens",
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
                [19, "3"],
                [45, "9"],
                [24, "0"],
                [29, "5"],
                [15, "2"],
            ],
            "bench": [
                [27, "C"],
                [14, "CF"],
                [23, "RF"],
                [2, "3B"],
            ],
            "bullpen": [17, 48, 34, 66, 54, 60, 57, 43, 38, 50, 35],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
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
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [36, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 41, 31, 61, 66, 37, 24, 46, 56, 32],
        },
        "umpires": {
            "HP": "Bill Welke",
            "1B": "Nic Lentz",
            "2B": "Alfonso Márquez",
            "3B": "Lance Barrett",
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
# Pitching: BOS #22 Rick Porcello
t1 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t1.new_ab()
t1.pitch_list("c b b")
t1.hit(1)

# 2. BAL #10 Adam Jones (X - X - 16)
t1.new_ab()
t1.out("(F)P3")

# 3. BAL #13 Manny Machado (X - X - 16)
t1.new_ab()
t1.pitch_list("f s b")
t1.out("L6")

# 4. BAL #6  Jonathan Schoop (X - X - 16)
t1.new_ab()
t1.pitch_list("b b c b")
t1.out("G1-3")


# Bot 1st
# Pitching: BAL #37 Dylan Bundy
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c f s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b f b b")
b1.reach("BB")
b1.advance(2, "13 SB")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
b1.new_ab()
b1.pitch_list("f 1 c f f f")
b1.out("P6")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
b1.new_ab()
b1.pitch_list("c b s f f f b b b")
b1.reach("BB")

# 5. BOS #2  Xander Bogaerts (X - 16 - 28)
b1.new_ab()
b1.pitch_list("c b f b f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("c b c s")
t2.out("K")

# 6. BAL #45 Mark Trumbo (X - X - X)
t2.new_ab()
t2.pitch_list("b s c s")
t2.out("K")

# 7. BAL #24 Pedro Alvarez (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b b")
t2.reach("BB")

# 8. BAL #29 Jace Peterson (X - X - 24)
t2.new_ab()
t2.pitch_list("b c f c")
t2.out("!K")


# Bot 2nd
# Pitching: BAL #37 Dylan Bundy
b2 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.out("F8")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(2)
b2.advance(3, "3 F9")

# 8. BOS #3  Sandy León (X - 36 - X)
b2.new_ab()
b2.pitch_list("b c c")
b2.out("F9")

# 9. BOS #19 Jackie Bradley Jr. (36 - X - X)
b2.new_ab()
b2.pitch_list("f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 9. BAL #15 Chance Sisco (X - X - X)
t3.new_ab()
t3.pitch_list("b s")
t3.hit(2)
t3.advance(3, "10 1B")
t3.advance(4, "6 SF7")

# 1. BAL #16 Trey Mancini (X - 15 - X)
t3.new_ab()
t3.pitch_list("b c s c")
t3.out("!K")

# 2. BAL #10 Adam Jones (X - 15 - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.advance(2, "13 BB")

# 3. BAL #13 Manny Machado (15 - X - 10)
t3.new_ab()
t3.pitch_list("f b f d b b")
t3.reach("BB")

# 4. BAL #6  Jonathan Schoop (15 - 10 - 13)
t3.new_ab()
t3.out("SF7", rbis=1)

# 5. BAL #19 Chris Davis (X - 10 - 13)
t3.new_ab()
t3.pitch_list("f b b s 2 s")
t3.out("K")


# Bot 3rd
# Pitching: BAL #37 Dylan Bundy
b3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b")
b3.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("b b c c b")
b3.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b3.new_ab()
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 6. BAL #45 Mark Trumbo (X - X - X)
t4.new_ab()
t4.pitch_list("f f b")
t4.out("G5-3")

# 7. BAL #24 Pedro Alvarez (X - X - X)
t4.new_ab()
t4.pitch_list("b b")
t4.out("G4-3")

# 8. BAL #29 Jace Peterson (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c b")
t4.reach("BB")

# 9. BAL #15 Chance Sisco (X - X - 29)
t4.new_ab()
t4.pitch_list("b 1 s s s")
t4.out("K")


# Bot 4th
# Pitching: BAL #37 Dylan Bundy
b4 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("f s f b")
b4.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.hit(4, rbis=1)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("f b c s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t5.new_ab()
t5.out("F8")

# 2. BAL #10 Adam Jones (X - X - X)
t5.new_ab()
t5.pitch_list("c f f b f")
t5.out("F9")

# 3. BAL #13 Manny Machado (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)

# 4. BAL #6  Jonathan Schoop (X - X - 13)
t5.new_ab()
t5.pitch_list("s f s")
t5.out("K")


# Bot 5th
# Pitching: BAL #37 Dylan Bundy
b5 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("s b b")
b5.hit(2)
b5.advance(4, "50 HR")

# 9. BOS #19 Jackie Bradley Jr. (X - 3 - X)
b5.new_ab()
b5.pitch_list("b f b f s")
b5.out("K")

# 1. BOS #50 Mookie Betts (X - 3 - X)
b5.new_ab()
b5.pitch_list("b c d")
b5.hit(4, rbis=2)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("f f f")
b5.hit(4, rbis=1)

# 3. BOS #13 Hanley Ramirez (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("P6")

# 4. BOS #28 J.D. Martinez (X - X - X)
b5.new_ab()
b5.pitch_list("c f c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 5. BAL #19 Chris Davis (X - X - X)
t6.new_ab()
t6.pitch_list("c b f s")
t6.out("K")

# 6. BAL #45 Mark Trumbo (X - X - X)
t6.new_ab()
t6.pitch_list("b s f f b f f b")
t6.hit(1)
t6.advance(4, "24 HR")

# 7. BAL #24 Pedro Alvarez (X - X - 45)
t6.new_ab()
t6.pitch_list("s s b b")
t6.hit(4, rbis=2)

# 8. BAL #29 Jace Peterson (X - X - X)
t6.new_ab()
t6.pitch_list("f b s")
t6.out("L8")

# 9. BAL #15 Chance Sisco (X - X - X)
t6.new_ab()
t6.pitch_list("b s b s s")
t6.out("K")


# Bot 6th
# Pitching: BAL #37 Dylan Bundy
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("s s b s")
b6.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("c s")
b6.out("F7")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("s s")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #22 Rick Porcello
t7.pitching_substitution(56)

# 1. BAL #16 Trey Mancini (X - X - X)
t7.new_ab()
t7.pitch_list("f b s f")
t7.out("G1-3")

# 2. BAL #10 Adam Jones (X - X - X)
t7.new_ab()
t7.pitch_list("f s b f f f f b f s")
t7.out("K")

# 3. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.pitch_list("c s f s")
t7.out("K")


# Bot 7th
# Pitching: BAL #66 Tanner Scott
b7 = game.new_inning()

# Pitching change (BAL): #66 Tanner Scott replaces #37 Dylan Bundy
b7.pitching_substitution(66)

# 8. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b b c b b")
b7.reach("BB")
b7.advance(2, "19 BB")
b7.advance(3, "50 F9")
b7.advance(4, "16 1B")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
b7.new_ab()
b7.pitch_list("b b b b")
b7.reach("BB")
b7.advance(2, "50 F9")
b7.advance(4, "16 1B")

# 1. BOS #50 Mookie Betts (X - 3 - 19)
b7.new_ab()
b7.pitch_list("b d d c f f")
b7.out("F9")

# 2. BOS #16 Andrew Benintendi (3 - 19 - X)
b7.new_ab()
b7.pitch_list("c s f b f f d")
b7.hit(1, rbis=2)
b7.advance(2, "13 E6")
b7.thrown_out(3, "28 DP5-3", 2, 50)

# Pitching change (BAL): #50 Miguel Castro replaces #66 Tanner Scott
b7.pitching_substitution(50)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
b7.new_ab()
b7.pitch_list("1 1 d f b 1 s")
b7.error(6)
b7.reach("E6")

# 4. BOS #28 J.D. Martinez (X - 16 - 13)
b7.new_ab()
b7.pitch_list("f")
b7.out("DP5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t8.pitching_substitution(32)

# 4. BAL #6  Jonathan Schoop (X - X - X)
t8.new_ab()
t8.pitch_list("s b s f f f b b f")
t8.out("F9")

# 5. BAL #19 Chris Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c s b s")
t8.out("K")

# 6. BAL #45 Mark Trumbo (X - X - X)
t8.new_ab()
t8.pitch_list("c b f s")
t8.out("K")


# Bot 8th
# Pitching: BAL #50 Miguel Castro
b8 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b b c b b")
b8.reach("BB")
b8.thrown_out(2, "36 DP4-6-3", 2, 50)

# 6. BOS #11 Rafael Devers (X - X - 2)
b8.new_ab()
b8.out("(F)P5")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
b8.new_ab()
b8.pitch_list("b")
b8.out("DP4-6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# 7. BAL #24 Pedro Alvarez (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("F9")

# 8. BAL #29 Jace Peterson (X - X - X)
t9.new_ab()
t9.pitch_list("b s b f")
t9.out("P6")

# 9. BAL #15 Chance Sisco (X - X - X)
t9.new_ab()
t9.pitch_list("b f f")
t9.out("F7")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: BAL
# LP: BAL #37 Dylan Bundy
game.losing_pitcher(37, is_away_team=True)

# print(game)
game.generate_scorecard()
