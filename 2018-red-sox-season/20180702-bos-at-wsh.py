import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ WSH, 2018-07-02
# https://www.baseball-reference.com/boxes/WAS/WAS201807020.shtml
# https://www.mlb.com/gameday/red-sox-vs-nationals/2018/07/02/530669/final/box

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-07-02 19:08-22:23",
        "at": "Nationals Park, Washington, DC",
        "att": "39,002",
        "temp": "95F, Clear",
        "wind": "10mph, Out To CF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                22: "Rick Porcello",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                28: "J.D. Martinez",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                44: "Brandon Workman",
                67: "William Cuevas",
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
                [16, "7"],
                [2, "6"],
                [18, "3"],
                [11, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
                [22, "1"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [28, "DH"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 44, 67, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Washington Nationals",
            "starter": 31,
            "roster": {
                # Lineup
                2: "Adam Eaton",
                7: "Trea Turner",
                22: "Juan Soto",
                6: "Anthony Rendon",
                34: "Bryce Harper",
                20: "Daniel Murphy",
                1: "Wilmer Difo",
                29: "Pedro Severino",
                31: "Max Scherzer",
                # Starting pitcher
                31: "Max Scherzer",
                # Bench
                14: "Mark Reynolds",
                8: "Brian Goodwin",
                64: "Spencer Kieboom",
                3: "Michael A. Taylor",
                # Bullpen
                58: "Jeremy Hellickson",
                27: "Shawn Kelley",
                21: "Brandon Kintzler",
                62: "Sean Doolittle",
                47: "Gio González",
                44: "Ryan Madson",
                40: "Kelvin Herrera",
                23: "Erick Fedde",
                60: "Justin Miller",
                33: "Matt Grace",
                55: "Tim Collins",
                57: "Tanner Roark",
            },
            "lefties": [62, 47, 33, 55],
            "lineup": [
                [2, "9"],
                [7, "6"],
                [22, "7"],
                [6, "5"],
                [34, "8"],
                [20, "3"],
                [1, "4"],
                [29, "2"],
                [31, "1"],
            ],
            "bench": [
                [14, "3B"],
                [8, "CF"],
                [64, "C"],
                [3, "CF"],
            ],
            "bullpen": [58, 27, 21, 62, 47, 44, 40, 23, 60, 33, 55, 57],
        },
        "umpires": {
            "HP": "Jerry Layne",
            "1B": "Vic Carapazza",
            "2B": "Jordan Baker",
            "3B": "Jeremie Rehak",
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
# Pitching: WSH #31 Max Scherzer
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c s b f")
t1.out("P3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c s s")
t1.out("K")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t1.new_ab()
t1.pitch_list("s f")
t1.out("F9")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. WSH #2  Adam Eaton (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("F9")

# 2. WSH #7  Trea Turner (X - X - X)
b1.new_ab()
b1.pitch_list("b c f f b")
b1.out("G3-1")

# 3. WSH #22 Juan Soto (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b b b b")
b1.reach("BB")
b1.thrown_out(2, "6 FC5-4", 3, 22)

# 4. WSH #6  Anthony Rendon (X - X - 22)
b1.new_ab()
b1.pitch_list("b f c")
b1.reach("FC5-4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: WSH #31 Max Scherzer
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c t")
t2.hit(1)
t2.advance(2, "12 HBP")
t2.advance(3, "3 WP")
t2.advance(4, "22 2B")

# 5. BOS #11 Rafael Devers (X - X - 18)
t2.new_ab()
t2.pitch_list("b b")
t2.out("P4")

# 6. BOS #12 Brock Holt (X - X - 18)
t2.new_ab()
t2.pitch_list("b")
t2.reach("HBP")
t2.advance(2, "3 WP")
t2.advance(4, "22 2B")

# 7. BOS #3  Sandy León (X - 18 - 12)
t2.new_ab(is_risp=True)
t2.pitch_list("b c s d s")
t2.wp()
t2.out("K")

# 8. BOS #19 Jackie Bradley Jr. (18 - 12 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("v v v v")
t2.reach("IBB")
t2.advance(4, "22 2B")

# 9. BOS #22 Rick Porcello (18 - 12 - 19)
t2.new_ab(is_risp=True)
t2.pitch_list("s s")
t2.hit(2, rbis=3)

# 1. BOS #50 Mookie Betts (X - 22 - X)
t2.new_ab(is_risp=True)
t2.pitch_list("b c b f d b")
t2.reach("BB")

# 2. BOS #16 Andrew Benintendi (X - 22 - 50)
t2.new_ab(is_risp=True)
t2.pitch_list("b c f b s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. WSH #34 Bryce Harper (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G4-3")

# 6. WSH #20 Daniel Murphy (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)
b2.advance(2, "1 1B")
b2.thrown_out(3, "1 9-5", 2, 22)

# 7. WSH #1  Wilmer Difo (X - X - 20)
b2.new_ab()
b2.pitch_list("b f")
b2.hit(1)

# 8. WSH #29 Pedro Severino (X - X - 1)
b2.new_ab()
b2.out("G1-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: WSH #31 Max Scherzer
t3 = game.new_inning()

# 3. BOS #2  Xander Bogaerts (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s")
t3.reach("HBP")
t3.advance(3, "12 1B")

# 4. BOS #18 Mitch Moreland (X - X - 2)
t3.new_ab()
t3.pitch_list("1 b c b f 1 f s")
t3.out("K")

# 5. BOS #11 Rafael Devers (X - X - 2)
t3.new_ab()
t3.pitch_list("c s f f f d f t")
t3.out("KT")

# 6. BOS #12 Brock Holt (X - X - 2)
t3.new_ab()
t3.pitch_list("b c b f 1 f f f f f f")
t3.hit(1)

# 7. BOS #3  Sandy León (2 - X - 12)
t3.new_ab(is_risp=True)
t3.pitch_list("b b s b")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 9. WSH #31 Max Scherzer (X - X - X)
b3.new_ab()
b3.pitch_list("c c")
b3.out("G1-3")

# 1. WSH #2  Adam Eaton (X - X - X)
b3.new_ab()
b3.pitch_list("c s f f b b f f")
b3.hit(1)
b3.thrown_out(2, "7 FC5-4", 2, 22)

# 2. WSH #7  Trea Turner (X - X - 2)
b3.new_ab()
b3.pitch_list("f")
b3.reach("FC5-4")

# 3. WSH #22 Juan Soto (X - X - 7)
b3.new_ab()
b3.pitch_list("c 1 f c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: WSH #31 Max Scherzer
t4 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t4.new_ab()
t4.out("F7")

# 9. BOS #22 Rick Porcello (X - X - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
t4.new_ab()
t4.pitch_list("b b b c")
t4.out("F8")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 4. WSH #6  Anthony Rendon (X - X - X)
b4.new_ab()
b4.hit(4)

# 5. WSH #34 Bryce Harper (X - X - X)
b4.new_ab()
b4.pitch_list("s f f c")
b4.out("!K")

# 6. WSH #20 Daniel Murphy (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("L3")

# 7. WSH #1  Wilmer Difo (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b c")
b4.hit(1)

# 8. WSH #29 Pedro Severino (X - X - 1)
b4.new_ab()
b4.pitch_list("f b c 1 c")
b4.out("!K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: WSH #31 Max Scherzer
t5 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("f b s b s")
t5.out("K")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("L7")

# 4. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("b c f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 9. WSH #31 Max Scherzer (X - X - X)
b5.new_ab()
b5.pitch_list("s")
b5.out("G1-3")

# 1. WSH #2  Adam Eaton (X - X - X)
b5.new_ab()
b5.pitch_list("c b b f f f b b")
b5.reach("BB")
b5.advance(2, "22 1B")

# 2. WSH #7  Trea Turner (X - X - 2)
b5.new_ab()
b5.pitch_list("b c")
b5.out("L5")

# 3. WSH #22 Juan Soto (X - X - 2)
b5.new_ab()
b5.hit(1)

# 4. WSH #6  Anthony Rendon (X - 2 - 22)
b5.new_ab(is_risp=True)
b5.pitch_list("c f f b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: WSH #31 Max Scherzer
t6 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c f f b f b")
t6.out("P4")

# 6. BOS #12 Brock Holt (X - X - X)
t6.new_ab()
t6.hit(1)
t6.advance(2, "3 SAC1-3")

# 7. BOS #3  Sandy León (X - X - 12)
t6.new_ab()
t6.pitch_list("f")
t6.out("SAC1-3")

# 8. BOS #19 Jackie Bradley Jr. (X - 12 - X)
t6.new_ab(is_risp=True)
t6.pitch_list("v v v v")
t6.reach("IBB")

# 9. BOS #22 Rick Porcello (X - 12 - 19)
t6.new_ab(is_risp=True)
t6.pitch_list("f s d c")
t6.out("!K")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 5. WSH #34 Bryce Harper (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("F7")

# 6. WSH #20 Daniel Murphy (X - X - X)
b6.new_ab()
b6.hit(4)

# 7. WSH #1  Wilmer Difo (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f b c")
b6.out("!K")

# 8. WSH #29 Pedro Severino (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: WSH #21 Brandon Kintzler
t7 = game.new_inning()

# Pitching change (WSH): #21 Brandon Kintzler replaces #31 Max Scherzer, batting 9th
t7.pitching_substitution(21)
t7.defensive_substitution(9, 21, "1")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c c b")
t7.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F7")

# 3. BOS #2  Xander Bogaerts (X - X - X)
t7.new_ab()
t7.pitch_list("c b s f b s")
t7.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("f b")
t7.out("F7")


# Bot 7th
# Pitching: BOS #32 Matt Barnes
b7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #22 Rick Porcello, batting 9th
b7.pitching_substitution(32)
b7.defensive_substitution(9, 32, "1")

# Offensive change (WSH): Pinch-hitter #8 Brian Goodwin replaces #21 Brandon Kintzler, batting 9th
b7.offensive_substitution(9, 8, "PH")

# 9. WSH #8  Brian Goodwin (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.out("L4")

# 1. WSH #2  Adam Eaton (X - X - X)
b7.new_ab()
b7.hit(1)
b7.advance(2, "22 BB")

# 2. WSH #7  Trea Turner (X - X - 2)
b7.new_ab()
b7.pitch_list("b c 1 c b f s")
b7.out("K")

# 3. WSH #22 Juan Soto (X - X - 2)
b7.new_ab()
b7.pitch_list("s b c b d b")
b7.reach("BB")
b7.thrown_out(2, "6 FC6", 3, 32)

# 4. WSH #6  Anthony Rendon (X - 2 - 22)
b7.new_ab(is_risp=True)
b7.pitch_list("c")
b7.reach("FC6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: WSH #55 Tim Collins
t8 = game.new_inning()

# Pitching change (WSH): #55 Tim Collins replaces #21 Brandon Kintzler, batting 9th
t8.pitching_substitution(55)
t8.defensive_substitution(9, 55, "1")

# 5. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("f c b b s")
t8.out("K")

# 6. BOS #12 Brock Holt (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(1)
t8.thrown_out(2, "3 POCS", 2, 55)

# 7. BOS #3  Sandy León (X - X - 12)
t8.new_ab()
t8.pitch_list("c b c 1 c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #56 Joe Kelly
b8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes, batting 9th
b8.pitching_substitution(56)
b8.defensive_substitution(9, 56, "1")

# 5. WSH #34 Bryce Harper (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.hit(4)

# 6. WSH #20 Daniel Murphy (X - X - X)
b8.new_ab()
b8.pitch_list("c f s")
b8.out("K")

# 7. WSH #1  Wilmer Difo (X - X - X)
b8.new_ab()
b8.pitch_list("c s b b s")
b8.out("K")

# Offensive change (WSH): Pinch-hitter #14 Mark Reynolds replaces #29 Pedro Severino, batting 8th
b8.offensive_substitution(8, 14, "PH")

# 8. WSH #14 Mark Reynolds (X - X - X)
b8.new_ab()
b8.pitch_list("b b c s b b")
b8.reach("BB")

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly, batting 7th
b8.pitching_substitution(46)
b8.defensive_substitution(7, 46, "1")

# Offensive change (WSH): Pinch-hitter #3 Michael A. Taylor replaces #55 Tim Collins, batting 9th
b8.offensive_substitution(9, 3, "PH")

# Defensive change (BOS): #7 Christian Vázquez replaces #56 Joe Kelly (P), playing C, batting 9th
b8.defensive_substitution(9, 7, "2")

# 9. WSH #3  Michael A. Taylor (X - X - 14)
b8.new_ab()
b8.pitch_list("s b b c f 1 b")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: WSH #27 Shawn Kelley
t9 = game.new_inning()

# Pitching change (WSH): #27 Shawn Kelley replaces #55 Tim Collins, batting 9th
t9.pitching_substitution(27)
t9.defensive_substitution(9, 27, "1")

# Defensive change (WSH): #64 Spencer Kieboom replaces #14 Mark Reynolds (PH), playing C, batting 8th
t9.defensive_substitution(8, 64, "2")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.hit(1)

# 9. BOS #7  Christian Vázquez (X - X - 19)
t9.new_ab()
t9.out("F9")

# 1. BOS #50 Mookie Betts (X - X - 19)
t9.new_ab()
t9.pitch_list("b 1 c")
t9.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - 19)
t9.new_ab()
t9.pitch_list("1 1 f f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# 1. WSH #2  Adam Eaton (X - X - X)
b9.new_ab()
b9.pitch_list("c b c f f f b s")
b9.out("K")

# 2. WSH #7  Trea Turner (X - X - X)
b9.new_ab()
b9.pitch_list("b c b c f")
b9.out("F9")

# 3. WSH #22 Juan Soto (X - X - X)
b9.new_ab()
b9.pitch_list("s s f b b b f b")
b9.reach("BB")

# 4. WSH #6  Anthony Rendon (X - X - 22)
b9.new_ab()
b9.pitch_list("b b b")
b9.out("L7")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: WSH
# LP: WSH #31 Max Scherzer
game.losing_pitcher(31)

# print(game)
game.generate_scorecard()
