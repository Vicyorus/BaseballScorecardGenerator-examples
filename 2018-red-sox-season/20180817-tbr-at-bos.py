import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBR @ BOS, 2018-08-17
# https://www.baseball-reference.com/boxes/BOS/BOS201808170.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/08/17/531247/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-17 19:20-22:17 (0:10 delay)",
        "at": "Fenway Park, Boston, MA",
        "att": "37,012",
        "temp": "75F, Cloudy",
        "wind": "6mph, In From RF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 55,
            "roster": {
                # Lineup
                0: "Mallex Smith",
                5: "Matt Duffy",
                29: "Tommy Pham",
                44: "C.J. Cron",
                18: "Joey Wendle",
                27: "Carlos Gómez",
                39: "Kevin Kiermaier",
                1: "Willy Adames",
                43: "Michael Pérez",
                # Starting pitcher
                55: "Ryne Stanek",
                # Bench
                35: "Brandon Lowe",
                9: "Jake Bauers",
                26: "Ji Man Choi",
                45: "Jesús Sucre",
                # Bullpen
                46: "José Alvarado",
                20: "Tyler Glasnow",
                61: "Hunter Wood",
                48: "Ryan Yarbrough",
                68: "Jalen Beeks",
                56: "Adam Kolarek",
                52: "Chaz Roe",
                42: "Blake Snell",
                72: "Yonny Chirinos",
                63: "Diego Castillo",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 68, 56, 42],
            "lineup": [
                [0, "9"],
                [5, "5"],
                [29, "7"],
                [44, "3"],
                [18, "4"],
                [27, "0"],
                [39, "8"],
                [1, "6"],
                [43, "2"],
            ],
            "bench": [
                [35, "2B"],
                [9, "1B"],
                [26, "1B"],
                [45, "C"],
            ],
            "bullpen": [46, 20, 61, 48, 68, 56, 52, 42, 72, 63, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 61,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                5: "Ian Kinsler",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                61: "Brian Johnson",
                # Bench
                25: "Steve Pearce",
                12: "Brock Holt",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                22: "Rick Porcello",
                56: "Joe Kelly",
                31: "Drew Pomeranz",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
                37: "Heath Hembree",
            },
            "lefties": [61, 24, 31],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [5, "4"],
                [36, "5"],
                [23, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [12, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 24, 46, 76, 70, 22, 56, 31, 17, 32, 37],
        },
        "umpires": {
            "HP": "Chad Whitson",
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
# Pitching: BOS #61 Brian Johnson
t1 = game.new_inning()

# 1. TBR #0  Mallex Smith (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)
t1.thrown_out(2, "5 DP4-6-3", 1, 61)

# 2. TBR #5  Matt Duffy (X - X - 0)
t1.new_ab()
t1.pitch_list("1 f f")
t1.out("DP4-6-3")

# 3. TBR #29 Tommy Pham (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c b")
t1.reach("BB")
t1.advance(3, "44 2B")
t1.advance(4, "18 2B")

# 4. TBR #44 C.J. Cron (X - X - 29)
t1.new_ab()
t1.hit(2)
t1.advance(4, "18 2B")

# 5. TBR #18 Joey Wendle (29 - 44 - X)
t1.new_ab()
t1.pitch_list("c b")
t1.hit(2, rbis=2)
t1.advance(4, "27 1B")

# 6. TBR #27 Carlos Gómez (X - 18 - X)
t1.new_ab()
t1.pitch_list("s b b")
t1.hit(1, rbis=1)

# 7. TBR #39 Kevin Kiermaier (X - X - 27)
t1.new_ab()
t1.out("P5")


# Bot 1st
# Pitching: TBR #55 Ryne Stanek
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b b b c c")
b1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b s b")
b1.hit(1)
b1.advance(2, "18 WP")
b1.advance(3, "18 F8")
b1.advance(4, "2 3B")

# 3. BOS #18 Mitch Moreland (X - X - 16)
b1.new_ab()
b1.pitch_list("b f c 1 1 b")
b1.wp()
b1.out("F8")

# 4. BOS #28 J.D. Martinez (16 - X - X)
b1.new_ab()
b1.pitch_list("b d f b s d")
b1.reach("BB")
b1.advance(4, "2 3B")

# 5. BOS #2  Xander Bogaerts (16 - X - 28)
b1.new_ab()
b1.pitch_list("b c b f f f b")
b1.hit(3, rbis=2)

# 6. BOS #5  Ian Kinsler (2 - X - X)
b1.new_ab()
b1.pitch_list("b s")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #61 Brian Johnson
t2 = game.new_inning()

# 8. TBR #1  Willy Adames (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b")
t2.out("G5-3")

# 9. TBR #43 Michael Pérez (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b")
t2.out("F9")

# 1. TBR #0  Mallex Smith (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b c s")
t2.out("K")


# Bot 2nd
# Pitching: TBR #72 Yonny Chirinos
b2 = game.new_inning()

# Pitching change (TBR): #72 Yonny Chirinos replaces #55 Ryne Stanek
b2.pitching_substitution(72)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")

# 8. BOS #23 Blake Swihart (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F7")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.hit(1)

# 1. BOS #50 Mookie Betts (X - X - 19)
b2.new_ab()
b2.pitch_list("c f b b 1 b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #61 Brian Johnson
t3 = game.new_inning()

# 2. TBR #5  Matt Duffy (X - X - X)
t3.new_ab()
t3.pitch_list("b c f b")
t3.out("F8")

# 3. TBR #29 Tommy Pham (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b f")
t3.out("L8")

# 4. TBR #44 C.J. Cron (X - X - X)
t3.new_ab()
t3.pitch_list("b f b")
t3.out("(F)P2")


# Bot 3rd
# Pitching: TBR #72 Yonny Chirinos
b3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("b f")
b3.out("L7")

# 3. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("f b s b")
b3.out("G6-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("F9")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #61 Brian Johnson
t4 = game.new_inning()

# 5. TBR #18 Joey Wendle (X - X - X)
t4.new_ab()
t4.out("G4-3")

# 6. TBR #27 Carlos Gómez (X - X - X)
t4.new_ab()
t4.pitch_list("f s b s")
t4.out("K")

# 7. TBR #39 Kevin Kiermaier (X - X - X)
t4.new_ab()
t4.pitch_list("c b b")
t4.out("G4-3")


# Bot 4th
# Pitching: TBR #72 Yonny Chirinos
b4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.hit(2)
b4.advance(3, "5 L9")
b4.advance(4, "36 1B")

# 6. BOS #5  Ian Kinsler (X - 2 - X)
b4.new_ab()
b4.pitch_list("b f")
b4.out("L9")

# 7. BOS #36 Eduardo Núñez (2 - X - X)
b4.new_ab()
b4.pitch_list("b f c b")
b4.hit(1, rbis=1)
b4.thrown_out(2, "23 FC6", 2, 72)

# 8. BOS #23 Blake Swihart (X - X - 36)
b4.new_ab()
b4.reach("FC6")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
b4.new_ab()
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #61 Brian Johnson
t5 = game.new_inning()

# 8. TBR #1  Willy Adames (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("G5-3")

# 9. TBR #43 Michael Pérez (X - X - X)
t5.new_ab()
t5.pitch_list("b b b c d")
t5.reach("BB")

# 1. TBR #0  Mallex Smith (X - X - 43)
t5.new_ab()
t5.out("P5")

# 2. TBR #5  Matt Duffy (X - X - 43)
t5.new_ab()
t5.pitch_list("c b b f b")
t5.out("G5-3")


# Bot 5th
# Pitching: TBR #72 Yonny Chirinos
b5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b f b f")
b5.hit(2)
b5.advance(3, "16 G4-3")
b5.advance(4, "18 1B")

# 2. BOS #16 Andrew Benintendi (X - 50 - X)
b5.new_ab()
b5.pitch_list("b")
b5.out("G4-3")

# 3. BOS #18 Mitch Moreland (50 - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.hit(1, rbis=1)
b5.advance(2, "28 G5-3")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b5.new_ab()
b5.pitch_list("b s f f b f b")
b5.out("G5-3")

# 5. BOS #2  Xander Bogaerts (X - 18 - X)
b5.new_ab()
b5.pitch_list("c d b")
b5.out("P4")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #61 Brian Johnson
t6 = game.new_inning()

# 3. TBR #29 Tommy Pham (X - X - X)
t6.new_ab()
t6.pitch_list("b c b c")
t6.out("F9")

# 4. TBR #44 C.J. Cron (X - X - X)
t6.new_ab()
t6.pitch_list("b f s f b b")
t6.out("G5-3")

# 5. TBR #18 Joey Wendle (X - X - X)
t6.new_ab()
t6.pitch_list("b c b c f b f")
t6.hit(2)

# Pitching change (BOS): #37 Heath Hembree replaces #61 Brian Johnson
t6.pitching_substitution(37)

# Offensive change (TBR): Pinch-hitter #9 Jake Bauers replaces #27 Carlos Gómez, batting 6th
t6.offensive_substitution(6, 9, "PH")

# 6. TBR #9  Jake Bauers (X - 18 - X)
t6.new_ab()
t6.pitch_list("f b b f s")
t6.out("K")


# Bot 6th
# Pitching: TBR #72 Yonny Chirinos
b6 = game.new_inning()

# Defensive switch (TBR): #9 Jake Bauers moves to DH
b6.defensive_switch(9, "0")

# 6. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("b b b b")
b6.reach("BB")
b6.thrown_out(2, "23 FC4-6", 2, 72)

# 7. BOS #36 Eduardo Núñez (X - X - 5)
b6.new_ab()
b6.pitch_list("f")
b6.out("L8")

# 8. BOS #23 Blake Swihart (X - X - 5)
b6.new_ab()
b6.pitch_list("1 b 1 c")
b6.reach("FC4-6")
b6.advance(4, "19 2B")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 23)
b6.new_ab()
b6.pitch_list("d")
b6.hit(2, rbis=1)

# 1. BOS #50 Mookie Betts (X - 19 - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("P4")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #70 Ryan Brasier
t7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #37 Heath Hembree
t7.pitching_substitution(70)

# 7. TBR #39 Kevin Kiermaier (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.hit(1)
t7.thrown_out(2, "1 CS", 2, 70)

# 8. TBR #1  Willy Adames (X - X - 39)
t7.new_ab()
t7.pitch_list("f 1 b f b f b s")
t7.out("KDP2-4")

# 9. TBR #43 Michael Pérez (X - X - X)
t7.new_ab()
t7.pitch_list("c f b b s")
t7.out("K")


# Bot 7th
# Pitching: TBR #72 Yonny Chirinos
b7 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.out("G6-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.hit(2)
b7.advance(4, "28 1B")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
b7.new_ab()
b7.hit(1, rbis=1)
b7.advance(3, "2 2B")
b7.advance(4, "36 WP")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b7.new_ab()
b7.pitch_list("b b c f f")
b7.hit(2)
b7.advance(3, "36 WP")

# 6. BOS #5  Ian Kinsler (28 - 2 - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G5-3")

# 7. BOS #36 Eduardo Núñez (28 - 2 - X)
b7.new_ab()
b7.pitch_list("b b")
b7.wp()
b7.out("L6")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #70 Ryan Brasier
t8.pitching_substitution(32)

# 1. TBR #0  Mallex Smith (X - X - X)
t8.new_ab()
t8.pitch_list("b b")
t8.hit(1)
t8.advance(2, "5 HBP")

# 2. TBR #5  Matt Duffy (X - X - 0)
t8.new_ab()
t8.reach("HBP")

# 3. TBR #29 Tommy Pham (X - 0 - 5)
t8.new_ab()
t8.pitch_list("c b f c")
t8.out("!K")

# 4. TBR #44 C.J. Cron (X - 0 - 5)
t8.new_ab()
t8.pitch_list("s s b")
t8.out("IF4")

# 5. TBR #18 Joey Wendle (X - 0 - 5)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K2-3")


# Bot 8th
# Pitching: TBR #63 Diego Castillo
b8 = game.new_inning()

# Pitching change (TBR): #63 Diego Castillo replaces #72 Yonny Chirinos
b8.pitching_substitution(63)

# 8. BOS #23 Blake Swihart (X - X - X)
b8.new_ab()
b8.pitch_list("b c f t")
b8.out("KT")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("s s")
b8.out("G6-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b c b")
b8.out("F8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #47 Tyler Thornburg
t9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #32 Matt Barnes
t9.pitching_substitution(47)

# 6. TBR #9  Jake Bauers (X - X - X)
t9.new_ab()
t9.pitch_list("b c b c f b")
t9.out("G4-3")

# 7. TBR #39 Kevin Kiermaier (X - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.out("G1-3")

# 8. TBR #1  Willy Adames (X - X - X)
t9.new_ab()
t9.pitch_list("s s b")
t9.out("G5-3")

# Winning team: BOS
# WP: BOS #61 Brian Johnson
game.winning_pitcher(61)

# Loser team: TBR
# LP: TBR #72 Yonny Chirinos
game.losing_pitcher(72, is_away_team=True)

# print(game)
game.generate_scorecard()
