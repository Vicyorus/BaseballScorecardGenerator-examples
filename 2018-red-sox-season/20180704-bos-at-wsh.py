import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ WSH, 2018-07-04
# https://www.baseball-reference.com/boxes/WAS/WAS201807040.shtml
# https://www.mlb.com/gameday/red-sox-vs-nationals/2018/07/04/530695/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-04 11:07-14:30",
        "at": "Nationals Park, Washington, DC",
        "att": "42,528",
        "temp": "89F, Partly Cloudy",
        "wind": "3mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                12: "Brock Holt",
                28: "J.D. Martinez",
                25: "Steve Pearce",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                57: "Eduardo Rodriguez",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                18: "Mitch Moreland",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
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
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [12, "6"],
                [28, "7"],
                [25, "3"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
                [57, "1"],
            ],
            "bench": [
                [18, "1B"],
                [23, "C"],
                [16, "LF"],
                [2, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 44, 22, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Washington Nationals",
            "starter": 23,
            "roster": {
                # Lineup
                2: "Adam Eaton",
                7: "Trea Turner",
                6: "Anthony Rendon",
                34: "Bryce Harper",
                14: "Mark Reynolds",
                3: "Michael A. Taylor",
                1: "Wilmer Difo",
                29: "Pedro Severino",
                23: "Erick Fedde",
                # Starting pitcher
                23: "Erick Fedde",
                # Bench
                15: "Matt Adams",
                20: "Daniel Murphy",
                8: "Brian Goodwin",
                64: "Spencer Kieboom",
                22: "Juan Soto",
                # Bullpen
                58: "Jeremy Hellickson",
                27: "Shawn Kelley",
                21: "Brandon Kintzler",
                62: "Sean Doolittle",
                47: "Gio González",
                44: "Ryan Madson",
                31: "Max Scherzer",
                40: "Kelvin Herrera",
                60: "Justin Miller",
                33: "Matt Grace",
                57: "Tanner Roark",
            },
            "lefties": [62, 47, 33],
            "lineup": [
                [2, "7"],
                [7, "6"],
                [6, "5"],
                [34, "9"],
                [14, "3"],
                [3, "8"],
                [1, "4"],
                [29, "2"],
                [23, "1"],
            ],
            "bench": [
                [15, "1B"],
                [20, "2B"],
                [8, "CF"],
                [64, "C"],
                [22, "RF"],
            ],
            "bullpen": [58, 27, 21, 62, 47, 44, 31, 40, 60, 33, 57],
        },
        "umpires": {
            "HP": "Jordan Baker",
            "1B": "Jeremie Rehak",
            "2B": "Jerry Layne",
            "3B": "Vic Carapazza",
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
# Pitching: WSH #23 Erick Fedde
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.hit(1)
t1.thrown_out(2, "12 FC3-6", 1, 23)

# 2. BOS #12 Brock Holt (X - X - 50)
t1.new_ab()
t1.pitch_list("c 1 b b")
t1.reach("FC3-6")
t1.advance(2, "28 G4-3")

# 3. BOS #28 J.D. Martinez (X - X - 12)
t1.new_ab()
t1.pitch_list("c c b b b f f f")
t1.out("G4-3")

# 4. BOS #25 Steve Pearce (X - 12 - X)
t1.new_ab()
t1.pitch_list("c b b c")
t1.out("G6-3")


# Bot 1st
# Pitching: BOS #57 Eduardo Rodriguez
b1 = game.new_inning()

# 1. WSH #2  Adam Eaton (X - X - X)
b1.new_ab()
b1.pitch_list("t s s")
b1.out("K")

# 2. WSH #7  Trea Turner (X - X - X)
b1.new_ab()
b1.pitch_list("b b s f")
b1.hit(1)

# 3. WSH #6  Anthony Rendon (X - X - 7)
b1.new_ab()
b1.pitch_list("f b")
b1.out("P4")

# 4. WSH #34 Bryce Harper (X - X - 7)
b1.new_ab()
b1.pitch_list("b c")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: WSH #23 Erick Fedde
t2 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("f b c")
t2.hit(1)
t2.thrown_out(2, "19 PO", 2, 33)

# Pitching change (WSH): #33 Matt Grace replaces #23 Erick Fedde, batting 9th
t2.pitching_substitution(33)
t2.defensive_substitution(9, 33, "1")

# 6. BOS #36 Eduardo Núñez (X - X - 11)
t2.new_ab()
t2.pitch_list("1 s b f 1 f f 1 s")
t2.out("K")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 11)
t2.new_ab()
t2.pitch_list("1 b c")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #57 Eduardo Rodriguez
b2 = game.new_inning()

# 5. WSH #14 Mark Reynolds (X - X - X)
b2.new_ab()
b2.pitch_list("s s s")
b2.out("K")

# 6. WSH #3  Michael A. Taylor (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b s")
b2.out("K")

# 7. WSH #1  Wilmer Difo (X - X - X)
b2.new_ab()
b2.pitch_list("b b b b")
b2.reach("BB")

# 8. WSH #29 Pedro Severino (X - X - 1)
b2.new_ab()
b2.pitch_list("b f f b")
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: WSH #33 Matt Grace
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b b f f b f")
t3.out("G6-3")

# 9. BOS #57 Eduardo Rodriguez (X - X - X)
t3.new_ab()
t3.pitch_list("s c s")
t3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("G5-3")


# Bot 3rd
# Pitching: BOS #57 Eduardo Rodriguez
b3 = game.new_inning()

# 9. WSH #23 Erick Fedde (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("L5")

# 1. WSH #2  Adam Eaton (X - X - X)
b3.new_ab()
b3.pitch_list("b c")
b3.out("F8")

# 2. WSH #7  Trea Turner (X - X - X)
b3.new_ab()
b3.pitch_list("c f b b")
b3.hit(1)

# 3. WSH #6  Anthony Rendon (X - X - 7)
b3.new_ab()
b3.pitch_list("1 b")
b3.out("F7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: WSH #33 Matt Grace
t4 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("f c b b")
t4.hit(2)

# 4. BOS #25 Steve Pearce (X - 28 - X)
t4.new_ab()
t4.out("G6-3")

# 5. BOS #11 Rafael Devers (X - 28 - X)
t4.new_ab()
t4.pitch_list("s d f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #57 Eduardo Rodriguez
b4 = game.new_inning()

# 4. WSH #34 Bryce Harper (X - X - X)
b4.new_ab()
b4.pitch_list("s b f s")
b4.out("K")

# 5. WSH #14 Mark Reynolds (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b f s")
b4.out("K")

# 6. WSH #3  Michael A. Taylor (X - X - X)
b4.new_ab()
b4.pitch_list("s b s b b f f f f")
b4.out("L9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: WSH #33 Matt Grace
t5 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("b f")
t5.out("L9")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("f b f f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #57 Eduardo Rodriguez
b5 = game.new_inning()

# 7. WSH #1  Wilmer Difo (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f b f s")
b5.out("K")

# 8. WSH #29 Pedro Severino (X - X - X)
b5.new_ab()
b5.hit(1)
b5.error(5)
b5.advance(2, "E5")

# Offensive change (WSH): Pinch-hitter #8 Brian Goodwin replaces #33 Matt Grace, batting 9th
b5.offensive_substitution(9, 8, "PH")

# 9. WSH #8  Brian Goodwin (X - 29 - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("L8")

# 1. WSH #2  Adam Eaton (X - 29 - X)
b5.new_ab()
b5.pitch_list("c b 2 f")
b5.out("F9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: WSH #21 Brandon Kintzler
t6 = game.new_inning()

# Pitching change (WSH): #21 Brandon Kintzler replaces #33 Matt Grace, batting 9th
t6.pitching_substitution(21)
t6.defensive_substitution(9, 21, "1")

# 9. BOS #57 Eduardo Rodriguez (X - X - X)
t6.new_ab()
t6.out("G1-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c c")
t6.hit(1)
t6.advance(3, "28 1B")

# 2. BOS #12 Brock Holt (X - X - 50)
t6.new_ab()
t6.pitch_list("1 f 1 1 f b f 1 b c")
t6.out("!K")

# 3. BOS #28 J.D. Martinez (X - X - 50)
t6.new_ab()
t6.pitch_list("1 s 1 c f f p 1 b")
t6.hit(1)

# 4. BOS #25 Steve Pearce (50 - X - 28)
t6.new_ab()
t6.pitch_list("b f")
t6.out("F8")


# Bot 6th
# Pitching: BOS #57 Eduardo Rodriguez
b6 = game.new_inning()

# 2. WSH #7  Trea Turner (X - X - X)
b6.new_ab()
b6.pitch_list("s")
b6.out("G5-3")

# 3. WSH #6  Anthony Rendon (X - X - X)
b6.new_ab()
b6.out("L9")

# 4. WSH #34 Bryce Harper (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: WSH #44 Ryan Madson
t7 = game.new_inning()

# Pitching change (WSH): #44 Ryan Madson replaces #21 Brandon Kintzler, batting 9th
t7.pitching_substitution(44)
t7.defensive_substitution(9, 44, "1")

# 5. BOS #11 Rafael Devers (X - X - X)
t7.new_ab()
t7.pitch_list("b b f")
t7.hit(2)
t7.advance(3, "36 1B")
t7.advance(4, "19 (F)SF7")

# 6. BOS #36 Eduardo Núñez (X - 11 - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(1)
t7.error(7)
t7.advance(3, "19 E7")
t7.advance("U", "16 WP")

# 7. BOS #19 Jackie Bradley Jr. (11 - X - 36)
t7.new_ab()
t7.pitch_list("b b s b s")
t7.out("(F)SF7", rbis=1)

# 8. BOS #7  Christian Vázquez (36 - X - X)
t7.new_ab()
t7.pitch_list("f b f")
t7.out("G3")

# Offensive change (BOS): Pinch-hitter #16 Andrew Benintendi replaces #57 Eduardo Rodriguez, batting 9th
t7.offensive_substitution(9, 16, "PH")

# 9. BOS #16 Andrew Benintendi (36 - X - X)
t7.new_ab()
t7.pitch_list("c f b b b f b")
t7.wp()
t7.reach("BB")

# 1. BOS #50 Mookie Betts (X - X - 16)
t7.new_ab()
t7.pitch_list("1 c")
t7.out("F8")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #57 Eduardo Rodriguez, batting 9th
b7.pitching_substitution(32)
b7.defensive_substitution(9, 32, "1")

# Offensive change (WSH): Pinch-hitter #20 Daniel Murphy replaces #14 Mark Reynolds, batting 5th
b7.offensive_substitution(5, 20, "PH")

# 5. WSH #20 Daniel Murphy (X - X - X)
b7.new_ab()
b7.pitch_list("c b f b f")
b7.out("G3-1")

# 6. WSH #3  Michael A. Taylor (X - X - X)
b7.new_ab()
b7.pitch_list("b f b")
b7.hit(1)

# 7. WSH #1  Wilmer Difo (X - X - 3)
b7.new_ab()
b7.pitch_list("1 d 1 f b f 1 f f 1 b c")
b7.out("!K")

# 8. WSH #29 Pedro Severino (X - X - 3)
b7.new_ab()
b7.out("P5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: WSH #27 Shawn Kelley
t8 = game.new_inning()

# Pitching change (WSH): #27 Shawn Kelley replaces #44 Ryan Madson, batting 9th
t8.pitching_substitution(27)
t8.defensive_substitution(9, 27, "1")

# Defensive switch (WSH): #20 Daniel Murphy moves to 1B
t8.defensive_switch(20, "3")

# 2. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("c b f f")
t8.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b s f b c")
t8.out("!K")

# 4. BOS #25 Steve Pearce (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes, batting 9th
b8.pitching_substitution(56)
b8.defensive_substitution(9, 56, "1")

# Offensive change (WSH): Pinch-hitter #22 Juan Soto replaces #27 Shawn Kelley, batting 9th
b8.offensive_substitution(9, 22, "PH")

# 9. WSH #22 Juan Soto (X - X - X)
b8.new_ab()
b8.pitch_list("b b f b f")
b8.out("L4")

# 1. WSH #2  Adam Eaton (X - X - X)
b8.new_ab()
b8.pitch_list("f c f f f s")
b8.out("K")

# 2. WSH #7  Trea Turner (X - X - X)
b8.new_ab()
b8.pitch_list("c c s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: WSH #40 Kelvin Herrera
t9 = game.new_inning()

# Pitching change (WSH): #40 Kelvin Herrera replaces #27 Shawn Kelley, batting 1st
t9.pitching_substitution(40)
t9.defensive_substitution(1, 40, "1")

# Defensive switch (WSH): #22 Juan Soto moves to LF
t9.defensive_switch(22, "7")

# 5. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("F7")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("f b b")
t9.hit(1)
t9.advance(4, "19 2B")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
t9.new_ab()
t9.pitch_list("f 1 b b s b")
t9.hit(2, rbis=1)
t9.advance(3, "50 HBP")
t9.thrown_out(4, "12 FC1-2", 3, 60)

# 8. BOS #7  Christian Vázquez (X - 19 - X)
t9.new_ab()
t9.pitch_list("c b b s s")
t9.out("K")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #56 Joe Kelly, batting 9th
t9.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - 19 - X)
t9.new_ab()
t9.pitch_list("b c c b f f b b")
t9.reach("BB")
t9.advance(2, "50 HBP")

# 1. BOS #50 Mookie Betts (X - 19 - 23)
t9.new_ab()
t9.pitch_list("b c b f")
t9.reach("HBP")

# Pitching change (WSH): #60 Justin Miller replaces #40 Kelvin Herrera, batting 1st
t9.pitching_substitution(60)
t9.defensive_substitution(1, 60, "1")

# 2. BOS #12 Brock Holt (19 - 23 - 50)
t9.new_ab()
t9.pitch_list("b")
t9.reach("FC1-2")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly, batting 9th
b9.pitching_substitution(46)
b9.defensive_substitution(9, 46, "1")

# 3. WSH #6  Anthony Rendon (X - X - X)
b9.new_ab()
b9.pitch_list("b c b")
b9.hit(1)
b9.advance(2, "20 1B")

# 4. WSH #34 Bryce Harper (X - X - 6)
b9.new_ab()
b9.pitch_list("c c b f f s")
b9.out("K")

# 5. WSH #20 Daniel Murphy (X - X - 6)
b9.new_ab()
b9.pitch_list("f b")
b9.hit(1)

# 6. WSH #3  Michael A. Taylor (X - 6 - 20)
b9.new_ab()
b9.pitch_list("d s c t")
b9.out("KT")

# 7. WSH #1  Wilmer Difo (X - 6 - 20)
b9.new_ab()
b9.pitch_list("s b b f")
b9.out("(F)P2")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: WSH
# LP: WSH #44 Ryan Madson
game.losing_pitcher(44)

# print(game)
game.generate_scorecard()
