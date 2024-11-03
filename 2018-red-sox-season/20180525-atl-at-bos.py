import os
from baseball_scorecard.baseball_scorecard import Scorecard

# ATL @ BOS, 2018-05-25
# https://www.baseball-reference.com/boxes/BOS/BOS201805250.shtml
# https://www.mlb.com/gameday/braves-vs-red-sox/2018/05/25/530155/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-25 19:11-22:24",
        "at": "Fenway Park, Boston, MA",
        "att": "37,008",
        "temp": "85F, Partly Cloudy",
        "wind": "15mph, Out To CF",
        "away": {
            "team": "Atlanta Braves",
            "starter": 49,
            "roster": {
                # Lineup
                1: "Ozzie Albies",
                13: "Ronald Acuña Jr.",
                5: "Freddie Freeman",
                22: "Nick Markakis",
                24: "Kurt Suzuki",
                11: "Ender Inciarte",
                25: "Tyler Flowers",
                17: "Johan Camargo",
                7: "Dansby Swanson",
                # Starting pitcher
                49: "Julio Teheran",
                # Bench
                27: "Ryan Flaherty",
                20: "Preston Tucker",
                8: "Charlie Culberson",
                # Bullpen
                39: "Sam Freeman",
                51: "Shane Carle",
                30: "Peter Moylan",
                58: "Dan Winkler",
                38: "Arodys Vizcaíno",
                45: "Matt Wisler",
                33: "A.J. Minter",
                26: "Mike Foltynewicz",
                50: "Lucas Sims",
                15: "Sean Newcomb",
                63: "Jesse Biddle",
                32: "Brandon McCarthy",
            },
            "lefties": [39, 33, 15, 63],
            "lineup": [
                [1, "4"],
                [13, "9"],
                [5, "3"],
                [22, "7"],
                [24, "0"],
                [11, "8"],
                [25, "2"],
                [17, "5"],
                [7, "6"],
            ],
            "bench": [
                [27, "2B"],
                [20, "LF"],
                [8, "1B"],
            ],
            "bullpen": [39, 51, 30, 58, 38, 45, 33, 26, 50, 15, 63, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 57,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                57: "Eduardo Rodriguez",
                # Bench
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                15: "Dustin Pedroia",
                3: "Sandy León",
                # Bullpen
                35: "Steven Wright",
                22: "Rick Porcello",
                41: "Chris Sale",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [57, 41, 31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [18, "3"],
                [2, "6"],
                [11, "5"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [36, "SS"],
                [23, "C"],
                [15, "2B"],
                [3, "C"],
            ],
            "bullpen": [35, 22, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Jeff Nelson",
            "1B": "Laz Diaz",
            "2B": "Manny Gonzalez",
            "3B": "Andy Fletcher",
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
# Pitching: BOS #57 Eduardo Rodriguez
t1 = game.new_inning()

# 1. ATL #1  Ozzie Albies (X - X - X)
t1.new_ab()
t1.pitch_list("f")
t1.hit(1)
t1.advance(2, "22 BB")
t1.thrown_out(3, "24 FC5", 3, 57)

# 2. ATL #13 Ronald Acuña Jr. (X - X - 1)
t1.new_ab()
t1.pitch_list("b f b s s")
t1.out("K")

# 3. ATL #5  Freddie Freeman (X - X - 1)
t1.new_ab()
t1.pitch_list("c 1 s s")
t1.out("K")

# 4. ATL #22 Nick Markakis (X - X - 1)
t1.new_ab()
t1.pitch_list("b b b c c b")
t1.reach("BB")

# 5. ATL #24 Kurt Suzuki (X - 1 - 22)
t1.new_ab(is_risp=True)
t1.pitch_list("c")
t1.reach("FC5")


# Bot 1st
# Pitching: ATL #49 Julio Teheran
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c f b")
b1.out("F8")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c s")
b1.out("F8")

# 3. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c s f b b")
b1.out("L9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #57 Eduardo Rodriguez
t2 = game.new_inning()

# 6. ATL #11 Ender Inciarte (X - X - X)
t2.new_ab()
t2.pitch_list("f b b")
t2.out("G3")

# 7. ATL #25 Tyler Flowers (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b f")
t2.hit(1)
t2.advance(2, "17 1B")

# 8. ATL #17 Johan Camargo (X - X - 25)
t2.new_ab()
t2.pitch_list("f b f")
t2.hit(1)

# 9. ATL #7  Dansby Swanson (X - 25 - 17)
t2.new_ab(is_risp=True)
t2.pitch_list("b")
t2.out("L8")

# 1. ATL #1  Ozzie Albies (X - 25 - 17)
t2.new_ab(is_risp=True)
t2.pitch_list("f")
t2.out("F9")


# Bot 2nd
# Pitching: ATL #49 Julio Teheran
b2 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b2.new_ab()
b2.pitch_list("b")
b2.hit(1)
b2.thrown_out(2, "2 FC6-4", 1, 49)

# 5. BOS #2  Xander Bogaerts (X - X - 18)
b2.new_ab()
b2.pitch_list("c b")
b2.reach("FC6-4")
b2.advance(2, "12 BB")

# 6. BOS #11 Rafael Devers (X - X - 2)
b2.new_ab()
b2.pitch_list("s s f s")
b2.out("K")

# 7. BOS #12 Brock Holt (X - X - 2)
b2.new_ab()
b2.pitch_list("1 b b b b")
b2.reach("BB")

# 8. BOS #7  Christian Vázquez (X - 2 - 12)
b2.new_ab(is_risp=True)
b2.pitch_list("c b")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #57 Eduardo Rodriguez
t3 = game.new_inning()

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.hit(1)
t3.advance(2, "5 1B")
t3.advance(4, "22 2B")

# 3. ATL #5  Freddie Freeman (X - X - 13)
t3.new_ab()
t3.pitch_list("b c b")
t3.hit(1)
t3.advance(4, "22 2B")

# 4. ATL #22 Nick Markakis (X - 13 - 5)
t3.new_ab(is_risp=True)
t3.hit(2, rbis=2)

# 5. ATL #24 Kurt Suzuki (X - 22 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f f f s")
t3.out("K")

# 6. ATL #11 Ender Inciarte (X - 22 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("f c b")
t3.out("G6-3")

# 7. ATL #25 Tyler Flowers (X - 22 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("c b")
t3.out("G5-3")


# Bot 3rd
# Pitching: ATL #49 Julio Teheran
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c b b b s")
b3.out("G4-3")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("c b b s b s")
b3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c b f b b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #57 Eduardo Rodriguez
t4 = game.new_inning()

# 8. ATL #17 Johan Camargo (X - X - X)
t4.new_ab()
t4.pitch_list("c")
t4.out("P4")

# 9. ATL #7  Dansby Swanson (X - X - X)
t4.new_ab()
t4.pitch_list("c b f b b s")
t4.out("K")

# 1. ATL #1  Ozzie Albies (X - X - X)
t4.new_ab()
t4.pitch_list("b b b b")
t4.reach("BB")

# 2. ATL #13 Ronald Acuña Jr. (X - X - 1)
t4.new_ab()
t4.pitch_list("s f b")
t4.out("L8")


# Bot 4th
# Pitching: ATL #49 Julio Teheran
b4 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("s s b b")
b4.hit(4)

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b b c b c")
b4.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b")
b4.hit(4)

# 6. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("c b b b b")
b4.reach("BB")
b4.thrown_out(1, "12 PO", 2, 49)

# 7. BOS #12 Brock Holt (X - X - 11)
b4.new_ab()
b4.pitch_list("c b 1 c")
b4.out("G3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #57 Eduardo Rodriguez
t5 = game.new_inning()

# 3. ATL #5  Freddie Freeman (X - X - X)
t5.new_ab()
t5.pitch_list("b b s b f s")
t5.out("K")

# 4. ATL #22 Nick Markakis (X - X - X)
t5.new_ab()
t5.pitch_list("s t b f b b c")
t5.out("!K")

# 5. ATL #24 Kurt Suzuki (X - X - X)
t5.new_ab()
t5.pitch_list("f b f f b")
t5.out("G6-3")


# Bot 5th
# Pitching: ATL #49 Julio Teheran
b5 = game.new_inning()

# 8. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("c b")
b5.out("G4-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.hit(3)
b5.advance(4, "16 SF8")

# 1. BOS #50 Mookie Betts (19 - X - X)
b5.new_ab(is_risp=True)
b5.pitch_list("b c b b s b")
b5.reach("BB")
b5.advance(2, "28 SB")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b5.new_ab(is_risp=True)
b5.pitch_list("1 1 1 b b s 1 f f 1")
b5.out("SF8", rbis=1)

# 3. BOS #28 J.D. Martinez (X - X - 50)
b5.new_ab(is_risp=True)
b5.pitch_list("1 c c b f")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 6. ATL #11 Ender Inciarte (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f s")
t6.out("K")

# 7. ATL #25 Tyler Flowers (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G6-3")

# 8. ATL #17 Johan Camargo (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b b")
t6.reach("BB")

# Pitching change (BOS): #37 Heath Hembree replaces #57 Eduardo Rodriguez
t6.pitching_substitution(37)

# 9. ATL #7  Dansby Swanson (X - X - 17)
t6.new_ab()
t6.pitch_list("s f b f b s")
t6.out("K")


# Bot 6th
# Pitching: ATL #49 Julio Teheran
b6 = game.new_inning()

# 4. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f c")
b6.out("!K")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f b")
b6.out("G1-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b6.new_ab()
b6.pitch_list("b s b b")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #56 Joe Kelly
t7 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #37 Heath Hembree
t7.pitching_substitution(56)

# 1. ATL #1  Ozzie Albies (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("F7")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("f f b b f b s")
t7.out("K")

# 3. ATL #5  Freddie Freeman (X - X - X)
t7.new_ab()
t7.pitch_list("c b b f b b")
t7.reach("BB")

# 4. ATL #22 Nick Markakis (X - X - 5)
t7.new_ab()
t7.pitch_list("1")
t7.out("G1-3")


# Bot 7th
# Pitching: ATL #63 Jesse Biddle
b7 = game.new_inning()

# Pitching change (ATL): #63 Jesse Biddle replaces #49 Julio Teheran
b7.pitching_substitution(63)

# 7. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.pitch_list("b c")
b7.hit(1)
b7.advance(2, "50 SB")
b7.advance(4, "50 HR")

# 8. BOS #7  Christian Vázquez (X - X - 12)
b7.new_ab()
b7.out("L4")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 12)
b7.new_ab()
b7.pitch_list("c s c")
b7.out("!K")

# Pitching change (ATL): #45 Matt Wisler replaces #63 Jesse Biddle
b7.pitching_substitution(45)

# 1. BOS #50 Mookie Betts (X - X - 12)
b7.new_ab(is_risp=True)
b7.pitch_list("f b")
b7.hit(4, rbis=2)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b7.new_ab()
b7.pitch_list("b c b c f")
b7.out("(F)P5")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #32 Matt Barnes
t8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #56 Joe Kelly
t8.pitching_substitution(32)

# 5. ATL #24 Kurt Suzuki (X - X - X)
t8.new_ab()
t8.pitch_list("b f f b f")
t8.out("F9")

# 6. ATL #11 Ender Inciarte (X - X - X)
t8.new_ab()
t8.pitch_list("m")
t8.out("G4-3")

# 7. ATL #25 Tyler Flowers (X - X - X)
t8.new_ab()
t8.pitch_list("s b f b c")
t8.out("!K")


# Bot 8th
# Pitching: ATL #45 Matt Wisler
b8 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.out("G5-3")

# 4. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b b c")
b8.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("s s b b b")
b8.out("G6-3")

# 6. BOS #11 Rafael Devers (X - X - X)
b8.new_ab()
b8.pitch_list("b b s")
b8.out("F7")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
t9.pitching_substitution(46)

# 8. ATL #17 Johan Camargo (X - X - X)
t9.new_ab()
t9.pitch_list("f b b b s c")
t9.out("!K")

# 9. ATL #7  Dansby Swanson (X - X - X)
t9.new_ab()
t9.pitch_list("c s b")
t9.hit(2)
t9.advance(3, "1 G3-1")

# 1. ATL #1  Ozzie Albies (X - 7 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b c f")
t9.out("G3-1")

# 2. ATL #13 Ronald Acuña Jr. (7 - X - X)
t9.new_ab(is_risp=True)
t9.pitch_list("s s s")
t9.out("K")

# Winning team: BOS
# WP: BOS #57 Eduardo Rodriguez
game.winning_pitcher(57)

# Loser team: ATL
# LP: ATL #49 Julio Teheran
game.losing_pitcher(49, is_away_team=True)

# print(game)
game.generate_scorecard()
