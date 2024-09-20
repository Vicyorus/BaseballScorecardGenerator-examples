import os
from baseball_scorecard.baseball_scorecard import Scorecard

# NYY @ BOS, 2018-08-05
# https://www.baseball-reference.com/boxes/BOS/BOS201808050.shtml
# https://www.mlb.com/gameday/yankees-vs-red-sox/2018/08/05/531089/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-08-05 20:10-00:49 +1",
        "at": "Fenway Park, Boston, MA",
        "att": "37,830",
        "temp": "79F, Partly Cloudy",
        "wind": "5mph, In From RF",
        "away": {
            "team": "New York Yankees",
            "starter": 19,
            "roster": {
                # Lineup
                31: "Aaron Hicks",
                27: "Giancarlo Stanton",
                18: "Didi Gregorius",
                25: "Gleyber Torres",
                41: "Miguel Andujar",
                45: "Luke Voit",
                11: "Brett Gardner",
                28: "Austin Romine",
                38: "Shane Robinson",
                # Starting pitcher
                19: "Masahiro Tanaka",
                # Bench
                33: "Greg Bird",
                66: "Kyle Higashioka",
                14: "Neil Walker",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                36: "Lance Lynn",
                43: "Chance Adams",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                53: "Zack Britton",
                57: "Chad Green",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [52, 53, 54],
            "lineup": [
                [31, "8"],
                [27, "0"],
                [18, "6"],
                [25, "4"],
                [41, "5"],
                [45, "3"],
                [11, "7"],
                [28, "2"],
                [38, "9"],
            ],
            "bench": [
                [33, "1B"],
                [66, "C"],
                [14, "2B"],
            ],
            "bullpen": [67, 68, 40, 36, 43, 55, 56, 52, 53, 57, 30, 54],
        },
        "home": {
            "team": "Boston Red Sox",
            "starter": 24,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                25: "Steve Pearce",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                12: "Brock Holt",
                3: "Sandy León",
                # Starting pitcher
                24: "David Price",
                # Bench
                68: "Dan Butler",
                38: "Tony Renda",
                19: "Jackie Bradley Jr.",
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
                [50, "8"],
                [16, "7"],
                [25, "0"],
                [28, "9"],
                [2, "6"],
                [18, "3"],
                [36, "5"],
                [12, "4"],
                [3, "2"],
            ],
            "bench": [
                [68, "C"],
                [38, "2B"],
                [19, "CF"],
            ],
            "bullpen": [47, 44, 22, 31, 61, 37, 46, 76, 70, 56, 17, 32],
        },
        "umpires": {
            "HP": "Chris Conroy",
            "1B": "Dan Bellino",
            "2B": "Adam Hamari",
            "3B": "Phil Cuzzi",
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

# 1. NYY #31 Aaron Hicks (X - X - X)
t1.new_ab()
t1.pitch_list("b f b b")
t1.out("G6-3")

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t1.new_ab()
t1.pitch_list("c b b b")
t1.hit(1)
t1.advance(2, "18 HBP")
t1.advance(3, "41 1B")

# 3. NYY #18 Didi Gregorius (X - X - 27)
t1.new_ab()
t1.reach("HBP")
t1.advance(2, "41 1B")

# 4. NYY #25 Gleyber Torres (X - 27 - 18)
t1.new_ab()
t1.pitch_list("c f f c")
t1.out("!K")

# 5. NYY #41 Miguel Andujar (X - 27 - 18)
t1.new_ab()
t1.pitch_list("b")
t1.hit(1)

# 6. NYY #45 Luke Voit (27 - 18 - 41)
t1.new_ab()
t1.pitch_list("b s")
t1.out("G1-3")


# Bot 1st
# Pitching: NYY #19 Masahiro Tanaka
b1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
b1.new_ab()
b1.pitch_list("c s f")
b1.out("G4-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
b1.new_ab()
b1.pitch_list("c f")
b1.hit(2)

# 3. BOS #25 Steve Pearce (X - 16 - X)
b1.new_ab()
b1.pitch_list("b s c 2 s")
b1.out("K")

# 4. BOS #28 J.D. Martinez (X - 16 - X)
b1.new_ab()
b1.pitch_list("b s c d d s")
b1.out("K")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: BOS #24 David Price
t2 = game.new_inning()

# 7. NYY #11 Brett Gardner (X - X - X)
t2.new_ab()
t2.pitch_list("b s")
t2.out("F8")

# 8. NYY #28 Austin Romine (X - X - X)
t2.new_ab()
t2.pitch_list("b s s b")
t2.out("P4")

# 9. NYY #38 Shane Robinson (X - X - X)
t2.new_ab()
t2.pitch_list("s")
t2.out("L8")


# Bot 2nd
# Pitching: NYY #19 Masahiro Tanaka
b2 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b2.new_ab()
b2.pitch_list("c b")
b2.hit(1)
b2.thrown_out(2, "36 CS", 2, 19)

# 6. BOS #18 Mitch Moreland (X - X - 2)
b2.new_ab()
b2.pitch_list("b f 1")
b2.out("L6")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
b2.new_ab()
b2.pitch_list("b c b d c")
b2.hit(1)

# 8. BOS #12 Brock Holt (X - X - 36)
b2.new_ab()
b2.pitch_list("1 b b f")
b2.out("L8")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: BOS #24 David Price
t3 = game.new_inning()

# 1. NYY #31 Aaron Hicks (X - X - X)
t3.new_ab()
t3.pitch_list("b f s b f b f")
t3.out("G6-3")

# 2. NYY #27 Giancarlo Stanton (X - X - X)
t3.new_ab()
t3.pitch_list("b b c f s")
t3.out("K")

# 3. NYY #18 Didi Gregorius (X - X - X)
t3.new_ab()
t3.pitch_list("b")
t3.out("F8")


# Bot 3rd
# Pitching: NYY #19 Masahiro Tanaka
b3 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b3.new_ab()
b3.pitch_list("c f s")
b3.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b3.new_ab()
b3.pitch_list("b b b c f")
b3.hit(1)
b3.advance(2, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - X - 50)
b3.new_ab()
b3.pitch_list("b 1 c b 1")
b3.hit(1)

# 3. BOS #25 Steve Pearce (X - 50 - 16)
b3.new_ab()
b3.pitch_list("f d d s s")
b3.out("K")

# 4. BOS #28 J.D. Martinez (X - 50 - 16)
b3.new_ab()
b3.pitch_list("b 2 b s f b s")
b3.out("K")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: BOS #24 David Price
t4 = game.new_inning()

# 4. NYY #25 Gleyber Torres (X - X - X)
t4.new_ab()
t4.pitch_list("s b s b")
t4.out("L6")

# 5. NYY #41 Miguel Andujar (X - X - X)
t4.new_ab()
t4.pitch_list("b s")
t4.out("G6-3")

# 6. NYY #45 Luke Voit (X - X - X)
t4.new_ab()
t4.pitch_list("s b b s f b b")
t4.reach("BB")

# 7. NYY #11 Brett Gardner (X - X - 45)
t4.new_ab()
t4.pitch_list("c b f f b b c")
t4.out("!K")


# Bot 4th
# Pitching: NYY #19 Masahiro Tanaka
b4 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b4.new_ab()
b4.pitch_list("b b b f f b")
b4.reach("BB")

# 6. BOS #18 Mitch Moreland (X - X - 2)
b4.new_ab()
b4.pitch_list("d b f f b f f f s")
b4.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 2)
b4.new_ab()
b4.pitch_list("b 1 f 1 b f f f b s")
b4.out("K")

# 8. BOS #12 Brock Holt (X - X - 2)
b4.new_ab()
b4.pitch_list("d")
b4.out("L7")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: BOS #24 David Price
t5 = game.new_inning()

# 8. NYY #28 Austin Romine (X - X - X)
t5.new_ab()
t5.hit(1)
t5.advance(2, "38 SAC3-4")
t5.advance(3, "31 G4-3")

# 9. NYY #38 Shane Robinson (X - X - 28)
t5.new_ab()
t5.pitch_list("b s")
t5.out("SAC3-4")

# 1. NYY #31 Aaron Hicks (X - 28 - X)
t5.new_ab()
t5.pitch_list("c f")
t5.out("G4-3")

# 2. NYY #27 Giancarlo Stanton (28 - X - X)
t5.new_ab()
t5.pitch_list("f")
t5.out("G6-3")


# Bot 5th
# Pitching: NYY #19 Masahiro Tanaka
b5 = game.new_inning()

# 9. BOS #3  Sandy León (X - X - X)
b5.new_ab()
b5.pitch_list("s c b s")
b5.out("K")

# 1. BOS #50 Mookie Betts (X - X - X)
b5.new_ab()
b5.pitch_list("b b")
b5.hit(4)

# 2. BOS #16 Andrew Benintendi (X - X - X)
b5.new_ab()
b5.pitch_list("b b c f c")
b5.out("!K")

# 3. BOS #25 Steve Pearce (X - X - X)
b5.new_ab()
b5.pitch_list("b c")
b5.error(5)
b5.reach("E5", end_base=2)

# Pitching change (NYY): #30 David Robertson replaces #19 Masahiro Tanaka
b5.pitching_substitution(30)

# 4. BOS #28 J.D. Martinez (X - 25 - X)
b5.new_ab()
b5.pitch_list("s b d b f s")
b5.out("K")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: BOS #24 David Price
t6 = game.new_inning()

# 3. NYY #18 Didi Gregorius (X - X - X)
t6.new_ab()
t6.pitch_list("c")
t6.out("G4-3")

# 4. NYY #25 Gleyber Torres (X - X - X)
t6.new_ab()
t6.pitch_list("b b f b f b")
t6.reach("BB")

# 5. NYY #41 Miguel Andujar (X - X - 25)
t6.new_ab()
t6.pitch_list("c b f f s")
t6.out("K")

# 6. NYY #45 Luke Voit (X - X - 25)
t6.new_ab()
t6.pitch_list("b s b s b t")
t6.out("KT")


# Bot 6th
# Pitching: NYY #30 David Robertson
b6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
b6.new_ab()
b6.pitch_list("b b c")
b6.out("F9")

# 6. BOS #18 Mitch Moreland (X - X - X)
b6.new_ab()
b6.pitch_list("b b")
b6.out("G3")

# 7. BOS #36 Eduardo Núñez (X - X - X)
b6.new_ab()
b6.pitch_list("b c b f")
b6.hit(1)

# 8. BOS #12 Brock Holt (X - X - 36)
b6.new_ab()
b6.pitch_list("c 1")
b6.out("G4-3")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: BOS #24 David Price
t7 = game.new_inning()

# 7. NYY #11 Brett Gardner (X - X - X)
t7.new_ab()
t7.pitch_list("b b f c f")
t7.hit(1)
t7.advance(2, "28 BB")
t7.advance(3, "38 BB")
t7.advance(4, "31 FC6")

# 8. NYY #28 Austin Romine (X - X - 11)
t7.new_ab()
t7.pitch_list("b f f f 1 b b b")
t7.reach("BB")
t7.advance(2, "38 BB")
t7.error(6)
t7.advance(3, "31 FC6")
t7.advance(4, "31 E6")

# Pitching change (BOS): #37 Heath Hembree replaces #24 David Price
t7.pitching_substitution(37)

# 9. NYY #38 Shane Robinson (X - 11 - 28)
t7.new_ab()
t7.pitch_list("l b l b b f b")
t7.reach("BB")
t7.advance(3, "31 E6")
t7.advance("U", "27 1B")

# 1. NYY #31 Aaron Hicks (11 - 28 - 38)
t7.new_ab()
t7.pitch_list("b c s b")
t7.reach("FC6", rbis=1)
t7.advance(2, "27 1B")
t7.advance(3, "18 WP")
t7.advance("U", "25 SF8")

# 2. NYY #27 Giancarlo Stanton (38 - X - 31)
t7.new_ab()
t7.pitch_list("c b")
t7.hit(1, rbis=1)
t7.advance(2, "18 WP")

# 3. NYY #18 Didi Gregorius (X - 31 - 27)
t7.new_ab()
t7.pitch_list("b f f b b f s")
t7.wp()
t7.out("K")

# Pitching change (BOS): #70 Ryan Brasier replaces #37 Heath Hembree
t7.pitching_substitution(70)

# 4. NYY #25 Gleyber Torres (31 - 27 - X)
t7.new_ab()
t7.out("SF8", rbis=1)

# 5. NYY #41 Miguel Andujar (X - 27 - X)
t7.new_ab()
t7.pitch_list("b s f")
t7.out("G6-3")


# Bot 7th
# Pitching: NYY #53 Zack Britton
b7 = game.new_inning()

# Pitching change (NYY): #53 Zack Britton replaces #30 David Robertson
b7.pitching_substitution(53)

# Defensive change (NYY): #33 Greg Bird replaces #45 Luke Voit (1B), playing 1B, batting 6th
b7.defensive_substitution(6, 33, "3")

# 9. BOS #3  Sandy León (X - X - X)
b7.new_ab()
b7.pitch_list("b b b c c b")
b7.reach("BB")
b7.advance(2, "16 PB")
b7.advance(3, "16 G4-3")

# 1. BOS #50 Mookie Betts (X - X - 3)
b7.new_ab()
b7.pitch_list("d c c b c")
b7.out("!K")

# 2. BOS #16 Andrew Benintendi (X - X - 3)
b7.new_ab()
b7.pitch_list("c d d b c f")
b7.pb()
b7.out("G4-3")

# 3. BOS #25 Steve Pearce (3 - X - X)
b7.new_ab()
b7.pitch_list("c d b")
b7.out("G6-3")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: BOS #70 Ryan Brasier
t8 = game.new_inning()

# 6. NYY #33 Greg Bird (X - X - X)
t8.new_ab()
t8.pitch_list("s f s")
t8.out("K")

# 7. NYY #11 Brett Gardner (X - X - X)
t8.new_ab()
t8.pitch_list("b c")
t8.hit(1)
t8.advance(3, "28 G6-3")

# 8. NYY #28 Austin Romine (X - X - 11)
t8.new_ab()
t8.pitch_list("1 f 1 1 f 1 b 1 b b f")
t8.out("G6-3")

# 9. NYY #38 Shane Robinson (11 - X - X)
t8.new_ab()
t8.pitch_list("c d f b f f")
t8.out("F9")


# Bot 8th
# Pitching: NYY #68 Dellin Betances
b8 = game.new_inning()

# Pitching change (NYY): #68 Dellin Betances replaces #53 Zack Britton
b8.pitching_substitution(68)

# 4. BOS #28 J.D. Martinez (X - X - X)
b8.new_ab()
b8.pitch_list("b b")
b8.reach("HBP")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
b8.new_ab()
b8.pitch_list("c b b c t")
b8.out("KT")

# 6. BOS #18 Mitch Moreland (X - X - 28)
b8.new_ab()
b8.pitch_list("b f c f f b s")
b8.out("K")

# 7. BOS #36 Eduardo Núñez (X - X - 28)
b8.new_ab()
b8.pitch_list("c b b d")
b8.out("G5-3")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: BOS #47 Tyler Thornburg
t9 = game.new_inning()

# Pitching change (BOS): #47 Tyler Thornburg replaces #70 Ryan Brasier
t9.pitching_substitution(47)

# 1. NYY #31 Aaron Hicks (X - X - X)
t9.new_ab()
t9.pitch_list("b b f s b d")
t9.reach("BB")
t9.advance(2, "25 BB")

# 2. NYY #27 Giancarlo Stanton (X - X - 31)
t9.new_ab()
t9.pitch_list("d")
t9.out("(F)P5")

# 3. NYY #18 Didi Gregorius (X - X - 31)
t9.new_ab()
t9.pitch_list("c b")
t9.out("F8")

# 4. NYY #25 Gleyber Torres (X - X - 31)
t9.new_ab()
t9.pitch_list("b f f b b d")
t9.reach("BB")

# 5. NYY #41 Miguel Andujar (X - 31 - 25)
t9.new_ab()
t9.pitch_list("b")
t9.out("F7")


# Bot 9th
# Pitching: NYY #54 Aroldis Chapman
b9 = game.new_inning()

# Pitching change (NYY): #54 Aroldis Chapman replaces #68 Dellin Betances
b9.pitching_substitution(54)

# 8. BOS #12 Brock Holt (X - X - X)
b9.new_ab()
b9.pitch_list("c b f b f b c")
b9.out("!K")

# 9. BOS #3  Sandy León (X - X - X)
b9.new_ab()
b9.pitch_list("c b b b b")
b9.reach("BB")
b9.advance(2, "50 BB")
b9.advance(3, "25 BB")
b9.advance(4, "28 1B")

# 1. BOS #50 Mookie Betts (X - X - 3)
b9.new_ab()
b9.pitch_list("b c b b f b")
b9.reach("BB")
b9.advance(2, "25 BB")
b9.advance(4, "28 1B")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
b9.new_ab()
b9.pitch_list("b c f b f c")
b9.out("!K")

# 3. BOS #25 Steve Pearce (X - 3 - 50)
b9.new_ab()
b9.pitch_list("b b c b c d")
b9.reach("BB")
# Offensive change (BOS): Pinch-runner #19 Jackie Bradley Jr. replaces #25 Steve Pearce
b9.offensive_substitution(3, 19, "PR")
b9.atbase("PR")
b9.advance(2, "28 1B")
b9.advance(3, "2 E5")
b9.advance("U", "2 E5")

# 4. BOS #28 J.D. Martinez (3 - 50 - 25)
b9.new_ab()
b9.hit(1, rbis=2)
b9.advance(2, "2 E5")

# 5. BOS #2  Xander Bogaerts (X - 19 - 28)
b9.new_ab()
b9.pitch_list("c d")
b9.error(5)
b9.reach("E5")

# 6. BOS #18 Mitch Moreland (X - 28 - 2)
b9.new_ab()
b9.pitch_list("c s b b s")
b9.out("K")


##########################################################
# 10th Inning
##########################################################
# Top 10th
# Pitching: BOS #32 Matt Barnes
t10 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #47 Tyler Thornburg
t10.pitching_substitution(32)

# Defensive switch (BOS): #19 Jackie Bradley Jr. moves to DH
t10.defensive_switch(19, "0")

# 6. NYY #33 Greg Bird (X - X - X)
t10.new_ab()
t10.pitch_list("b")
t10.out("F8")

# 7. NYY #11 Brett Gardner (X - X - X)
t10.new_ab()
t10.pitch_list("b c")
t10.out("F7")

# 8. NYY #28 Austin Romine (X - X - X)
t10.new_ab()
t10.pitch_list("c b s s")
t10.out("K2-3")


# Bot 10th
# Pitching: NYY #56 Jonathan Holder
b10 = game.new_inning()

# Pitching change (NYY): #56 Jonathan Holder replaces #54 Aroldis Chapman
b10.pitching_substitution(56)

# 7. BOS #36 Eduardo Núñez (X - X - X)
b10.new_ab()
b10.pitch_list("b c c b f s")
b10.out("K")

# 8. BOS #12 Brock Holt (X - X - X)
b10.new_ab()
b10.pitch_list("c")
b10.out("G4-3")

# 9. BOS #3  Sandy León (X - X - X)
b10.new_ab()
b10.pitch_list("b f f")
b10.hit(1)
b10.advance(2, "50 WP")
# Offensive change (BOS): Pinch-runner #38 Tony Renda replaces #3 Sandy León
b10.offensive_substitution(9, 38, "PR")
b10.atbase("PR")
b10.advance(4, "16 1B")

# 1. BOS #50 Mookie Betts (X - X - 3)
b10.new_ab()
b10.pitch_list("b v v v")
b10.wp()
b10.reach("IBB")
b10.advance(2, "16 1B")

# 2. BOS #16 Andrew Benintendi (X - 3 - 50)
b10.new_ab()
b10.pitch_list("b b c")
b10.hit(1, rbis=1)

# Winning team: BOS
# WP: BOS #32 Matt Barnes
game.winning_pitcher(32)

# Loser team: NYY
# LP: NYY #56 Jonathan Holder
game.losing_pitcher(56, is_away_team=True)

# print(game)
game.generate_scorecard()
