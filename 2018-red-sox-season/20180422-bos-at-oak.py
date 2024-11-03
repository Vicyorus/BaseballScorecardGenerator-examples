import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ OAK, 2018-04-22
# https://www.baseball-reference.com/boxes/OAK/OAK201804220.shtml
# https://www.mlb.com/gameday/red-sox-vs-athletics/2018/04/22/529721/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-04-22 16:07-18:51",
        "at": "Oakland Coliseum, Oakland, CA",
        "att": "29,804",
        "temp": "70F, Cloudy",
        "wind": "9mph, Out To RF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                19: "Jackie Bradley Jr.",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                11: "Rafael Devers",
                23: "Blake Swihart",
                12: "Brock Holt",
                7: "Christian Vázquez",
                5: "Tzu-Wei Lin",
                # Starting pitcher
                24: "David Price",
                # Bench
                36: "Eduardo Núñez",
                50: "Mookie Betts",
                3: "Sandy León",
                13: "Hanley Ramirez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61],
            "lineup": [
                [19, "9"],
                [16, "8"],
                [28, "7"],
                [18, "3"],
                [11, "5"],
                [23, "0"],
                [12, "4"],
                [7, "2"],
                [5, "6"],
            ],
            "bench": [
                [36, "SS"],
                [50, "SS"],
                [3, "C"],
                [13, "SS"],
            ],
            "bullpen": [57, 39, 22, 41, 31, 61, 37, 46, 76, 56, 32],
        },
        "home": {
            "team": "Oakland Athletics",
            "starter": 33,
            "roster": {
                # Lineup
                10: "Marcus Semien",
                25: "Stephen Piscotty",
                8: "Jed Lowrie",
                2: "Khris Davis",
                26: "Matt Chapman",
                20: "Mark Canha",
                18: "Chad Pinder",
                5: "Jake Smolinski",
                13: "Bruce Maxwell",
                # Starting pitcher
                33: "Daniel Mengden",
                # Bench
                28: "Matt Olson",
                23: "Matt Joyce",
                21: "Jonathan Lucroy",
                # Bullpen
                15: "Emilio Pagán",
                55: "Sean Manaea",
                66: "Ryan Dull",
                40: "Chris Bassitt",
                49: "Kendall Graveman",
                44: "Chris Hatcher",
                53: "Trevor Cahill",
                52: "Ryan Buchter",
                60: "Andrew Triggs",
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
                [20, "3"],
                [18, "7"],
                [5, "8"],
                [13, "2"],
            ],
            "bench": [
                [28, "1B"],
                [23, "RF"],
                [21, "C"],
            ],
            "bullpen": [15, 55, 66, 40, 49, 44, 53, 52, 60, 39, 46, 36],
        },
        "umpires": {
            "HP": "Adrian Johnson",
            "1B": "Tripp Gibson",
            "2B": "Brian Gorman",
            "3B": "Hunter Wendelstedt",
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
# Pitching: OAK #33 Daniel Mengden
t1 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("b b s c b")
t1.hit(1)
t1.advance(2, "18 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 19)
t1.new_ab()
t1.pitch_list("1 1 s 1 1 f b")
t1.out("L7")

# 3. BOS #28 J.D. Martinez (X - X - 19)
t1.new_ab()
t1.pitch_list("c c b f f t")
t1.out("KT")

# 4. BOS #18 Mitch Moreland (X - X - 19)
t1.new_ab()
t1.pitch_list("c b f")
t1.hit(1)

# 5. BOS #11 Rafael Devers (X - 19 - 18)
t1.new_ab(is_risp=True)
t1.pitch_list("c f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #24 David Price
b1 = game.new_inning()

# 1. OAK #10 Marcus Semien (X - X - X)
b1.new_ab()
b1.pitch_list("c")
b1.hit(2)
b1.advance(3, "25 G6-3")
b1.advance(4, "2 1B")

# 2. OAK #25 Stephen Piscotty (X - 10 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s")
b1.out("G6-3")

# 3. OAK #8  Jed Lowrie (10 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("b s b f b c")
b1.out("!K")

# 4. OAK #2  Khris Davis (10 - X - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.hit(1, rbis=1)

# 5. OAK #26 Matt Chapman (X - X - 2)
b1.new_ab()
b1.pitch_list("c f")
b1.out("(F)P2")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: OAK #33 Daniel Mengden
t2 = game.new_inning()

# 6. BOS #23 Blake Swihart (X - X - X)
t2.new_ab()
t2.pitch_list("f f f f b f b b c")
t2.out("!K")

# 7. BOS #12 Brock Holt (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G5-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t2.new_ab()
t2.pitch_list("f f f f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #24 David Price
b2 = game.new_inning()

# 6. OAK #20 Mark Canha (X - X - X)
b2.new_ab()
b2.pitch_list("b c f b f")
b2.hit(1)
b2.thrown_out(2, "5 DP5-4-3", 2, 24)

# 7. OAK #18 Chad Pinder (X - X - 20)
b2.new_ab()
b2.pitch_list("c c c")
b2.out("!K")

# 8. OAK #5  Jake Smolinski (X - X - 20)
b2.new_ab()
b2.out("DP5-4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: OAK #33 Daniel Mengden
t3 = game.new_inning()

# 9. BOS #5  Tzu-Wei Lin (X - X - X)
t3.new_ab()
t3.pitch_list("c b f f")
t3.out("L6")

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("b f b")
t3.out("F8")


# Bot 3rd
# Pitching: BOS #24 David Price
b3 = game.new_inning()

# 9. OAK #13 Bruce Maxwell (X - X - X)
b3.new_ab()
b3.out("G6-3")

# 1. OAK #10 Marcus Semien (X - X - X)
b3.new_ab()
b3.pitch_list("c f")
b3.out("L9")

# 2. OAK #25 Stephen Piscotty (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("L4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: OAK #33 Daniel Mengden
t4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("b s s f c")
t4.out("!K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("L8")

# 5. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.pitch_list("c s f")
t4.out("L7")


# Bot 4th
# Pitching: BOS #24 David Price
b4 = game.new_inning()

# 3. OAK #8  Jed Lowrie (X - X - X)
b4.new_ab()
b4.pitch_list("b f b c b s")
b4.out("K")

# 4. OAK #2  Khris Davis (X - X - X)
b4.new_ab()
b4.pitch_list("s b")
b4.out("P3")

# 5. OAK #26 Matt Chapman (X - X - X)
b4.new_ab()
b4.pitch_list("b b c f f f b b")
b4.reach("BB")
b4.thrown_out(2, "20 FC6-4", 3, 24)

# 6. OAK #20 Mark Canha (X - X - 26)
b4.new_ab()
b4.reach("FC6-4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: OAK #33 Daniel Mengden
t5 = game.new_inning()

# 6. BOS #23 Blake Swihart (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("L7")

# 7. BOS #12 Brock Holt (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("b b c b")
t5.hit(2)

# 9. BOS #5  Tzu-Wei Lin (X - 7 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b d c d s f")
t5.out("(F)P2")


# Bot 5th
# Pitching: BOS #24 David Price
b5 = game.new_inning()

# 7. OAK #18 Chad Pinder (X - X - X)
b5.new_ab()
b5.pitch_list("s b f b t")
b5.out("KT")

# 8. OAK #5  Jake Smolinski (X - X - X)
b5.new_ab()
b5.pitch_list("b")
b5.hit(2)

# 9. OAK #13 Bruce Maxwell (X - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b f f")
b5.out("F7")

# 1. OAK #10 Marcus Semien (X - 5 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("f b")
b5.out("L9")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: OAK #33 Daniel Mengden
t6 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("f")
t6.out("F9")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("G3-1")

# 3. BOS #28 J.D. Martinez (X - X - X)
t6.new_ab()
t6.pitch_list("s b")
t6.out("G6-3")


# Bot 6th
# Pitching: BOS #24 David Price
b6 = game.new_inning()

# 2. OAK #25 Stephen Piscotty (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(1)
b6.thrown_out(2, "8 DP4-6-3", 1, 24)

# 3. OAK #8  Jed Lowrie (X - X - 25)
b6.new_ab()
b6.out("DP4-6-3")

# 4. OAK #2  Khris Davis (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: OAK #33 Daniel Mengden
t7 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t7.new_ab()
t7.pitch_list("f c b")
t7.hit(1)
t7.advance(2, "11 1B")
t7.thrown_out(3, "23 FC2-5", 1, 33)

# 5. BOS #11 Rafael Devers (X - X - 18)
t7.new_ab()
t7.pitch_list("d d c s b")
t7.hit(1)
t7.advance(2, "23 FC2-5")
t7.advance(4, "12 2B")

# 6. BOS #23 Blake Swihart (X - 18 - 11)
t7.new_ab(is_risp=True)
t7.pitch_list("c")
t7.reach("FC2-5")
t7.advance(3, "12 2B")

# 7. BOS #12 Brock Holt (X - 11 - 23)
t7.new_ab(is_risp=True)
t7.pitch_list("b b f b f")
t7.hit(2, rbis=1)

# Pitching change (OAK): #36 Yusmeiro Petit replaces #33 Daniel Mengden
t7.pitching_substitution(36)

# 8. BOS #7  Christian Vázquez (23 - 12 - X)
t7.new_ab(is_risp=True)
t7.out("(F)P3")

# 9. BOS #5  Tzu-Wei Lin (23 - 12 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("c c s")
t7.out("K")


# Bot 7th
# Pitching: BOS #24 David Price
b7 = game.new_inning()

# 5. OAK #26 Matt Chapman (X - X - X)
b7.new_ab()
b7.pitch_list("b f b c c")
b7.out("!K")

# 6. OAK #20 Mark Canha (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F9")

# 7. OAK #18 Chad Pinder (X - X - X)
b7.new_ab()
b7.pitch_list("f")
b7.hit(1)
b7.thrown_out(2, "5 FC6-4", 3, 24)

# 8. OAK #5  Jake Smolinski (X - X - 18)
b7.new_ab()
b7.pitch_list("c")
b7.reach("FC6-4")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: OAK #52 Ryan Buchter
t8 = game.new_inning()

# Pitching change (OAK): #52 Ryan Buchter replaces #36 Yusmeiro Petit
t8.pitching_substitution(52)

# Defensive switch (OAK): #20 Mark Canha moves to LF
t8.defensive_switch(20, "7")

# Defensive change (OAK): #28 Matt Olson replaces #18 Chad Pinder (LF), playing 1B, batting 7th
t8.defensive_substitution(7, 28, "3")

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t8.new_ab()
t8.pitch_list("b f s f b s")
t8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b b s f b b")
t8.reach("BB")
t8.advance(2, "18 SB")

# Pitching change (OAK): #39 Blake Treinen replaces #52 Ryan Buchter
t8.pitching_substitution(39)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t8.new_ab()
t8.pitch_list("s s f b f 1 s")
t8.out("K")

# 4. BOS #18 Mitch Moreland (X - X - 16)
t8.new_ab(is_risp=True)
t8.pitch_list("1 s 1 t s")
t8.out("K")


# Bot 8th
# Pitching: BOS #24 David Price
b8 = game.new_inning()

# 9. OAK #13 Bruce Maxwell (X - X - X)
b8.new_ab()
b8.pitch_list("b b f")
b8.out("G5-3")

# 1. OAK #10 Marcus Semien (X - X - X)
b8.new_ab()
b8.pitch_list("s")
b8.hit(1)
b8.advance(2, "25 1B")
b8.advance(4, "2 HR")

# 2. OAK #25 Stephen Piscotty (X - X - 10)
b8.new_ab()
b8.pitch_list("s b")
b8.hit(1)
b8.advance(4, "2 HR")

# 3. OAK #8  Jed Lowrie (X - 10 - 25)
b8.new_ab(is_risp=True)
b8.pitch_list("b f b f s")
b8.out("K")

# 4. OAK #2  Khris Davis (X - 10 - 25)
b8.new_ab(is_risp=True)
b8.hit(4, rbis=3)

# Pitching change (BOS): #39 Carson Smith replaces #24 David Price
b8.pitching_substitution(39)

# 5. OAK #26 Matt Chapman (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("(F)F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: OAK #39 Blake Treinen
t9 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
t9.new_ab()
t9.pitch_list("c f s")
t9.out("K")

# 6. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("G1-3")

# 7. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c")
t9.error(6)
t9.reach("E6")
t9.advance(2, "7 DI")

# 8. BOS #7  Christian Vázquez (X - X - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("c s d b b f f")
t9.out("P3")

# Winning team: OAK
# WP: OAK #39 Blake Treinen
game.winning_pitcher(39)

# Loser team: BOS
# LP: BOS #24 David Price
game.losing_pitcher(24, is_away_team=True)

# print(game)
game.generate_scorecard()
