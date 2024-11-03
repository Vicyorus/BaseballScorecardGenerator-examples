import os
from baseball_scorecard.baseball_scorecard import Scorecard

# ATL @ BOS, 2018-05-27
# https://www.baseball-reference.com/boxes/BOS/BOS201805270.shtml
# https://www.mlb.com/gameday/braves-vs-red-sox/2018/05/27/530185/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-27 13:08-16:01",
        "at": "Fenway Park, Boston, MA",
        "att": "36,543",
        "temp": "55F, Cloudy",
        "wind": "18mph, In From RF",
        "away": {
            "team": "Atlanta Braves",
            "starter": 26,
            "roster": {
                # Lineup
                1: "Ozzie Albies",
                13: "Ronald Acuña Jr.",
                5: "Freddie Freeman",
                22: "Nick Markakis",
                24: "Kurt Suzuki",
                11: "Ender Inciarte",
                25: "Tyler Flowers",
                7: "Dansby Swanson",
                8: "Charlie Culberson",
                # Starting pitcher
                26: "Mike Foltynewicz",
                # Bench
                17: "Johan Camargo",
                27: "Ryan Flaherty",
                20: "Preston Tucker",
                # Bullpen
                39: "Sam Freeman",
                51: "Shane Carle",
                30: "Peter Moylan",
                58: "Dan Winkler",
                49: "Julio Teheran",
                38: "Arodys Vizcaíno",
                45: "Matt Wisler",
                33: "A.J. Minter",
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
                [7, "6"],
                [8, "5"],
            ],
            "bench": [
                [17, "3B"],
                [27, "2B"],
                [20, "LF"],
            ],
            "bullpen": [39, 51, 30, 58, 49, 38, 45, 33, 50, 15, 63, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                16: "Andrew Benintendi",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                15: "Dustin Pedroia",
                11: "Rafael Devers",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                12: "Brock Holt",
                28: "J.D. Martinez",
                50: "Mookie Betts",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 24],
            "lineup": [
                [16, "8"],
                [2, "6"],
                [18, "3"],
                [15, "4"],
                [11, "0"],
                [36, "5"],
                [23, "7"],
                [3, "2"],
                [19, "9"],
            ],
            "bench": [
                [12, "2B"],
                [28, "DH"],
                [50, "SS"],
                [7, "C"],
            ],
            "bullpen": [57, 35, 22, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Manny Gonzalez",
            "1B": "Andy Fletcher",
            "2B": "Jeff Nelson",
            "3B": "Laz Diaz",
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

# 1. ATL #1  Ozzie Albies (X - X - X)
t1.new_ab()
t1.pitch_list("s b c s")
t1.out("K")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("c s f b s")
t1.out("K")

# 3. ATL #5  Freddie Freeman (X - X - X)
t1.new_ab()
t1.pitch_list("b b b c f")
t1.out("L9")


# Bot 1st
# Pitching: ATL #26 Mike Foltynewicz
b1 = game.new_inning()

# 1. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.out("L9")

# 2. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("b f c s")
b1.out("K")

# 3. BOS #18 Mitch Moreland (X - X - X)
b1.new_ab()
b1.pitch_list("c b")
b1.out("L8")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 4. ATL #22 Nick Markakis (X - X - X)
t2.new_ab()
t2.pitch_list("c b b b c f f b")
t2.reach("BB")
t2.advance(2, "24 1B")
t2.advance(4, "25 HR")

# 5. ATL #24 Kurt Suzuki (X - X - 22)
t2.new_ab()
t2.pitch_list("b")
t2.hit(1)
t2.advance(4, "25 HR")

# 6. ATL #11 Ender Inciarte (X - 22 - 24)
t2.new_ab(is_risp=True)
t2.out("B5")

# 7. ATL #25 Tyler Flowers (X - 22 - 24)
t2.new_ab(is_risp=True)
t2.pitch_list("c s")
t2.hit(4, rbis=3)

# 8. ATL #7  Dansby Swanson (X - X - X)
t2.new_ab()
t2.pitch_list("b b c c f s")
t2.out("K")

# 9. ATL #8  Charlie Culberson (X - X - X)
t2.new_ab()
t2.pitch_list("b s s s")
t2.out("K")


# Bot 2nd
# Pitching: ATL #26 Mike Foltynewicz
b2 = game.new_inning()

# 4. BOS #15 Dustin Pedroia (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c b")
b2.reach("BB")
b2.advance(2, "23 BB")

# 5. BOS #11 Rafael Devers (X - X - 15)
b2.new_ab()
b2.pitch_list("c c f b s")
b2.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - 15)
b2.new_ab()
b2.pitch_list("c b f b c")
b2.out("!K")

# 7. BOS #23 Blake Swihart (X - X - 15)
b2.new_ab()
b2.pitch_list("b b b c t b")
b2.reach("BB")

# 8. BOS #3  Sandy León (X - 15 - 23)
b2.new_ab(is_risp=True)
b2.pitch_list("c f f f b s")
b2.out("K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 1. ATL #1  Ozzie Albies (X - X - X)
t3.new_ab()
t3.pitch_list("b b f f f s")
t3.out("K")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c b s b t")
t3.out("KT")

# 3. ATL #5  Freddie Freeman (X - X - X)
t3.new_ab()
t3.out("G4-3")


# Bot 3rd
# Pitching: ATL #26 Mike Foltynewicz
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("c")
b3.out("G3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("f f b b b f b")
b3.reach("BB")
b3.thrown_out(2, "2 DP6-4-3", 2, 26)

# 2. BOS #2  Xander Bogaerts (X - X - 16)
b3.new_ab()
b3.pitch_list("b")
b3.out("DP6-4-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 4. ATL #22 Nick Markakis (X - X - X)
t4.new_ab()
t4.pitch_list("f c b b")
t4.out("G4-3")

# 5. ATL #24 Kurt Suzuki (X - X - X)
t4.new_ab()
t4.pitch_list("s c s")
t4.out("K")

# 6. ATL #11 Ender Inciarte (X - X - X)
t4.new_ab()
t4.hit(2)

# 7. ATL #25 Tyler Flowers (X - 11 - X)
t4.new_ab(is_risp=True)
t4.pitch_list("c b c b b c")
t4.out("!K")


# Bot 4th
# Pitching: ATL #26 Mike Foltynewicz
b4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.out("G3")

# 4. BOS #15 Dustin Pedroia (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.out("L9")

# 5. BOS #11 Rafael Devers (X - X - X)
b4.new_ab()
b4.pitch_list("c b f b b f t")
b4.out("KT")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 8. ATL #7  Dansby Swanson (X - X - X)
t5.new_ab()
t5.pitch_list("b s b b b")
t5.reach("BB")
t5.advance(2, "8 PB")
t5.error(9)
t5.advance(4, "8 E9")

# 9. ATL #8  Charlie Culberson (X - X - 7)
t5.new_ab(is_risp=True)
t5.pitch_list("c s b f f f")
t5.pb()
t5.hit(1)
t5.advance(2, "E9")
t5.advance(3, "1 G4-3")
t5.advance(4, "5 2B")

# 1. ATL #1  Ozzie Albies (X - 8 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c c")
t5.out("G4-3")

# 2. ATL #13 Ronald Acuña Jr. (8 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("b f f b d f f b")
t5.reach("BB")
t5.advance(4, "5 2B")

# 3. ATL #5  Freddie Freeman (8 - X - 13)
t5.new_ab(is_risp=True)
t5.hit(2, rbis=2)
t5.advance(3, "T")

# Pitching change (BOS): #61 Brian Johnson replaces #41 Chris Sale
t5.pitching_substitution(61)

# 4. ATL #22 Nick Markakis (5 - X - X)
t5.new_ab(is_risp=True)
t5.out("G6-3")

# 5. ATL #24 Kurt Suzuki (5 - X - X)
t5.new_ab(is_risp=True)
t5.pitch_list("c b f")
t5.out("G6-3")


# Bot 5th
# Pitching: ATL #26 Mike Foltynewicz
b5 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c")
b5.out("G1-3")

# 7. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("c f")
b5.out("G3-1")

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("b c b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #61 Brian Johnson
t6 = game.new_inning()

# 6. ATL #11 Ender Inciarte (X - X - X)
t6.new_ab()
t6.out("F7")

# 7. ATL #25 Tyler Flowers (X - X - X)
t6.new_ab()
t6.pitch_list("c f b b b b")
t6.reach("BB")

# 8. ATL #7  Dansby Swanson (X - X - 25)
t6.new_ab()
t6.pitch_list("s")
t6.out("F7")

# 9. ATL #8  Charlie Culberson (X - X - 25)
t6.new_ab()
t6.pitch_list("c")
t6.out("L7")


# Bot 6th
# Pitching: ATL #26 Mike Foltynewicz
b6 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.out("G4-3")

# 1. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f b")
b6.hit(2)
b6.advance(4, "18 3B")

# 2. BOS #2  Xander Bogaerts (X - 16 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b c d b c")
b6.out("L4")

# 3. BOS #18 Mitch Moreland (X - 16 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b s")
b6.hit(3, rbis=1)

# 4. BOS #15 Dustin Pedroia (18 - X - X)
b6.new_ab(is_risp=True)
b6.pitch_list("c b")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #61 Brian Johnson
t7 = game.new_inning()

# 1. ATL #1  Ozzie Albies (X - X - X)
t7.new_ab()
t7.pitch_list("f")
t7.out("F7")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t7.new_ab()
t7.pitch_list("c b c b")
t7.hit(1)
# Offensive change (ATL): Pinch-runner #20 Preston Tucker replaces #13 Ronald Acuña Jr.
t7.offensive_substitution(2, 20, "PR")
t7.atbase("PR")
t7.advance(2, "5 G4-3")

# 3. ATL #5  Freddie Freeman (X - X - 13)
t7.new_ab()
t7.pitch_list("b f d")
t7.out("G4-3")

# 4. ATL #22 Nick Markakis (X - 20 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("d c")
t7.out("G6-3")


# Bot 7th
# Pitching: ATL #26 Mike Foltynewicz
b7 = game.new_inning()

# Defensive switch (ATL): #20 Preston Tucker moves to LF
b7.defensive_switch(20, "7")

# Defensive switch (ATL): #22 Nick Markakis moves to RF
b7.defensive_switch(22, "9")

# 5. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b f b s f f f")
b7.hit(2)

# 6. BOS #36 Eduardo Núñez (X - 11 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("f c")
b7.out("P3")

# 7. BOS #23 Blake Swihart (X - 11 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("s s b s")
b7.out("K")

# 8. BOS #3  Sandy León (X - 11 - X)
b7.new_ab(is_risp=True)
b7.pitch_list("c b b c b f f")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #76 Hector Velázquez
t8 = game.new_inning()

# Pitching change (BOS): #76 Hector Velázquez replaces #61 Brian Johnson
t8.pitching_substitution(76)

# 5. ATL #24 Kurt Suzuki (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.hit(2)

# 6. ATL #11 Ender Inciarte (X - 24 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.out("F8")

# 7. ATL #25 Tyler Flowers (X - 24 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("c b c s")
t8.out("K")

# 8. ATL #7  Dansby Swanson (X - 24 - X)
t8.new_ab(is_risp=True)
t8.pitch_list("b b f f b f f b")
t8.reach("BB")

# 9. ATL #8  Charlie Culberson (X - 24 - 7)
t8.new_ab(is_risp=True)
t8.pitch_list("b")
t8.out("G4-3")


# Bot 8th
# Pitching: ATL #33 A.J. Minter
b8 = game.new_inning()

# Pitching change (ATL): #33 A.J. Minter replaces #26 Mike Foltynewicz
b8.pitching_substitution(33)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.hit(1)
b8.advance(2, "2 BB")

# 1. BOS #16 Andrew Benintendi (X - X - 19)
b8.new_ab()
b8.pitch_list("b")
b8.out("(F)F7")

# 2. BOS #2  Xander Bogaerts (X - X - 19)
b8.new_ab()
b8.pitch_list("b d b b")
b8.reach("BB")

# 3. BOS #18 Mitch Moreland (X - 19 - 2)
b8.new_ab(is_risp=True)
b8.pitch_list("f c b s")
b8.out("K")

# 4. BOS #15 Dustin Pedroia (X - 19 - 2)
b8.new_ab(is_risp=True)
b8.pitch_list("c b f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #76 Hector Velázquez
t9 = game.new_inning()

# 1. ATL #1  Ozzie Albies (X - X - X)
t9.new_ab()
t9.pitch_list("f f s")
t9.out("K")

# 2. ATL #20 Preston Tucker (X - X - X)
t9.new_ab()
t9.pitch_list("f")
t9.hit(1)
t9.advance(2, "5 BB")
t9.advance(3, "22 FC3-6")
t9.advance(4, "24 1B")

# 3. ATL #5  Freddie Freeman (X - X - 20)
t9.new_ab()
t9.pitch_list("b d f d s b")
t9.reach("BB")
t9.thrown_out(2, "22 FC3-6", 2, 76)

# 4. ATL #22 Nick Markakis (X - 20 - 5)
t9.new_ab(is_risp=True)
t9.pitch_list("c b c d")
t9.reach("FC3-6")
t9.advance(2, "24 1B")

# 5. ATL #24 Kurt Suzuki (20 - X - 22)
t9.new_ab(is_risp=True)
t9.hit(1, rbis=1)

# 6. ATL #11 Ender Inciarte (X - 22 - 24)
t9.new_ab(is_risp=True)
t9.pitch_list("d b")
t9.out("F8")


# Bot 9th
# Pitching: ATL #38 Arodys Vizcaíno
b9 = game.new_inning()

# Pitching change (ATL): #38 Arodys Vizcaíno replaces #33 A.J. Minter
b9.pitching_substitution(38)

# 5. BOS #11 Rafael Devers (X - X - X)
b9.new_ab()
b9.pitch_list("b s f f")
b9.out("G3")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b9.new_ab()
b9.pitch_list("b b c")
b9.out("P4")

# 7. BOS #23 Blake Swihart (X - X - X)
b9.new_ab()
b9.pitch_list("c b s c")
b9.out("!K")

# Winning team: ATL
# WP: ATL #26 Mike Foltynewicz
game.winning_pitcher(26, is_away_team=True)

# Loser team: BOS
# LP: BOS #41 Chris Sale
game.losing_pitcher(41)

# print(game)
game.generate_scorecard()
