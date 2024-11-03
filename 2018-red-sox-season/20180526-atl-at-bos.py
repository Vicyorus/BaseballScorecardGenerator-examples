import os
from baseball_scorecard.baseball_scorecard import Scorecard

# ATL @ BOS, 2018-05-26
# https://www.baseball-reference.com/boxes/BOS/BOS201805260.shtml
# https://www.mlb.com/gameday/braves-vs-red-sox/2018/05/26/530170/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-26 13:05-16:34",
        "at": "Fenway Park, Boston, MA",
        "att": "36,510",
        "temp": "85F, Sunny",
        "wind": "8mph, Out To RF",
        "away": {
            "team": "Atlanta Braves",
            "starter": 15,
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
                15: "Sean Newcomb",
                # Bench
                27: "Ryan Flaherty",
                20: "Preston Tucker",
                8: "Charlie Culberson",
                # Bullpen
                39: "Sam Freeman",
                51: "Shane Carle",
                30: "Peter Moylan",
                58: "Dan Winkler",
                49: "Julio Teheran",
                38: "Arodys Vizcaíno",
                45: "Matt Wisler",
                33: "A.J. Minter",
                26: "Mike Foltynewicz",
                50: "Lucas Sims",
                63: "Jesse Biddle",
                32: "Brandon McCarthy",
            },
            "lefties": [15, 39, 33, 63],
            "lineup": [
                [1, "4"],
                [13, "9"],
                [5, "3"],
                [22, "7"],
                [24, "2"],
                [11, "8"],
                [25, "0"],
                [17, "5"],
                [7, "6"],
            ],
            "bench": [
                [27, "2B"],
                [20, "LF"],
                [8, "1B"],
            ],
            "bullpen": [39, 51, 30, 58, 49, 38, 45, 33, 26, 50, 63, 32],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 31,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                18: "Mitch Moreland",
                2: "Xander Bogaerts",
                15: "Dustin Pedroia",
                36: "Eduardo Núñez",
                23: "Blake Swihart",
                7: "Christian Vázquez",
                # Starting pitcher
                31: "Drew Pomeranz",
                # Bench
                12: "Brock Holt",
                11: "Rafael Devers",
                19: "Jackie Bradley Jr.",
                3: "Sandy León",
                # Bullpen
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
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
                [16, "8"],
                [28, "7"],
                [18, "3"],
                [2, "6"],
                [15, "4"],
                [36, "5"],
                [23, "0"],
                [7, "2"],
            ],
            "bench": [
                [12, "2B"],
                [11, "3B"],
                [19, "CF"],
                [3, "C"],
            ],
            "bullpen": [57, 35, 22, 41, 61, 37, 24, 46, 76, 56, 32],
        },
        "umpires": {
            "HP": "Laz Diaz",
            "1B": "Manny Gonzalez",
            "2B": "Andy Fletcher",
            "3B": "Jeff Nelson",
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
# Pitching: BOS #31 Drew Pomeranz
t1 = game.new_inning()

# 1. ATL #1  Ozzie Albies (X - X - X)
t1.new_ab()
t1.pitch_list("b s b c")
t1.out("G6-3")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t1.new_ab()
t1.pitch_list("b f f f")
t1.out("G5-3")

# 3. ATL #5  Freddie Freeman (X - X - X)
t1.new_ab()
t1.pitch_list("b s f f")
t1.hit(1)
t1.advance(3, "22 2B")

# 4. ATL #22 Nick Markakis (X - X - 5)
t1.new_ab()
t1.hit(2)

# 5. ATL #24 Kurt Suzuki (5 - 22 - X)
t1.new_ab(is_risp=True)
t1.pitch_list("b b c f b f c")
t1.out("!K")


# Bot 1st
# Pitching: ATL #15 Sean Newcomb
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("b f s f c")
b1.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.hit(1)
b1.advance(2, "28 BB")
b1.advance(3, "2 BB")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.pitch_list("b b d b")
b1.reach("BB")
b1.advance(2, "2 BB")

# 4. BOS #18 Mitch Moreland (X - 16 - 28)
b1.new_ab(is_risp=True)
b1.pitch_list("f f f f s")
b1.out("K")

# 5. BOS #2  Xander Bogaerts (X - 16 - 28)
b1.new_ab(is_risp=True)
b1.pitch_list("b d c b c d")
b1.reach("BB")

# 6. BOS #15 Dustin Pedroia (16 - 28 - 2)
b1.new_ab(is_risp=True)
b1.pitch_list("b")
b1.out("F9")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #31 Drew Pomeranz
t2 = game.new_inning()

# 6. ATL #11 Ender Inciarte (X - X - X)
t2.new_ab()
t2.pitch_list("b b c b c b")
t2.reach("BB")
t2.advance(4, "7 HR")

# 7. ATL #25 Tyler Flowers (X - X - 11)
t2.new_ab()
t2.pitch_list("c f 1 1 f s")
t2.out("K")

# 8. ATL #17 Johan Camargo (X - X - 11)
t2.new_ab()
t2.out("(F)P2")

# 9. ATL #7  Dansby Swanson (X - X - 11)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(4, rbis=2)

# 1. ATL #1  Ozzie Albies (X - X - X)
t2.new_ab()
t2.pitch_list("f f")
t2.out("L9")


# Bot 2nd
# Pitching: ATL #15 Sean Newcomb
b2 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.pitch_list("b b f f")
b2.hit(1)
b2.advance(2, "23 BB")
b2.advance(3, "7 FC5-4")

# 8. BOS #23 Blake Swihart (X - X - 36)
b2.new_ab()
b2.pitch_list("b c b 1 f b f b")
b2.reach("BB")
b2.thrown_out(2, "7 FC5-4", 1, 15)

# 9. BOS #7  Christian Vázquez (X - 36 - 23)
b2.new_ab(is_risp=True)
b2.pitch_list("c b d c")
b2.reach("FC5-4")
b2.thrown_out(2, "16 FC3-6", 3, 15)

# 1. BOS #50 Mookie Betts (36 - X - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("b b c f")
b2.out("P5")

# 2. BOS #16 Andrew Benintendi (36 - X - 7)
b2.new_ab(is_risp=True)
b2.pitch_list("b b f")
b2.reach("FC3-6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #31 Drew Pomeranz
t3 = game.new_inning()

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t3.new_ab()
t3.pitch_list("b c b b f f")
t3.out("G6-3")

# 3. ATL #5  Freddie Freeman (X - X - X)
t3.new_ab()
t3.pitch_list("b s f b f b")
t3.out("G4-3")

# 4. ATL #22 Nick Markakis (X - X - X)
t3.new_ab()
t3.pitch_list("c b")
t3.hit(2)
t3.advance(4, "24 2B")

# 5. ATL #24 Kurt Suzuki (X - 22 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b")
t3.hit(2, rbis=1)

# 6. ATL #11 Ender Inciarte (X - 24 - X)
t3.new_ab(is_risp=True)
t3.pitch_list("b c b f f d f d")
t3.reach("BB")

# 7. ATL #25 Tyler Flowers (X - 24 - 11)
t3.new_ab(is_risp=True)
t3.pitch_list("d f b c b c")
t3.out("!K")


# Bot 3rd
# Pitching: ATL #15 Sean Newcomb
b3 = game.new_inning()

# 3. BOS #28 J.D. Martinez (X - X - X)
b3.new_ab()
b3.pitch_list("c b s b s")
b3.out("K")

# 4. BOS #18 Mitch Moreland (X - X - X)
b3.new_ab()
b3.pitch_list("c b b s b")
b3.hit(3)
b3.advance(4, "2 1B")

# 5. BOS #2  Xander Bogaerts (18 - X - X)
b3.new_ab(is_risp=True)
b3.pitch_list("c b f")
b3.hit(1, rbis=1)
b3.advance(2, "15 PB")
b3.advance(4, "23 1B")

# 6. BOS #15 Dustin Pedroia (X - X - 2)
b3.new_ab(is_risp=True)
b3.pitch_list("d b b b")
b3.pb()
b3.reach("BB")
b3.advance(2, "23 1B")
b3.advance(4, "7 1B")

# 7. BOS #36 Eduardo Núñez (X - 2 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("b c b b f f s")
b3.out("K")

# 8. BOS #23 Blake Swihart (X - 2 - 15)
b3.new_ab(is_risp=True)
b3.pitch_list("c b f b f")
b3.hit(1, rbis=1)
b3.advance(3, "7 1B")

# 9. BOS #7  Christian Vázquez (X - 15 - 23)
b3.new_ab(is_risp=True)
b3.hit(1, rbis=1)
b3.thrown_out(2, "50 FC6-4", 3, 15)

# 1. BOS #50 Mookie Betts (23 - X - 7)
b3.new_ab(is_risp=True)
b3.pitch_list("f b")
b3.reach("FC6-4")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #31 Drew Pomeranz
t4 = game.new_inning()

# 8. ATL #17 Johan Camargo (X - X - X)
t4.new_ab()
t4.pitch_list("b c c b")
t4.out("G5-3")

# 9. ATL #7  Dansby Swanson (X - X - X)
t4.new_ab()
t4.pitch_list("b b c c b f")
t4.hit(1)
t4.advance(2, "1 BB")
t4.advance(3, "13 1B")
t4.advance(4, "5 1B")

# 1. ATL #1  Ozzie Albies (X - X - 7)
t4.new_ab()
t4.pitch_list("b b d b")
t4.reach("BB")
t4.advance(2, "13 1B")
t4.advance(3, "5 1B")
t4.advance(4, "22 SF8")

# Pitching change (BOS): #76 Hector Velázquez replaces #31 Drew Pomeranz
t4.pitching_substitution(76)

# 2. ATL #13 Ronald Acuña Jr. (X - 7 - 1)
t4.new_ab(is_risp=True)
t4.pitch_list("c b b f")
t4.hit(1)
t4.advance(2, "5 1B")

# 3. ATL #5  Freddie Freeman (7 - 1 - 13)
t4.new_ab(is_risp=True)
t4.pitch_list("f d f")
t4.hit(1, rbis=1)

# 4. ATL #22 Nick Markakis (1 - 13 - 5)
t4.new_ab(is_risp=True)
t4.out("SF8", rbis=1)

# 5. ATL #24 Kurt Suzuki (X - 13 - 5)
t4.new_ab(is_risp=True)
t4.out("P6")


# Bot 4th
# Pitching: ATL #63 Jesse Biddle
b4 = game.new_inning()

# Pitching change (ATL): #63 Jesse Biddle replaces #15 Sean Newcomb
b4.pitching_substitution(63)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b4.new_ab()
b4.pitch_list("b b")
b4.hit(4)

# 3. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("c b f f f")
b4.out("L9")

# 4. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("c b s b f")
b4.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("c")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #35 Steven Wright
t5 = game.new_inning()

# Pitching change (BOS): #35 Steven Wright replaces #76 Hector Velázquez
t5.pitching_substitution(35)

# 6. ATL #11 Ender Inciarte (X - X - X)
t5.new_ab()
t5.pitch_list("c c b")
t5.out("P6")

# 7. ATL #25 Tyler Flowers (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(1)
t5.thrown_out(2, "17 DP6-4-3", 2, 35)

# 8. ATL #17 Johan Camargo (X - X - 25)
t5.new_ab()
t5.pitch_list("s")
t5.out("DP6-4-3")


# Bot 5th
# Pitching: ATL #30 Peter Moylan
b5 = game.new_inning()

# Pitching change (ATL): #30 Peter Moylan replaces #63 Jesse Biddle
b5.pitching_substitution(30)

# 6. BOS #15 Dustin Pedroia (X - X - X)
b5.new_ab()
b5.pitch_list("b b c f f f b f f")
b5.out("G1-6-3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b5.new_ab()
b5.pitch_list("c c b s")
b5.out("K")

# 8. BOS #23 Blake Swihart (X - X - X)
b5.new_ab()
b5.pitch_list("f b b c c")
b5.out("!K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #35 Steven Wright
t6 = game.new_inning()

# 9. ATL #7  Dansby Swanson (X - X - X)
t6.new_ab()
t6.pitch_list("b b c f f")
t6.out("P4")

# 1. ATL #1  Ozzie Albies (X - X - X)
t6.new_ab()
t6.pitch_list("b c f f f")
t6.out("L7")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)

# 3. ATL #5  Freddie Freeman (X - X - 13)
t6.new_ab()
t6.pitch_list("s s s")
t6.out("K2-3")


# Bot 6th
# Pitching: ATL #30 Peter Moylan
b6 = game.new_inning()

# 9. BOS #7  Christian Vázquez (X - X - X)
b6.new_ab()
b6.pitch_list("c")
b6.out("F8")

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b c b")
b6.hit(1)
b6.advance(2, "16 HBP")
b6.advance(3, "28 F9")
b6.advance(4, "18 2B")

# Pitching change (ATL): #39 Sam Freeman replaces #30 Peter Moylan
b6.pitching_substitution(39)

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b6.new_ab()
b6.pitch_list("1 b b 1")
b6.reach("HBP")
b6.advance(4, "18 2B")

# 3. BOS #28 J.D. Martinez (X - 50 - 16)
b6.new_ab(is_risp=True)
b6.pitch_list("b f s d")
b6.out("F9")

# 4. BOS #18 Mitch Moreland (50 - X - 16)
b6.new_ab(is_risp=True)
b6.pitch_list("d c s")
b6.hit(2, rbis=2)
b6.advance(3, "2 WP")

# 5. BOS #2  Xander Bogaerts (X - 18 - X)
b6.new_ab(is_risp=True)
b6.pitch_list("b d b b")
b6.wp()
b6.reach("BB")

# 6. BOS #15 Dustin Pedroia (18 - X - 2)
b6.new_ab(is_risp=True)
b6.pitch_list("c")
b6.out("L9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #35 Steven Wright
t7 = game.new_inning()

# 4. ATL #22 Nick Markakis (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c")
t7.out("G6-3")

# 5. ATL #24 Kurt Suzuki (X - X - X)
t7.new_ab()
t7.pitch_list("b")
t7.out("G5-3")

# 6. ATL #11 Ender Inciarte (X - X - X)
t7.new_ab()
t7.pitch_list("b b b c b")
t7.reach("BB")

# 7. ATL #25 Tyler Flowers (X - X - 11)
t7.new_ab()
t7.pitch_list("c b 1")
t7.out("F9")


# Bot 7th
# Pitching: ATL #58 Dan Winkler
b7 = game.new_inning()

# Pitching change (ATL): #58 Dan Winkler replaces #39 Sam Freeman
b7.pitching_substitution(58)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.error(4)
b7.reach("E4")
b7.advance(2, "50 BB")
b7.advance("U", "16 3B")

# 8. BOS #23 Blake Swihart (X - X - 36)
b7.new_ab()
b7.pitch_list("c s 1 f d b f s")
b7.out("K")

# 9. BOS #7  Christian Vázquez (X - X - 36)
b7.new_ab()
b7.pitch_list("b b")
b7.out("F9")

# 1. BOS #50 Mookie Betts (X - X - 36)
b7.new_ab()
b7.pitch_list("b b b c b")
b7.reach("BB")
b7.advance("U", "16 3B")

# 2. BOS #16 Andrew Benintendi (X - 36 - 50)
b7.new_ab(is_risp=True)
b7.pitch_list("b c b f")
b7.hit(3, rbis=2)

# 3. BOS #28 J.D. Martinez (16 - X - X)
b7.new_ab(is_risp=True)
b7.pitch_list("b f b s")
b7.out("G4-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #35 Steven Wright
t8.pitching_substitution(56)

# 8. ATL #17 Johan Camargo (X - X - X)
t8.new_ab()
t8.pitch_list("c b f b")
t8.out("P2")

# 9. ATL #7  Dansby Swanson (X - X - X)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K")

# 1. ATL #1  Ozzie Albies (X - X - X)
t8.new_ab()
t8.pitch_list("c")
t8.out("G1-3")


# Bot 8th
# Pitching: ATL #50 Lucas Sims
b8 = game.new_inning()

# Pitching change (ATL): #50 Lucas Sims replaces #58 Dan Winkler
b8.pitching_substitution(50)

# 4. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("s b s b f f f b")
b8.out("G4-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G5-3")

# 6. BOS #15 Dustin Pedroia (X - X - X)
b8.new_ab()
b8.pitch_list("c b")
b8.out("G6-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #56 Joe Kelly
t9.pitching_substitution(46)

# Defensive switch (BOS): #16 Andrew Benintendi moves to LF
t9.defensive_switch(16, "7")

# Defensive change (BOS): #19 Jackie Bradley Jr. replaces #28 J.D. Martinez (LF), playing CF, batting 3rd
t9.defensive_substitution(3, 19, "8")

# 2. ATL #13 Ronald Acuña Jr. (X - X - X)
t9.new_ab()
t9.pitch_list("c b s")
t9.hit(4)

# 3. ATL #5  Freddie Freeman (X - X - X)
t9.new_ab()
t9.out("L9")

# 4. ATL #22 Nick Markakis (X - X - X)
t9.new_ab()
t9.pitch_list("b b c")
t9.out("G6-3")

# 5. ATL #24 Kurt Suzuki (X - X - X)
t9.new_ab()
t9.pitch_list("b")
t9.out("F9")

# Winning team: BOS
# WP: BOS #35 Steven Wright
game.winning_pitcher(35)
# SV: BOS #46 Craig Kimbrel
game.save_pitcher(46)

# Loser team: ATL
# LP: ATL #39 Sam Freeman
game.losing_pitcher(39, is_away_team=True)

# print(game)
game.generate_scorecard()
