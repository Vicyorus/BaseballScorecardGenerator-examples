import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ ATL, 2018-09-04
# https://www.baseball-reference.com/boxes/ATL/ATL201809040.shtml
# https://www.mlb.com/gameday/red-sox-vs-braves/2018/09/04/531478/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-04 19:35-22:38",
        "at": "SunTrust Park, Atlanta, GA",
        "att": "35,333",
        "temp": "83F, Partly Cloudy",
        "wind": "6mph, L To R",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                5: "Ian Kinsler",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                25: "Steve Pearce",
                36: "Eduardo Núñez",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                22: "Rick Porcello",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                30: "Tzu-Wei Lin",
                18: "Mitch Moreland",
                12: "Brock Holt",
                59: "Sam Travis",
                11: "Rafael Devers",
                23: "Blake Swihart",
                16: "Andrew Benintendi",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
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
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [57, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [5, "4"],
                [28, "7"],
                [2, "6"],
                [25, "3"],
                [36, "5"],
                [19, "8"],
                [3, "2"],
                [22, "1"],
            ],
            "bench": [
                [30, "OF"],
                [18, "1B"],
                [12, "2B"],
                [59, "1B"],
                [11, "3B"],
                [23, "C"],
                [16, "LF"],
                [0, "2B"],
                [7, "C"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 17, 32],
        },
        "home": {
            "team": "Atlanta Braves",
            "starter": 15,
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
                15: "Sean Newcomb",
                # Starting pitcher
                15: "Sean Newcomb",
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
                62: "Touki Toussaint",
                58: "Dan Winkler",
                49: "Julio Teheran",
                33: "A.J. Minter",
                26: "Mike Foltynewicz",
                36: "Kolby Allard",
                63: "Jesse Biddle",
                19: "Aníbal Sánchez",
                73: "Kyle Wright",
                46: "Brad Brach",
                72: "Bryse Wilson",
            },
            "lefties": [15, 48, 39, 33, 36, 63],
            "lineup": [
                [13, "7"],
                [11, "8"],
                [5, "3"],
                [22, "9"],
                [17, "5"],
                [24, "2"],
                [1, "4"],
                [7, "6"],
                [15, "1"],
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
            "bullpen": [48, 64, 39, 51, 45, 62, 58, 49, 33, 26, 36, 63, 19, 73, 46, 72],
        },
        "umpires": {
            "HP": "Jansen Visconti",
            "1B": "Tim Timmons",
            "2B": "Mike Muchlinski",
            "3B": "Mike Winters",
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
# Pitching: ATL #15 Sean Newcomb
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F9")

# 2. BOS #5  Ian Kinsler (X - X - X)
t1.new_ab()
t1.pitch_list("b")
t1.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
t1.new_ab()
t1.pitch_list("b f f s")
t1.out("K")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("G5-3")

# 2. ATL #11 Ender Inciarte (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("F8")

# 3. ATL #5  Freddie Freeman (X - X - X)
b1.new_ab()
b1.pitch_list("c s f f f f")
b1.out("P5")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: ATL #15 Sean Newcomb
t2 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b b c s")
t2.out("L5")

# 5. BOS #25 Steve Pearce (X - X - X)
t2.new_ab()
t2.pitch_list("b b s s")
t2.hit(1)

# 6. BOS #36 Eduardo Núñez (X - X - 25)
t2.new_ab()
t2.pitch_list("b b d")
t2.out("L6")

# 7. BOS #19 Jackie Bradley Jr. (X - X - 25)
t2.new_ab()
t2.out("F9")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 4. ATL #22 Nick Markakis (X - X - X)
b2.new_ab()
b2.pitch_list("b b c")
b2.out("L8")

# 5. ATL #17 Johan Camargo (X - X - X)
b2.new_ab()
b2.pitch_list("b b c s f")
b2.out("(F)F9")

# 6. ATL #24 Kurt Suzuki (X - X - X)
b2.new_ab()
b2.pitch_list("s b b f f")
b2.hit(4)

# 7. ATL #1  Ozzie Albies (X - X - X)
b2.new_ab()
b2.pitch_list("b b f f")
b2.error(4)
b2.reach("E4")
b2.advance(2, "7 HBP")

# 8. ATL #7  Dansby Swanson (X - X - 1)
b2.new_ab()
b2.pitch_list("b c 1 f b")
b2.reach("HBP")
# Offensive change (ATL): Pinch-runner #8 Charlie Culberson replaces #7 Dansby Swanson
b2.offensive_substitution(8, 8, "PR")
b2.atbase("PR")

# 9. ATL #15 Sean Newcomb (X - 1 - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("b s c f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: ATL #15 Sean Newcomb
t3 = game.new_inning()

# Defensive switch (ATL): #8 Charlie Culberson moves to SS
t3.defensive_switch(8, "6")

# 8. BOS #3  Sandy León (X - X - X)
t3.new_ab()
t3.pitch_list("c b c")
t3.out("G4-3")

# 9. BOS #22 Rick Porcello (X - X - X)
t3.new_ab()
t3.pitch_list("c s")
t3.out("G6-3")

# 1. BOS #50 Mookie Betts (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b b")
t3.reach("BB")
t3.advance(2, "5 SB")

# 2. BOS #5  Ian Kinsler (X - X - 50)
t3.new_ab(is_risp=True)
t3.pitch_list("d b c b")
t3.out("G6-3")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("s f b s")
b3.out("K")

# 2. ATL #11 Ender Inciarte (X - X - X)
b3.new_ab()
b3.pitch_list("b b c f")
b3.out("F8")

# 3. ATL #5  Freddie Freeman (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f f")
b3.hit(1)
b3.advance(2, "22 BB")

# 4. ATL #22 Nick Markakis (X - X - 5)
b3.new_ab()
b3.pitch_list("b b b c b")
b3.reach("BB")

# 5. ATL #17 Johan Camargo (X - 5 - 22)
b3.new_ab(is_risp=True)
b3.pitch_list("c f b f s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: ATL #15 Sean Newcomb
t4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
t4.new_ab()
t4.pitch_list("c b b b d")
t4.reach("BB")
t4.advance(3, "2 2B")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
t4.new_ab()
t4.pitch_list("b b")
t4.hit(2)

# 5. BOS #25 Steve Pearce (28 - 2 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("b b b b")
t4.reach("BB")

# 6. BOS #36 Eduardo Núñez (28 - 2 - 25)
t4.new_ab(is_risp=True)
t4.pitch_list("f d")
t4.out("P6")

# 7. BOS #19 Jackie Bradley Jr. (28 - 2 - 25)
t4.new_ab(is_risp=True)
t4.pitch_list("c b f c")
t4.out("!K")

# 8. BOS #3  Sandy León (28 - 2 - 25)
t4.new_ab(is_risp=True)
t4.pitch_list("b")
t4.out("L8")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 6. ATL #24 Kurt Suzuki (X - X - X)
b4.new_ab()
b4.pitch_list("b c f")
b4.out("G4-3")

# 7. ATL #1  Ozzie Albies (X - X - X)
b4.new_ab()
b4.pitch_list("f b b f s")
b4.out("K")

# 8. ATL #8  Charlie Culberson (X - X - X)
b4.new_ab()
b4.pitch_list("c s s")
b4.out("K")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: ATL #15 Sean Newcomb
t5 = game.new_inning()

# 9. BOS #22 Rick Porcello (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "50 BB")
t5.advance(3, "28 1B")
t5.advance(4, "2 BB")

# 1. BOS #50 Mookie Betts (X - X - 22)
t5.new_ab()
t5.pitch_list("c b b b s b")
t5.reach("BB")
t5.advance(2, "28 1B")
t5.advance(3, "2 BB")
t5.advance(4, "25 1B")

# 2. BOS #5  Ian Kinsler (X - 22 - 50)
t5.new_ab(is_risp=True)
t5.pitch_list("b b f")
t5.out("F9")

# 3. BOS #28 J.D. Martinez (X - 22 - 50)
t5.new_ab(is_risp=True)
t5.hit(1)
t5.advance(2, "2 BB")
t5.advance(3, "25 1B")
t5.advance(4, "36 G5-3")

# 4. BOS #2  Xander Bogaerts (22 - 50 - 28)
t5.new_ab(is_risp=True)
t5.pitch_list("d c b b b")
t5.reach("BB", rbis=1)
t5.advance(2, "25 1B")
t5.advance(3, "36 G5-3")

# Pitching change (ATL): #51 Shane Carle replaces #15 Sean Newcomb, batting 9th
t5.pitching_substitution(51)
t5.defensive_substitution(9, 51, "1")

# 5. BOS #25 Steve Pearce (50 - 28 - 2)
t5.new_ab(is_risp=True)
t5.pitch_list("b f b")
t5.hit(1, rbis=1)
t5.advance(2, "36 G5-3")

# 6. BOS #36 Eduardo Núñez (28 - 2 - 25)
t5.new_ab(is_risp=True)
t5.pitch_list("c")
t5.out("G5-3", rbis=1)

# 7. BOS #19 Jackie Bradley Jr. (2 - 25 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("v v v v")
t5.reach("IBB")

# 8. BOS #3  Sandy León (2 - 25 - 19)
t5.new_ab(is_risp=True)
t5.pitch_list("b s b b f s")
t5.out("K")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# Offensive change (ATL): Pinch-hitter #8 Preston Tucker replaces #51 Shane Carle, batting 9th
b5.offensive_substitution(9, 8, "PH")

# 9. ATL #8  Preston Tucker (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.reach("HBP")

# 1. ATL #13 Ronald Acuña Jr. (X - X - 8)
b5.new_ab()
b5.pitch_list("c f b f")
b5.out("L9")

# 2. ATL #11 Ender Inciarte (X - X - 8)
b5.new_ab()
b5.pitch_list("s f f b f")
b5.out("F8")

# 3. ATL #5  Freddie Freeman (X - X - 8)
b5.new_ab()
b5.pitch_list("b s")
b5.out("L8")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: ATL #64 Luke Jackson
t6 = game.new_inning()

# Pitching change (ATL): #64 Luke Jackson replaces #51 Shane Carle, batting 9th
t6.pitching_substitution(64)
t6.defensive_substitution(9, 64, "1")

# Offensive change (BOS): Pinch-hitter #11 Rafael Devers replaces #22 Rick Porcello, batting 9th
t6.offensive_substitution(9, 11, "PH")

# 9. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("b b b b")
t6.reach("BB")
t6.advance(2, "50 G5-3")
t6.advance(3, "5 1B")
t6.advance(4, "25 1B")

# 1. BOS #50 Mookie Betts (X - X - 11)
t6.new_ab()
t6.pitch_list("b b b c c")
t6.out("G5-3")

# 2. BOS #5  Ian Kinsler (X - 11 - X)
t6.new_ab(is_risp=True)
t6.hit(1)
t6.advance(2, "2 BB")
t6.advance(4, "25 1B")

# 3. BOS #28 J.D. Martinez (11 - X - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("b c b 1")
t6.out("(F)P3")

# 4. BOS #2  Xander Bogaerts (11 - X - 5)
t6.new_ab(is_risp=True)
t6.pitch_list("b b c d b")
t6.reach("BB")
t6.advance(2, "25 1B")

# 5. BOS #25 Steve Pearce (11 - 5 - 2)
t6.new_ab(is_risp=True)
t6.pitch_list("b")
t6.hit(1, rbis=2)

# 6. BOS #36 Eduardo Núñez (X - 2 - 25)
t6.new_ab(is_risp=True)
t6.pitch_list("c f s")
t6.out("K")


# Bot 6th
# Pitching: BOS #35 Steven Wright
b6 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #22 Rick Porcello, batting 9th
b6.pitching_substitution(35)
b6.defensive_substitution(9, 35, "1")

# 4. ATL #22 Nick Markakis (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b f")
b6.out("F7")

# 5. ATL #17 Johan Camargo (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G5-3")

# 6. ATL #24 Kurt Suzuki (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.hit(2)

# 7. ATL #1  Ozzie Albies (X - 24 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c b b b")
b6.reach("BB")

# 8. ATL #8  Charlie Culberson (X - 24 - 1)
b6.new_ab(is_risp=True)
b6.pitch_list("c f f f s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: ATL #73 Kyle Wright
t7 = game.new_inning()

# Pitching change (ATL): #73 Kyle Wright replaces #64 Luke Jackson, batting 6th
t7.pitching_substitution(73)
t7.defensive_substitution(6, 73, "1")

# Defensive change (ATL): #12 René Rivera replaces #64 Luke Jackson (P), playing C, batting 9th
t7.defensive_substitution(9, 12, "2")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("b s b c s")
t7.out("K")

# 8. BOS #3  Sandy León (X - X - X)
t7.new_ab()
t7.pitch_list("c b f b b s")
t7.out("K")

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #35 Steven Wright, batting 9th
t7.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c b b")
t7.out("G3")


# Bot 7th
# Pitching: BOS #56 Joe Kelly
b7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #35 Steven Wright, batting 9th
b7.pitching_substitution(56)
b7.defensive_substitution(9, 56, "1")

# 9. ATL #12 René Rivera (X - X - X)
b7.new_ab()
b7.pitch_list("c s s")
b7.out("K")

# 1. ATL #13 Ronald Acuña Jr. (X - X - X)
b7.new_ab()
b7.pitch_list("b s f f b f f b b")
b7.reach("BB")

# 2. ATL #11 Ender Inciarte (X - X - 13)
b7.new_ab()
b7.pitch_list("s f s")
b7.out("K")

# 3. ATL #5  Freddie Freeman (X - X - 13)
b7.new_ab()
b7.pitch_list("b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: ATL #73 Kyle Wright
t8 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("F9")

# 2. BOS #5  Ian Kinsler (X - X - X)
t8.new_ab()
t8.pitch_list("b b b c b")
t8.reach("BB")
t8.advance(2, "2 SB")

# 3. BOS #28 J.D. Martinez (X - X - 5)
t8.new_ab()
t8.pitch_list("c b d")
t8.out("F9")

# 4. BOS #2  Xander Bogaerts (X - X - 5)
t8.new_ab(is_risp=True)
t8.pitch_list("s b")
t8.out("F7")


# Bot 8th
# Pitching: BOS #70 Ryan Brasier
b8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly, batting 9th
b8.pitching_substitution(70)
b8.defensive_substitution(9, 70, "1")

# 4. ATL #22 Nick Markakis (X - X - X)
b8.new_ab()
b8.pitch_list("f b")
b8.hit(1)
b8.thrown_out(2, "17 DP1-6-3", 1, 70)

# 5. ATL #17 Johan Camargo (X - X - 22)
b8.new_ab()
b8.pitch_list("s s")
b8.out("DP1-6-3")

# Offensive change (ATL): Pinch-hitter #20 Lucas Duda replaces #73 Kyle Wright, batting 6th
b8.offensive_substitution(6, 20, "PH")

# 6. ATL #20 Lucas Duda (X - X - X)
b8.new_ab()
b8.pitch_list("c f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: ATL #46 Brad Brach
t9 = game.new_inning()

# Pitching change (ATL): #46 Brad Brach replaces #73 Kyle Wright, batting 6th
t9.pitching_substitution(46)
t9.defensive_substitution(6, 46, "1")

# 5. BOS #25 Steve Pearce (X - X - X)
t9.new_ab()
t9.pitch_list("c b f b t")
t9.out("KT")

# 6. BOS #36 Eduardo Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("P6")

# 7. BOS #19 Jackie Bradley Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("f b f b")
t9.hit(2)

# 8. BOS #3  Sandy León (X - 19 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("s s d")
t9.out("G1-4-3")


# Bot 9th
# Pitching: BOS #37 Heath Hembree
b9 = game.new_inning()

# Pitching change (BOS): #37 Heath Hembree replaces #70 Ryan Brasier, batting 9th
b9.pitching_substitution(37)
b9.defensive_substitution(9, 37, "1")

# 7. ATL #1  Ozzie Albies (X - X - X)
b9.new_ab()
b9.pitch_list("f f b b c")
b9.out("!K")

# 8. ATL #8  Charlie Culberson (X - X - X)
b9.new_ab()
b9.out("G5-3")

# 9. ATL #12 René Rivera (X - X - X)
b9.new_ab()
b9.pitch_list("s b f s")
b9.out("K")

# Winning team: BOS
# WP: BOS #22 Rick Porcello
game.winning_pitcher(22, is_away_team=True)

# Loser team: ATL
# LP: ATL #15 Sean Newcomb
game.losing_pitcher(15)

# print(game)
game.generate_scorecard()
