import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ ATL, 2018-09-05
# https://www.baseball-reference.com/boxes/ATL/ATL201809050.shtml
# https://www.mlb.com/gameday/red-sox-vs-braves/2018/09/05/531493/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-05 12:11-15:55",
        "at": "SunTrust Park, Atlanta, GA",
        "att": "28,386",
        "temp": "81F, Cloudy",
        "wind": "9mph, In From LF",
        "away": {
            "team": "Boston Red Sox",
            "starter": 76,
            "roster": {
                # Lineup
                19: "Jackie Bradley Jr.",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                0: "Brandon Phillips",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                76: "Hector Velázquez",
                # Starting pitcher
                76: "Hector Velázquez",
                # Bench
                30: "Tzu-Wei Lin",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                59: "Sam Travis",
                5: "Ian Kinsler",
                28: "J.D. Martinez",
                50: "Mookie Betts",
                2: "Xander Bogaerts",
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
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 31, 61, 66, 63, 24],
            "lineup": [
                [19, "8"],
                [23, "9"],
                [16, "7"],
                [18, "3"],
                [0, "4"],
                [11, "5"],
                [12, "6"],
                [7, "2"],
                [76, "1"],
            ],
            "bench": [
                [30, "OF"],
                [25, "1B"],
                [36, "SS"],
                [59, "1B"],
                [5, "2B"],
                [28, "DH"],
                [50, "SS"],
                [2, "2B"],
                [3, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 31, 61, 66, 37, 63, 24, 46, 70, 56, 17, 32],
        },
        "home": {
            "team": "Atlanta Braves",
            "starter": 26,
            "roster": {
                # Lineup
                13: "Ronald Acuña Jr.",
                11: "Ender Inciarte",
                22: "Nick Markakis",
                17: "Johan Camargo",
                20: "Lucas Duda",
                1: "Ozzie Albies",
                25: "Tyler Flowers",
                8: "Charlie Culberson",
                26: "Mike Foltynewicz",
                # Starting pitcher
                26: "Mike Foltynewicz",
                # Bench
                23: "Adam Duvall",
                12: "René Rivera",
                27: "Ryan Flaherty",
                5: "Freddie Freeman",
                8: "Preston Tucker",
                24: "Kurt Suzuki",
                18: "Lane Adams",
                7: "Dansby Swanson",
                # Bullpen
                48: "Jonny Venters",
                64: "Luke Jackson",
                39: "Sam Freeman",
                51: "Shane Carle",
                45: "Kevin Gausman",
                62: "Touki Toussaint",
                58: "Dan Winkler",
                49: "Julio Teheran",
                33: "A.J. Minter",
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
                [22, "9"],
                [17, "5"],
                [20, "3"],
                [1, "4"],
                [25, "2"],
                [8, "6"],
                [26, "1"],
            ],
            "bench": [
                [23, "RF"],
                [12, "C"],
                [27, "2B"],
                [5, "1B"],
                [8, "LF"],
                [24, "C"],
                [18, "LF"],
                [7, "SS"],
            ],
            "bullpen": [48, 64, 39, 51, 45, 62, 58, 49, 33, 36, 15, 63, 19, 73, 46, 72],
        },
        "umpires": {
            "HP": "Tim Timmons",
            "1B": "Mike Muchlinski",
            "2B": "Mike Winters",
            "3B": "Jansen Visconti",
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
# Pitching: ATL #26 Mike Foltynewicz
t1 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("f b")
t1.out("F7")

# 2. BOS #23 Blake Swihart (X - X - X)
t1.new_ab()
t1.out("F8")

# 3. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("c b t f")
t1.out("F8")


# Bot 1st
# Pitching: BOS #76 Hector Velázquez
b1 = game.new_inning()

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(4)

# 2. ATL #11 Ender Inciarte (X - X - X)
b1.new_ab()
b1.hit(3)
b1.advance(4, "22 1B")

# 3. ATL #22 Nick Markakis (11 - X - X)
b1.new_ab()
b1.pitch_list("c b f")
b1.hit(1, rbis=1)
b1.advance(2, "17 1B")
b1.advance(3, "20 DP1-6-3")

# 4. ATL #17 Johan Camargo (X - X - 22)
b1.new_ab()
b1.hit(1)
b1.thrown_out(2, "20 DP1-6-3", 1, 76)

# 5. ATL #20 Lucas Duda (X - 22 - 17)
b1.new_ab()
b1.out("DP1-6-3")

# 6. ATL #1  Ozzie Albies (22 - X - X)
b1.new_ab()
b1.pitch_list("s b")
b1.out("G3-1")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: ATL #26 Mike Foltynewicz
t2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
t2.new_ab()
t2.pitch_list("c b b f s")
t2.out("K")

# 5. BOS #0  Brandon Phillips (X - X - X)
t2.new_ab()
t2.pitch_list("b b f f b b")
t2.reach("BB")
t2.advance(3, "11 1B")
t2.advance(4, "12 G3")

# 6. BOS #11 Rafael Devers (X - X - 0)
t2.new_ab()
t2.hit(1)
t2.advance(2, "12 G3")

# 7. BOS #12 Brock Holt (0 - X - 11)
t2.new_ab()
t2.pitch_list("c d f 1 b b")
t2.out("G3", rbis=1)

# 8. BOS #7  Christian Vázquez (X - 11 - X)
t2.new_ab()
t2.pitch_list("v v v v")
t2.reach("IBB")

# 9. BOS #76 Hector Velázquez (X - 11 - 7)
t2.new_ab()
t2.pitch_list("b b c f")
t2.out("G4-3")


# Bot 2nd
# Pitching: BOS #76 Hector Velázquez
b2 = game.new_inning()

# 7. ATL #25 Tyler Flowers (X - X - X)
b2.new_ab()
b2.pitch_list("c f b b s")
b2.out("K")

# 8. ATL #8  Charlie Culberson (X - X - X)
b2.new_ab()
b2.pitch_list("c s b b f b f")
b2.out("L9")

# 9. ATL #26 Mike Foltynewicz (X - X - X)
b2.new_ab()
b2.pitch_list("c f s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: ATL #26 Mike Foltynewicz
t3 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s b f f")
t3.out("G6-3")

# 2. BOS #23 Blake Swihart (X - X - X)
t3.new_ab()
t3.pitch_list("b b c s f s")
t3.out("K")

# 3. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.hit(1)
t3.error(9)
t3.advance(2, "E9")

# 4. BOS #18 Mitch Moreland (X - 16 - X)
t3.new_ab()
t3.out("F8")


# Bot 3rd
# Pitching: BOS #76 Hector Velázquez
b3 = game.new_inning()

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("b b c b b")
b3.reach("BB")
b3.advance(2, "22 G6-3")

# 2. ATL #11 Ender Inciarte (X - X - 13)
b3.new_ab()
b3.pitch_list("1")
b3.out("F8")

# 3. ATL #22 Nick Markakis (X - X - 13)
b3.new_ab()
b3.pitch_list("1 b c 1 b 1 c")
b3.out("G6-3")

# 4. ATL #17 Johan Camargo (X - 13 - X)
b3.new_ab()
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: ATL #26 Mike Foltynewicz
t4 = game.new_inning()

# 5. BOS #0  Brandon Phillips (X - X - X)
t4.new_ab()
t4.pitch_list("b")
t4.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.out("G4-3")

# 7. BOS #12 Brock Holt (X - X - X)
t4.new_ab()
t4.pitch_list("c b c f b b c")
t4.out("!K")


# Bot 4th
# Pitching: BOS #76 Hector Velázquez
b4 = game.new_inning()

# 5. ATL #20 Lucas Duda (X - X - X)
b4.new_ab()
b4.pitch_list("c s b b b b")
b4.reach("BB")
b4.advance(3, "25 2B")
b4.thrown_out(4, "25 7-6-2", 2, 76)

# 6. ATL #1  Ozzie Albies (X - X - 20)
b4.new_ab()
b4.pitch_list("c")
b4.out("(F)P4")

# 7. ATL #25 Tyler Flowers (X - X - 20)
b4.new_ab()
b4.pitch_list("f c f")
b4.hit(2)
b4.advance(3, "T")

# 8. ATL #8  Charlie Culberson (25 - X - X)
b4.new_ab()
b4.pitch_list("v v v v")
b4.reach("IBB")

# 9. ATL #26 Mike Foltynewicz (25 - X - 8)
b4.new_ab()
b4.pitch_list("f b b f")
b4.out("G1-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: ATL #26 Mike Foltynewicz
t5 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
t5.new_ab()
t5.pitch_list("b c b s")
t5.out("G6-3")

# Offensive change (BOS): Pinch-hitter #59 Sam Travis replaces #76 Hector Velázquez, batting 9th
t5.offensive_substitution(9, 59, "PH")

# 9. BOS #59 Sam Travis (X - X - X)
t5.new_ab()
t5.pitch_list("b c b c")
t5.out("F8")

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("G4-3")


# Bot 5th
# Pitching: BOS #31 Drew Pomeranz
b5 = game.new_inning()

# Pitching change (BOS): #31 Drew Pomeranz replaces #76 Hector Velázquez, batting 9th
b5.pitching_substitution(31)
b5.defensive_substitution(9, 31, "1")

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("f b b f b f f f b")
b5.reach("BB")
b5.advance(3, "11 1B")
b5.advance(4, "22 1B")

# 2. ATL #11 Ender Inciarte (X - X - 13)
b5.new_ab()
b5.pitch_list("1 l b")
b5.hit(1)
b5.advance(2, "T")
b5.advance(3, "22 1B")
b5.advance(4, "24 FC6-4")

# 3. ATL #22 Nick Markakis (13 - 11 - X)
b5.new_ab()
b5.pitch_list("c f b")
b5.hit(1, rbis=1)
b5.advance(2, "17 BB")
b5.advance(3, "24 FC6-4")
b5.advance(4, "1 3B")

# 4. ATL #17 Johan Camargo (11 - X - 22)
b5.new_ab()
b5.pitch_list("b f d b b")
b5.reach("BB")
b5.thrown_out(2, "24 FC6-4", 1, 31)

# Offensive change (ATL): Pinch-hitter #24 Kurt Suzuki replaces #20 Lucas Duda, batting 5th
b5.offensive_substitution(5, 24, "PH")

# 5. ATL #24 Kurt Suzuki (11 - 22 - 17)
b5.new_ab()
b5.pitch_list("f b b")
b5.reach("FC6-4", rbis=1)
# Offensive change (ATL): Pinch-runner #27 Ryan Flaherty replaces #24 Kurt Suzuki
b5.offensive_substitution(5, 27, "PR")
b5.atbase("PR")
b5.advance(4, "1 3B")

# 6. ATL #1  Ozzie Albies (22 - X - 24)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(3, rbis=2)
b5.advance(4, "25 1B")

# Pitching change (BOS): #67 William Cuevas replaces #31 Drew Pomeranz, batting 9th
b5.pitching_substitution(67)
b5.defensive_substitution(9, 67, "1")

# 7. ATL #25 Tyler Flowers (1 - X - X)
b5.new_ab()
b5.pitch_list("c c b")
b5.hit(1, rbis=1)
b5.advance(2, "8 BB")

# 8. ATL #8  Charlie Culberson (X - X - 25)
b5.new_ab()
b5.pitch_list("b b b t f b")
b5.reach("BB")

# 9. ATL #26 Mike Foltynewicz (X - 25 - 8)
b5.new_ab()
b5.pitch_list("c m s")
b5.out("K")

# 1. ATL #13 Ronald Acuña Jr. (X - 25 - 8)
b5.new_ab()
b5.pitch_list("b f c b s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: ATL #26 Mike Foltynewicz
t6 = game.new_inning()

# Defensive switch (ATL): #27 Ryan Flaherty moves to 1B
t6.defensive_switch(27, "3")

# 2. BOS #23 Blake Swihart (X - X - X)
t6.new_ab()
t6.pitch_list("c b f b s")
t6.out("K")

# 3. BOS #16 Andrew Benintendi (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b c")
t6.out("!K")

# 4. BOS #18 Mitch Moreland (X - X - X)
t6.new_ab()
t6.pitch_list("b b b c f")
t6.out("G3")


# Bot 6th
# Pitching: BOS #67 William Cuevas
b6 = game.new_inning()

# 2. ATL #11 Ender Inciarte (X - X - X)
b6.new_ab()
b6.pitch_list("b c")
b6.out("F7")

# 3. ATL #22 Nick Markakis (X - X - X)
b6.new_ab()
b6.pitch_list("b c f b")
b6.out("L7")

# 4. ATL #17 Johan Camargo (X - X - X)
b6.new_ab()
b6.pitch_list("c s b")
b6.reach("HBP")
b6.advance(2, "27 BB")

# 5. ATL #27 Ryan Flaherty (X - X - 17)
b6.new_ab()
b6.pitch_list("b b d c b")
b6.reach("BB")

# 6. ATL #1  Ozzie Albies (X - 17 - 27)
b6.new_ab()
b6.pitch_list("f b s b f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: ATL #63 Jesse Biddle
t7 = game.new_inning()

# Pitching change (ATL): #63 Jesse Biddle replaces #26 Mike Foltynewicz, batting 9th
t7.pitching_substitution(63)
t7.defensive_substitution(9, 63, "1")

# 5. BOS #0  Brandon Phillips (X - X - X)
t7.new_ab()
t7.pitch_list("b f b b f b")
t7.reach("BB")
t7.thrown_out(2, "11 DP4-6-3", 1, 63)

# 6. BOS #11 Rafael Devers (X - X - 0)
t7.new_ab()
t7.pitch_list("c b d")
t7.out("DP4-6-3")

# 7. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.out("G4-3")


# Bot 7th
# Pitching: BOS #66 Bobby Poyner
b7 = game.new_inning()

# Pitching change (BOS): #66 Bobby Poyner replaces #67 William Cuevas, batting 7th
b7.pitching_substitution(66)
b7.defensive_substitution(7, 66, "1")

# Defensive change (BOS): #30 Tzu-Wei Lin replaces #67 William Cuevas (P), playing SS, batting 9th
b7.defensive_substitution(9, 30, "6")

# 7. ATL #25 Tyler Flowers (X - X - X)
b7.new_ab()
b7.pitch_list("c b")
b7.out("L8")

# 8. ATL #8  Charlie Culberson (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")

# Offensive change (ATL): Pinch-hitter #23 Adam Duvall replaces #63 Jesse Biddle, batting 9th
b7.offensive_substitution(9, 23, "PH")

# 9. ATL #23 Adam Duvall (X - X - X)
b7.new_ab()
b7.pitch_list("c f s")
b7.out("K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: ATL #58 Dan Winkler
t8 = game.new_inning()

# Pitching change (ATL): #58 Dan Winkler replaces #63 Jesse Biddle, batting 3rd
t8.pitching_substitution(58)
t8.defensive_substitution(3, 58, "1")

# Defensive switch (ATL): #23 Adam Duvall moves to RF
t8.defensive_switch(23, "9")

# 8. BOS #7  Christian Vázquez (X - X - X)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.advance(2, "30 1B")
t8.advance(3, "19 1B")
t8.advance(4, "23 2B")

# 9. BOS #30 Tzu-Wei Lin (X - X - 7)
t8.new_ab()
t8.pitch_list("f")
t8.hit(1)
t8.advance(2, "19 1B")
t8.advance(4, "23 2B")

# 1. BOS #19 Jackie Bradley Jr. (X - 7 - 30)
t8.new_ab()
t8.pitch_list("c")
t8.hit(1)
t8.advance(3, "23 2B")
t8.advance(4, "16 1B")

# 2. BOS #23 Blake Swihart (7 - 30 - 19)
t8.new_ab()
t8.pitch_list("c b b")
t8.hit(2, rbis=2)
t8.advance(3, "16 1B")
t8.advance(4, "25 SF7")

# Pitching change (ATL): #48 Jonny Venters replaces #58 Dan Winkler, batting 3rd
t8.pitching_substitution(48)
t8.defensive_substitution(3, 48, "1")

# 3. BOS #16 Andrew Benintendi (19 - 23 - X)
t8.new_ab()
t8.pitch_list("s s")
t8.hit(1, rbis=1)
t8.advance(3, "0 E5")
t8.advance(4, "5 1B")

# Offensive change (BOS): Pinch-hitter #25 Steve Pearce replaces #18 Mitch Moreland, batting 4th
t8.offensive_substitution(4, 25, "PH")

# 4. BOS #25 Steve Pearce (23 - X - 16)
t8.new_ab()
t8.pitch_list("b 1 b c")
t8.out("SF7", rbis=1)

# 5. BOS #0  Brandon Phillips (X - X - 16)
t8.new_ab()
t8.pitch_list("c s 1 f b")
t8.error(5)
t8.reach("E5", end_base=2)
t8.advance("U", "5 1B")

# Pitching change (ATL): #46 Brad Brach replaces #48 Jonny Venters, batting 3rd
t8.pitching_substitution(46)
t8.defensive_substitution(3, 46, "1")

# Offensive change (BOS): Pinch-hitter #5 Ian Kinsler replaces #11 Rafael Devers, batting 6th
t8.offensive_substitution(6, 5, "PH")

# 6. BOS #5  Ian Kinsler (16 - 0 - X)
t8.new_ab()
t8.pitch_list("b")
t8.hit(1, rbis=2)
t8.advance(3, "7 1B")

# Offensive change (BOS): Pinch-hitter #36 Eduardo Núñez replaces #66 Bobby Poyner, batting 7th
t8.offensive_substitution(7, 36, "PH")

# 7. BOS #36 Eduardo Núñez (X - X - 5)
t8.new_ab()
t8.pitch_list("1 b f b f d 1")
t8.out("F8")

# 8. BOS #7  Christian Vázquez (X - X - 5)
t8.new_ab()
t8.hit(1)
t8.advance(2, "2 BB")

# Pitching change (ATL): #33 A.J. Minter replaces #46 Brad Brach, batting 9th
t8.pitching_substitution(33)
t8.defensive_substitution(9, 33, "1")

# Offensive change (BOS): Pinch-hitter #2 Xander Bogaerts replaces #30 Tzu-Wei Lin, batting 9th
t8.offensive_substitution(9, 2, "PH")

# Defensive change (ATL): #5 Freddie Freeman replaces #46 Brad Brach (P), playing 1B, batting 3rd
t8.defensive_substitution(3, 5, "3")

# Defensive switch (ATL): #17 Johan Camargo moves to SS
t8.defensive_switch(17, "6")

# Defensive switch (ATL): #27 Ryan Flaherty moves to 3B
t8.defensive_switch(27, "5")

# Defensive switch (ATL): #8 Charlie Culberson moves to RF
t8.defensive_switch(8, "9")

# 9. BOS #2  Xander Bogaerts (5 - X - 7)
t8.new_ab()
t8.pitch_list("b d c b b")
t8.reach("BB")

# Offensive change (BOS): Pinch-hitter #50 Mookie Betts replaces #19 Jackie Bradley Jr., batting 1st
t8.offensive_substitution(1, 50, "PH")

# 1. BOS #50 Mookie Betts (5 - 7 - 2)
t8.new_ab()
t8.pitch_list("b b c c f f c")
t8.out("!K")


# Bot 8th
# Pitching: BOS #44 Brandon Workman
b8 = game.new_inning()

# Pitching change (BOS): #44 Brandon Workman replaces #66 Bobby Poyner, batting 7th
b8.pitching_substitution(44)
b8.defensive_substitution(7, 44, "1")

# Defensive switch (BOS): #50 Mookie Betts moves to CF
b8.defensive_switch(50, "8")

# Defensive switch (BOS): #25 Steve Pearce moves to 1B
b8.defensive_switch(25, "3")

# Defensive switch (BOS): #0 Brandon Phillips moves to 3B
b8.defensive_switch(0, "5")

# Defensive switch (BOS): #5 Ian Kinsler moves to 2B
b8.defensive_switch(5, "4")

# Defensive switch (BOS): #2 Xander Bogaerts moves to SS
b8.defensive_switch(2, "6")

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c b s b f s")
b8.out("K")

# 2. ATL #11 Ender Inciarte (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("L8")

# 3. ATL #5  Freddie Freeman (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.hit(4)

# 4. ATL #17 Johan Camargo (X - X - X)
b8.new_ab()
b8.pitch_list("c b b")
b8.out("G4-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: ATL #33 A.J. Minter
t9 = game.new_inning()

# Defensive switch (ATL): #17 Johan Camargo moves to 3B
t9.defensive_switch(17, "5")

# Defensive change (ATL): #7 Dansby Swanson replaces #27 Ryan Flaherty (PR), playing SS, batting 5th
t9.defensive_substitution(5, 7, "6")

# Defensive change (ATL): #18 Lane Adams replaces #8 Charlie Culberson (SS), playing RF, batting 8th
t9.defensive_substitution(8, 18, "9")

# 2. BOS #23 Blake Swihart (X - X - X)
t9.new_ab()
t9.pitch_list("b f b s f")
t9.out("P4")

# 3. BOS #16 Andrew Benintendi (X - X - X)
t9.new_ab()
t9.pitch_list("c f f")
t9.hit(1)
t9.advance(4, "0 HR")

# 4. BOS #25 Steve Pearce (X - X - 16)
t9.new_ab()
t9.pitch_list("b c 1 1 b f c")
t9.out("!K")

# 5. BOS #0  Brandon Phillips (X - X - 16)
t9.new_ab()
t9.pitch_list("1")
t9.hit(4, rbis=2)

# 6. BOS #5  Ian Kinsler (X - X - X)
t9.new_ab()
t9.pitch_list("c c b f b f f s")
t9.out("K")


# Bot 9th
# Pitching: BOS #46 Craig Kimbrel
b9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #44 Brandon Workman, batting 7th
b9.pitching_substitution(46)
b9.defensive_substitution(7, 46, "1")

# 5. ATL #7  Dansby Swanson (X - X - X)
b9.new_ab()
b9.pitch_list("s s s")
b9.out("K")

# 6. ATL #1  Ozzie Albies (X - X - X)
b9.new_ab()
b9.pitch_list("b c")
b9.out("F8")

# 7. ATL #25 Tyler Flowers (X - X - X)
b9.new_ab()
b9.pitch_list("b c b b c b")
b9.reach("BB")
# Offensive change (ATL): Pinch-runner #62 Touki Toussaint replaces #25 Tyler Flowers
b9.offensive_substitution(7, 62, "PR")
b9.atbase("PR")

# 8. ATL #18 Lane Adams (X - X - 25)
b9.new_ab()
b9.pitch_list("b s b f b s")
b9.out("K")

# Winning team: BOS
# WP: BOS #44 Brandon Workman
game.winning_pitcher(44, is_away_team=True)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46, is_away_team=True)

# Loser team: ATL
# LP: ATL #33 A.J. Minter
game.losing_pitcher(33)

# print(game)
game.generate_scorecard()
