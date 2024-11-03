import os
from baseball_scorecard.baseball_scorecard import Scorecard

# OAK @ BOS, 2018-05-14
# https://www.baseball-reference.com/boxes/BOS/BOS201805140.shtml
# https://www.mlb.com/gameday/athletics-vs-red-sox/2018/05/14/530022/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-14 19:12-21:52",
        "at": "Fenway Park, Boston, MA",
        "att": "35,249",
        "temp": "65F, Clear",
        "wind": "6mph, Out To CF",
        "away": {
            "team": "Oakland Athletics",
            "starter": 55,
            "roster": {
                # Lineup
                10: "Marcus Semien",
                23: "Matt Joyce",
                8: "Jed Lowrie",
                2: "Khris Davis",
                28: "Matt Olson",
                26: "Matt Chapman",
                20: "Mark Canha",
                21: "Jonathan Lucroy",
                11: "Dustin Fowler",
                # Starting pitcher
                55: "Sean Manaea",
                # Bench
                13: "Bruce Maxwell",
                18: "Chad Pinder",
                5: "Jake Smolinski",
                # Bullpen
                62: "Lou Trivino",
                66: "Ryan Dull",
                49: "Kendall Graveman",
                44: "Chris Hatcher",
                57: "Wilmer Font",
                30: "Brett Anderson",
                60: "Andrew Triggs",
                33: "Daniel Mengden",
                39: "Blake Treinen",
                46: "Santiago Casilla",
                35: "Danny Coulombe",
                36: "Yusmeiro Petit",
            },
            "lefties": [55, 30, 35],
            "lineup": [
                [10, "6"],
                [23, "7"],
                [8, "4"],
                [2, "0"],
                [28, "3"],
                [26, "5"],
                [20, "9"],
                [21, "2"],
                [11, "8"],
            ],
            "bench": [
                [13, "1B"],
                [18, "LF"],
                [5, "CF"],
            ],
            "bullpen": [62, 66, 49, 44, 57, 30, 60, 33, 39, 46, 35, 36],
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
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                11: "Rafael Devers",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                39: "Carson Smith",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "3"],
                [28, "7"],
                [2, "6"],
                [36, "4"],
                [23, "0"],
                [11, "5"],
                [3, "2"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [19, "CF"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 39, 41, 31, 61, 37, 24, 46, 56, 32],
        },
        "umpires": {
            "HP": "Ben May",
            "1B": "Mark Wegner",
            "2B": "John Tumpane",
            "3B": "Jim Reynolds",
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

# 1. OAK #10 Marcus Semien (X - X - X)
t1.new_ab()
t1.pitch_list("c b c b")
t1.out("(F)P2")

# 2. OAK #23 Matt Joyce (X - X - X)
t1.new_ab()
t1.pitch_list("f b t f b s")
t1.out("K")

# 3. OAK #8  Jed Lowrie (X - X - X)
t1.new_ab()
t1.pitch_list("s b c f b f b f f f")
t1.out("F7")


# Bot 1st
# Pitching: OAK #55 Sean Manaea
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c c b")
b1.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.out("G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b1.new_ab()
b1.pitch_list("b c f b")
b1.out("G2-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #22 Rick Porcello
t2 = game.new_inning()

# 4. OAK #2  Khris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(2, "26 1B")
t2.advance(3, "20 F9")

# 5. OAK #28 Matt Olson (X - X - 2)
t2.new_ab()
t2.pitch_list("b b f s s")
t2.out("K")

# 6. OAK #26 Matt Chapman (X - X - 2)
t2.new_ab()
t2.pitch_list("b b c f")
t2.hit(1)
t2.thrown_out(2, "21 FC6-4", 3, 22)

# 7. OAK #20 Mark Canha (X - 2 - 26)
t2.new_ab(is_risp=True)
t2.pitch_list("t b b b f")
t2.out("F9")

# 8. OAK #21 Jonathan Lucroy (2 - X - 26)
t2.new_ab(is_risp=True)
t2.pitch_list("b c")
t2.reach("FC6-4")


# Bot 2nd
# Pitching: OAK #55 Sean Manaea
b2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b2.new_ab()
b2.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b2.new_ab()
b2.pitch_list("c b")
b2.out("F9")

# 6. BOS #36 Eduardo Núñez (X - X - 28)
b2.new_ab()
b2.pitch_list("b c")
b2.out("F9")

# 7. BOS #23 Blake Swihart (X - X - 28)
b2.new_ab()
b2.pitch_list("c c f f f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #22 Rick Porcello
t3 = game.new_inning()

# 9. OAK #11 Dustin Fowler (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b c")
t3.out("!K")

# 1. OAK #10 Marcus Semien (X - X - X)
t3.new_ab()
t3.pitch_list("b b f")
t3.out("G5-3")

# 2. OAK #23 Matt Joyce (X - X - X)
t3.new_ab()
t3.pitch_list("b f s b b")
t3.hit(4)

# 3. OAK #8  Jed Lowrie (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F7")


# Bot 3rd
# Pitching: OAK #55 Sean Manaea
b3 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("f f s")
b3.out("K")

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("b f s s")
b3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("f f b b")
b3.hit(1)
b3.advance(2, "16 SB")
b3.advance(3, "16 WP")
b3.advance(4, "16 E5")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab(is_risp=True)
b3.pitch_list("c b b f b f")
b3.wp()
b3.hit(1, rbis=1)
b3.error(5)
b3.advance(2, "E5")
b3.advance("U", "13 1B")

# 3. BOS #13 Hanley Ramirez (X - 16 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("f")
b3.hit(1, rbis=1)

# 4. BOS #28 J.D. Martinez (X - X - 13)
b3.new_ab()
b3.pitch_list("b")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #22 Rick Porcello
t4 = game.new_inning()

# 4. OAK #2  Khris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("G6-3")

# 5. OAK #28 Matt Olson (X - X - X)
t4.new_ab()
t4.hit(1)
t4.advance(2, "26 1B")
t4.advance(4, "21 2B")

# 6. OAK #26 Matt Chapman (X - X - 28)
t4.new_ab()
t4.pitch_list("c b")
t4.hit(1)
t4.advance(4, "21 2B")

# 7. OAK #20 Mark Canha (X - 28 - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("b f c c")
t4.out("!K")

# 8. OAK #21 Jonathan Lucroy (X - 28 - 26)
t4.new_ab(is_risp=True)
t4.pitch_list("c b b f b")
t4.hit(2, rbis=2)
t4.advance(4, "11 3B")

# 9. OAK #11 Dustin Fowler (X - 21 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("f")
t4.hit(3, rbis=1)

# 1. OAK #10 Marcus Semien (11 - X - X)
t4.new_ab(is_risp=True)
t4.pitch_list("d c")
t4.out("G6-3")


# Bot 4th
# Pitching: OAK #55 Sean Manaea
b4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c b c b d")
b4.reach("BB")
b4.advance(2, "36 1B")
b4.advance(3, "23 DP6-4-3")

# 6. BOS #36 Eduardo Núñez (X - X - 2)
b4.new_ab()
b4.pitch_list("1")
b4.hit(1)
b4.thrown_out(2, "23 DP6-4-3", 1, 55)

# 7. BOS #23 Blake Swihart (X - 2 - 36)
b4.new_ab(is_risp=True)
b4.out("DP6-4-3")

# 8. BOS #11 Rafael Devers (2 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("c")
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #22 Rick Porcello
t5 = game.new_inning()

# 2. OAK #23 Matt Joyce (X - X - X)
t5.new_ab()
t5.pitch_list("c b c")
t5.hit(1)
t5.thrown_out(2, "2 DP5-4-3", 2, 22)

# 3. OAK #8  Jed Lowrie (X - X - 23)
t5.new_ab()
t5.pitch_list("t f")
t5.out("L8")

# 4. OAK #2  Khris Davis (X - X - 23)
t5.new_ab()
t5.pitch_list("b 1")
t5.out("DP5-4-3")


# Bot 5th
# Pitching: OAK #55 Sean Manaea
b5 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("c f b")
b5.hit(1)
b5.advance(3, "50 2B")
b5.advance(4, "13 FC6-4-5-6")

# 1. BOS #50 Mookie Betts (X - X - 3)
b5.new_ab()
b5.pitch_list("c f f")
b5.hit(2)
b5.thrown_out(3, "13 FC6-4-5-6", 2, 55)

# 2. BOS #16 Andrew Benintendi (3 - 50 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("d")
b5.out("F9")

# 3. BOS #13 Hanley Ramirez (3 - 50 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.reach("FC6-4-5-6", end_base=2, rbis=1)

# 4. BOS #28 J.D. Martinez (X - 13 - X)
b5.new_ab(is_risp=True)
b5.out("L9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #22 Rick Porcello
t6 = game.new_inning()

# 5. OAK #28 Matt Olson (X - X - X)
t6.new_ab()
t6.pitch_list("b b s b s f")
t6.hit(4)

# 6. OAK #26 Matt Chapman (X - X - X)
t6.new_ab()
t6.pitch_list("b b f f b c")
t6.out("!K")

# 7. OAK #20 Mark Canha (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("G4-3")

# 8. OAK #21 Jonathan Lucroy (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G6-3")


# Bot 6th
# Pitching: OAK #55 Sean Manaea
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("b c c f f")
b6.out("L4")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 7. BOS #23 Blake Swihart (X - X - X)
b6.new_ab()
b6.pitch_list("c f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #22 Rick Porcello
t7.pitching_substitution(37)

# 9. OAK #11 Dustin Fowler (X - X - X)
t7.new_ab()
t7.pitch_list("b c f")
t7.out("G5-3")

# 1. OAK #10 Marcus Semien (X - X - X)
t7.new_ab()
t7.pitch_list("b b s s b")
t7.hit(1)

# 2. OAK #23 Matt Joyce (X - X - 10)
t7.new_ab()
t7.pitch_list("b s 1 b f s")
t7.out("K")

# 3. OAK #8  Jed Lowrie (X - X - 10)
t7.new_ab()
t7.pitch_list("b b c")
t7.out("G3")


# Bot 7th
# Pitching: OAK #55 Sean Manaea
b7 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b f c f")
b7.hit(4)

# 9. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b c b")
b7.error(5)
b7.reach("E5")
b7.advance(2, "13 WP")

# Pitching change (OAK): #36 Yusmeiro Petit replaces #55 Sean Manaea
b7.pitching_substitution(36)

# 1. BOS #50 Mookie Betts (X - X - 3)
b7.new_ab()
b7.pitch_list("b c")
b7.out("F7")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
b7.new_ab()
b7.pitch_list("c b c")
b7.out("L8")

# 3. BOS #13 Hanley Ramirez (X - X - 3)
b7.new_ab(is_risp=True)
b7.pitch_list("b")
b7.wp()
b7.out("(F)F9")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #39 Carson Smith
t8 = game.new_inning()

# Pitching change (BOS): #39 Carson Smith replaces #37 Heath Hembree
t8.pitching_substitution(39)

# 4. OAK #2  Khris Davis (X - X - X)
t8.new_ab()
t8.pitch_list("c b")
t8.hit(4)

# 5. OAK #28 Matt Olson (X - X - X)
t8.new_ab()
t8.out("G5-3")

# 6. OAK #26 Matt Chapman (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("F8")

# 7. OAK #20 Mark Canha (X - X - X)
t8.new_ab()
t8.pitch_list("b c s b")
t8.out("L6")


# Bot 8th
# Pitching: OAK #36 Yusmeiro Petit
b8 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("b c s b")
b8.out("G6-3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.out("G6-3")

# 7. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("L9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #61 Brian Johnson
t9 = game.new_inning()

# Pitching change (BOS): #61 Brian Johnson replaces #39 Carson Smith
t9.pitching_substitution(61)

# 8. OAK #21 Jonathan Lucroy (X - X - X)
t9.new_ab()
t9.pitch_list("b c c b f b")
t9.out("G5-3")

# 9. OAK #11 Dustin Fowler (X - X - X)
t9.new_ab()
t9.pitch_list("f f b")
t9.out("F7")

# 1. OAK #10 Marcus Semien (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b s")
t9.out("K")


# Bot 9th
# Pitching: OAK #39 Blake Treinen
b9 = game.new_inning()

# Pitching change (OAK): #39 Blake Treinen replaces #36 Yusmeiro Petit
b9.pitching_substitution(39)

# 8. BOS #11 Rafael Devers (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G1-3")

# Offensive change (BOS): Pinch-hitter #18 Mitch Moreland replaces #3 Sandy León, batting 9th
b9.offensive_substitution(9, 18, "PH")

# 9. BOS #18 Mitch Moreland (X - X - X)
b9.new_ab()
b9.pitch_list("b f s")
b9.out("F7")

# 1. BOS #50 Mookie Betts (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G6-3")

# Winning team: OAK
# WP: OAK #55 Sean Manaea
game.winning_pitcher(55, is_away_team=True)
# SV: OAK #39 Blake Treinen
game.save_pitcher(39, is_away_team=True)

# Loser team: BOS
# LP: BOS #22 Rick Porcello
game.losing_pitcher(22)

# print(game)
game.generate_scorecard()
