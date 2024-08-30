import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ OAK, 2018-04-20
# https://www.baseball-reference.com/boxes/OAK/OAK201804200.shtml
# https://www.mlb.com/gameday/red-sox-vs-athletics/2018/04/20/529691/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-20 22:07-01:23 +1",
        "at": "Oakland Coliseum, Oakland, CA",
        "att": "23,473",
        "temp": "60F, Clear",
        "wind": "13mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                12: "Brock Holt",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                5: "Tzu-Wei Lin",
                28: "J.D. Martinez",
                23: "Blake Swihart",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
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
            "lefties": [31, 57, 41, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "0"],
                [18, "3"],
                [11, "5"],
                [36, "4"],
                [19, "8"],
                [7, "2"],
                [12, "6"],
            ],
            "bench": [
                [5, "OF"],
                [28, "DH"],
                [23, "C"],
                [3, "C"],
            ],
            "bullpen": [57, 39, 22, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "Oakland Athletics",
            "starter": 49,
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
                49: "Kendall Graveman",
                # Bench
                23: "Matt Joyce",
                13: "Bruce Maxwell",
                5: "Jake Smolinski",
                # Bullpen
                15: "Emilio Pagán",
                55: "Sean Manaea",
                66: "Ryan Dull",
                54: "Josh Lucas",
                40: "Chris Bassitt",
                44: "Chris Hatcher",
                53: "Trevor Cahill",
                52: "Ryan Buchter",
                60: "Andrew Triggs",
                33: "Daniel Mengden",
                39: "Blake Treinen",
                46: "Santiago Casilla",
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
            "bullpen": [15, 55, 66, 54, 40, 44, 53, 52, 60, 33, 39, 46],
        },
        "umpires": {
            "HP": "Brian Gorman",
            "1B": "Hunter Wendelstedt",
            "2B": "Adrian Johnson",
            "3B": "Tripp Gibson",
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
# Pitching: OAK #49 Kendall Graveman
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("c b s")
t1.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b c b s f f b s")
t1.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "18 CS", 3, 49)

# 4. BOS #18 Mitch Moreland (X - X - 13)
t1.new_ab()
t1.pitch_list("b")
t1.no_ab("CS")


# Bot 1st
# Pitching: BOS #31 Drew Pomeranz
b1 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("G3")

# 2. OAK #25 Stephen Piscotty (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c f f b")
b1.reach("BB")
b1.advance(4, "8 2B")

# 3. OAK #8  Jed Lowrie (X - X - 25)
b1.new_ab()
b1.pitch_list("c 1 b")
b1.hit(2, rbis=1)
b1.advance(3, "26 WP")
b1.advance(4, "28 1B")

# 4. OAK #2  Khris Davis (X - 8 - X)
b1.new_ab()
b1.pitch_list("c b b f f s")
b1.out("K")

# 5. OAK #26 Matt Chapman (X - 8 - X)
b1.new_ab()
b1.pitch_list("c d f b s")
b1.wp()
b1.reach("K")
b1.advance(2, "28 1B")
b1.advance(4, "20 1B")

# 6. OAK #28 Matt Olson (8 - X - 26)
b1.new_ab()
b1.pitch_list("f c")
b1.hit(1, rbis=1)
b1.advance(3, "20 1B")

# 7. OAK #20 Mark Canha (X - 26 - 28)
b1.new_ab()
b1.pitch_list("c f f b f d")
b1.hit(1, rbis=1)
b1.advance(2, "18 WP")

# 8. OAK #18 Chad Pinder (28 - X - 20)
b1.new_ab()
b1.pitch_list("b c f f b b f f c")
b1.wp()
b1.out("!K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: OAK #49 Kendall Graveman
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b c s")
t2.out("K")

# 5. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.hit(1)
t2.advance(2, "36 1B")
t2.advance(4, "19 HR")

# 6. BOS #36 Eduardo Núñez (X - X - 11)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(4, "19 HR")

# 7. BOS #19 Jackie Bradley Jr. (X - 11 - 36)
t2.new_ab()
t2.pitch_list("b s f d")
t2.hit(4, rbis=3)

# 8. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("c b c")
t2.out("G3")

# 9. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("b c c f b")
t2.out("G6-3")


# Bot 2nd
# Pitching: BOS #31 Drew Pomeranz
b2 = game.new_inning()

# 9. OAK #21 Jonathan Lucroy (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("F9")

# 1. OAK #10 Marcus Semien (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f f b")
b2.reach("BB")
b2.advance(2, "8 1B")

# 2. OAK #25 Stephen Piscotty (X - X - 10)
b2.new_ab()
b2.pitch_list("b")
b2.out("F7")

# 3. OAK #8  Jed Lowrie (X - X - 10)
b2.new_ab()
b2.pitch_list("1 c b")
b2.hit(1)

# 4. OAK #2  Khris Davis (X - 10 - 8)
b2.new_ab()
b2.pitch_list("b s f b b t")
b2.out("KT")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: OAK #49 Kendall Graveman
t3 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("L5")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("f b b f b f s")
t3.out("K")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t3.new_ab()
t3.pitch_list("b f b f s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #31 Drew Pomeranz
b3 = game.new_inning()

# 5. OAK #26 Matt Chapman (X - X - X)
b3.new_ab()
b3.pitch_list("c f c")
b3.out("!K")

# 6. OAK #28 Matt Olson (X - X - X)
b3.new_ab()
b3.pitch_list("c f b b s")
b3.out("K")

# 7. OAK #20 Mark Canha (X - X - X)
b3.new_ab()
b3.pitch_list("c b c c")
b3.out("!K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: OAK #49 Kendall Graveman
t4 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b f c")
t4.out("G6-3")

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("L7")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b c f s")
t4.out("K")


# Bot 4th
# Pitching: BOS #31 Drew Pomeranz
b4 = game.new_inning()

# 8. OAK #18 Chad Pinder (X - X - X)
b4.new_ab()
b4.pitch_list("f b b f")
b4.hit(2)

# 9. OAK #21 Jonathan Lucroy (X - 18 - X)
b4.new_ab()
b4.pitch_list("c 2")
b4.out("F8")

# 1. OAK #10 Marcus Semien (X - 18 - X)
b4.new_ab()
b4.pitch_list("c b f")
b4.out("L7")

# Pitching change (BOS): #76 Hector Velázquez replaces #31 Drew Pomeranz
b4.pitching_substitution(76)

# 2. OAK #25 Stephen Piscotty (X - 18 - X)
b4.new_ab()
b4.pitch_list("b c")
b4.out("L6")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: OAK #49 Kendall Graveman
t5 = game.new_inning()

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("c b c")
t5.out("G3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("f b c b s")
t5.out("K")

# 9. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("G1-3")


# Bot 5th
# Pitching: BOS #76 Hector Velázquez
b5 = game.new_inning()

# 3. OAK #8  Jed Lowrie (X - X - X)
b5.new_ab()
b5.pitch_list("f b f")
b5.hit(1)
b5.thrown_out(2, "2 DP5-4-3", 1, 76)

# 4. OAK #2  Khris Davis (X - X - 8)
b5.new_ab()
b5.out("DP5-4-3")

# 5. OAK #26 Matt Chapman (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f")
b5.hit(1)

# 6. OAK #28 Matt Olson (X - X - 26)
b5.new_ab()
b5.pitch_list("b 1 b 1 b c")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: OAK #49 Kendall Graveman
t6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t6.new_ab()
t6.pitch_list("c b c f")
t6.hit(1)
t6.advance(2, "16 1B")
t6.advance(3, "13 1B")
t6.advance(4, "18 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t6.new_ab()
t6.pitch_list("1 c d s b 1")
t6.hit(1)
t6.advance(2, "13 1B")
t6.advance(4, "18 HR")

# 3. BOS #13 Hanley Ramirez (X - 50 - 16)
t6.new_ab()
t6.pitch_list("b b c c b")
t6.hit(1)
t6.advance(4, "18 HR")

# Pitching change (OAK): #15 Emilio Pagán replaces #49 Kendall Graveman
t6.pitching_substitution(15)

# 4. BOS #18 Mitch Moreland (50 - 16 - 13)
t6.new_ab()
t6.hit(4, rbis=4)

# 5. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("s s")
t6.out("L9")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t6.new_ab()
t6.pitch_list("b f")
t6.hit(2)

# 7. BOS #19 Jackie Bradley Jr. (X - 36 - X)
t6.new_ab()
t6.pitch_list("b s s b")
t6.out("F7")

# 8. BOS #7  Christian Vázquez (X - 36 - X)
t6.new_ab()
t6.pitch_list("s")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #76 Hector Velázquez
b6 = game.new_inning()

# 7. OAK #20 Mark Canha (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.out("L8")

# 8. OAK #18 Chad Pinder (X - X - X)
b6.new_ab()
b6.out("G6-3")

# 9. OAK #21 Jonathan Lucroy (X - X - X)
b6.new_ab()
b6.pitch_list("c b b b")
b6.hit(1)

# 1. OAK #10 Marcus Semien (X - X - 21)
b6.new_ab()
b6.pitch_list("b b f f f")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: OAK #54 Josh Lucas
t7 = game.new_inning()

# Pitching change (OAK): #54 Josh Lucas replaces #15 Emilio Pagán
t7.pitching_substitution(54)

# 9. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.hit(1)
t7.thrown_out(2, "50 DP6-4-3", 1, 54)

# 1. BOS #50 Mookie Betts (X - X - 12)
t7.new_ab()
t7.pitch_list("1 s")
t7.out("DP6-4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.out("F7")


# Bot 7th
# Pitching: BOS #76 Hector Velázquez
b7 = game.new_inning()

# 2. OAK #25 Stephen Piscotty (X - X - X)
b7.new_ab()
b7.out("G5-3")

# 3. OAK #8  Jed Lowrie (X - X - X)
b7.new_ab()
b7.pitch_list("b b c f b f f")
b7.hit(2)
b7.advance(3, "28 1B")

# 4. OAK #2  Khris Davis (X - 8 - X)
b7.new_ab()
b7.pitch_list("b")
b7.reach("HBP")
b7.advance(2, "28 1B")

# 5. OAK #26 Matt Chapman (X - 8 - 2)
b7.new_ab()
b7.pitch_list("c f t")
b7.out("KT")

# Pitching change (BOS): #61 Brian Johnson replaces #76 Hector Velázquez
b7.pitching_substitution(61)

# 6. OAK #28 Matt Olson (X - 8 - 2)
b7.new_ab()
b7.pitch_list("c b")
b7.hit(1)

# Pitching change (BOS): #32 Matt Barnes replaces #61 Brian Johnson
b7.pitching_substitution(32)

# Offensive change (OAK): Pinch-hitter #23 Matt Joyce replaces #20 Mark Canha, batting 7th
b7.offensive_substitution(7, 23, "PH")

# 7. OAK #23 Matt Joyce (8 - 2 - 28)
b7.new_ab()
b7.pitch_list("c b d c d f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: OAK #54 Josh Lucas
t8 = game.new_inning()

# Defensive switch (OAK): #23 Matt Joyce moves to CF
t8.defensive_switch(23, "8")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t8.new_ab()
t8.out("P6")

# 4. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")

# 5. BOS #11 Rafael Devers (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# 8. OAK #18 Chad Pinder (X - X - X)
b8.new_ab()
b8.pitch_list("f s b b c")
b8.out("!K")

# 9. OAK #21 Jonathan Lucroy (X - X - X)
b8.new_ab()
b8.pitch_list("b c b f")
b8.out("G5-3")

# 1. OAK #10 Marcus Semien (X - X - X)
b8.new_ab()
b8.pitch_list("c f f")
b8.out("G3-1")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: OAK #54 Josh Lucas
t9 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("c b")
t9.hit(1)
t9.advance(2, "19 BB")
t9.advance(3, "7 DP5-4-3")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 36)
t9.new_ab()
t9.pitch_list("b b f f f d 1 b")
t9.reach("BB")
t9.thrown_out(2, "7 DP5-4-3", 1, 54)

# 8. BOS #7  Christian Vázquez (X - 36 - 19)
t9.new_ab()
t9.pitch_list("m")
t9.out("DP5-4-3")

# 9. BOS #12 Brock Holt (36 - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.out("G5-3")


# Bot 9th
# Pitching: BOS #56 Joe Kelly
b9 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #32 Matt Barnes
b9.pitching_substitution(56)

# 2. OAK #25 Stephen Piscotty (X - X - X)
b9.new_ab()
b9.pitch_list("b c s")
b9.out("G4-3")

# 3. OAK #8  Jed Lowrie (X - X - X)
b9.new_ab()
b9.pitch_list("c s")
b9.out("F8")

# 4. OAK #2  Khris Davis (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #76 Hector Velázquez
game.winning_pitcher(76, is_away_team=True)

# Loser team: OAK
# LP: OAK #49 Kendall Graveman
game.losing_pitcher(49)

# print(game)
game.generate_scorecard()
