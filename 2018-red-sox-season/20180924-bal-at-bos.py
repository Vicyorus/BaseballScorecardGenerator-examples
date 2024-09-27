import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BAL @ BOS, 2018-09-24
# https://www.baseball-reference.com/boxes/BOS/BOS201809240.shtml
# https://www.mlb.com/gameday/orioles-vs-red-sox/2018/09/24/531743/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-09-24 19:12-22:18",
        "at": "Fenway Park, Boston, MA",
        "att": "35,619",
        "temp": "56F, Cloudy",
        "wind": "14mph, In From RF",
        "away": {
            "team": "Baltimore Orioles",
            "starter": 37,
            "roster": {
                # Lineup
                3: "Cedric Mullins",
                16: "Trey Mancini",
                2: "Jonathan Villar",
                10: "Adam Jones",
                62: "DJ Stewart",
                1: "Tim Beckham",
                39: "Renato Núñez",
                12: "Stevie Wilkerson",
                36: "Caleb Joseph",
                # Starting pitcher
                37: "Dylan Bundy",
                # Bench
                28: "Breyvic Valera",
                19: "Chris Davis",
                29: "Jace Peterson",
                61: "Austin Wynns",
                34: "John Andreoli",
                15: "Chance Sisco",
                64: "Corban Joseph",
                23: "Joey Rickard",
                # Bullpen
                31: "Jimmy Yacabonis",
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
                57: "Donnie Hart",
                43: "Mike Wright Jr.",
                50: "Miguel Castro",
                67: "John Means",
                59: "Luis F. Ortiz",
            },
            "lefties": [63, 66, 51, 65, 57, 67],
            "lineup": [
                [3, "8"],
                [16, "3"],
                [2, "6"],
                [10, "7"],
                [62, "9"],
                [1, "0"],
                [39, "5"],
                [12, "4"],
                [36, "2"],
            ],
            "bench": [
                [28, "LF"],
                [19, "1B"],
                [29, "SS"],
                [61, "C"],
                [34, "OF"],
                [15, "C"],
                [64, "1B"],
                [23, "RF"],
            ],
            "bullpen": [31, 63, 52, 17, 32, 41, 49, 66, 54, 51, 65, 58, 60, 57, 43, 50, 67, 59],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                11: "Rafael Devers",
                25: "Steve Pearce",
                12: "Brock Holt",
                7: "Christian Vázquez",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                30: "Tzu-Wei Lin",
                36: "Eduardo Núñez",
                18: "Mitch Moreland",
                59: "Sam Travis",
                5: "Ian Kinsler",
                23: "Blake Swihart",
                3: "Sandy León",
                0: "Brandon Phillips",
                # Bullpen
                47: "Tyler Thornburg",
                57: "Eduardo Rodriguez",
                35: "Steven Wright",
                44: "Brandon Workman",
                67: "William Cuevas",
                22: "Rick Porcello",
                41: "Chris Sale",
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
            "lefties": [57, 41, 31, 61, 66, 63, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [28, "0"],
                [2, "6"],
                [11, "5"],
                [25, "3"],
                [12, "4"],
                [7, "2"],
                [19, "8"],
            ],
            "bench": [
                [30, "OF"],
                [36, "SS"],
                [18, "1B"],
                [59, "1B"],
                [5, "2B"],
                [23, "C"],
                [3, "C"],
                [0, "2B"],
            ],
            "bullpen": [47, 57, 35, 44, 67, 22, 41, 31, 61, 66, 37, 63, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Tim Timmons",
            "1B": "Ryan Blakney",
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
# Pitching: BOS #17 Nathan Eovaldi
t1 = game.new_inning()

# 1. BAL #3  Cedric Mullins (X - X - X)
t1.new_ab()
t1.pitch_list("c c b")
t1.out("G3-1")

# 2. BAL #16 Trey Mancini (X - X - X)
t1.new_ab()
t1.hit(1)
t1.thrown_out(2, "10 FC6-4", 3, 17)

# 3. BAL #2  Jonathan Villar (X - X - 16)
t1.new_ab()
t1.pitch_list("f f s")
t1.out("K")

# 4. BAL #10 Adam Jones (X - X - 16)
t1.new_ab()
t1.reach("FC6-4")


# Bot 1st
# Pitching: BAL #37 Dylan Bundy
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c f f b b s")
b1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b b c b f b")
b1.reach("BB")
b1.error(2)
b1.advance(2, "28 SB")
b1.advance(3, "28 E2")

# 3. BOS #28 J.D. Martinez (X - X - 16)
b1.new_ab()
b1.pitch_list("b f 1 b c b s")
b1.out("K")

# 4. BOS #2  Xander Bogaerts (16 - X - X)
b1.new_ab()
b1.pitch_list("b s s b f f")
b1.out("G5-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #17 Nathan Eovaldi
t2 = game.new_inning()

# 5. BAL #62 DJ Stewart (X - X - X)
t2.new_ab()
t2.pitch_list("c f t")
t2.out("KT")

# 6. BAL #1  Tim Beckham (X - X - X)
t2.new_ab()
t2.pitch_list("b b f s f f c")
t2.out("!K")

# 7. BAL #39 Renato Núñez (X - X - X)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(1)

# 8. BAL #12 Stevie Wilkerson (X - X - 39)
t2.new_ab()
t2.out("G4-3")


# Bot 2nd
# Pitching: BAL #37 Dylan Bundy
b2 = game.new_inning()

# 5. BOS #11 Rafael Devers (X - X - X)
b2.new_ab()
b2.pitch_list("b f f b s")
b2.out("K")

# 6. BOS #25 Steve Pearce (X - X - X)
b2.new_ab()
b2.pitch_list("c c b f f")
b2.hit(2)
b2.advance(4, "12 2B")

# 7. BOS #12 Brock Holt (X - 25 - X)
b2.new_ab()
b2.pitch_list("d c d b")
b2.hit(2, rbis=1)
b2.advance(4, "7 1B")

# 8. BOS #7  Christian Vázquez (X - 12 - X)
b2.new_ab()
b2.pitch_list("c f")
b2.hit(1, rbis=1)
b2.advance(4, "50 HR")

# 9. BOS #19 Jackie Bradley Jr. (X - X - 7)
b2.new_ab()
b2.pitch_list("b 1 f f s")
b2.out("K")

# 1. BOS #50 Mookie Betts (X - X - 7)
b2.new_ab()
b2.pitch_list("b")
b2.hit(4, rbis=2)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b2.new_ab()
b2.pitch_list("b b f b")
b2.hit(1)

# 3. BOS #28 J.D. Martinez (X - X - 16)
b2.new_ab()
b2.pitch_list("s d f 1 c")
b2.out("!K")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #17 Nathan Eovaldi
t3 = game.new_inning()

# 9. BAL #36 Caleb Joseph (X - X - X)
t3.new_ab()
t3.pitch_list("c b s b f b f")
t3.out("G6-3")

# 1. BAL #3  Cedric Mullins (X - X - X)
t3.new_ab()
t3.pitch_list("b f b f c")
t3.out("!K")

# 2. BAL #16 Trey Mancini (X - X - X)
t3.new_ab()
t3.pitch_list("c b c s")
t3.out("K")


# Bot 3rd
# Pitching: BAL #37 Dylan Bundy
b3 = game.new_inning()

# 4. BOS #2  Xander Bogaerts (X - X - X)
b3.new_ab()
b3.pitch_list("c f f f f")
b3.out("G1-3")

# 5. BOS #11 Rafael Devers (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.out("P6")

# 6. BOS #25 Steve Pearce (X - X - X)
b3.new_ab()
b3.pitch_list("c f b f b f f b b")
b3.reach("BB")
b3.advance(2, "12 BB")

# 7. BOS #12 Brock Holt (X - X - 25)
b3.new_ab()
b3.pitch_list("f b d c b b")
b3.reach("BB")

# 8. BOS #7  Christian Vázquez (X - 25 - 12)
b3.new_ab()
b3.pitch_list("s f b f f f")
b3.out("(F)P3")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #17 Nathan Eovaldi
t4 = game.new_inning()

# 3. BAL #2  Jonathan Villar (X - X - X)
t4.new_ab()
t4.pitch_list("b s f f b t")
t4.out("KT")

# 4. BAL #10 Adam Jones (X - X - X)
t4.new_ab()
t4.pitch_list("b f s")
t4.out("L9")

# 5. BAL #62 DJ Stewart (X - X - X)
t4.new_ab()
t4.pitch_list("c f b b b c")
t4.out("!K")


# Bot 4th
# Pitching: BAL #57 Donnie Hart
b4 = game.new_inning()

# Pitching change (BAL): #57 Donnie Hart replaces #37 Dylan Bundy
b4.pitching_substitution(57)

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b4.new_ab()
b4.pitch_list("b b f f")
b4.hit(1)
b4.advance(3, "50 1B")
b4.advance(4, "16 1B")

# 1. BOS #50 Mookie Betts (X - X - 19)
b4.new_ab()
b4.pitch_list("c b")
b4.hit(1)
b4.advance(2, "16 SB")
b4.advance(3, "16 1B")
b4.advance(4, "2 1B")

# 2. BOS #16 Andrew Benintendi (19 - X - 50)
b4.new_ab()
b4.pitch_list("c 1 c f b")
b4.hit(1, rbis=1)
b4.advance(2, "28 BB")
b4.advance(3, "2 1B")
b4.thrown_out(4, "11 DP1-2-5", 1, 57)

# 3. BOS #28 J.D. Martinez (50 - X - 16)
b4.new_ab()
b4.pitch_list("b b f b b")
b4.reach("BB")
b4.advance(2, "2 1B")
b4.thrown_out(3, "11 DP1-2-5", 2, 57)

# 4. BOS #2  Xander Bogaerts (50 - 16 - 28)
b4.new_ab()
b4.pitch_list("b b c")
b4.hit(1, rbis=1)
b4.advance(2, "11 DP1-2-5")

# 5. BOS #11 Rafael Devers (16 - 28 - 2)
b4.new_ab()
b4.pitch_list("c b")
b4.reach("DP1-2-5")

# 6. BOS #25 Steve Pearce (X - 2 - 11)
b4.new_ab()
b4.pitch_list("c f f")
b4.out("F9")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #17 Nathan Eovaldi
t5 = game.new_inning()

# 6. BAL #1  Tim Beckham (X - X - X)
t5.new_ab()
t5.pitch_list("f b")
t5.hit(1)
t5.advance(3, "39 1B")
t5.advance(4, "12 WP")

# 7. BAL #39 Renato Núñez (X - X - 1)
t5.new_ab()
t5.pitch_list("b 1 c s b")
t5.hit(1)
t5.advance(2, "12 WP")
t5.advance(3, "3 WP")

# 8. BAL #12 Stevie Wilkerson (1 - X - 39)
t5.new_ab()
t5.pitch_list("c b f f b b f f f f c")
t5.wp()
t5.out("!K")

# 9. BAL #36 Caleb Joseph (X - 39 - X)
t5.new_ab()
t5.pitch_list("b c s s")
t5.out("K")

# 1. BAL #3  Cedric Mullins (X - 39 - X)
t5.new_ab()
t5.pitch_list("b f b s c")
t5.wp()
t5.out("!K")


# Bot 5th
# Pitching: BAL #63 Sean Gilmartin
b5 = game.new_inning()

# Pitching change (BAL): #63 Sean Gilmartin replaces #57 Donnie Hart
b5.pitching_substitution(63)

# 7. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("b b c s b")
b5.out("G3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b5.new_ab()
b5.pitch_list("c b f b b f f")
b5.out("G5-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("c s b")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #57 Eduardo Rodriguez
t6 = game.new_inning()

# Pitching change (BOS): #57 Eduardo Rodriguez replaces #17 Nathan Eovaldi
t6.pitching_substitution(57)

# 2. BAL #16 Trey Mancini (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.out("F9")

# 3. BAL #2  Jonathan Villar (X - X - X)
t6.new_ab()
t6.pitch_list("b f s f")
t6.out("F8")

# 4. BAL #10 Adam Jones (X - X - X)
t6.new_ab()
t6.out("F8")


# Bot 6th
# Pitching: BAL #63 Sean Gilmartin
b6 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b c b b")
b6.out("P4")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("c b f b s")
b6.out("K")

# 3. BOS #28 J.D. Martinez (X - X - X)
b6.new_ab()
b6.pitch_list("b b f b b")
b6.reach("BB")
b6.advance(3, "2 1B")

# 4. BOS #2  Xander Bogaerts (X - X - 28)
b6.new_ab()
b6.pitch_list("f b c b")
b6.hit(1)

# 5. BOS #11 Rafael Devers (28 - X - 2)
b6.new_ab()
b6.pitch_list("s")
b6.out("G6-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #57 Eduardo Rodriguez
t7 = game.new_inning()

# Offensive change (BAL): Pinch-hitter #23 Joey Rickard replaces #62 DJ Stewart, batting 5th
t7.offensive_substitution(5, 23, "PH")

# 5. BAL #23 Joey Rickard (X - X - X)
t7.new_ab()
t7.pitch_list("b b")
t7.out("P3")

# 6. BAL #1  Tim Beckham (X - X - X)
t7.new_ab()
t7.pitch_list("b b t c b c")
t7.out("!K")

# 7. BAL #39 Renato Núñez (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1)

# 8. BAL #12 Stevie Wilkerson (X - X - 39)
t7.new_ab()
t7.pitch_list("b f f s")
t7.out("K")


# Bot 7th
# Pitching: BAL #63 Sean Gilmartin
b7 = game.new_inning()

# Defensive switch (BAL): #23 Joey Rickard moves to RF
b7.defensive_switch(23, "9")

# 6. BOS #25 Steve Pearce (X - X - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("G4-3")

# 7. BOS #12 Brock Holt (X - X - X)
b7.new_ab()
b7.out("G4-3")

# 8. BOS #7  Christian Vázquez (X - X - X)
b7.new_ab()
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #56 Joe Kelly
t8 = game.new_inning()

# Pitching change (BOS): #56 Joe Kelly replaces #57 Eduardo Rodriguez
t8.pitching_substitution(56)

# 9. BAL #36 Caleb Joseph (X - X - X)
t8.new_ab()
t8.hit(1)
t8.advance(2, "3 BB")
t8.advance(3, "2 BB")
t8.advance(4, "10 SF8")

# 1. BAL #3  Cedric Mullins (X - X - 36)
t8.new_ab()
t8.pitch_list("b b c b f f b")
t8.reach("BB")
t8.advance(2, "2 BB")
t8.advance(3, "10 SF8")

# 2. BAL #16 Trey Mancini (X - 36 - 3)
t8.new_ab()
t8.pitch_list("c c s")
t8.out("K")

# 3. BAL #2  Jonathan Villar (X - 36 - 3)
t8.new_ab()
t8.pitch_list("d b s b b")
t8.reach("BB")
t8.thrown_out(1, "64 PO", 3, 70)

# Pitching change (BOS): #70 Ryan Brasier replaces #56 Joe Kelly
t8.pitching_substitution(70)

# 4. BAL #10 Adam Jones (36 - 3 - 2)
t8.new_ab()
t8.pitch_list("c b 1 s f")
t8.out("SF8", rbis=1)

# Offensive change (BAL): Pinch-hitter #64 Corban Joseph replaces #23 Joey Rickard, batting 5th
t8.offensive_substitution(5, 64, "PH")

# 5. BAL #64 Corban Joseph (3 - X - 2)
t8.new_ab()
t8.pitch_list("b c 1")
t8.no_ab("PO")


# Bot 8th
# Pitching: BAL #63 Sean Gilmartin
b8 = game.new_inning()

# Defensive switch (BAL): #16 Trey Mancini moves to LF
b8.defensive_switch(16, "7")

# Defensive switch (BAL): #10 Adam Jones moves to RF
b8.defensive_switch(10, "9")

# Defensive switch (BAL): #64 Corban Joseph moves to 1B
b8.defensive_switch(64, "3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b8.new_ab()
b8.pitch_list("t")
b8.out("L7")

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("b c c b s")
b8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("L8")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #32 Matt Barnes
t9 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #70 Ryan Brasier
t9.pitching_substitution(32)

# 5. BAL #64 Corban Joseph (X - X - X)
t9.new_ab()
t9.hit(1)
t9.thrown_out(2, "1 DP4-3", 1, 32)

# 6. BAL #1  Tim Beckham (X - X - 64)
t9.new_ab()
t9.pitch_list("d c 1")
t9.out("DP4-3")

# 7. BAL #39 Renato Núñez (X - X - X)
t9.new_ab()
t9.pitch_list("b c s")
t9.out("G4-3")

# Winning team: BOS
# WP: BOS #17 Nathan Eovaldi
game.winning_pitcher(17)

# Loser team: BAL
# LP: BAL #37 Dylan Bundy
game.losing_pitcher(37, is_away_team=True)

# print(game)
game.generate_scorecard()
