import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ OAK, 2018-04-21
# https://www.baseball-reference.com/boxes/OAK/OAK201804210.shtml
# https://www.mlb.com/gameday/red-sox-vs-athletics/2018/04/21/529706/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-21 21:07-23:23",
        "at": "Oakland Coliseum, Oakland, CA",
        "att": "25,746",
        "temp": "70F, Partly Cloudy",
        "wind": "7mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                18: "Mitch Moreland",
                12: "Brock Holt",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
                [19, "8"],
                [5, "6"],
            ],
            "bench": [
                [18, "1B"],
                [12, "2B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 22, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Oakland Athletics",
            "starter": 55,
            "roster": {
                # Lineup
                10: "Marcus Semien",
                25: "Stephen Piscotty",
                8: "Jed Lowrie",
                2: "Khris Davis",
                26: "Matt Chapman",
                28: "Matt Olson",
                20: "Mark Canha",
                18: "Chad Pinder",
                21: "Jonathan Lucroy",
                # Starting pitcher
                55: "Sean Manaea",
                # Bench
                23: "Matt Joyce",
                13: "Bruce Maxwell",
                5: "Jake Smolinski",
                # Bullpen
                15: "Emilio Pagán",
                66: "Ryan Dull",
                40: "Chris Bassitt",
                49: "Kendall Graveman",
                44: "Chris Hatcher",
                53: "Trevor Cahill",
                52: "Ryan Buchter",
                60: "Andrew Triggs",
                33: "Daniel Mengden",
                39: "Blake Treinen",
                46: "Santiago Casilla",
                36: "Yusmeiro Petit",
            },
            "lefties": [55, 52],
            "lineup": [
                [10, "6"],
                [25, "9"],
                [8, "4"],
                [2, "0"],
                [26, "5"],
                [28, "3"],
                [20, "8"],
                [18, "7"],
                [21, "2"],
            ],
            "bench": [
                [23, "RF"],
                [13, "1B"],
                [5, "CF"],
            ],
            "bullpen": [15, 66, 40, 49, 44, 53, 52, 60, 33, 39, 46, 36],
        },
        "umpires": {
            "HP": "Hunter Wendelstedt",
            "1B": "Adrian Johnson",
            "2B": "Tripp Gibson",
            "3B": "Brian Gorman",
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
# Pitching: OAK #55 Sean Manaea
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b b c s b b")
t1.reach("BB")
t1.thrown_out(2, "16 FC4-6", 1, 55)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t1.new_ab()
t1.pitch_list("b")
t1.reach("FC4-6")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t1.new_ab()
t1.pitch_list("b f s b s")
t1.out("K")

# 4. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab()
t1.pitch_list("c b s s")
t1.out("K")


# Bot 1st
# Pitching: BOS #41 Chris Sale
b1 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
b1.new_ab()
b1.pitch_list("b b f s b f b")
b1.reach("BB")
b1.advance(2, "8 SB")
b1.advance(4, "8 2B")

# 2. OAK #25 Stephen Piscotty (X - X - 10)
b1.new_ab()
b1.pitch_list("b b b c c s")
b1.out("K")

# 3. OAK #8  Jed Lowrie (X - X - 10)
b1.new_ab()
b1.pitch_list("1 b b")
b1.hit(2, rbis=1)

# 4. OAK #2  Khris Davis (X - 8 - X)
b1.new_ab()
b1.pitch_list("c f c")
b1.out("!K")

# 5. OAK #26 Matt Chapman (X - 8 - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: OAK #55 Sean Manaea
t2 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b f c s")
t2.out("K")

# 7. BOS #3  Sandy León (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("P6")


# Bot 2nd
# Pitching: BOS #41 Chris Sale
b2 = game.new_inning()

# 6. OAK #28 Matt Olson (X - X - X)
b2.new_ab()
b2.pitch_list("b b")
b2.out("G3-1")

# 7. OAK #20 Mark Canha (X - X - X)
b2.new_ab()
b2.pitch_list("c b c f")
b2.out("P2")

# 8. OAK #18 Chad Pinder (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: OAK #55 Sean Manaea
t3 = game.new_inning()

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b f s")
t3.out("K")

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t3.new_ab()
t3.pitch_list("c f b b f c")
t3.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c c")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #41 Chris Sale
b3 = game.new_inning()

# 9. OAK #21 Jonathan Lucroy (X - X - X)
b3.new_ab()
b3.pitch_list("c c f s")
b3.out("K")

# 1. OAK #10 Marcus Semien (X - X - X)
b3.new_ab()
b3.pitch_list("c b f f b b")
b3.hit(1)
b3.advance(4, "25 2B")

# 2. OAK #25 Stephen Piscotty (X - X - 10)
b3.new_ab()
b3.pitch_list("s f d")
b3.hit(2, rbis=1)

# 3. OAK #8  Jed Lowrie (X - 25 - X)
b3.new_ab()
b3.pitch_list("c b s s")
b3.out("K")

# 4. OAK #2  Khris Davis (X - 25 - X)
b3.new_ab()
b3.pitch_list("c s b d c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: OAK #55 Sean Manaea
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.pitch_list("c s b")
t4.out("G6-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t4.new_ab()
t4.pitch_list("f f s")
t4.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("f b f f t")
t4.out("KT")


# Bot 4th
# Pitching: BOS #41 Chris Sale
b4 = game.new_inning()

# 5. OAK #26 Matt Chapman (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G2-3")

# 6. OAK #28 Matt Olson (X - X - X)
b4.new_ab()
b4.pitch_list("c b b s f f c")
b4.out("!K")

# 7. OAK #20 Mark Canha (X - X - X)
b4.new_ab()
b4.pitch_list("b b s")
b4.hit(2)

# 8. OAK #18 Chad Pinder (X - 20 - X)
b4.new_ab()
b4.pitch_list("f f s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: OAK #55 Sean Manaea
t5 = game.new_inning()

# 5. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.out("L9")

# 6. BOS #11 Rafael Devers (X - X - X)
t5.new_ab()
t5.out("F7")

# 7. BOS #3  Sandy León (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.error(6)
t5.reach("E6")
t5.advance(2, "19 WP")

# 8. BOS #19 Jackie Bradley Jr. (X - X - 3)
t5.new_ab()
t5.pitch_list("f c b d f b s")
t5.wp()
t5.out("K2-3")


# Bot 5th
# Pitching: BOS #41 Chris Sale
b5 = game.new_inning()

# 9. OAK #21 Jonathan Lucroy (X - X - X)
b5.new_ab()
b5.out("G5-3")

# 1. OAK #10 Marcus Semien (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(4)

# 2. OAK #25 Stephen Piscotty (X - X - X)
b5.new_ab()
b5.pitch_list("b c f s")
b5.out("K")

# 3. OAK #8  Jed Lowrie (X - X - X)
b5.new_ab()
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: OAK #55 Sean Manaea
t6 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("L9")

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G6-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c f")
t6.out("G3")


# Bot 6th
# Pitching: BOS #41 Chris Sale
b6 = game.new_inning()

# 4. OAK #2  Khris Davis (X - X - X)
b6.new_ab()
b6.out("G6-3")

# 5. OAK #26 Matt Chapman (X - X - X)
b6.new_ab()
b6.pitch_list("f b c")
b6.hit(3)

# 6. OAK #28 Matt Olson (26 - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("F8")

# 7. OAK #20 Mark Canha (26 - X - X)
b6.new_ab()
b6.pitch_list("c d f b")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: OAK #55 Sean Manaea
t7 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
t7.new_ab()
t7.pitch_list("b s f f")
t7.out("(F)P3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("f b")
t7.out("G5-3")

# 5. BOS #36 Eduardo Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("c s b")
t7.out("P1")


# Bot 7th
# Pitching: BOS #41 Chris Sale
b7 = game.new_inning()

# 8. OAK #18 Chad Pinder (X - X - X)
b7.new_ab()
b7.pitch_list("b f f f b s")
b7.out("K")

# 9. OAK #21 Jonathan Lucroy (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.out("F9")

# 1. OAK #10 Marcus Semien (X - X - X)
b7.new_ab()
b7.pitch_list("c b s b b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: OAK #55 Sean Manaea
t8 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b c")
t8.out("!K")

# 7. BOS #3  Sandy León (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("P3")

# 8. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b f f s")
t8.out("K")


# Bot 8th
# Pitching: BOS #37 Heath Hembree
b8 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #41 Chris Sale
b8.pitching_substitution(37)

# 2. OAK #25 Stephen Piscotty (X - X - X)
b8.new_ab()
b8.pitch_list("b f b")
b8.out("G1-3")

# 3. OAK #8  Jed Lowrie (X - X - X)
b8.new_ab()
b8.pitch_list("b s")
b8.out("G1-3")

# 4. OAK #2  Khris Davis (X - X - X)
b8.new_ab()
b8.hit(2)

# 5. OAK #26 Matt Chapman (X - 2 - X)
b8.new_ab()
b8.pitch_list("b b b b")
b8.reach("BB")

# 6. OAK #28 Matt Olson (X - 2 - 26)
b8.new_ab()
b8.pitch_list("d b")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: OAK #55 Sean Manaea
t9 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #5 Tzu-Wei Lin, batting 9th
t9.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.out("G6-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t9.new_ab()
t9.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("b s c f b b b")
t9.reach("BB")
t9.thrown_out(2, "13 FC6-4", 3, 55)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t9.new_ab()
t9.pitch_list("d b")
t9.reach("FC6-4")

# Winning team: OAK
# WP: OAK #55 Sean Manaea
game.winning_pitcher(55)

# Loser team: BOS
# LP: BOS #41 Chris Sale
game.losing_pitcher(41, is_away_team=True)

# print(game)
game.generate_scorecard()
