import os
from baseball_scorecard.baseball_scorecard import Scorecard

# TBR @ BOS, 2018-08-18
# https://www.baseball-reference.com/boxes/BOS/BOS201808180.shtml
# https://www.mlb.com/gameday/rays-vs-red-sox/2018/08/18/531262/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-18 19:11-21:39",
        "at": "Fenway Park, Boston, MA",
        "att": "36,654",
        "temp": "76F, Cloudy",
        "wind": "7mph, In From LF",
        "away": {
            "team": "Tampa Bay Rays",
            "starter": 20,
            "roster": {
                # Lineup
                27: "Carlos Gómez",
                5: "Matt Duffy",
                9: "Jake Bauers",
                29: "Tommy Pham",
                44: "C.J. Cron",
                18: "Joey Wendle",
                1: "Willy Adames",
                39: "Kevin Kiermaier",
                43: "Michael Pérez",
                # Starting pitcher
                20: "Tyler Glasnow",
                # Bench
                35: "Brandon Lowe",
                26: "Ji Man Choi",
                0: "Mallex Smith",
                45: "Jesús Sucre",
                # Bullpen
                46: "José Alvarado",
                61: "Hunter Wood",
                48: "Ryan Yarbrough",
                68: "Jalen Beeks",
                56: "Adam Kolarek",
                52: "Chaz Roe",
                55: "Ryne Stanek",
                42: "Blake Snell",
                72: "Yonny Chirinos",
                63: "Diego Castillo",
                54: "Sergio Romo",
            },
            "lefties": [46, 48, 68, 56, 42],
            "lineup": [
                [27, "9"],
                [5, "5"],
                [9, "3"],
                [29, "7"],
                [44, "0"],
                [18, "4"],
                [1, "6"],
                [39, "8"],
                [43, "2"],
            ],
            "bench": [
                [35, "2B"],
                [26, "1B"],
                [0, "OF"],
                [45, "C"],
            ],
            "bullpen": [46, 61, 48, 68, 56, 52, 55, 42, 72, 63, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                5: "Ian Kinsler",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                24: "David Price",
                # Bench
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [24, 31, 61],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [5, "4"],
                [12, "5"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [36, "SS"],
                [23, "C"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Mark Wegner",
            "1B": "John Tumpane",
            "2B": "Jim Reynolds",
            "3B": "Chad Whitson",
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

# 1. TBR #27 Carlos Gómez (X - X - X)
t1.new_ab()
t1.pitch_list("c f b")
t1.error(6)
t1.reach("E6")
t1.advance(2, "5 1B")
t1.advance(3, "9 IF3")

# 2. TBR #5  Matt Duffy (X - X - 27)
t1.new_ab()
t1.hit(1)

# 3. TBR #9  Jake Bauers (X - 27 - 5)
t1.new_ab()
t1.out("IF3")

# 4. TBR #29 Tommy Pham (27 - X - 5)
t1.new_ab()
t1.pitch_list("d c b f f c")
t1.out("!K")

# 5. TBR #44 C.J. Cron (27 - X - 5)
t1.new_ab()
t1.pitch_list("b f s f b f f b")
t1.out("G1-3")


# Bot 1st
# Pitching: TBR #20 Tyler Glasnow
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c c b s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(2)
b1.advance(4, "18 2B")

# 3. BOS #18 Mitch Moreland (X - 16 - X)
b1.new_ab()
b1.hit(2, rbis=1)
b1.advance(3, "28 SB")
b1.advance(4, "5 BB")

# 4. BOS #28 J.D. Martinez (X - 18 - X)
b1.new_ab()
b1.pitch_list("b b f b b")
b1.reach("BB")
b1.advance(2, "2 SB")
b1.advance(3, "5 BB")
b1.advance(4, "12 FC3")

# 5. BOS #2  Xander Bogaerts (18 - X - 28)
b1.new_ab()
b1.pitch_list("1 b b b b")
b1.reach("BB")
b1.advance(2, "5 BB")
b1.error(3)
b1.advance(3, "12 FC3")
b1.advance("U", "12 E3")

# 6. BOS #5  Ian Kinsler (18 - 28 - 2)
b1.new_ab()
b1.pitch_list("d b b b")
b1.reach("BB", rbis=1)
b1.advance(2, "12 E3")
b1.thrown_out(3, "3 CS", 2, 20)

# 7. BOS #12 Brock Holt (28 - 2 - 5)
b1.new_ab()
b1.pitch_list("c b b c f b f")
b1.reach("FC3", rbis=1)
b1.thrown_out(2, "3 1-5", 3, 20)

# 8. BOS #3  Sandy León (X - 5 - 12)
b1.new_ab()
b1.pitch_list("n")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 6. TBR #18 Joey Wendle (X - X - X)
t2.new_ab()
t2.pitch_list("c s f")
t2.out("P4")

# 7. TBR #1  Willy Adames (X - X - X)
t2.new_ab()
t2.pitch_list("b b f")
t2.out("L9")

# 8. TBR #39 Kevin Kiermaier (X - X - X)
t2.new_ab()
t2.out("G4-3")


# Bot 2nd
# Pitching: TBR #20 Tyler Glasnow
b2 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("c b f s")
b2.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b2.new_ab()
b2.pitch_list("b f f b s")
b2.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("F9")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 9. TBR #43 Michael Pérez (X - X - X)
t3.new_ab()
t3.pitch_list("c f c")
t3.out("!K")

# 1. TBR #27 Carlos Gómez (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("B5-3")

# 2. TBR #5  Matt Duffy (X - X - X)
t3.new_ab()
t3.pitch_list("c s f c")
t3.out("!K")


# Bot 3rd
# Pitching: TBR #20 Tyler Glasnow
b3 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("P4")

# 4. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("c b f s")
b3.out("K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("b s f b b")
b3.hit(4)

# 6. BOS #5  Ian Kinsler (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G5-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 3. TBR #9  Jake Bauers (X - X - X)
t4.new_ab()
t4.pitch_list("c b f f s")
t4.out("K")

# 4. TBR #29 Tommy Pham (X - X - X)
t4.new_ab()
t4.pitch_list("f b b b b")
t4.reach("BB")
t4.advance(2, "44 1B")
t4.thrown_out(2, "18 DP7-4", 3, 24)

# 5. TBR #44 C.J. Cron (X - X - 29)
t4.new_ab()
t4.pitch_list("c")
t4.hit(1)

# 6. TBR #18 Joey Wendle (X - 29 - 44)
t4.new_ab()
t4.pitch_list("f b b b f f f")
t4.out("DP7-4")


# Bot 4th
# Pitching: TBR #20 Tyler Glasnow
b4 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b4.new_ab()
b4.pitch_list("b b b f")
b4.out("F8")

# 8. BOS #3  Sandy León (X - X - X)
b4.new_ab()
b4.pitch_list("c b b")
b4.out("L3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.out("G4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 7. TBR #1  Willy Adames (X - X - X)
t5.new_ab()
t5.pitch_list("f f f c")
t5.out("!K")

# 8. TBR #39 Kevin Kiermaier (X - X - X)
t5.new_ab()
t5.pitch_list("b f f")
t5.out("G6-3")

# 9. TBR #43 Michael Pérez (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "27 HBP")

# 1. TBR #27 Carlos Gómez (X - X - 43)
t5.new_ab()
t5.reach("HBP")

# 2. TBR #5  Matt Duffy (X - 43 - 27)
t5.new_ab()
t5.out("F8")


# Bot 5th
# Pitching: TBR #20 Tyler Glasnow
b5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.out("P6")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("c b b")
b5.out("G5-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 3. TBR #9  Jake Bauers (X - X - X)
t6.new_ab()
t6.pitch_list("b f b s b d")
t6.reach("BB")
t6.advance(4, "44 HR")

# 4. TBR #29 Tommy Pham (X - X - 9)
t6.new_ab()
t6.pitch_list("b b c f b c")
t6.out("!K")

# 5. TBR #44 C.J. Cron (X - X - 9)
t6.new_ab()
t6.hit(4, rbis=2)

# 6. TBR #18 Joey Wendle (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("L8")

# 7. TBR #1  Willy Adames (X - X - X)
t6.new_ab()
t6.pitch_list("c b b f")
t6.out("G6-3")


# Bot 6th
# Pitching: TBR #20 Tyler Glasnow
b6 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b")
b6.out("L8")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b")
b6.out("G3-1")

# 6. BOS #5  Ian Kinsler (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 8. TBR #39 Kevin Kiermaier (X - X - X)
t7.new_ab()
t7.pitch_list("c")
t7.hit(2)

# 9. TBR #43 Michael Pérez (X - 39 - X)
t7.new_ab()
t7.pitch_list("s f c")
t7.out("!K")

# 1. TBR #27 Carlos Gómez (X - 39 - X)
t7.new_ab()
t7.pitch_list("f f c")
t7.out("!K")

# 2. TBR #5  Matt Duffy (X - 39 - X)
t7.new_ab()
t7.pitch_list("b f b")
t7.out("L3")


# Bot 7th
# Pitching: TBR #20 Tyler Glasnow
b7 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("c b b f")
b7.out("F7")

# 8. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("c c b b b f")
b7.out("P5")

# Pitching change (TBR): #56 Adam Kolarek replaces #20 Tyler Glasnow
b7.pitching_substitution(56)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("c f b s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #70 Ryan Brasier
t8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #24 David Price
t8.pitching_substitution(70)

# 3. TBR #9  Jake Bauers (X - X - X)
t8.new_ab()
t8.pitch_list("b s b")
t8.out("G6-3")

# 4. TBR #29 Tommy Pham (X - X - X)
t8.new_ab()
t8.pitch_list("s c s")
t8.out("K")

# 5. TBR #44 C.J. Cron (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("F9")


# Bot 8th
# Pitching: TBR #56 Adam Kolarek
b8 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b c")
b8.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b c f")
b8.out("G6-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.hit(1)
b8.thrown_out(2, "28 FC5-6", 3, 56)

# 4. BOS #28 J.D. Martinez (X - X - 16)
b8.new_ab()
b8.pitch_list("1 1 b b s")
b8.reach("FC5-6")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #70 Ryan Brasier
t9.pitching_substitution(46)

# 6. TBR #18 Joey Wendle (X - X - X)
t9.new_ab()
t9.pitch_list("b f t")
t9.out("G6-3")

# 7. TBR #1  Willy Adames (X - X - X)
t9.new_ab()
t9.pitch_list("c f b b s")
t9.out("K")

# 8. TBR #39 Kevin Kiermaier (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F7")

# Winning team: BOS
# WP: BOS #24 David Price
game.winning_pitcher(24)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: TBR
# LP: TBR #20 Tyler Glasnow
game.losing_pitcher(20, is_away_team=True)

# print(game)
game.generate_scorecard()
