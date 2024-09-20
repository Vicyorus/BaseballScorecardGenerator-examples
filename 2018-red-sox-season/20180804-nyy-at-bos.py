import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-08-04
# https://www.baseball-reference.com/boxes/BOS/BOS201808040.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/08/04/531074/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-04 16:06-18:39",
        "at": "Fenway Park, Boston, MA",
        "att": "36,699",
        "temp": "76F, Cloudy",
        "wind": "9mph, Out To LF",
        "away": {
            "team": "New York Yankees",
            "starter": 43,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                31: "Aaron Hicks",
                25: "Gleyber Torres",
                33: "Greg Bird",
                41: "Miguel Andujar",
                28: "Austin Romine",
                38: "Shane Robinson",
                # Starting pitcher
                43: "Chance Adams",
                # Bench
                66: "Kyle Higashioka",
                45: "Luke Voit",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                36: "Lance Lynn",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                53: "Zack Britton",
                19: "Masahiro Tanaka",
                57: "Chad Green",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 53, 54],
            "lineup": [
                [11, "7"],
                [27, "0"],
                [18, "6"],
                [31, "8"],
                [25, "4"],
                [33, "3"],
                [41, "5"],
                [28, "2"],
                [38, "9"],
            ],
            "bench": [
                [66, "C"],
                [45, "1B"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 40, 36, 55, 56, 52, 53, 19, 57, 30, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 17,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                18: "Mitch Moreland",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                19: "Jackie Bradley Jr.",
                # Starting pitcher
                17: "Nathan Eovaldi",
                # Bench
                25: "Steve Pearce",
                68: "Dan Butler",
                38: "Tony Renda",
                # Bullpen
                47: "Tyler Thornburg",
                44: "Brandon Workman",
                22: "Rick Porcello",
                31: "Drew Pomeranz",
                61: "Brian Johnson",
                37: "Heath Hembree",
                24: "David Price",
                46: "Craig Kimbrel",
                76: "Hector Velázquez",
                70: "Ryan Brasier",
                56: "Joe Kelly",
                32: "Matt Barnes",
            },
            "lefties": [31, 61, 24],
            "lineup": [
                [50, "9"],
                [16, "7"],
                [18, "3"],
                [28, "0"],
                [2, "6"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
                [19, "8"],
            ],
            "bench": [
                [25, "1B"],
                [68, "C"],
                [38, "2B"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 24, 46, 76, 70, 56, 32],
        },
        "umpires": {
            "HP": "Phil Cuzzi",
            "1B": "Chris Conroy",
            "2B": "Dan Bellino",
            "3B": "Adam Hamari",
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

# 1. NYY #11 Brett Gardner (X - X - X)
t1.new_ab()
t1.pitch_list("b c")
t1.out("P4")

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t1.new_ab()
t1.pitch_list("b s b t s")
t1.out("K")

# 3. NYY #18 Didi Gregorius (X - X - X)
t1.new_ab()
t1.pitch_list("b f")
t1.out("P6")


# Bot 1st
# Pitching: NYY #43 Chance Adams
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c b b")
b1.out("G5-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("b")
b1.hit(1)
b1.advance(2, "18 PB")
b1.advance(4, "18 HR")

# 3. BOS #18 Mitch Moreland (X - X - 16)
b1.new_ab()
b1.pitch_list("1 b b c")
b1.pb()
b1.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
b1.new_ab()
b1.pitch_list("c f f")
b1.out("L9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b1.new_ab()
b1.pitch_list("c c b f")
b1.out("F7")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #17 Nathan Eovaldi
t2 = game.new_inning()

# 4. NYY #31 Aaron Hicks (X - X - X)
t2.new_ab()
t2.pitch_list("b b c f b b")
t2.reach("BB")
t2.thrown_out(2, "25 DP6-3", 1, 17)

# 5. NYY #25 Gleyber Torres (X - X - 31)
t2.new_ab()
t2.out("DP6-3")

# 6. NYY #33 Greg Bird (X - X - X)
t2.new_ab()
t2.pitch_list("c s b b f")
t2.out("F8")


# Bot 2nd
# Pitching: NYY #43 Chance Adams
b2 = game.new_inning()

# 6. BOS #36 Eduardo Núñez (X - X - X)
b2.new_ab()
b2.out("G6-3")

# 7. BOS #12 Brock Holt (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c b")
b2.out("G3")

# 8. BOS #3  Sandy León (X - X - X)
b2.new_ab()
b2.pitch_list("b b b c f f f")
b2.out("L6")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #17 Nathan Eovaldi
t3 = game.new_inning()

# 7. NYY #41 Miguel Andujar (X - X - X)
t3.new_ab()
t3.pitch_list("f b s s")
t3.out("K")

# 8. NYY #28 Austin Romine (X - X - X)
t3.new_ab()
t3.pitch_list("f b")
t3.out("G6-3")

# 9. NYY #38 Shane Robinson (X - X - X)
t3.new_ab()
t3.pitch_list("c")
t3.out("F9")


# Bot 3rd
# Pitching: NYY #43 Chance Adams
b3 = game.new_inning()

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b3.new_ab()
b3.pitch_list("f")
b3.out("L8")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b c f f b s")
b3.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b3.new_ab()
b3.pitch_list("c b")
b3.out("L6")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #17 Nathan Eovaldi
t4 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
t4.new_ab()
t4.pitch_list("b c b")
t4.hit(1)
t4.thrown_out(2, "18 DP4-6-3", 2, 17)

# 2. NYY #27 Giancarlo Stanton (X - X - 11)
t4.new_ab()
t4.out("L8")

# 3. NYY #18 Didi Gregorius (X - X - 11)
t4.new_ab()
t4.out("DP4-6-3")


# Bot 4th
# Pitching: NYY #43 Chance Adams
b4 = game.new_inning()

# 3. BOS #18 Mitch Moreland (X - X - X)
b4.new_ab()
b4.pitch_list("b f f b f s")
b4.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
b4.new_ab()
b4.pitch_list("f b")
b4.hit(4)

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b c b b b")
b4.reach("BB")
b4.thrown_out(2, "36 DP6-4-3", 2, 43)

# 6. BOS #36 Eduardo Núñez (X - X - 2)
b4.new_ab()
b4.pitch_list("b 1 b c b f f f f")
b4.out("DP6-4-3")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #17 Nathan Eovaldi
t5 = game.new_inning()

# 4. NYY #31 Aaron Hicks (X - X - X)
t5.new_ab()
t5.pitch_list("b")
t5.out("P6")

# 5. NYY #25 Gleyber Torres (X - X - X)
t5.new_ab()
t5.pitch_list("c b f f f b f")
t5.out("L8")

# 6. NYY #33 Greg Bird (X - X - X)
t5.new_ab()
t5.out("G4-3")


# Bot 5th
# Pitching: NYY #43 Chance Adams
b5 = game.new_inning()

# 7. BOS #12 Brock Holt (X - X - X)
b5.new_ab()
b5.pitch_list("b c s b b")
b5.out("F7")

# 8. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("c f b f f")
b5.out("G6-3")

# 9. BOS #19 Jackie Bradley Jr. (X - X - X)
b5.new_ab()
b5.pitch_list("b f")
b5.out("G4-3")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #17 Nathan Eovaldi
t6 = game.new_inning()

# 7. NYY #41 Miguel Andujar (X - X - X)
t6.new_ab()
t6.pitch_list("b")
t6.hit(1)
t6.thrown_out(2, "38 FC6-4", 2, 17)

# 8. NYY #28 Austin Romine (X - X - 41)
t6.new_ab()
t6.pitch_list("s")
t6.out("F9")

# 9. NYY #38 Shane Robinson (X - X - 41)
t6.new_ab()
t6.pitch_list("s 1")
t6.reach("FC6-4")

# 1. NYY #11 Brett Gardner (X - X - 38)
t6.new_ab()
t6.pitch_list("c c b b f")
t6.out("P5")


# Bot 6th
# Pitching: NYY #57 Chad Green
b6 = game.new_inning()

# Pitching change (NYY): #57 Chad Green replaces #43 Chance Adams
b6.pitching_substitution(57)

# 1. BOS #50 Mookie Betts (X - X - X)
b6.new_ab()
b6.pitch_list("b f f b s")
b6.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b6.new_ab()
b6.pitch_list("b s s f")
b6.out("G4-3")

# 3. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("f c s")
b6.out("K")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #17 Nathan Eovaldi
t7 = game.new_inning()

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(2)

# 3. NYY #18 Didi Gregorius (X - 27 - X)
t7.new_ab()
t7.pitch_list("f f f")
t7.out("(F)P3")

# 4. NYY #31 Aaron Hicks (X - 27 - X)
t7.new_ab()
t7.pitch_list("c")
t7.out("L8")

# 5. NYY #25 Gleyber Torres (X - 27 - X)
t7.new_ab()
t7.pitch_list("c b b s f s")
t7.out("K")


# Bot 7th
# Pitching: NYY #67 A.J. Cole
b7 = game.new_inning()

# Pitching change (NYY): #67 A.J. Cole replaces #57 Chad Green
b7.pitching_substitution(67)

# 4. BOS #28 J.D. Martinez (X - X - X)
b7.new_ab()
b7.pitch_list("c b b b f")
b7.out("F9")

# 5. BOS #2  Xander Bogaerts (X - X - X)
b7.new_ab()
b7.pitch_list("c c s")
b7.out("K")

# 6. BOS #36 Eduardo Núñez (X - X - X)
b7.new_ab()
b7.pitch_list("s b b")
b7.hit(1)
b7.advance(2, "12 1B")
b7.advance(4, "3 2B")

# 7. BOS #12 Brock Holt (X - X - 36)
b7.new_ab()
b7.pitch_list("c 1 1 1 t")
b7.hit(1)
b7.advance(3, "3 2B")

# 8. BOS #3  Sandy León (X - 36 - 12)
b7.new_ab()
b7.hit(2, rbis=1)

# 9. BOS #19 Jackie Bradley Jr. (12 - 3 - X)
b7.new_ab()
b7.pitch_list("c")
b7.out("F8")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #17 Nathan Eovaldi
t8 = game.new_inning()

# 6. NYY #33 Greg Bird (X - X - X)
t8.new_ab()
t8.pitch_list("c t f")
t8.out("F7")

# 7. NYY #41 Miguel Andujar (X - X - X)
t8.new_ab()
t8.pitch_list("c c b b b f")
t8.out("L8")

# 8. NYY #28 Austin Romine (X - X - X)
t8.new_ab()
t8.pitch_list("b s f b c")
t8.out("!K")


# Bot 8th
# Pitching: NYY #67 A.J. Cole
b8 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b8.new_ab()
b8.pitch_list("c b f f f s")
b8.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b8.new_ab()
b8.pitch_list("s f s")
b8.out("K")

# 3. BOS #18 Mitch Moreland (X - X - X)
b8.new_ab()
b8.pitch_list("b c b b s f b")
b8.reach("BB")

# 4. BOS #28 J.D. Martinez (X - X - 18)
b8.new_ab()
b8.pitch_list("d f f f s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #46 Craig Kimbrel
t9 = game.new_inning()

# Pitching change (BOS): #46 Craig Kimbrel replaces #17 Nathan Eovaldi
t9.pitching_substitution(46)

# Offensive change (NYY): Pinch-hitter #14 Neil Walker replaces #38 Shane Robinson, batting 9th
t9.offensive_substitution(9, 14, "PH")

# 9. NYY #14 Neil Walker (X - X - X)
t9.new_ab()
t9.pitch_list("c s f b f b c")
t9.out("!K")

# 1. NYY #11 Brett Gardner (X - X - X)
t9.new_ab()
t9.pitch_list("c c c")
t9.out("!K")

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t9.new_ab()
t9.pitch_list("s s b")
t9.hit(2)
t9.advance(4, "18 2B")

# 3. NYY #18 Didi Gregorius (X - 27 - X)
t9.new_ab()
t9.pitch_list("b")
t9.hit(2, rbis=1)
t9.advance(3, "25 BB")

# 4. NYY #31 Aaron Hicks (X - 18 - X)
t9.new_ab()
t9.pitch_list("b b b c b")
t9.reach("BB")
t9.advance(2, "25 BB")

# 5. NYY #25 Gleyber Torres (X - 18 - 31)
t9.new_ab()
t9.pitch_list("b d s c b f b")
t9.reach("BB")

# 6. NYY #33 Greg Bird (18 - 31 - 25)
t9.new_ab()
t9.pitch_list("f b b")
t9.out("F8")

# Winning team: BOS
# WP: BOS #17 Nathan Eovaldi
game.winning_pitcher(17)

# Loser team: NYY
# LP: NYY #43 Chance Adams
game.losing_pitcher(43, is_away_team=True)

# print(game)
game.generate_scorecard()
