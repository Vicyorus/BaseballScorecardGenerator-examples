import os
from baseball_scorecard.baseball_scorecard import Scorecard

# BOS @ NYY, 2018-05-09
# https://www.baseball-reference.com/boxes/NYA/NYA201805090.shtml
# https://www.mlb.com/gameday/red-sox-vs-yankees/2018/05/09/529950/final

game = Scorecard(
    os.path.dirname(os.path.abspath(__file__)),
    {
        "scorer": "Vicyorus",
        "date": "2018-05-09 19:09-22:51",
        "at": "Yankee Stadium, Bronx, NY",
        "att": "47,088",
        "temp": "68F, Partly Cloudy",
        "wind": "9mph, R To L",
        "away": {
            "team": "Boston Red Sox",
            "starter": 22,
            "roster": {
                # Lineup
                50: "Mookie Betts",
                16: "Andrew Benintendi",
                13: "Hanley Ramirez",
                28: "J.D. Martinez",
                2: "Xander Bogaerts",
                18: "Mitch Moreland",
                36: "Eduardo Núñez",
                11: "Rafael Devers",
                3: "Sandy León",
                # Starting pitcher
                22: "Rick Porcello",
                # Bench
                12: "Brock Holt",
                23: "Blake Swihart",
                19: "Jackie Bradley Jr.",
                7: "Christian Vázquez",
                # Bullpen
                57: "Eduardo Rodriguez",
                39: "Carson Smith",
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
                [50, "8"],
                [16, "7"],
                [13, "0"],
                [28, "9"],
                [2, "6"],
                [18, "3"],
                [36, "4"],
                [11, "5"],
                [3, "2"],
            ],
            "bench": [
                [12, "2B"],
                [23, "C"],
                [19, "CF"],
                [7, "C"],
            ],
            "bullpen": [57, 39, 41, 31, 61, 37, 24, 46, 76, 56, 32],
        },
        "home": {
            "team": "New York Yankees",
            "starter": 19,
            "roster": {
                # Lineup
                11: "Brett Gardner",
                99: "Aaron Judge",
                18: "Didi Gregorius",
                27: "Giancarlo Stanton",
                24: "Gary Sánchez",
                31: "Aaron Hicks",
                14: "Neil Walker",
                41: "Miguel Andujar",
                25: "Gleyber Torres",
                # Starting pitcher
                19: "Masahiro Tanaka",
                # Bench
                28: "Austin Romine",
                74: "Ronald Torreyes",
                26: "Tyler Austin",
                # Bullpen
                67: "A.J. Cole",
                68: "Dellin Betances",
                40: "Luis Severino",
                45: "Chasen Shreve",
                65: "Domingo Germán",
                55: "Sonny Gray",
                56: "Jonathan Holder",
                52: "CC Sabathia",
                57: "Chad Green",
                61: "David Hale",
                30: "David Robertson",
                54: "Aroldis Chapman",
            },
            "lefties": [45, 52, 54],
            "lineup": [
                [11, "7"],
                [99, "9"],
                [18, "6"],
                [27, "0"],
                [24, "2"],
                [31, "8"],
                [14, "3"],
                [41, "5"],
                [25, "4"],
            ],
            "bench": [
                [28, "C"],
                [74, "SS"],
                [26, "1B"],
            ],
            "bullpen": [67, 68, 40, 45, 65, 55, 56, 52, 57, 61, 30, 54],
        },
        "umpires": {
            "HP": "Cory Blaser",
            "1B": "Stu Scheurwater",
            "2B": "Eric Cooper",
            "3B": "Gary Cederstrom",
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
# Pitching: NYY #19 Masahiro Tanaka
t1 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t1.new_ab()
t1.pitch_list("b f s b f f f f f b s")
t1.out("K")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t1.new_ab()
t1.pitch_list("s f")
t1.out("F8")

# 3. BOS #13 Hanley Ramirez (X - X - X)
t1.new_ab()
t1.pitch_list("c b f f f f s")
t1.out("K2-3")


# Bot 1st
# Pitching: BOS #22 Rick Porcello
b1 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b1.new_ab()
b1.pitch_list("b b")
b1.hit(2)
b1.advance(4, "99 1B")

# 2. NYY #99 Aaron Judge (X - 11 - X)
b1.new_ab()
b1.hit(1, rbis=1)
b1.thrown_out(2, "27 DP4-6-3", 2, 22)

# 3. NYY #18 Didi Gregorius (X - X - 99)
b1.new_ab()
b1.pitch_list("c f b s")
b1.out("K")

# 4. NYY #27 Giancarlo Stanton (X - X - 99)
b1.new_ab()
b1.pitch_list("c")
b1.out("DP4-6-3")


##########################################################
# 2nd Inning
##########################################################
# Top 2nd
# Pitching: NYY #19 Masahiro Tanaka
t2 = game.new_inning()

# 4. BOS #28 J.D. Martinez (X - X - X)
t2.new_ab()
t2.pitch_list("c f b")
t2.out("G6-3")

# 5. BOS #2  Xander Bogaerts (X - X - X)
t2.new_ab()
t2.pitch_list("b b b c f")
t2.hit(1)
t2.advance(4, "18 HR")

# 6. BOS #18 Mitch Moreland (X - X - 2)
t2.new_ab()
t2.pitch_list("b b")
t2.hit(4, rbis=2)

# 7. BOS #36 Eduardo Núñez (X - X - X)
t2.new_ab()
t2.out("L9")

# 8. BOS #11 Rafael Devers (X - X - X)
t2.new_ab()
t2.pitch_list("b s b f")
t2.hit(1)
t2.advance(2, "3 1B")

# 9. BOS #3  Sandy León (X - X - 11)
t2.new_ab()
t2.pitch_list("c")
t2.hit(1)
t2.thrown_out(2, "50 FC5-4", 3, 19)

# 1. BOS #50 Mookie Betts (X - 11 - 3)
t2.new_ab()
t2.pitch_list("b s 2 b")
t2.reach("FC5-4")


# Bot 2nd
# Pitching: BOS #22 Rick Porcello
b2 = game.new_inning()

# 5. NYY #24 Gary Sánchez (X - X - X)
b2.new_ab()
b2.pitch_list("c")
b2.out("G1-3")

# 6. NYY #31 Aaron Hicks (X - X - X)
b2.new_ab()
b2.pitch_list("b b c c b b")
b2.reach("BB")
b2.advance(2, "41 1B")
b2.advance(3, "25 SB")

# 7. NYY #14 Neil Walker (X - X - 31)
b2.new_ab()
b2.pitch_list("c f b c")
b2.out("!K")

# 8. NYY #41 Miguel Andujar (X - X - 31)
b2.new_ab()
b2.pitch_list("1 1")
b2.hit(1)

# 9. NYY #25 Gleyber Torres (X - 31 - 41)
b2.new_ab()
b2.pitch_list("s d s b b")
b2.out("G5-3")


##########################################################
# 3rd Inning
##########################################################
# Top 3rd
# Pitching: NYY #19 Masahiro Tanaka
t3 = game.new_inning()

# 2. BOS #16 Andrew Benintendi (X - X - X)
t3.new_ab()
t3.pitch_list("c b b s b d")
t3.reach("BB")
t3.thrown_out(2, "13 DP6-4-3", 1, 19)

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t3.new_ab()
t3.pitch_list("b 1")
t3.out("DP6-4-3")

# 4. BOS #28 J.D. Martinez (X - X - X)
t3.new_ab()
t3.pitch_list("c b f b b b")
t3.reach("BB")
t3.advance(2, "2 1B")

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t3.new_ab()
t3.hit(1)

# 6. BOS #18 Mitch Moreland (X - 28 - 2)
t3.new_ab()
t3.pitch_list("f b f f d s")
t3.out("K")


# Bot 3rd
# Pitching: BOS #22 Rick Porcello
b3 = game.new_inning()

# 1. NYY #11 Brett Gardner (X - X - X)
b3.new_ab()
b3.pitch_list("b b")
b3.hit(2)
b3.advance(3, "18 G3")
b3.advance(4, "27 2B")

# 2. NYY #99 Aaron Judge (X - 11 - X)
b3.new_ab()
b3.pitch_list("b s b b d")
b3.reach("BB")
b3.advance(2, "18 G3")
b3.advance(4, "27 2B")

# 3. NYY #18 Didi Gregorius (X - 11 - 99)
b3.new_ab()
b3.out("G3")

# 4. NYY #27 Giancarlo Stanton (11 - 99 - X)
b3.new_ab()
b3.pitch_list("f b b c")
b3.hit(2, rbis=2)
b3.advance(3, "24 1B")
b3.advance(4, "31 SF8")

# 5. NYY #24 Gary Sánchez (X - 27 - X)
b3.new_ab()
b3.pitch_list("d c c")
b3.hit(1)

# 6. NYY #31 Aaron Hicks (27 - X - 24)
b3.new_ab()
b3.pitch_list("f")
b3.out("SF8", rbis=1)

# 7. NYY #14 Neil Walker (X - X - 24)
b3.new_ab()
b3.pitch_list("b d")
b3.out("F8")


##########################################################
# 4th Inning
##########################################################
# Top 4th
# Pitching: NYY #19 Masahiro Tanaka
t4 = game.new_inning()

# 7. BOS #36 Eduardo Núñez (X - X - X)
t4.new_ab()
t4.pitch_list("b f")
t4.out("L8")

# 8. BOS #11 Rafael Devers (X - X - X)
t4.new_ab()
t4.hit(1)
t4.thrown_out(2, "3 DP4-6-3", 2, 19)

# 9. BOS #3  Sandy León (X - X - 11)
t4.new_ab()
t4.pitch_list("c b 1")
t4.out("DP4-6-3")


# Bot 4th
# Pitching: BOS #22 Rick Porcello
b4 = game.new_inning()

# 8. NYY #41 Miguel Andujar (X - X - X)
b4.new_ab()
b4.pitch_list("c f b b f")
b4.out("F9")

# 9. NYY #25 Gleyber Torres (X - X - X)
b4.new_ab()
b4.pitch_list("b b s f")
b4.out("G5-3")

# 1. NYY #11 Brett Gardner (X - X - X)
b4.new_ab()
b4.out("G3-1")


##########################################################
# 5th Inning
##########################################################
# Top 5th
# Pitching: NYY #19 Masahiro Tanaka
t5 = game.new_inning()

# 1. BOS #50 Mookie Betts (X - X - X)
t5.new_ab()
t5.pitch_list("c c")
t5.out("G1-3")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t5.new_ab()
t5.pitch_list("c")
t5.hit(4, rbis=1)

# 3. BOS #13 Hanley Ramirez (X - X - X)
t5.new_ab()
t5.out("F7")

# 4. BOS #28 J.D. Martinez (X - X - X)
t5.new_ab()
t5.pitch_list("c b")
t5.out("L9")


# Bot 5th
# Pitching: BOS #22 Rick Porcello
b5 = game.new_inning()

# 2. NYY #99 Aaron Judge (X - X - X)
b5.new_ab()
b5.hit(1)
b5.error(1)
b5.advance(2, "E1")
b5.advance(3, "27 HBP")
b5.advance(4, "24 SF8")

# 3. NYY #18 Didi Gregorius (X - 99 - X)
b5.new_ab()
b5.pitch_list("b b d b")
b5.reach("BB")
b5.advance(2, "27 HBP")
b5.advance(3, "31 FC6")

# 4. NYY #27 Giancarlo Stanton (X - 99 - 18)
b5.new_ab()
b5.reach("HBP")
b5.thrown_out(2, "31 FC6", 2, 22)

# 5. NYY #24 Gary Sánchez (99 - 18 - 27)
b5.new_ab()
b5.pitch_list("s d b s d")
b5.out("SF8", rbis=1)

# 6. NYY #31 Aaron Hicks (X - 18 - 27)
b5.new_ab()
b5.pitch_list("f d b f")
b5.reach("FC6")

# 7. NYY #14 Neil Walker (18 - X - 31)
b5.new_ab()
b5.pitch_list("f")
b5.out("L7")


##########################################################
# 6th Inning
##########################################################
# Top 6th
# Pitching: NYY #19 Masahiro Tanaka
t6 = game.new_inning()

# 5. BOS #2  Xander Bogaerts (X - X - X)
t6.new_ab()
t6.pitch_list("c b s")
t6.hit(2)
t6.advance(3, "18 G4-3")
t6.advance(4, "36 SF8")

# 6. BOS #18 Mitch Moreland (X - 2 - X)
t6.new_ab()
t6.pitch_list("f b d")
t6.out("G4-3")

# Pitching change (NYY): #57 Chad Green replaces #19 Masahiro Tanaka
t6.pitching_substitution(57)

# 7. BOS #36 Eduardo Núñez (2 - X - X)
t6.new_ab()
t6.out("SF8", rbis=1)

# 8. BOS #11 Rafael Devers (X - X - X)
t6.new_ab()
t6.pitch_list("c b c f t")
t6.out("KT")


# Bot 6th
# Pitching: BOS #22 Rick Porcello
b6 = game.new_inning()

# 8. NYY #41 Miguel Andujar (X - X - X)
b6.new_ab()
b6.pitch_list("c b s s")
b6.out("K")

# 9. NYY #25 Gleyber Torres (X - X - X)
b6.new_ab()
b6.pitch_list("b b b")
b6.hit(1)
b6.thrown_out(2, "11 FC6-4", 2, 61)

# Pitching change (BOS): #61 Brian Johnson replaces #22 Rick Porcello
b6.pitching_substitution(61)

# 1. NYY #11 Brett Gardner (X - X - 25)
b6.new_ab()
b6.pitch_list("1 c c b f f d d")
b6.reach("FC6-4")

# 2. NYY #99 Aaron Judge (X - X - 11)
b6.new_ab()
b6.pitch_list("c d s")
b6.out("F9")


##########################################################
# 7th Inning
##########################################################
# Top 7th
# Pitching: NYY #57 Chad Green
t7 = game.new_inning()

# Offensive change (BOS): Pinch-hitter #12 Brock Holt replaces #3 Sandy León, batting 9th
t7.offensive_substitution(9, 12, "PH")

# 9. BOS #12 Brock Holt (X - X - X)
t7.new_ab()
t7.pitch_list("c c")
t7.out("L6")

# 1. BOS #50 Mookie Betts (X - X - X)
t7.new_ab()
t7.pitch_list("c b s b b")
t7.out("L7")

# 2. BOS #16 Andrew Benintendi (X - X - X)
t7.new_ab()
t7.pitch_list("c b b c b b")
t7.reach("BB")
t7.advance(4, "13 HR")

# 3. BOS #13 Hanley Ramirez (X - X - 16)
t7.new_ab()
t7.pitch_list("1 f b")
t7.hit(4, rbis=2)

# 4. BOS #28 J.D. Martinez (X - X - X)
t7.new_ab()
t7.pitch_list("c s b b")
t7.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t7.new_ab()
t7.pitch_list("b c f s")
t7.out("K")


# Bot 7th
# Pitching: BOS #61 Brian Johnson
b7 = game.new_inning()

# Defensive change (BOS): #7 Christian Vázquez replaces #12 Brock Holt (PH), playing C, batting 9th
b7.defensive_substitution(9, 7, "2")

# 3. NYY #18 Didi Gregorius (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("L7")

# Pitching change (BOS): #39 Carson Smith replaces #61 Brian Johnson
b7.pitching_substitution(39)

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b7.new_ab()
b7.pitch_list("b")
b7.out("G6-3")

# 5. NYY #24 Gary Sánchez (X - X - X)
b7.new_ab()
b7.pitch_list("c b b")
b7.hit(1)

# 6. NYY #31 Aaron Hicks (X - X - 24)
b7.new_ab()
b7.pitch_list("b s s b d c")
b7.out("!K")


##########################################################
# 8th Inning
##########################################################
# Top 8th
# Pitching: NYY #45 Chasen Shreve
t8 = game.new_inning()

# Pitching change (NYY): #45 Chasen Shreve replaces #57 Chad Green
t8.pitching_substitution(45)

# 6. BOS #18 Mitch Moreland (X - X - X)
t8.new_ab()
t8.pitch_list("f b f b b d")
t8.reach("BB")
t8.advance(3, "36 2B")

# 7. BOS #36 Eduardo Núñez (X - X - 18)
t8.new_ab()
t8.pitch_list("1 f")
t8.hit(2)

# 8. BOS #11 Rafael Devers (18 - 36 - X)
t8.new_ab()
t8.pitch_list("f c b s")
t8.out("K")

# Pitching change (NYY): #56 Jonathan Holder replaces #45 Chasen Shreve
t8.pitching_substitution(56)

# 9. BOS #7  Christian Vázquez (18 - 36 - X)
t8.new_ab()
t8.pitch_list("b c b f s")
t8.out("K")

# 1. BOS #50 Mookie Betts (18 - 36 - X)
t8.new_ab()
t8.pitch_list("v v v v")
t8.reach("IBB")

# 2. BOS #16 Andrew Benintendi (18 - 36 - 50)
t8.new_ab()
t8.pitch_list("c b b")
t8.out("G6-3")


# Bot 8th
# Pitching: BOS #32 Matt Barnes
b8 = game.new_inning()

# Pitching change (BOS): #32 Matt Barnes replaces #39 Carson Smith
b8.pitching_substitution(32)

# 7. NYY #14 Neil Walker (X - X - X)
b8.new_ab()
b8.pitch_list("b b c s")
b8.hit(2)
b8.advance(3, "41 G4-3")
b8.advance(4, "11 3B")

# 8. NYY #41 Miguel Andujar (X - 14 - X)
b8.new_ab()
b8.pitch_list("b b")
b8.out("G4-3")

# 9. NYY #25 Gleyber Torres (14 - X - X)
b8.new_ab()
b8.pitch_list("b d b c b")
b8.reach("BB")
b8.advance(4, "11 3B")

# Pitching change (BOS): #46 Craig Kimbrel replaces #32 Matt Barnes
b8.pitching_substitution(46)

# 1. NYY #11 Brett Gardner (14 - X - 25)
b8.new_ab()
b8.pitch_list("b b b c 1 f f")
b8.hit(3, rbis=2)
b8.advance(4, "99 HR")

# 2. NYY #99 Aaron Judge (11 - X - X)
b8.new_ab()
b8.pitch_list("f b f")
b8.hit(4, rbis=2)

# 3. NYY #18 Didi Gregorius (X - X - X)
b8.new_ab()
b8.pitch_list("f c t")
b8.out("KT")

# 4. NYY #27 Giancarlo Stanton (X - X - X)
b8.new_ab()
b8.pitch_list("s s b s")
b8.out("K")


##########################################################
# 9th Inning
##########################################################
# Top 9th
# Pitching: NYY #54 Aroldis Chapman
t9 = game.new_inning()

# Pitching change (NYY): #54 Aroldis Chapman replaces #56 Jonathan Holder
t9.pitching_substitution(54)

# 3. BOS #13 Hanley Ramirez (X - X - X)
t9.new_ab()
t9.pitch_list("c s f s")
t9.out("K")

# 4. BOS #28 J.D. Martinez (X - X - X)
t9.new_ab()
t9.pitch_list("b f s b f")
t9.hit(1)

# 5. BOS #2  Xander Bogaerts (X - X - 28)
t9.new_ab()
t9.pitch_list("f t d f f s")
t9.out("K")

# 6. BOS #18 Mitch Moreland (X - X - 28)
t9.new_ab()
t9.pitch_list("c b f s")
t9.out("K")

# Winning team: NYY
# WP: NYY #56 Jonathan Holder
game.winning_pitcher(56)
# SV: NYY #54 Aroldis Chapman
game.save_pitcher(54)

# Loser team: BOS
# LP: BOS #32 Matt Barnes
game.losing_pitcher(32, is_away_team=True)

# print(game)
game.generate_scorecard()
