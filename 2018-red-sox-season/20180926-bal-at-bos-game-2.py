import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-09-26, game 2 of 2
# https://www.baseball-reference.com/boxes/BOS/BOS201809262.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/09/26/531771/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-26 19:12-22:57",
        "at": "Fenway Park, Boston, MA",
        "att": "34,445",
        "temp": "78F, Partly Cloudy",
        "wind": "16mph, Out To LF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 31,
            "roster": {
                # Lineup
                3: "Cedric Mullins",
                2: "Jonathan Villar",
                16: "Trey Mancini",
                10: "Adam Jones",
                39: "Renato Núñez",
                23: "Joey Rickard",
                34: "John Andreoli",
                12: "Stevie Wilkerson",
                36: "Caleb Joseph",
                # Starting pitcher
                31: "Jimmy Yacabonis",
                # Bench
                1: "Tim Beckham",
                28: "Breyvic Valera",
                19: "Chris Davis",
                29: "Jace Peterson",
                61: "Austin Wynns",
                62: "DJ Stewart",
                15: "Chance Sisco",
                64: "Corban Joseph",
                # Bullpen
                63: "Sean Gilmartin",
                52: "Ryan Meisinger",
                17: "Alex Cobb",
                32: "Yefry Ramírez",
                41: "David Hess",
                49: "Cody Carroll",
                66: "Tanner Scott",
                54: "Andrew Cashner",
                51: "Paul Fry",
                65: "Josh Rogers",
                58: "Evan Phillips",
                60: "Mychal Givens",
                37: "Dylan Bundy",
                57: "Donnie Hart",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                67: "John Means",
                59: "Luis F. Ortiz",
            },
            "lefties": [63, 66, 51, 65, 57, 67],
            "lineup": [
                [3, "8"],
                [2, "6"],
                [16, "3"],
                [10, "0"],
                [39, "5"],
                [23, "7"],
                [34, "9"],
                [12, "4"],
                [36, "2"],
            ],
            "bench": [
                [1, "SS"],
                [28, "LF"],
                [19, "1B"],
                [29, "SS"],
                [61, "C"],
                [62, "RF"],
                [15, "C"],
                [64, "1B"],
            ],
            "bullpen": [
                63,
                52,
                17,
                32,
                41,
                49,
                66,
                54,
                51,
                65,
                58,
                60,
                37,
                57,
                43,
                50,
                67,
                59,
            ],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 41,
            "roster": {
                # Lineup
                19: "Jackie Bradley Jr.",
                12: "Brock Holt",
                25: "Steve Pearce",
                11: "Rafael Devers",
                23: "Blake Swihart",
                0: "Brandon Phillips",
                7: "Christian Vázquez",
                59: "Sam Travis",
                30: "Tzu-Wei Lin",
                # Starting pitcher
                41: "Chris Sale",
                # Bench
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                5: "Ian Kinsler",
                28: "J.D. Martinez",
                16: "Andrew Benintendi",
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
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                17: "Nathan Eovaldi",
                32: "Matt Barnes",
            },
            "lefties": [41, 57, 31, 61, 66, 63, 24],
            "lineup": [
                [19, "8"],
                [12, "5"],
                [25, "3"],
                [11, "0"],
                [23, "9"],
                [0, "4"],
                [7, "2"],
                [59, "7"],
                [30, "6"],
            ],
            "bench": [
                [36, "SS"],
                [18, "1B"],
                [5, "2B"],
                [28, "DH"],
                [16, "LF"],
                [50, "SS"],
                [2, "2B"],
                [3, "C"],
            ],
            "bullpen": [
                47,
                57,
                35,
                44,
                67,
                22,
                31,
                61,
                66,
                37,
                63,
                24,
                46,
                76,
                70,
                56,
                17,
                32,
            ],
        },
        "umpires": {
            "HP": "Mike Muchlinski",
            "1B": "Mike Winters",
            "2B": "Tim Timmons",
            "3B": "Sean Barber",
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

# 1. BAL #3  Cedric Mullins (X - X - X)
t1.new_ab()
t1.pitch_list("b l f")
t1.reach("HBP")
t1.advance(4, "16 3B")

# 2. BAL #2  Jonathan Villar (X - X - 3)
t1.new_ab()
t1.pitch_list("b s s f t")
t1.out("KT")

# 3. BAL #16 Trey Mancini (X - X - 3)
t1.new_ab()
t1.pitch_list("b 1 b")
t1.hit(3, rbis=1)
t1.advance(4, "39 SF7")

# 4. BAL #10 Adam Jones (16 - X - X)
t1.new_ab(is_risp=True)
t1.pitch_list("c f")
t1.reach("HBP")

# 5. BAL #39 Renato Núñez (16 - X - 10)
t1.new_ab(is_risp=True)
t1.pitch_list("b f")
t1.out("SF7", rbis=1)

# 6. BAL #23 Joey Rickard (X - X - 10)
t1.new_ab()
t1.pitch_list("d f b b")
t1.out("F8")


# Bot 1st
# Pitching: BAL #31 Jimmy Yacabonis
b1 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
b1.new_ab()
b1.pitch_list("c b f f f b f")
b1.hit(1)
b1.advance(3, "12 1B")
b1.advance("U", "0 E6")

# 2. BOS #12 Brock Holt (X - X - 19)
b1.new_ab()
b1.pitch_list("b 1 t b 1")
b1.hit(1)
b1.advance(2, "11 BB")
b1.advance(3, "0 E6")

# 3. BOS #25 Steve Pearce (19 - X - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("c b b f")
b1.out("P6")

# 4. BOS #11 Rafael Devers (19 - X - 12)
b1.new_ab(is_risp=True)
b1.pitch_list("b b c b b")
b1.reach("BB")
b1.advance(2, "0 E6")

# 5. BOS #23 Blake Swihart (19 - 12 - 11)
b1.new_ab(is_risp=True)
b1.pitch_list("s f b c")
b1.out("!K")

# 6. BOS #0  Brandon Phillips (19 - 12 - 11)
b1.new_ab(is_risp=True)
b1.pitch_list("c c")
b1.error(6)
b1.reach("E6")

# 7. BOS #7  Christian Vázquez (12 - 11 - 0)
b1.new_ab(is_risp=True)
b1.pitch_list("c b d c b")
b1.out("G6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #41 Chris Sale
t2 = game.new_inning()

# 7. BAL #34 John Andreoli (X - X - X)
t2.new_ab()
t2.pitch_list("c b s")
t2.out("L5")

# 8. BAL #12 Stevie Wilkerson (X - X - X)
t2.new_ab()
t2.pitch_list("f s f s")
t2.out("K")

# 9. BAL #36 Caleb Joseph (X - X - X)
t2.new_ab()
t2.pitch_list("b c b b f s")
t2.out("K")


# Bot 2nd
# Pitching: BAL #31 Jimmy Yacabonis
b2 = game.new_inning()

# 8. BOS #59 Sam Travis (X - X - X)
b2.new_ab()
b2.out("G1-3")

# 9. BOS #30 Tzu-Wei Lin (X - X - X)
b2.new_ab()
b2.pitch_list("c b b f")
b2.out("L8")

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
b2.new_ab()
b2.pitch_list("b b s b")
b2.out("G4-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #41 Chris Sale
t3 = game.new_inning()

# 1. BAL #3  Cedric Mullins (X - X - X)
t3.new_ab()
t3.pitch_list("c c b")
t3.out("G5-3")

# 2. BAL #2  Jonathan Villar (X - X - X)
t3.new_ab()
t3.pitch_list("f")
t3.out("L7")

# 3. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("c b b f s")
t3.out("K2-3")


# Bot 3rd
# Pitching: BAL #31 Jimmy Yacabonis
b3 = game.new_inning()

# 2. BOS #12 Brock Holt (X - X - X)
b3.new_ab()
b3.pitch_list("c s")
b3.out("L8")

# 3. BOS #25 Steve Pearce (X - X - X)
b3.new_ab()
b3.pitch_list("b b b b")
b3.reach("BB")
b3.advance(2, "11 WP")

# 4. BOS #11 Rafael Devers (X - X - 25)
b3.new_ab(is_risp=True)
b3.pitch_list("b s 2 s c")
b3.wp()
b3.out("!K")

# 5. BOS #23 Blake Swihart (X - 25 - X)
b3.new_ab(is_risp=True)
b3.pitch_list("d b b c b")
b3.reach("BB")

# 6. BOS #0  Brandon Phillips (X - 25 - 23)
b3.new_ab(is_risp=True)
b3.pitch_list("c b c")
b3.out("G6-3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #41 Chris Sale
t4 = game.new_inning()

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("f b s")
t4.hit(1)
t4.error(4)
t4.advance(2, "23 E4")

# 5. BAL #39 Renato Núñez (X - X - 10)
t4.new_ab()
t4.pitch_list("b t f f s")
t4.out("K")

# 6. BAL #23 Joey Rickard (X - X - 10)
t4.new_ab()
t4.pitch_list("f b f")
t4.reach("FC5")

# 7. BAL #34 John Andreoli (X - 10 - 23)
t4.new_ab(is_risp=True)
t4.pitch_list("c c b f b b t")
t4.out("KT")

# 8. BAL #12 Stevie Wilkerson (X - 10 - 23)
t4.new_ab(is_risp=True)
t4.pitch_list("f f b s")
t4.out("K")


# Bot 4th
# Pitching: BAL #31 Jimmy Yacabonis
b4 = game.new_inning()

# 7. BOS #7  Christian Vázquez (X - X - X)
b4.new_ab()
b4.pitch_list("b")
b4.out("G5-3")

# 8. BOS #59 Sam Travis (X - X - X)
b4.new_ab()
b4.pitch_list("b c b")
b4.hit(1)
b4.advance(4, "30 3B")

# 9. BOS #30 Tzu-Wei Lin (X - X - 59)
b4.new_ab()
b4.hit(3, rbis=1)

# 1. BOS #19 Jackie Bradley Jr. (30 - X - X)
b4.new_ab(is_risp=True)
b4.pitch_list("s c b f b b f f b")
b4.reach("BB")

# Pitching change (BAL): #66 Tanner Scott replaces #31 Jimmy Yacabonis
b4.pitching_substitution(66)

# 2. BOS #12 Brock Holt (30 - X - 19)
b4.new_ab(is_risp=True)
b4.pitch_list("b c f c")
b4.out("!K")

# 3. BOS #25 Steve Pearce (30 - X - 19)
b4.new_ab(is_risp=True)
b4.pitch_list("c b")
b4.out("G6-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #41 Chris Sale
t5 = game.new_inning()

# 9. BAL #36 Caleb Joseph (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.hit(1)
t5.advance(2, "16 BB")
t5.advance(4, "10 2B")

# 1. BAL #3  Cedric Mullins (X - X - 36)
t5.new_ab()
t5.pitch_list("b b l")
t5.out("B1")

# 2. BAL #2  Jonathan Villar (X - X - 36)
t5.new_ab()
t5.pitch_list("c s d b c")
t5.out("!K")

# 3. BAL #16 Trey Mancini (X - X - 36)
t5.new_ab()
t5.pitch_list("b c b b b")
t5.reach("BB")
t5.advance(3, "10 2B")

# 4. BAL #10 Adam Jones (X - 36 - 16)
t5.new_ab(is_risp=True)
t5.pitch_list("c f b")
t5.hit(2, rbis=1)

# Pitching change (BOS): #57 Eduardo Rodriguez replaces #41 Chris Sale
t5.pitching_substitution(57)

# 5. BAL #39 Renato Núñez (16 - 10 - X)
t5.new_ab(is_risp=True)
t5.pitch_list("s b b")
t5.out("F8")


# Bot 5th
# Pitching: BAL #66 Tanner Scott
b5 = game.new_inning()

# 4. BOS #11 Rafael Devers (X - X - X)
b5.new_ab()
b5.pitch_list("c s b f f f")
b5.hit(2)
b5.advance(4, "23 1B")

# 5. BOS #23 Blake Swihart (X - 11 - X)
b5.new_ab(is_risp=True)
b5.hit(1, rbis=1)
b5.advance(2, "0 SB")
b5.advance(3, "59 L8")

# 6. BOS #0  Brandon Phillips (X - X - 23)
b5.new_ab(is_risp=True)
b5.pitch_list("b b s s s")
b5.out("K")

# 7. BOS #7  Christian Vázquez (X - 23 - X)
b5.new_ab(is_risp=True)
b5.pitch_list("s d b b f b")
b5.reach("BB")
b5.advance(2, "30 WP")

# 8. BOS #59 Sam Travis (X - 23 - 7)
b5.new_ab(is_risp=True)
b5.pitch_list("b c f f")
b5.out("L8")

# 9. BOS #30 Tzu-Wei Lin (23 - X - 7)
b5.new_ab(is_risp=True)
b5.pitch_list("b")
b5.wp()
b5.out("G3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# 6. BAL #23 Joey Rickard (X - X - X)
t6.new_ab()
t6.pitch_list("b s f s")
t6.out("K")

# 7. BAL #34 John Andreoli (X - X - X)
t6.new_ab()
t6.pitch_list("s b c c")
t6.out("!K")

# 8. BAL #12 Stevie Wilkerson (X - X - X)
t6.new_ab()
t6.pitch_list("b s s s")
t6.out("K")


# Bot 6th
# Pitching: BAL #66 Tanner Scott
b6 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
b6.new_ab()
b6.out("B1-3")

# 2. BOS #12 Brock Holt (X - X - X)
b6.new_ab()
b6.pitch_list("c b b f f")
b6.out("G5-3")

# 3. BOS #25 Steve Pearce (X - X - X)
b6.new_ab()
b6.pitch_list("b c s s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #32 Matt Barnes
t7 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #57 Eduardo Rodriguez
t7.pitching_substitution(32)

# 9. BAL #36 Caleb Joseph (X - X - X)
t7.new_ab()
t7.pitch_list("b c b")
t7.hit(2)
t7.advance(3, "3 WP")
t7.advance(4, "16 1B")

# 1. BAL #3  Cedric Mullins (X - 36 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("l b b b f f s")
t7.wp()
t7.out("K")

# 2. BAL #2  Jonathan Villar (36 - X - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b b b")
t7.reach("BB")
t7.advance(2, "16 SB")
t7.advance(4, "16 1B")

# 3. BAL #16 Trey Mancini (36 - X - 2)
t7.new_ab(is_risp=True)
t7.pitch_list("f f 1 1 b")
t7.hit(1, rbis=2)
t7.advance(2, "10 1B")
t7.advance(4, "39 1B")

# 4. BAL #10 Adam Jones (X - X - 16)
t7.new_ab()
t7.pitch_list("s d")
t7.hit(1)
t7.advance(3, "39 1B")

# 5. BAL #39 Renato Núñez (X - 16 - 10)
t7.new_ab(is_risp=True)
t7.pitch_list("b")
t7.hit(1, rbis=1)
# Offensive change (BAL): Pinch-runner #29 Jace Peterson replaces #39 Renato Núñez
t7.offensive_substitution(5, 29, "PR")
t7.atbase("PR")
t7.advance(2, "62 SB")

# Pitching change (BOS): #76 Hector Velázquez replaces #32 Matt Barnes
t7.pitching_substitution(76)

# Offensive change (BAL): Pinch-hitter #62 DJ Stewart replaces #23 Joey Rickard, batting 6th
t7.offensive_substitution(6, 62, "PH")

# 6. BAL #62 DJ Stewart (10 - X - 39)
t7.new_ab(is_risp=True)
t7.pitch_list("c b s 1 b b s")
t7.out("K")

# 7. BAL #34 John Andreoli (10 - 29 - X)
t7.new_ab(is_risp=True)
t7.pitch_list("b b s f")
t7.out("P3")


# Bot 7th
# Pitching: BAL #51 Paul Fry
b7 = game.new_inning()

# Pitching change (BAL): #51 Paul Fry replaces #66 Tanner Scott
b7.pitching_substitution(51)

# Defensive switch (BAL): #29 Jace Peterson moves to 3B
b7.defensive_switch(29, "5")

# Defensive switch (BAL): #62 DJ Stewart moves to LF
b7.defensive_switch(62, "7")

# 4. BOS #11 Rafael Devers (X - X - X)
b7.new_ab()
b7.pitch_list("b b")
b7.out("G5-3")

# 5. BOS #23 Blake Swihart (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")

# 6. BOS #0  Brandon Phillips (X - X - X)
b7.new_ab()
b7.pitch_list("f f f f b f b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #70 Ryan Brasier
t8 = game.new_inning()

# Pitching change (BOS): #70 Ryan Brasier replaces #76 Hector Velázquez
t8.pitching_substitution(70)

# 8. BAL #12 Stevie Wilkerson (X - X - X)
t8.new_ab()
t8.pitch_list("b")
t8.out("G6-3")

# 9. BAL #36 Caleb Joseph (X - X - X)
t8.new_ab()
t8.pitch_list("c s b")
t8.out("L8")

# 1. BAL #3  Cedric Mullins (X - X - X)
t8.new_ab()
t8.pitch_list("s b b b")
t8.out("G4-3")


# Bot 8th
# Pitching: BAL #51 Paul Fry
b8 = game.new_inning()

# 7. BOS #7  Christian Vázquez (X - X - X)
b8.new_ab()
b8.pitch_list("b")
b8.out("G4-3")

# 8. BOS #59 Sam Travis (X - X - X)
b8.new_ab()
b8.pitch_list("c")
b8.out("G5-3")

# 9. BOS #30 Tzu-Wei Lin (X - X - X)
b8.new_ab()
b8.pitch_list("c f b")
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #70 Ryan Brasier
t9.pitching_substitution(46)

# Defensive switch (BOS): #12 Brock Holt moves to RF
t9.defensive_switch(12, "9")

# Defensive switch (BOS): #23 Blake Swihart moves to C
t9.defensive_switch(23, "2")

# Defensive switch (BOS): #7 Christian Vázquez moves to 3B
t9.defensive_switch(7, "5")

# 2. BAL #2  Jonathan Villar (X - X - X)
t9.new_ab()
t9.pitch_list("s b f b b b")
t9.reach("BB")
t9.advance(2, "16 SB")
t9.advance(3, "16 F9")
t9.advance(4, "10 WP")

# 3. BAL #16 Trey Mancini (X - X - 2)
t9.new_ab(is_risp=True)
t9.pitch_list("f b c")
t9.out("F9")

# 4. BAL #10 Adam Jones (2 - X - X)
t9.new_ab()
t9.pitch_list("b f")
t9.wp()
t9.reach("HBP")
t9.advance(2, "29 BB")
t9.advance(3, "62 BB")
t9.advance(4, "34 2B")

# 5. BAL #29 Jace Peterson (X - X - 10)
t9.new_ab()
t9.pitch_list("b b s f d b")
t9.reach("BB")
t9.advance(2, "62 BB")
t9.advance(4, "34 2B")

# 6. BAL #62 DJ Stewart (X - 10 - 29)
t9.new_ab(is_risp=True)
t9.pitch_list("t b s f b b f b")
t9.reach("BB")
t9.advance(3, "34 2B")
t9.advance(4, "12 1B")

# Pitching change (BOS): #63 Robby Scott replaces #46 Craig Kimbrel
t9.pitching_substitution(63)

# 7. BAL #34 John Andreoli (10 - 29 - 62)
t9.new_ab(is_risp=True)
t9.pitch_list("c b s f")
t9.hit(2, rbis=2)
t9.advance(3, "12 1B")

# 8. BAL #12 Stevie Wilkerson (62 - 34 - X)
t9.new_ab(is_risp=True)
t9.pitch_list("b b")
t9.hit(1, rbis=1)

# 9. BAL #36 Caleb Joseph (34 - X - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("c d b b f s")
t9.out("K")

# 1. BAL #3  Cedric Mullins (34 - X - 12)
t9.new_ab(is_risp=True)
t9.pitch_list("b c b d")
t9.out("F9")


# Bot 9th
# Pitching: BAL #51 Paul Fry
b9 = game.new_inning()

# 1. BOS #19 Jackie Bradley Jr. (X - X - X)
b9.new_ab()
b9.pitch_list("b c s s")
b9.out("K")

# 2. BOS #12 Brock Holt (X - X - X)
b9.new_ab()
b9.pitch_list("s")
b9.out("L6")

# 3. BOS #25 Steve Pearce (X - X - X)
b9.new_ab()
b9.pitch_list("b b b c f")
b9.out("G6-3")

# Winning team: BAL
# WP: BAL #66 Tanner Scott
game.winning_pitcher(66, is_away_team=True)
# SV: BAL #51 Paul Fry
game.save_pitcher(51, is_away_team=True)

# Loser team: BOS
# LP: BOS #32 Matt Barnes
game.losing_pitcher(32)

# print(game)
game.generate_scorecard()
