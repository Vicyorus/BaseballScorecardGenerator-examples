import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ ATL, 2018-09-03
# https://www.baseball-reference.com/boxes/ATL/ATL201809030.shtml
# https://www.mlb.com/gameday/red-sox-vs-braves/2018/09/03/531463/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-03 13:08-16:48",
        "at": "SunTrust Park, Atlanta, GA",
        "att": "40,394",
        "temp": "83F, Sunny",
        "wind": "10mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                5: "Ian Kinsler",
                7: "Christian Vázquez",
                17: "Nathan Eovaldi",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                12: "Brock Holt",
                59: "Sam Travis",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                66: "Bobby Poyner",
                37: "Heath Hembree",
                63: "Robby Scott",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "8"],
                [16, "7"],
                [28, "9"],
                [2, "6"],
                [18, "3"],
                [36, "5"],
                [5, "4"],
                [7, "2"],
                [17, "1"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [12, "2B"],
                [59, "1B"],
                [23, "C"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 32],
        },
        "home": {
            "team": "Atlanta Braves",
            "starter": 62,
            "roster": {
                # Lineup
                13: "Ronald Acuña Jr.",
                11: "Ender Inciarte",
                5: "Freddie Freeman",
                22: "Nick Markakis",
                17: "Johan Camargo",
                24: "Kurt Suzuki",
                1: "Ozzie Albies",
                7: "Dansby Swanson",
                62: "Touki Toussaint",
                # Starting pitcher
                62: "Touki Toussaint",
                # Bench
                23: "Adam Duvall",
                12: "René Rivera",
                27: "Ryan Flaherty",
                8: "Preston Tucker",
                20: "Lucas Duda",
                18: "Lane Adams",
                8: "Charlie Culberson",
                25: "Tyler Flowers",
                # Bullpen
                48: "Jonny Venters",
                64: "Luke Jackson",
                39: "Sam Freeman",
                51: "Shane Carle",
                45: "Kevin Gausman",
                58: "Dan Winkler",
                49: "Julio Teheran",
                33: "A.J. Minter",
                26: "Mike Foltynewicz",
                36: "Kolby Allard",
                15: "Sean Newcomb",
                63: "Jesse Biddle",
                19: "Aníbal Sánchez",
                73: "Kyle Wright",
                46: "Brad Brach",
                72: "Bryse Wilson",
            },
            "lefties": [48, 39, 33, 36, 15, 63],
            "lineup": [
                [13, "7"],
                [11, "8"],
                [5, "3"],
                [22, "9"],
                [17, "5"],
                [24, "2"],
                [1, "4"],
                [7, "6"],
                [62, "1"],
            ],
            "bench": [
                [23, "RF"],
                [12, "C"],
                [27, "2B"],
                [8, "LF"],
                [20, "1B"],
                [18, "LF"],
                [8, "1B"],
                [25, "C"],
            ],
            "bullpen": [48, 64, 39, 51, 45, 58, 49, 33, 26, 36, 15, 63, 19, 73, 46, 72],
        },
        "umpires": {
            "HP": "Mike Winters",
            "1B": "Jansen Visconti",
            "2B": "Tim Timmons",
            "3B": "Mike Muchlinski",
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
# Pitching: ATL #62 Touki Toussaint
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b c c s")
t1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("b b b b")
t1.reach("BB")
t1.thrown_out(2, "28 DP6-4-3", 2, 62)

# 3. BOS #28 J.D. Martinez (X - X - 16)
t1.new_ab()
t1.pitch_list("b d")
t1.out("DP6-4-3")


# Bot 1st
# Pitching: BOS #17 Nathan Eovaldi
b1 = game.new_inning()

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b1.new_ab()
b1.pitch_list("s b c b f c")
b1.out("!K")

# 2. ATL #11 Ender Inciarte (X - X - X)
b1.new_ab()
b1.pitch_list("c s b b f b b")
b1.reach("BB")
b1.advance(2, "5 BB")
b1.advance(3, "17 BB")

# 3. ATL #5  Freddie Freeman (X - X - 11)
b1.new_ab()
b1.pitch_list("s 1 b s f f b b f f 1 b")
b1.reach("BB")
b1.advance(2, "17 BB")

# 4. ATL #22 Nick Markakis (X - 11 - 5)
b1.new_ab()
b1.pitch_list("b s c s")
b1.out("K")

# 5. ATL #17 Johan Camargo (X - 11 - 5)
b1.new_ab()
b1.pitch_list("b f s b f b f f b")
b1.reach("BB")
b1.thrown_out(2, "24 FC6-4", 3, 17)

# 6. ATL #24 Kurt Suzuki (11 - 5 - 17)
b1.new_ab()
b1.pitch_list("c b")
b1.reach("FC6-4")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: ATL #62 Touki Toussaint
t2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("c")
t2.out("G1-3")

# 5. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("b s b b b")
t2.reach("BB")
t2.thrown_out(2, "36 FC6-4", 2, 62)

# 6. BOS #36 Eduardo Núñez (X - X - 18)
t2.new_ab()
t2.pitch_list("f")
t2.reach("FC6-4")

# 7. BOS #5  Ian Kinsler (X - X - 36)
t2.new_ab()
t2.pitch_list("c f s")
t2.out("K")


# Bot 2nd
# Pitching: BOS #17 Nathan Eovaldi
b2 = game.new_inning()

# 7. ATL #1  Ozzie Albies (X - X - X)
b2.new_ab()
b2.pitch_list("s b b")
b2.out("L3")

# 8. ATL #7  Dansby Swanson (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.out("G6-3")

# 9. ATL #62 Touki Toussaint (X - X - X)
b2.new_ab()
b2.pitch_list("c f b f f f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: ATL #62 Touki Toussaint
t3 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t3.new_ab()
t3.pitch_list("b c")
t3.out("L8")

# 9. BOS #17 Nathan Eovaldi (X - X - X)
t3.new_ab()
t3.pitch_list("b c c b b c")
t3.out("!K")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("G4-3")


# Bot 3rd
# Pitching: BOS #17 Nathan Eovaldi
b3 = game.new_inning()

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b s b s s")
b3.out("K")

# 2. ATL #11 Ender Inciarte (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c f f")
b3.out("G4-3")

# 3. ATL #5  Freddie Freeman (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.hit(1)

# 4. ATL #22 Nick Markakis (X - X - 5)
b3.new_ab()
b3.pitch_list("c b b f")
b3.out("G4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: ATL #62 Touki Toussaint
t4 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t4.new_ab()
t4.out("G4-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b b f f f s")
t4.out("K")

# 4. BOS #2  Xander Bogaerts (X - X - X)
t4.new_ab()
t4.pitch_list("c c s")
t4.out("K")


# Bot 4th
# Pitching: BOS #17 Nathan Eovaldi
b4 = game.new_inning()

# 5. ATL #17 Johan Camargo (X - X - X)
b4.new_ab()
b4.pitch_list("b b f b f f b")
b4.reach("BB")
b4.advance(2, "24 1B")
b4.advance(3, "1 F9")
b4.thrown_out(4, "62 FC3-2", 2, 44)

# 6. ATL #24 Kurt Suzuki (X - X - 17)
b4.new_ab()
b4.pitch_list("b")
b4.hit(1)
b4.advance(2, "7 BB")
b4.advance(3, "62 FC3-2")

# 7. ATL #1  Ozzie Albies (X - 17 - 24)
b4.new_ab()
b4.pitch_list("s b s b f")
b4.out("F9")

# Pitching change (BOS): #44 Brandon Workman replaces #17 Nathan Eovaldi, batting 9th
b4.pitching_substitution(44)
b4.defensive_substitution(9, 44, "1")

# 8. ATL #7  Dansby Swanson (17 - X - 24)
b4.new_ab()
b4.pitch_list("d s f 1 d f b d")
b4.reach("BB")
b4.advance(2, "62 FC3-2")

# 9. ATL #62 Touki Toussaint (17 - 24 - 7)
b4.new_ab()
b4.pitch_list("d")
b4.reach("FC3-2")

# 1. ATL #13 Ronald Acuña Jr. (24 - 7 - 62)
b4.new_ab()
b4.pitch_list("b b")
b4.out("P4")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: ATL #62 Touki Toussaint
t5 = game.new_inning()

# 5. BOS #18 Mitch Moreland (X - X - X)
t5.new_ab()
t5.pitch_list("c s s")
t5.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.hit(2)
t5.advance(4, "5 2B")

# 7. BOS #5  Ian Kinsler (X - 36 - X)
t5.new_ab()
t5.hit(2, rbis=1)
t5.advance(4, "7 2B")

# 8. BOS #7  Christian Vázquez (X - 5 - X)
t5.new_ab()
t5.pitch_list("c d c b")
t5.hit(2, rbis=1)
t5.advance(3, "23 G4-3")
t5.advance(4, "50 1B")

# Offensive change (BOS): Pinch-hitter #23 Blake Swihart replaces #44 Brandon Workman, batting 9th
t5.offensive_substitution(9, 23, "PH")

# 9. BOS #23 Blake Swihart (X - 7 - X)
t5.new_ab()
t5.pitch_list("c f b b b")
t5.out("G4-3")

# 1. BOS #50 Mookie Betts (7 - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1, rbis=1)
t5.advance(3, "16 1B")

# Pitching change (ATL): #39 Sam Freeman replaces #62 Touki Toussaint, batting 9th
t5.pitching_substitution(39)
t5.defensive_substitution(9, 39, "1")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
t5.new_ab()
t5.pitch_list("1 1 f")
t5.hit(1)

# 3. BOS #28 J.D. Martinez (50 - X - 16)
t5.new_ab()
t5.pitch_list("b")
t5.out("(F)F9")


# Bot 5th
# Pitching: BOS #35 Steven Wright
b5 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #44 Brandon Workman, batting 9th
b5.pitching_substitution(35)
b5.defensive_substitution(9, 35, "1")

# 2. ATL #11 Ender Inciarte (X - X - X)
b5.new_ab()
b5.pitch_list("c f b f")
b5.reach("HBP")
b5.thrown_out(2, "5 FC4-5", 1, 35)

# 3. ATL #5  Freddie Freeman (X - X - 11)
b5.new_ab()
b5.pitch_list("b f b f f")
b5.reach("FC4-5")
b5.thrown_out(2, "22 FC6-4", 2, 35)

# 4. ATL #22 Nick Markakis (X - X - 5)
b5.new_ab()
b5.pitch_list("c")
b5.reach("FC6-4")
b5.advance(3, "17 1B")

# 5. ATL #17 Johan Camargo (X - X - 22)
b5.new_ab()
b5.pitch_list("c f f b")
b5.hit(1)

# 6. ATL #24 Kurt Suzuki (22 - X - 17)
b5.new_ab()
b5.pitch_list("c b f f")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: ATL #39 Sam Freeman
t6 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F9")

# 5. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.hit(1)

# Pitching change (ATL): #64 Luke Jackson replaces #39 Sam Freeman, batting 9th
t6.pitching_substitution(64)
t6.defensive_substitution(9, 64, "1")

# 6. BOS #36 Eduardo Núñez (X - X - 18)
t6.new_ab()
t6.pitch_list("c d s s")
t6.out("K")

# 7. BOS #5  Ian Kinsler (X - X - 18)
t6.new_ab()
t6.pitch_list("c")
t6.out("G5-3")


# Bot 6th
# Pitching: BOS #56 Joe Kelly
b6 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #35 Steven Wright, batting 9th
b6.pitching_substitution(56)
b6.defensive_substitution(9, 56, "1")

# 7. ATL #1  Ozzie Albies (X - X - X)
b6.new_ab()
b6.pitch_list("b")
b6.hit(4)

# 8. ATL #7  Dansby Swanson (X - X - X)
b6.new_ab()
b6.pitch_list("b c c b b f f")
b6.out("G4-3")

# Offensive change (ATL): Pinch-hitter #8 Preston Tucker replaces #64 Luke Jackson, batting 9th
b6.offensive_substitution(9, 8, "PH")

# 9. ATL #8  Preston Tucker (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G3-1")

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("G5-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: ATL #51 Shane Carle
t7 = game.new_inning()

# Pitching change (ATL): #51 Shane Carle replaces #64 Luke Jackson, batting 9th
t7.pitching_substitution(51)
t7.defensive_substitution(9, 51, "1")

# 8. BOS #7  Christian Vázquez (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.out("G4-3")

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #56 Joe Kelly, batting 9th
t7.offensive_substitution(9, 59, "PH")

# 9. BOS #59 Sam Travis (X - X - X)
t7.new_ab()
t7.out("G5-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("b b c f")
t7.out("G6-3")


# Bot 7th
# Pitching: BOS #70 Ryan Brasier
b7 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly, batting 9th
b7.pitching_substitution(70)
b7.defensive_substitution(9, 70, "1")

# 2. ATL #11 Ender Inciarte (X - X - X)
b7.new_ab()
b7.pitch_list("s b b c f")
b7.hit(1)
b7.advance(2, "22 1B")
b7.advance(3, "17 1B")
b7.advance(4, "24 SF9")

# 3. ATL #5  Freddie Freeman (X - X - 11)
b7.new_ab()
b7.pitch_list("b 1")
b7.out("L7")

# 4. ATL #22 Nick Markakis (X - X - 11)
b7.new_ab()
b7.pitch_list("1 1 s s f d f b")
b7.hit(1)
b7.advance(2, "17 1B")
b7.advance(3, "24 SF9")

# 5. ATL #17 Johan Camargo (X - 11 - 22)
b7.new_ab()
b7.pitch_list("c b d")
b7.hit(1)

# 6. ATL #24 Kurt Suzuki (11 - 22 - 17)
b7.new_ab()
b7.pitch_list("b f f")
b7.out("SF9", rbis=1)

# Pitching change (BOS): #37 Heath Hembree replaces #70 Ryan Brasier, batting 9th
b7.pitching_substitution(37)
b7.defensive_substitution(9, 37, "1")

# 7. ATL #1  Ozzie Albies (22 - X - 17)
b7.new_ab()
b7.pitch_list("s b f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: ATL #63 Jesse Biddle
t8 = game.new_inning()

# Pitching change (ATL): #63 Jesse Biddle replaces #51 Shane Carle, batting 9th
t8.pitching_substitution(63)
t8.defensive_substitution(9, 63, "1")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t8.new_ab()
t8.pitch_list("b b c c")
t8.out("G6-3")

# 3. BOS #28 J.D. Martinez (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1)
t8.advance(2, "18 BB")
t8.error(3)
t8.advance(3, "36 E3")
t8.advance("U", "5 1B")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t8.new_ab()
t8.pitch_list("c s s")
t8.out("K")

# 5. BOS #18 Mitch Moreland (X - X - 28)
t8.new_ab()
t8.pitch_list("b d f b b")
t8.reach("BB")
t8.advance(2, "36 E3")
t8.advance("U", "5 1B")

# 6. BOS #36 Eduardo Núñez (X - 28 - 18)
t8.new_ab()
t8.pitch_list("c")
t8.reach("FC3")
t8.advance(2, "5 1B")

# 7. BOS #5  Ian Kinsler (28 - 18 - 36)
t8.new_ab()
t8.pitch_list("d f")
t8.hit(1, rbis=2)

# 8. BOS #7  Christian Vázquez (X - 36 - 5)
t8.new_ab()
t8.pitch_list("c b b b f")
t8.out("F8")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #37 Heath Hembree, batting 9th
b8.pitching_substitution(32)
b8.defensive_substitution(9, 32, "1")

# 8. ATL #7  Dansby Swanson (X - X - X)
b8.new_ab()
b8.pitch_list("c c f b")
b8.hit(1)
b8.advance(2, "20 SB")
b8.advance(3, "20 G2-3")

# Offensive change (ATL): Pinch-hitter #20 Lucas Duda replaces #63 Jesse Biddle, batting 9th
b8.offensive_substitution(9, 20, "PH")

# 9. ATL #20 Lucas Duda (X - X - 7)
b8.new_ab()
b8.pitch_list("c b s")
b8.out("G2-3")

# 1. ATL #13 Ronald Acuña Jr. (7 - X - X)
b8.new_ab()
b8.pitch_list("f b c b d s")
b8.out("K")

# 2. ATL #11 Ender Inciarte (7 - X - X)
b8.new_ab()
b8.pitch_list("b d b c")
b8.out("F9")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: ATL #72 Bryse Wilson
t9 = game.new_inning()

# Pitching change (ATL): #72 Bryse Wilson replaces #63 Jesse Biddle, batting 9th
t9.pitching_substitution(72)
t9.defensive_substitution(9, 72, "1")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #32 Matt Barnes, batting 9th
t9.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Brock Holt (X - X - X)
t9.new_ab()
t9.pitch_list("c s f b b b b")
t9.reach("BB")
t9.advance(3, "16 2B")
t9.advance(4, "2 2B")

# 1. BOS #50 Mookie Betts (X - X - 12)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("L9")

# 2. BOS #16 Andrew Benintendi (X - X - 12)
t9.new_ab()
t9.pitch_list("s b b f")
t9.hit(2)
t9.advance(4, "2 2B")

# 3. BOS #28 J.D. Martinez (12 - 16 - X)
t9.new_ab()
t9.pitch_list("v v v v")
t9.reach("IBB")
t9.advance(3, "2 2B")
t9.advance(4, "36 SF8")

# 4. BOS #2  Xander Bogaerts (12 - 16 - 28)
t9.new_ab()
t9.pitch_list("c s f")
t9.hit(2, rbis=2)

# 5. BOS #18 Mitch Moreland (28 - 2 - X)
t9.new_ab()
t9.pitch_list("v v v v")
t9.reach("IBB")

# 6. BOS #36 Eduardo Núñez (28 - 2 - 18)
t9.new_ab()
t9.pitch_list("s")
t9.out("SF8", rbis=1)

# 7. BOS #5  Ian Kinsler (X - 2 - 18)
t9.new_ab()
t9.pitch_list("c b b")
t9.out("L9")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes, batting 3rd
b9.pitching_substitution(46)
b9.defensive_substitution(3, 46, "1")

# Defensive switch (BOS): #50 Mookie Betts moves to RF
b9.defensive_switch(50, "9")

# Defensive change (BOS): #19 Jackie Bradley Jr. replaces #12 Brock Holt (PH), playing CF, batting 9th
b9.defensive_substitution(9, 19, "8")

# 3. ATL #5  Freddie Freeman (X - X - X)
b9.new_ab()
b9.pitch_list("b")
b9.out("G4-3")

# 4. ATL #22 Nick Markakis (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c c f b")
b9.reach("BB")
b9.advance(2, "24 DI")

# 5. ATL #17 Johan Camargo (X - X - 22)
b9.new_ab()
b9.pitch_list("b f b f f c")
b9.out("!K")

# 6. ATL #24 Kurt Suzuki (X - X - 22)
b9.new_ab()
b9.pitch_list("c")
b9.out("F9")

# Winning team: BOS
# WP: BOS #44 Brandon Workman
game.winning_pitcher(44, is_away_team=True)

# Loser team: ATL
# LP: ATL #62 Touki Toussaint
game.losing_pitcher(62)

# print(game)
game.generate_scorecard()
