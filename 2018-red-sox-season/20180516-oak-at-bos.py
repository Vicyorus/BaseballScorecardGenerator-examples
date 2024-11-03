import os
from baseball_scorecard.baseball_scorecard import Scorecard

# OAK @ BOS, 2018-05-16
# https://www.baseball-reference.com/boxes/BOS/BOS201805160.shtml
# https://www.mlb.com/gameday/athletics-vs-red-sox/2018/05/16/530047/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-16 19:11-22:19",
        "at": "Fenway Park, Boston, MA",
        "att": "34,947",
        "temp": "51F, Partly Cloudy",
        "wind": "9mph, In From RF",
        "away": {
            "team": "Oakland Athletics",
            "starter": 53,
            "roster": {
                # Lineup
                10: "Marcus Semien",
                20: "Mark Canha",
                8: "Jed Lowrie",
                2: "Khris Davis",
                26: "Matt Chapman",
                28: "Matt Olson",
                25: "Stephen Piscotty",
                18: "Chad Pinder",
                21: "Jonathan Lucroy",
                # Starting pitcher
                53: "Trevor Cahill",
                # Bench
                11: "Dustin Fowler",
                23: "Matt Joyce",
                13: "Bruce Maxwell",
                # Bullpen
                62: "Lou Trivino",
                55: "Sean Manaea",
                66: "Ryan Dull",
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
                [20, "8"],
                [8, "4"],
                [2, "0"],
                [26, "5"],
                [28, "3"],
                [25, "9"],
                [18, "7"],
                [21, "2"],
            ],
            "bench": [
                [11, "CF"],
                [23, "RF"],
                [13, "1B"],
            ],
            "bullpen": [62, 55, 66, 44, 57, 30, 60, 33, 39, 46, 35, 36],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                7: "Christian Vázquez",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 66, 24],
            "lineup": [
                [50, "9"],
                [16, "8"],
                [13, "0"],
                [28, "7"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [7, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 22, 31, 61, 66, 37, 24, 46, 56, 32],
        },
        "umpires": {
            "HP": "John Tumpane",
            "1B": "Jim Reynolds",
            "2B": "Ben May",
            "3B": "Mark Wegner",
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
# Pitching: BOS #41 Chris Sale
t1 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
t1.new_ab()
t1.hit(1)
t1.advance(2, "8 BB")

# 2. OAK #20 Mark Canha (X - X - 10)
t1.new_ab()
t1.pitch_list("c f b 1 b s")
t1.out("K")

# 3. OAK #8  Jed Lowrie (X - X - 10)
t1.new_ab()
t1.pitch_list("b 1 b b c b")
t1.reach("BB")

# 4. OAK #2  Khris Davis (X - 10 - 8)
t1.new_ab(is_risp=True)
t1.pitch_list("c s b b s")
t1.out("K")

# 5. OAK #26 Matt Chapman (X - 10 - 8)
t1.new_ab(is_risp=True)
t1.pitch_list("b b b c s s")
t1.out("K")


# Bot 1st
# Pitching: OAK #53 Trevor Cahill
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b c b f f")
b1.hit(1)
b1.error(7)
b1.advance(2, "E7")
b1.advance(3, "16 1B")
b1.advance(4, "13 G6-3")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "13 G6-3")
b1.advance(4, "28 HR")

# 3. BOS #13 Hanley Ramirez (50 - X - 16)
b1.new_ab(is_risp=True)
b1.pitch_list("b s d c 1 b f 1")
b1.out("G6-3", rbis=1)

# 4. BOS #28 J.D. Martinez (X - 16 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b c d")
b1.hit(4, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c f b b b f")
b1.out("G6-3")

# 6. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("b c c b b d")
b1.reach("BB")

# 7. BOS #36 Eduardo Núñez (X - X - 18)
b1.new_ab()
b1.pitch_list("c b")
b1.out("L3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 6. OAK #28 Matt Olson (X - X - X)
t2.new_ab()
t2.pitch_list("b b t c s")
t2.out("K")

# 7. OAK #25 Stephen Piscotty (X - X - X)
t2.new_ab()
t2.out("P4")

# 8. OAK #18 Chad Pinder (X - X - X)
t2.new_ab()
t2.pitch_list("b b b b")
t2.reach("BB")

# 9. OAK #21 Jonathan Lucroy (X - X - 18)
t2.new_ab()
t2.pitch_list("c f f f b s")
t2.out("K")


# Bot 2nd
# Pitching: OAK #53 Trevor Cahill
b2 = game.new_inning()

# 8. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("f s")
b2.out("G4-3")

# 9. BOS #7  Christian Vázquez (X - X - X)
b2.new_ab()
b2.pitch_list("b c b f f")
b2.out("G1-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("b c b b")
b2.hit(1)
b2.thrown_out(2, "16 CS", 3, 53)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b2.new_ab()
b2.pitch_list("p")
b2.no_ab("CS")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b f")
t3.out("F8")

# 2. OAK #20 Mark Canha (X - X - X)
t3.new_ab()
t3.pitch_list("b b f")
t3.out("F8")

# 3. OAK #8  Jed Lowrie (X - X - X)
t3.new_ab()
t3.pitch_list("f b b b c f s")
t3.out("K")


# Bot 3rd
# Pitching: OAK #53 Trevor Cahill
b3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(1)
b3.advance(2, "13 G6-3")
b3.advance(3, "28 G4-3")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
b3.new_ab()
b3.pitch_list("f 1")
b3.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("b f s")
b3.out("G4-3")

# 5. BOS #2  Xander Bogaerts (16 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("s d")
b3.out("L7")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 4. OAK #2  Khris Davis (X - X - X)
t4.new_ab()
t4.pitch_list("b b f c f b f f f f b")
t4.reach("BB")
t4.advance(2, "26 PB")

# 5. OAK #26 Matt Chapman (X - X - 2)
t4.new_ab(is_risp=True)
t4.pitch_list("b f b s s")
t4.pb()
t4.out("K")

# 6. OAK #28 Matt Olson (X - 2 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c b c f b f")
t4.out("F7")

# 7. OAK #25 Stephen Piscotty (X - 2 - X)
t4.new_ab(is_risp=True)
t4.out("F8")


# Bot 4th
# Pitching: OAK #53 Trevor Cahill
b4 = game.new_inning()

# 6. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("s b b s f f b f s")
b4.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")

# 8. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 8. OAK #18 Chad Pinder (X - X - X)
t5.new_ab()
t5.pitch_list("b c f b b b")
t5.reach("BB")
t5.advance(4, "10 HR")

# 9. OAK #21 Jonathan Lucroy (X - X - 18)
t5.new_ab()
t5.pitch_list("f b f b c")
t5.out("!K")

# 1. OAK #10 Marcus Semien (X - X - 18)
t5.new_ab()
t5.pitch_list("c b")
t5.hit(4, rbis=2)

# 2. OAK #20 Mark Canha (X - X - X)
t5.new_ab()
t5.pitch_list("c s f f s")
t5.out("K")

# 3. OAK #8  Jed Lowrie (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("F9")


# Bot 5th
# Pitching: OAK #53 Trevor Cahill
b5 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("c s b b f b")
b5.out("G1-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #32 Matt Barnes
t6 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #41 Chris Sale
t6.pitching_substitution(32)

# 4. OAK #2  Khris Davis (X - X - X)
t6.new_ab()
t6.out("P3")

# 5. OAK #26 Matt Chapman (X - X - X)
t6.new_ab()
t6.pitch_list("c b b c t")
t6.out("KT")

# 6. OAK #28 Matt Olson (X - X - X)
t6.new_ab()
t6.pitch_list("b b c b")
t6.hit(1)

# 7. OAK #25 Stephen Piscotty (X - X - 28)
t6.new_ab()
t6.pitch_list("s 1 b f f s")
t6.out("K")


# Bot 6th
# Pitching: OAK #66 Ryan Dull
b6 = game.new_inning()

# Pitching change (OAK): #66 Ryan Dull replaces #53 Trevor Cahill
b6.pitching_substitution(66)

# 3. BOS #13 Hanley Ramirez (X - X - X)
b6.new_ab()
b6.pitch_list("s t b b")
b6.hit(1)
b6.advance(2, "28 BB")
b6.advance(4, "2 HR")

# 4. BOS #28 J.D. Martinez (X - X - 13)
b6.new_ab()
b6.pitch_list("1 c b b f b b")
b6.reach("BB")
b6.advance(4, "2 HR")

# 5. BOS #2  Xander Bogaerts (X - 13 - 28)
b6.new_ab(is_risp=True)
b6.pitch_list("c d")
b6.hit(4, rbis=3)

# 6. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b c s f b s")
b6.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("b b f f")
b6.hit(1)
b6.advance(2, "7 1B")

# 8. BOS #11 Rafael Devers (X - X - 36)
b6.new_ab()
b6.pitch_list("b")
b6.out("F8")

# 9. BOS #7  Christian Vázquez (X - X - 36)
b6.new_ab()
b6.pitch_list("b b f")
b6.hit(1)

# 1. BOS #50 Mookie Betts (X - 36 - 7)
b6.new_ab(is_risp=True)
b6.pitch_list("b f")
b6.out("(F)F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #37 Heath Hembree
t7 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #32 Matt Barnes
t7.pitching_substitution(37)

# Offensive change (OAK): Pinch-hitter #23 Matt Joyce replaces #18 Chad Pinder, batting 8th
t7.offensive_substitution(8, 23, "PH")

# 8. OAK #23 Matt Joyce (X - X - X)
t7.new_ab()
t7.pitch_list("s f b b b")
t7.hit(4)

# 9. OAK #21 Jonathan Lucroy (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("F9")

# 1. OAK #10 Marcus Semien (X - X - X)
t7.new_ab()
t7.pitch_list("f b b s f b s")
t7.out("K")

# 2. OAK #20 Mark Canha (X - X - X)
t7.new_ab()
t7.pitch_list("b b f f")
t7.out("F9")


# Bot 7th
# Pitching: OAK #44 Chris Hatcher
b7 = game.new_inning()

# Pitching change (OAK): #44 Chris Hatcher replaces #66 Ryan Dull
b7.pitching_substitution(44)

# Defensive switch (OAK): #23 Matt Joyce moves to LF
b7.defensive_switch(23, "7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c s b s")
b7.out("K2-3")

# 3. BOS #13 Hanley Ramirez (X - X - X)
b7.new_ab()
b7.pitch_list("b f c f")
b7.out("F9")

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t8.pitching_substitution(56)

# 3. OAK #8  Jed Lowrie (X - X - X)
t8.new_ab()
t8.pitch_list("b c b f b b")
t8.reach("BB")
t8.thrown_out(2, "2 FC6-4", 1, 56)

# 4. OAK #2  Khris Davis (X - X - 8)
t8.new_ab()
t8.pitch_list("c")
t8.reach("FC6-4")
t8.thrown_out(2, "26 DP6-4-3", 2, 56)

# 5. OAK #26 Matt Chapman (X - X - 2)
t8.new_ab()
t8.pitch_list("f c f")
t8.out("DP6-4-3")


# Bot 8th
# Pitching: OAK #35 Danny Coulombe
b8 = game.new_inning()

# Pitching change (OAK): #35 Danny Coulombe replaces #44 Chris Hatcher
b8.pitching_substitution(35)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c b f b f f s")
b8.out("K")

# 6. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("c b f s")
b8.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b8.new_ab()
b8.pitch_list("b f c f c")
b8.out("!K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
t9.pitching_substitution(46)

# 6. OAK #28 Matt Olson (X - X - X)
t9.new_ab()
t9.pitch_list("f b b s f")
t9.hit(4)

# 7. OAK #25 Stephen Piscotty (X - X - X)
t9.new_ab()
t9.pitch_list("c c s")
t9.out("K")

# 8. OAK #23 Matt Joyce (X - X - X)
t9.new_ab()
t9.pitch_list("b s")
t9.out("G4-3")

# 9. OAK #21 Jonathan Lucroy (X - X - X)
t9.new_ab()
t9.pitch_list("c b f f f f")
t9.out("F9")

# Winning team: BOS
# WP: BOS #41 Chris Sale
game.winning_pitcher(41)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: OAK
# LP: OAK #53 Trevor Cahill
game.losing_pitcher(53, is_away_team=True)

# print(game)
game.generate_scorecard()
