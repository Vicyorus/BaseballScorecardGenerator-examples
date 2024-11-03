import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-05-17
# https://www.baseball-reference.com/boxes/BOS/BOS201805170.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/05/17/529642/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-17 19:11-21:55",
        "at": "Fenway Park, Boston, MA",
        "att": "36,615",
        "temp": "68F, Partly Cloudy",
        "wind": "7mph, R To L",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 34,
            "roster": {
                # Lineup
                16: "Trey Mancini",
                10: "Adam Jones",
                13: "Manny Machado",
                6: "Jonathan Schoop",
                19: "Chris Davis",
                45: "Mark Trumbo",
                2: "Danny Valencia",
                23: "Joey Rickard",
                27: "Andrew Susac",
                # Starting pitcher
                34: "Kevin Gausman",
                # Bench
                29: "Jace Peterson",
                24: "Pedro Alvarez",
                15: "Chance Sisco",
                14: "Craig Gentry",
                # Bullpen
                17: "Alex Cobb",
                48: "Richard Bleier",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                60: "Mychal Givens",
                37: "Dylan Bundy",
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
                [45, "0"],
                [2, "5"],
                [23, "9"],
                [27, "2"],
            ],
            "bench": [
                [29, "SS"],
                [24, "3B"],
                [15, "C"],
                [14, "CF"],
            ],
            "bullpen": [17, 48, 66, 54, 60, 37, 57, 43, 38, 50, 35],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [24, 57, 41, 31, 61, 66],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [13, "3"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [18, "1B"],
                [23, "C"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 22, 41, 31, 61, 66, 37, 46, 56, 32],
        },
        "umpires": {
            "HP": "Tony Randazzo",
            "1B": "Lance Barrett",
            "2B": "Bill Welke",
            "3B": "Nic Lentz",
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
# Pitching: BOS #24 David Price
t1 = game.new_inning()

# 1. BAL #16 Trey Mancini (X - X - X)
t1.new_ab()
t1.pitch_list("b f f b b f s")
t1.out("K")

# 2. BAL #10 Adam Jones (X - X - X)
t1.new_ab()
t1.out("F9")

# 3. BAL #13 Manny Machado (X - X - X)
t1.new_ab()
t1.pitch_list("c c c")
t1.out("!K")


# Bot 1st
# Pitching: BAL #34 Kevin Gausman
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(1)
b1.advance(2, "13 SB")
b1.advance(4, "28 HR")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b1.new_ab()
b1.pitch_list("b c b 1 b")
b1.out("F8")

# 3. BOS #13 Hanley Ramirez (X - X - 50)
b1.new_ab(is_risp=True)
b1.pitch_list("c b t b f")
b1.out("G5-3")

# 4. BOS #28 J.D. Martinez (X - 50 - X)
b1.new_ab(is_risp=True)
b1.pitch_list("c b")
b1.hit(4, rbis=2)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c s f b b f b")
b1.hit(1)
b1.advance(2, "11 WP")

# 6. BOS #11 Rafael Devers (X - X - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("c b b b b")
b1.wp()
b1.reach("BB")

# 7. BOS #12 Brock Holt (X - 2 - 11)
b1.new_ab(is_risp=True)
b1.pitch_list("b b b c f s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 4. BAL #6  Jonathan Schoop (X - X - X)
t2.new_ab()
t2.pitch_list("b")
t2.out("(F)P3")

# 5. BAL #19 Chris Davis (X - X - X)
t2.new_ab()
t2.pitch_list("b c")
t2.out("G6-3")

# 6. BAL #45 Mark Trumbo (X - X - X)
t2.new_ab()
t2.pitch_list("b s f c")
t2.out("!K")


# Bot 2nd
# Pitching: BAL #34 Kevin Gausman
b2 = game.new_inning()

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("f b")
b2.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c s b f c")
b2.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("b c c b b")
b2.hit(1)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b2.new_ab()
b2.pitch_list("c b s 1 t")
b2.out("KT")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 7. BAL #2  Danny Valencia (X - X - X)
t3.new_ab()
t3.pitch_list("b c c")
t3.hit(1)

# 8. BAL #23 Joey Rickard (X - X - 2)
t3.new_ab()
t3.pitch_list("c")
t3.out("F8")

# 9. BAL #27 Andrew Susac (X - X - 2)
t3.new_ab()
t3.pitch_list("b f f s")
t3.out("K")

# 1. BAL #16 Trey Mancini (X - X - 2)
t3.new_ab()
t3.pitch_list("s b f b")
t3.out("G1-3")


# Bot 3rd
# Pitching: BAL #34 Kevin Gausman
b3 = game.new_inning()

# 3. BOS #13 Hanley Ramirez (X - X - X)
b3.new_ab()
b3.hit(1)
b3.thrown_out(2, "28 DP6-4-3", 1, 34)

# 4. BOS #28 J.D. Martinez (X - X - 13)
b3.new_ab()
b3.pitch_list("b f c b")
b3.out("DP6-4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("b")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 2. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("m f")
t4.out("L4")

# 3. BAL #13 Manny Machado (X - X - X)
t4.new_ab()
t4.out("F8")

# 4. BAL #6  Jonathan Schoop (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.hit(1)

# 5. BAL #19 Chris Davis (X - X - 6)
t4.new_ab()
t4.pitch_list("c f s")
t4.out("K")


# Bot 4th
# Pitching: BAL #34 Kevin Gausman
b4 = game.new_inning()

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.out("F9")

# 7. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b f f f s")
b4.out("K")

# 8. BOS #3  Sandy León (X - X - X)
b4.new_ab()
b4.pitch_list("c c t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 6. BAL #45 Mark Trumbo (X - X - X)
t5.new_ab()
t5.pitch_list("s f b s")
t5.out("K")

# 7. BAL #2  Danny Valencia (X - X - X)
t5.new_ab()
t5.hit(1)
t5.thrown_out(2, "7-4", 2, 24)

# 8. BAL #23 Joey Rickard (X - X - X)
t5.new_ab()
t5.pitch_list("b c")
t5.out("P6")


# Bot 5th
# Pitching: BAL #34 Kevin Gausman
b5 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b b b c b")
b5.reach("BB")
b5.advance(2, "50 SB")
b5.advance(3, "50 1B")
b5.advance(4, "16 SF9")

# 1. BOS #50 Mookie Betts (X - X - 19)
b5.new_ab(is_risp=True)
b5.pitch_list("c n 1 b s b")
b5.hit(1)
b5.advance(2, "13 SB")
b5.advance(3, "28 SB")
b5.advance(4, "2 HR")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b5.new_ab(is_risp=True)
b5.out("SF9", rbis=1)

# 3. BOS #13 Hanley Ramirez (X - X - 50)
b5.new_ab(is_risp=True)
b5.pitch_list("1 1 f f")
b5.hit(1)
b5.advance(2, "28 SB")
b5.advance(4, "2 HR")

# 4. BOS #28 J.D. Martinez (X - 50 - 13)
b5.new_ab(is_risp=True)
b5.pitch_list("b c s f b f b s")
b5.out("K")

# 5. BOS #2  Xander Bogaerts (50 - 13 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b c d b")
b5.hit(4, rbis=3)

# Pitching change (BAL): #57 Donnie Hart replaces #34 Kevin Gausman
b5.pitching_substitution(57)

# 6. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 9. BAL #27 Andrew Susac (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("P5")

# 1. BAL #16 Trey Mancini (X - X - X)
t6.new_ab()
t6.pitch_list("c b")
t6.out("G3")

# 2. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.pitch_list("b c")
t6.out("L9")


# Bot 6th
# Pitching: BAL #57 Donnie Hart
b6 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.pitch_list("c c b")
b6.out("G1-3")

# 8. BOS #3  Sandy León (X - X - X)
b6.new_ab()
b6.pitch_list("b f")
b6.hit(1)
b6.advance(2, "50 BB")
b6.advance(3, "16 BB")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
b6.new_ab()
b6.pitch_list("s b f")
b6.out("P4")

# Pitching change (BAL): #50 Miguel Castro replaces #57 Donnie Hart
b6.pitching_substitution(50)

# 1. BOS #50 Mookie Betts (X - X - 3)
b6.new_ab()
b6.pitch_list("c b b d b")
b6.reach("BB")
b6.advance(2, "16 BB")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
b6.new_ab(is_risp=True)
b6.pitch_list("b b b b")
b6.reach("BB")

# 3. BOS #13 Hanley Ramirez (3 - 50 - 16)
b6.new_ab(is_risp=True)
b6.pitch_list("c s b b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 3. BAL #13 Manny Machado (X - X - X)
t7.new_ab()
t7.out("G5-3")

# 4. BAL #6  Jonathan Schoop (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G4-3")

# 5. BAL #19 Chris Davis (X - X - X)
t7.new_ab()
t7.pitch_list("b f f f b s")
t7.out("K")


# Bot 7th
# Pitching: BAL #50 Miguel Castro
b7 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #28 J.D. Martinez, batting 4th
b7.offensive_substitution(4, 23, "PH")

# 4. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c")
b7.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c c f s")
b7.out("K")

# 6. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #24 David Price
t8 = game.new_inning()

# Defensive switch (BOS): #23 Blake Swihart moves to DH
t8.defensive_switch(23, "0")

# 6. BAL #45 Mark Trumbo (X - X - X)
t8.new_ab()
t8.pitch_list("t s")
t8.out("G5-3")

# 7. BAL #2  Danny Valencia (X - X - X)
t8.new_ab()
t8.out("L9")

# 8. BAL #23 Joey Rickard (X - X - X)
t8.new_ab()
t8.pitch_list("c f b b s")
t8.out("K")


# Bot 8th
# Pitching: BAL #38 Pedro Araújo
b8 = game.new_inning()

# Pitching change (BAL): #38 Pedro Araújo replaces #50 Miguel Castro
b8.pitching_substitution(38)

# 7. BOS #12 Brock Holt (X - X - X)
b8.new_ab()
b8.pitch_list("b f b f f")
b8.out("G3-1")

# 8. BOS #3  Sandy León (X - X - X)
b8.new_ab()
b8.pitch_list("b b f f")
b8.hit(1)
b8.thrown_out(2, "50 FC6-4", 3, 38)

# 9. BOS #19 Jackie Bradley Jr. (X - X - 3)
b8.new_ab()
b8.out("F7")

# 1. BOS #50 Mookie Betts (X - X - 3)
b8.new_ab()
b8.pitch_list("c d")
b8.reach("FC6-4")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #24 David Price
t9 = game.new_inning()

# 9. BAL #27 Andrew Susac (X - X - X)
t9.new_ab()
t9.pitch_list("s b f b b f")
t9.hit(2)
t9.advance(4, "13 HR")

# 1. BAL #16 Trey Mancini (X - 27 - X)
t9.new_ab(is_risp=True)
t9.out("(F)P3")

# 2. BAL #10 Adam Jones (X - 27 - X)
t9.new_ab(is_risp=True)
t9.out("(F)P5")

# 3. BAL #13 Manny Machado (X - 27 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b f f")
t9.hit(4, rbis=2)

# 4. BAL #6  Jonathan Schoop (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F8")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)

# Loser team: BAL
# LP: BAL #34 Kevin Gausman
game.losing_pitcher(34, is_away_team=True)

# print(game)
game.generate_scorecard()
